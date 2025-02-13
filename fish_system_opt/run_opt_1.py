import numpy as np

import csdl
from python_csdl_backend import Simulator
# from fish_system_opt.submodels.fish_geometry_model_bspline import EelGeometryModel
from fish_system_opt.submodels.fish_geometry_model_carangiform import FishGeometryModel
from fish_system_opt.submodels.fish_kinematics_model_poly_new import EelKinematicsModel
from fish_system_opt.submodels.fish_turn_kinematics_model import EelKinematicsModel as EelKinematicsModelTurn
# from fish_system_opt.submodels.fish_kinematics_model import EelKinematicsModel

from VAST.core.submodels.friction_submodels.eel_viscous_force import EelViscousModel
from VAST.core.vlm_llt.vlm_dynamic_old.VLM_prescribed_wake_solver import UVLMSolver
from VAST.core.submodels.output_submodels.vlm_post_processing.efficiency import EfficiencyModel
from fish_system_opt.submodels.com_model_carangifrom import CoMModel

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
plt.rcParams['text.usetex'] = False

def run_fish_sim(num_pts_L, num_pts_R,num_time_steps, v_x_val, tail_frequency_val, num_period, num_points_list, run_opt=False, del_sim=False,turn=False,problem_name='kin_opt'):
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
    state_names = ['v', 'w', 'p', 'q', 'r', 'theta', 'psi','phiw', 'gamma', 'psiw']
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
    eel_geometry_model = FishGeometryModel(surface_name=surface_name,
                                            surface_shape=surface_shape,
                                            num_points_list=num_points_list)
    fish_system_model.add(eel_geometry_model, name='EelGeometryModel')

    #########################################
    # add CoM model
    #########################################
    fish_system_model.add(CoMModel(surface_names=[surface_name], surface_shapes=[surface_shape]), 'CoMModel')


    # # add kinematics model
    if turn == False:
        eel_kinematics_model = EelKinematicsModel(surface_name=surface_name,
                                                    surface_shape=surface_shape,    
                                                    num_period=num_period,
                                                    num_time_steps=num_time_steps,
                                                    num_amp_cp=4)                                       
        fish_system_model.add(eel_kinematics_model, name='EelKinematicsModel')
        
    else:
        eel_kinematics_model = EelKinematicsModelTurn(surface_name=surface_name,
                                                    surface_shape=surface_shape,
                                                    num_period=num_period,
                                                    num_time_steps=num_time_steps)  
                                             
        fish_system_model.add(eel_kinematics_model, name='EelKinematicsModel')        
        theta_max = fish_system_model.declare_variable('theta_max', val=np.pi/48)

    #########################################
    # add hydrodynamics model
    #########################################
    np_ignore  = 1  

    fish_system_model.add(UVLMSolver(num_times=num_time_steps,states_dict=states_dict,
                                        surface_properties_dict=surface_properties_dict), 'fish_model')
    fish_system_model.add(EfficiencyModel(surface_names=[surface_name], surface_shapes=ode_surface_shapes,
                                            n_ignore=int(num_time_steps/num_period)*np_ignore),name='EfficiencyModel')
    try:
        fish_system_model.add(EelViscousModel(surface_shapes=ode_surface_shapes),name='EelViscousModel')
    except:
        fish_system_model.add(EelViscousModel(),name='EelViscousModel')

    # efficiency = fish_system_model.declare_variable('efficiency', shape=(1,))

    return fish_system_model#, efficiency

    ##############################################
    

run_opt = True
problem_name = 'kin_opt_1_v03_again'
# amplitude_scalar_0_var = 0.9
# v_x_list = np.array([0.2]) # saved as v03...
v_x_list = np.array([.3])
# v_x_list = np.array([1.])
# v_x_list = np.array([0.5])
turn_list = np.array([False,])

# amplitude_scalar_0_var = 0.4 #0.2
# tail_frequency_list = np.array([0.296,]) #0.2

# amplitude_scalar_0_var = 0.6 #0.6
amplitude_scalar_0_var =  0.3
# amplitude_scalar_0_var =  0.2203364
# tail_frequency_list = np.array([0.26225,]) #0.2
# tail_frequency_list = np.array([0.505585,]) #0.2
# tail_frequency_list = np.array([0.984,]) #0.2
# tail_frequency_list = np.array([1.223]) #0.2
# tail_frequency_list = np.array([1.46]) #0.2
tail_frequency_list = np.array([.48]) #0.2

# for turn case amp_max does not goes into the model, only frequency and theta_max matters

num_time_steps=70




fish_mp_model = csdl.Model()

#################################
################################

L = 1.0
num_pts_L = 41
num_pts_R = 5
num_period = 2
x1_val = 0.424
h1_val = 0.148
x2_val = 0.837
h2_val = 0.074
tail_width_val = 0.14218215

head_pts = int(num_pts_L * x1_val*L / L)
body_pts = int(num_pts_L * (x2_val-x1_val)*L / L)
tail_pts = num_pts_L - head_pts - body_pts
num_points_list = [head_pts, body_pts, tail_pts]
fish_model_list = []
# height =  b * np.sqrt(1 - ((x - a)/a)**2)
# exit()

num_cp_amp = 4
x = np.linspace(0, 1, num_cp_amp)
x_pts = np.linspace(0, 1, num_pts_L)


# height =  b * np.sqrt(1 - ((x - a)/a)**2)
a_0 = 0.02
a_1 = -0.08
a_2 = 0.16
amp_cp_vals =  np.array([a_0, a_1, a_2,0])

# amplitude_scalar = fish_mp_model.create_input('amplitude_scalar_0',val=0.32294)
amplitude_scalar = fish_mp_model.create_input('amplitude_max_0',val=amplitude_scalar_0_var)

amplitude_cp = fish_mp_model.create_input('eel_amplitude_cp_0', shape=(num_cp_amp,),val=amp_cp_vals)



for i in range(len(v_x_list)):
    tail_frequency_csdl = fish_mp_model.create_input(f'tail_frequency_{i}',val=tail_frequency_list[i])
fish_mp_model.create_input('x1', val=x1_val)
fish_mp_model.create_input('h1', val=h1_val)
fish_mp_model.create_input('x2', val=x2_val)
fish_mp_model.create_input('h2', val=h2_val)
fish_mp_model.create_input('tail_width', val=tail_width_val)


for i in range(len(v_x_list)):
    # problem_name = 'kin_opt_0930_can_10'
    turn = turn_list[i]
    fish_system_model = run_fish_sim(num_pts_L=41, num_pts_R=5,num_time_steps=70,
                v_x_val=v_x_list[i], tail_frequency_val=tail_frequency_list[i], 
                num_points_list=num_points_list,
                num_period=2, run_opt=run_opt,turn=turn, problem_name=problem_name)
    lower=0.2

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

    com_x = fish_system_model.declare_variable('eel_CoM_x')*1.

    fish_system_model.register_output('thrust_coeff_avr', thrust_coeff_avr)
    fish_system_model.print_var(avg_C_T)
    fish_system_model.print_var(C_F)
    fish_system_model.register_output('average_area', avg_area)

    if turn == True:
        a = fish_system_model.declare_variable('a_coeff',val=0.51)
        b = fish_system_model.declare_variable('b_coeff',val=0.08)
        thickness_ratio = 10

        L = fish_system_model.declare_variable('L', val=1.0)

        mass = 997 * np.pi * (b**2) * (L**2) * (-1.*L + 3*a) / (3 * thickness_ratio * a**2)

        # theta_max = fish_system_model.declare_variable('theta_max', val=np.pi/24)
        v_x = fish_system_model.declare_variable('v_x')
        F_total = fish_system_model.declare_variable('panel_forces_all',shape=(num_time_steps,int((num_pts_L-1)*(num_pts_R-1)),3))[int(num_time_steps/num_period)*np_ignore:,:,:]
        Fy = csdl.sum(F_total[:,:,1])/(num_time_steps)
        R = -mass * v_x**2 / Fy
        fish_system_model.register_output('R', R)

    # fish_system_model.add_constraint('thrust_coeff_avr',equals=0.,scaler=1e2)
    # fish_system_model.add_constraint('eel_CoM_x',upper=0.6,lower=0.4)
    # #########################################
    # fish_system_model.register_output('average_area', avg_area)
    # fish_system_model.add_constraint('average_area',equals=0.13907782)
    eel_height = fish_system_model.declare_variable('eel_height',shape=(num_pts_L,))
    # tail_width = fish_system_model.register_output('tail_width', eel_height[-1])
    head_width = fish_system_model.register_output('head_width', eel_height[0])

    
    fish_mp_model.add(fish_system_model, name=f'fish_system_model_{i}', promotes=[]) 
    fish_model_list.append(f'fish_system_model_{i}')

    fish_mp_model.connect('x1', f'fish_system_model_{i}'+'.x1')
    fish_mp_model.connect('h1', f'fish_system_model_{i}'+'.h1')
    fish_mp_model.connect('x2', f'fish_system_model_{i}'+'.x2')
    fish_mp_model.connect('h2', f'fish_system_model_{i}'+'.h2')
    fish_mp_model.connect('tail_width', f'fish_system_model_{i}'+'.tail_width')

    fish_mp_model.connect(f'tail_frequency_{i}', f'fish_system_model_{i}'+'.tail_frequency')
    if turn == True:
        fish_mp_model.connect('theta_max', f'fish_system_model_{i}'+'.theta_max')

    else:
        print(i, turn)
        fish_mp_model.connect(f'eel_amplitude_cp_{i}', f'fish_system_model_{i}'+'.eel_amplitude_cp')
        fish_mp_model.connect(f'amplitude_max_{i}', f'fish_system_model_{i}'+'.amplitude_max')

    fish_mp_model.add_design_variable(f'tail_frequency_{i}',upper=lower*12,lower=lower*.2)
    
    if turn == False:
        # fish_mp_model.add_design_variable(f'amplitude_max_{i}',upper=lower*2,lower=lower*0.08)
        # fish_mp_model.add_design_variable(f'coeff_const_{i}',upper=0.06,lower=0.01)
        # fish_mp_model.add_design_variable(f'coeff_linear_{i}',upper=-0.04,lower=-0.1)
        # fish_mp_model.add_design_variable('ratio',upper=5.,lower=2.)
        fish_mp_model.add_design_variable(f'amplitude_max_{i}',upper=2.0,lower=0.1)

    fish_mp_model.add_constraint(f'fish_system_model_{i}'+'.thrust_coeff_avr',equals=0.,scaler=1e2)
    # fish_mp_model.add_constraint(f'fish_system_model_{i}'+'.average_area',lower=0.13, upper=0.15)
    # fish_mp_model.add_constraint(f'fish_system_model_{i}'+'.head_width',upper=0.01)
    # fish_mp_model.add_constraint(f'fish_system_model_{i}'+'.tail_width',lower=0.02)
    # fish_mp_model.add_constraint(f'fish_system_model_{i}'+'.eel_CoM_x',upper=0.55,lower=0.45)

    if turn == True:
        fish_mp_model.add_design_variable('theta_max',upper=np.pi/12,lower=np.pi/48)
        # fish_mp_model.add_constraint(f'fish_system_model_{i}'+'.R',equals=3)
    

panel_total_power_0 = fish_mp_model.declare_variable('fish_system_model_0.panel_total_power') * 1.

sum_power = panel_total_power_0 #+ panel_total_power_1 + panel_total_power_2 + panel_total_power_3
combined_objective = sum_power*1. #+ 0.25 * R_sq

fish_mp_model.register_output('sum_power', combined_objective)

fish_mp_model.add_objective('sum_power')

simulator = Simulator(fish_mp_model, display_scripts=False)
if run_opt == False:
    simulator.run()

if run_opt == True:
    
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
        Major_iterations=80,
        Major_optimality=1e-7,
        Major_feasibility=1e-7,
        append2file=True,
        Major_step_limit=.1,
    )

    optimizer.solve()
    optimizer.print_results(summary_table=True)

if run_opt:
    case_name = '_' + problem_name + '.csv'
    
    # List of available models (you can dynamically identify them)
    available_models = fish_model_list
    available_models = sorted(set(available_models))  # Remove duplicates and sort
    
    # Data and headers
    data = []
    header = []
    
    for model in available_models:
        # Dynamically add each model's data and headers
        try:
            data.append(simulator[f"{model}.tail_frequency"].reshape(-1, 1))
            header.append(f"{model}_tail_frequency")
        except:
            pass
        
        try:
            data.append(simulator[f"{model}.amplitude_max"].reshape(-1, 1))
            header.append(f"{model}_amplitude_max")
        except:
            pass

        try:
            data.append(simulator[f"{model}.theta_max"].reshape(-1, 1))
            header.append(f"{model}_theta_max")
        except:
            pass

        try:
            data.append(simulator[f"{model}.efficiency"].reshape(-1, 1))
            header.append(f"{model}_efficiency")
        except:
            pass

        try:
            data.append(simulator[f"{model}.panel_total_power"].reshape(-1, 1))
            header.append(f"{model}_panel_total_power")
        except:
            pass

        try:
            data.append(simulator[f"{model}.thrust_power"].reshape(-1, 1))
            header.append(f"{model}_thrust_power")
        except:
            pass

    # Stack all the available data into a single array
    if data:  # Check if there is any data to stack
        data = np.hstack(data)
    else:
        data = np.array([])  # No data, create an empty array
    
    # Save all data to one CSV file with headers
    if data.size > 0:
        np.savetxt('results/all_data' + case_name, data, delimiter=",", header=",".join(header), comments='')
    else:
        print("No data to save.")

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

exit()
plt.ion()  # Turn on interactive mode
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

model = 'fish_system_model_0'
name = f"{model}.eel"
filenames = []
for i in range(num_time_steps):
    ax.clear()  # Clear previous points
    axis_equal(ax, simulator[name][:,:,:,0], simulator[name][:,:,:,1], simulator[name][:,:,:,2])
    data = simulator[name][i]
    x = data[:,:,0].flatten()
    y = data[:,:,1].flatten()
    z = data[:,:,2].flatten()
    ax.scatter(x, y, z)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    velocity_data = simulator['fish_system_model_0.eel_coll_vel'][i]
    u = velocity_data[:, :, 0].flatten()  # Velocity components in x
    v = velocity_data[:, :, 1].flatten()  # Velocity components in y
    w = velocity_data[:, :, 2].flatten()  # Velocity components in z
    # Scatter plot for the mesh points
    ax.scatter(x, y, z, color='b')
    # Adding velocity arrows
    panel_center = (0.25*(simulator[name][i, 0:-1, 0:-1, :] + simulator[name][i, 0:-1, 1:, :] + simulator[name][i, 1:, 0:-1, :] + simulator[name][i, 1:, 1:, :])).reshape(-1, 3)
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
x =  simulator[name][0,:,2,0]

plt.figure()
plt.plot(x_np, simulator['eel_amplitude_cp'],'.')
plt.plot(x,simulator['amplitude'])
plt.show()