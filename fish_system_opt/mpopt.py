import numpy as np

import csdl
from python_csdl_backend import Simulator
from fish_system_opt.submodels.fish_geometry_model_bspline import EelGeometryModel
from fish_system_opt.submodels.fish_kinematics_model_poly import EelKinematicsModel
# from fish_system_opt.submodels.fish_kinematics_model import EelKinematicsModel

from VAST.core.submodels.friction_submodels.eel_viscous_force import EelViscousModel
from VAST.core.vlm_llt.vlm_dynamic_old.VLM_prescribed_wake_solver import UVLMSolver
from VAST.core.submodels.output_submodels.vlm_post_processing.efficiency import EfficiencyModel
from fish_system_opt.submodels.com_model import CoMModel

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
plt.rcParams['text.usetex'] = False

def run_fish_sim(num_pts_L, num_pts_R,num_time_steps, v_x_val, tail_frequency_val, amp_max, num_period, run_opt=False, del_sim=False,problem_name='kin_opt'):
    #########################################
    # solver specific parameters
    #########################################
    surface_name = 'eel'
    # num_pts_L = 41
    # num_pts_R = 5
    L = 1.0
    s_1_ind = 5
    s_2_ind = num_pts_L-3

    # num_period = 2
    surface_shape = (num_pts_L,num_pts_R, 3) # shape of the fish mesh

    # num_time_steps = 60
    # shape to input to the fish hydrodynamic solver model:
    surface_shapes = [(num_time_steps, num_pts_L, num_pts_R, 3)] 
    surface_properties_dict = {'surface_names':[surface_name], 'surface_shapes':[surface_shape], 'frame':'wing_fixed',}
    ode_surface_shapes = [(num_time_steps, ) + surface_shape]
        
    # default all nessary states to zero, except for u, which is expanded from v_x
    state_names = ['v', 'w', 'p', 'q', 'r', 'theta', 'psi', 'x', 'y', 'z', 'phiw', 'gamma', 'psiw']
    states_dict = {state: np.zeros((num_time_steps, 1)) for state in state_names}
    #######################################################################################
    # set up a fish system model
    fish_system_model = csdl.Model()

    #######################################################################################
    # inputs to the fish_system_model
    #######################################################################################

    #########################################
    # inputs to the sub eel_geometry_model
    #########################################
    fish_system_model.create_input('L', val=L)
    a = 0.51
    b = 0.08
    num_cp = 6
    x = np.linspace(1e-3, 1, num_cp)
    height =  b * np.sqrt(1 - ((x - a)/a)**2)
    fish_system_model.declare_variable('control_points', val=height*0)

    #########################################
    # inputs to the sub kinematics model
    #########################################
    # tail_frequency_csdl = fish_system_model.create_input('tail_frequency',val=tail_frequency_val)

    #########################################
    # inputs to the sub kinematics model
    #########################################
    tail_frequency_csdl = fish_system_model.create_input('tail_frequency',val=tail_frequency_val)
    # TODO: check if this work, also for how v_x is given to the hydrodynamic model
    h_stepsize = num_period/ tail_frequency_csdl / (num_time_steps-1)

    fish_system_model.register_output('delta_t', h_stepsize)

    print('h_stepsize is',h_stepsize)
    ########################################
    # Timestep vector
    ########################################
    h_vec = csdl.expand(h_stepsize,shape=(num_time_steps-1,1))
    h = fish_system_model.register_output('h', h_vec)
    #########################################    
    fish_system_model.create_input('wave_length',val=0.95)
    eel_amplitude_cp_val  = np.array([0.02, -0.08, 0.16, 0])
    fish_system_model.create_input('eel_amplitude_cp', val=eel_amplitude_cp_val)
    fish_system_model.create_input('amplitude_max', val=amp_max)

    #########################################
    # inputs to viscous model
    #########################################
    v_x = fish_system_model.create_input('v_x', val=v_x_val)
    u = fish_system_model.register_output('u', csdl.expand(v_x,shape=(num_time_steps,1)))

    #########################################
    # inputs to the hydrodynamics model
    #########################################
    density = fish_system_model.create_input('density',val=np.ones((num_time_steps,1))*997)
    #########################################
    # add geometry and kinematics model
    # generate initial rigid fish mesh
    #########################################
    eel_geometry_model = EelGeometryModel(surface_name=surface_name,
                                            surface_shape=surface_shape,
                                            num_cp=num_cp,
                                            s_1_ind=s_1_ind,s_2_ind=s_2_ind)
    fish_system_model.add(eel_geometry_model, name='EelGeometryModel')

    #########################################
    # add CoM model
    #########################################
    fish_system_model.add(CoMModel(surface_names=[surface_name], surface_shapes=[surface_shape]), 'CoMModel')


    # # add kinematics model
    eel_kinematics_model = EelKinematicsModel(surface_name=surface_name,
                                                surface_shape=surface_shape,    
                                                num_period=num_period,
                                                num_time_steps=num_time_steps,
                                                num_amp_cp=eel_amplitude_cp_val.size)                                       
    fish_system_model.add(eel_kinematics_model, name='EelKinematicsModel')

    #########################################
    # add hydrodynamics model
    #########################################

    fish_system_model.add(UVLMSolver(num_times=num_time_steps,states_dict=states_dict,
                                        surface_properties_dict=surface_properties_dict), 'fish_model')
    fish_system_model.add(EfficiencyModel(surface_names=[surface_name], surface_shapes=ode_surface_shapes,
                                            n_ignore=int(num_time_steps/num_period)),name='EfficiencyModel')
    try:
        fish_system_model.add(EelViscousModel(surface_shapes=ode_surface_shapes),name='EelViscousModel')
    except:
        fish_system_model.add(EelViscousModel(),name='EelViscousModel')

    # efficiency = fish_system_model.declare_variable('efficiency', shape=(1,))

    return fish_system_model#, efficiency

    ##############################################
    

run_opt = True
problem_name = 'full_opt_1014_mp'
v_x_list = np.array([0.3, 0.9])
tail_frequency_list = np.array([0.5458, 1.409])
amplitude_max_list = np.array([0.0300627300556591, 0.0300627300556591])

num_time_steps=70

fish_mp_model = csdl.Model()
sum_eff = []

#################################
################################

a = 0.51
b = 0.08
num_cp = 6
num_pts_L = 41
num_pts_R = 5
num_period = 2
x = np.linspace(1e-3, 1, num_cp)
height =  b * np.sqrt(1 - ((x - a)/a)**2)
cps = fish_mp_model.create_input('control_points', val=height)
for i in range(len(v_x_list)):
    tail_frequency_csdl = fish_mp_model.create_input(f'tail_frequency_{i}',val=tail_frequency_list[i])
    amplitude_max = fish_mp_model.create_input(f'amplitude_max_{i}',val=amplitude_max_list[i])


for i in range(len(v_x_list)):
    problem_name = 'kin_opt_0930_can_10'
    fish_system_model = run_fish_sim(num_pts_L=41, num_pts_R=5,num_time_steps=70,
                v_x_val=v_x_list[i], tail_frequency_val=1.547, amp_max=0.0300627300556591, 
                #  v_x_val=v_x_val, tail_frequency_val=0.353, amp_max=0.2, 
                num_period=2, run_opt=run_opt,problem_name=problem_name)
    lower=0.3

    # efficiency = fish_system_model.declare_variable('efficiency', shape=(1,))

    np_ignore  = 1

    thrust = fish_system_model.declare_variable('thrust',shape=(num_time_steps,1))[int(num_time_steps/num_period)*np_ignore:,:]
    C_F = fish_system_model.declare_variable('C_F')
    area = fish_system_model.declare_variable('eel_s_panel',shape=(num_time_steps,int((num_pts_L-1)*(num_pts_R-1))))
    avg_area = csdl.sum(area)/num_time_steps
    density = fish_system_model.declare_variable('density',val=np.ones((num_time_steps,1))*997)
    avg_C_T = -csdl.sum(thrust)/(0.5*csdl.reshape(density[0,0],(1,))*v_x_list[i]**2*avg_area)/(num_time_steps-int(num_time_steps/num_period)*np_ignore)
    fish_system_model.register_output('avg_C_T', avg_C_T)
    thrust_coeff_avr = (avg_C_T - C_F)**2    
    # fish_system_model.print_var(thrust_coeff_avr)

    com_x = fish_system_model.declare_variable('eel_CoM_x')*1.

    fish_system_model.register_output('thrust_coeff_avr', thrust_coeff_avr)
    fish_system_model.print_var(avg_C_T)
    fish_system_model.print_var(C_F)
    fish_system_model.register_output('average_area', avg_area)

    # fish_system_model.add_constraint('thrust_coeff_avr',equals=0.,scaler=1e2)
    # fish_system_model.add_constraint('eel_CoM_x',upper=0.6,lower=0.4)
    # #########################################
    # fish_system_model.register_output('average_area', avg_area)
    # fish_system_model.add_constraint('average_area',equals=0.13907782)
    eel_height = fish_system_model.declare_variable('eel_height',shape=(num_pts_L,))
    tail_width = fish_system_model.register_output('tail_width', eel_height[-1])
    head_width = fish_system_model.register_output('head_width', eel_height[0])

    
    fish_mp_model.add(fish_system_model, name=f'fish_system_model_{i}', promotes=[]) 
    fish_mp_model.connect('control_points', f'fish_system_model_{i}'+'.control_points')
    fish_mp_model.connect(f'tail_frequency_{i}', f'fish_system_model_{i}'+'.tail_frequency')
    fish_mp_model.connect(f'amplitude_max_{i}', f'fish_system_model_{i}'+'.amplitude_max')

    fish_mp_model.add_design_variable(f'tail_frequency_{i}',upper=lower*12,lower=lower*.5)
    fish_mp_model.add_design_variable(f'amplitude_max_{i}',upper=lower*2,lower=lower*0.1)

    fish_mp_model.add_constraint(f'fish_system_model_{i}'+'.thrust_coeff_avr',equals=0.,scaler=1e2)
    fish_mp_model.add_constraint(f'fish_system_model_{i}'+'.average_area',equals=0.13907782)
    fish_mp_model.add_constraint(f'fish_system_model_{i}'+'.head_width',upper=0.01)
    fish_mp_model.add_constraint(f'fish_system_model_{i}'+'.tail_width',lower=0.05)
    fish_mp_model.add_constraint(f'fish_system_model_{i}'+'.eel_CoM_x',upper=0.6,lower=0.4)


fish_mp_model.add_design_variable('control_points',upper=0.2,lower=0.03)

eff0 = fish_mp_model.declare_variable('fish_system_model_0.efficiency',shape=(1,)) * 1.
eff1 = fish_mp_model.declare_variable('fish_system_model_1.efficiency',shape=(1,)) * 1.

sum_eff = eff0 + eff1
fish_mp_model.register_output('sum_eff', sum_eff)


fish_mp_model.add_objective('sum_eff',scaler=-1)


# total_eff = sum(sum_eff)    

# fish_mp_model.register_output('sum_eff', total_eff)    

sim = Simulator(fish_mp_model)

if run_opt == False:
    sim.run()

if run_opt == True:
    simulator = Simulator(fish_mp_model, display_scripts=False)
    simulator.run()    
    #####################
    # optimizaton
    #####################
    from modopt.csdl_library import CSDLProblem

    from modopt.snopt_library import SNOPT
    # Define problem for the optimization
    prob = CSDLProblem(
        problem_name=problem_name,
        simulator=simulator,
    )
    # optimizer = SLSQP(prob, maxiter=1)
    optimizer = SNOPT(
        prob, 
        Major_iterations=120,
        Major_optimality=1e-7,
        Major_feasibility=1e-7,
        append2file=True,
        Major_step_limit=.1,
    )

    optimizer.solve()
    optimizer.print_results(summary_table=True)



exit()

plt.figure()
plt.plot(total_forces_profile)
plt.show()

if run_opt == True:
    case_name = '_'+problem_name+'.txt'

    np.savetxt('results/thrust'+case_name,thrust) 
    np.savetxt('results/tail_frequency'+case_name,simulator["tail_frequency"])
    np.savetxt('results/amplitude_max'+case_name,simulator["amplitude_max"])
    np.savetxt('results/efficiency'+case_name,simulator["efficiency"])
    np.savetxt('results/panel_total_power'+case_name,simulator["panel_total_power"])
    np.savetxt('results/thrust_power'+case_name,simulator["thrust_power"])

##############################################################################################

from mpl_toolkits.mplot3d import Axes3D
import time

# Example data: A list of arrays, where each array represents a time step
# Replace this with your actual data

def axis_equal(ax, x, y, z):
    # Calculate the center and the range of the data in each dimension
    max_range = np.array([x.max()-x.min(), y.max()-y.min(), z.max()-z.min()]).max() / 2.0
    mid_x = (x.max()+x.min()) * 0.5
    mid_y = (y.max()+y.min()) * 0.5
    mid_z = (z.max()+z.min()) * 0.5
    # Set the limits so that the range is the same and centered around the data
    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)  


plt.ion()  # Turn on interactive mode
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')



filenames = []
for i in range(num_time_steps):
    ax.clear()  # Clear previous points
    axis_equal(ax, simulator['eel'][:,:,:,0], simulator['eel'][:,:,:,1], simulator['eel'][:,:,:,2])
    data = simulator['eel'][i]
    x = data[:,:,0].flatten()
    y = data[:,:,1].flatten()
    z = data[:,:,2].flatten()
    ax.scatter(x, y, z)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    velocity_data = simulator['eel_coll_vel'][i]
    u = velocity_data[:, :, 0].flatten()  # Velocity components in x
    v = velocity_data[:, :, 1].flatten()  # Velocity components in y
    w = velocity_data[:, :, 2].flatten()  # Velocity components in z
    # Scatter plot for the mesh points
    ax.scatter(x, y, z, color='b')
    # Adding velocity arrows
    panel_center = (0.25*(simulator['eel'][i, 0:-1, 0:-1, :] + simulator['eel'][i, 0:-1, 1:, :] + simulator['eel'][i, 1:, 0:-1, :] + simulator['eel'][i, 1:, 1:, :])).reshape(-1, 3)
    ax.quiver(panel_center[:,0], panel_center[:,1], panel_center[:, 2],
                    u, v, w, color='r')
    # change the view angle to x,y plane
    # ax.view_init(90, -90)
    plt.draw()
    plt.pause(0.1)  # Pause to update the plot
    time.sleep(0.01)  # Adjust as per your time step's actual duration
    # Save the current frame
    filename = problem_name+f'frame_{i}.png'
    plt.savefig(filename, dpi=200)
    filenames.append(filename)

import imageio
import os
# Create a GIF
with imageio.get_writer("my_animation"+problem_name+".gif", mode='I', duration=0.1) as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)

# Remove files
# for filename in filenames:
#     os.remove(filename)

plt.ioff()  # Turn off interactive mode
plt.show()

x_np = np.linspace(1e-3,1, num_amp_cp)
control_points_inital = (x_np + 0.03) / (1+0.03) * 0.125
x =  simulator['eel'][0,:,2,0]

plt.figure()
plt.plot(x_np, simulator['eel_amplitude_cp'],'.')
plt.plot(x,simulator['amplitude'])
plt.show()