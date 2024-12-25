import numpy as np

import csdl
from python_csdl_backend import Simulator
from fish_system_opt.submodels.fish_geometry_model import EelGeometryModel
from fish_system_opt.submodels.fish_kinematics_model_poly import EelKinematicsModel
from fish_system_opt.submodels.fish_turn_kinematics_model import EelKinematicsModel as EelKinematicsModelTurn
# from fish_system_opt.submodels.fish_kinematics_model import EelKinematicsModel

from VAST.core.submodels.friction_submodels.eel_viscous_force_3x import EelViscousModel
from VAST.core.vlm_llt.vlm_dynamic_old.VLM_prescribed_wake_solver import UVLMSolver
from VAST.core.submodels.output_submodels.vlm_post_processing.efficiency import EfficiencyModel

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
plt.rcParams['text.usetex'] = False

def run_fish_sim(num_pts_L, num_pts_R,num_time_steps, v_x_val, tail_frequency_val, amp_max, num_period, run_opt=False, del_sim=False,turn=False,problem_name='kin_opt'):
    #########################################
    # solver specific parameters
    #########################################
    surface_name = 'eel'
    L = 1.0
    s_1_ind = 5
    s_2_ind = num_pts_L-3

    surface_shape = (num_pts_L,num_pts_R, 3) # shape of the fish mesh

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
    a = 0.51
    b = 0.08
    num_cp = 6

    #########################################
    # inputs to the sub kinematics model
    #########################################

    #########################################
    # inputs to the sub kinematics model
    #########################################
    tail_frequency_csdl = fish_system_model.create_input('tail_frequency',val=tail_frequency_val)
    h_stepsize = num_period/ tail_frequency_csdl / (num_time_steps-1)

    fish_system_model.register_output('delta_t', h_stepsize)

    ########################################
    # Timestep vector
    ########################################
    h_vec = csdl.expand(h_stepsize,shape=(num_time_steps-1,))
    h = fish_system_model.register_output('h', h_vec)
    #########################################    
    fish_system_model.create_input('wave_length',val=0.95)

    #########################################
    # eel_amplitude_cp_val  = np.array([0.02, -0.08, 0.16, 0])

    coeff_const = fish_system_model.declare_variable('coeff_const', val=0.02)
    coeff_linear = fish_system_model.declare_variable('coeff_linear', val=-0.08)
    coeff_quad = coeff_linear * (-2.)

    # eel_amplitude_cp = fish_system_model.create_output('eel_amplitude_cp', shape=(4,), val=0.)
    # eel_amplitude_cp[0] = coeff_const
    # eel_amplitude_cp[1] = coeff_linear
    # eel_amplitude_cp[2] = coeff_quad
    
    # fish_system_model.create_input('eel_amplitude_cp', val=eel_amplitude_cp_val)
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
                                            s_1_ind=s_1_ind,s_2_ind=s_2_ind)
    fish_system_model.add(eel_geometry_model, name='EelGeometryModel')

    #########################################
    # add CoM model
    #########################################
    # fish_system_model.add(CoMModel(surface_names=[surface_name], surface_shapes=[surface_shape]), 'CoMModel')

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
                                        surface_properties_dict=surface_properties_dict,symmetry=False), 'fish_model')
    fish_system_model.add(EfficiencyModel(surface_names=[surface_name], surface_shapes=ode_surface_shapes,
                                            n_ignore=int(num_time_steps/num_period)*np_ignore),name='EfficiencyModel')
    try:
        fish_system_model.add(EelViscousModel(surface_shapes=ode_surface_shapes),name='EelViscousModel')
    except:
        fish_system_model.add(EelViscousModel(),name='EelViscousModel')

    # efficiency = fish_system_model.declare_variable('efficiency', shape=(1,))

    return fish_system_model#, efficiency

# thrust, avg_C_T, simulator = run_fish_sim(num_pts_L=41, num_pts_R=5,num_time_steps=70,
#              v_x_val=1., tail_frequency_val=1.08, amp_max=0.1, 
#              num_period=2, run_opt=True)

##############################################################################################
# for 3 x friction
# thrust, avg_C_T, simulator = run_fish_sim(num_pts_L=41, num_pts_R=5,num_time_steps=70,
#              v_x_val=1., tail_frequency_val=1.135, amp_max=0.13, 
#              num_period=2, run_opt=True)
run_opt = False
num_pts_L_list = np.array([11,21,31,41,51]).astype(int)
# num_pts_L_list = np.array([11,21,31,41,51]).astype(int)
num_pts_R_list = ((num_pts_L_list - 1) / 10 + 1).astype(int)

num_time_steps_list = np.array([10,20,30,40,50,60,70])

v_x_val_list = 0.5 * np.ones(num_pts_R_list.shape)
num_period = 2
avg_C_T_list = []
sim_list = []
problem_name = 'mesh_convergence_test_1112'
# test = 'mesh_grid'
test = 'mesh_grid'

if test == 'mesh_grid':
    for i in np.arange(len(num_pts_L_list)):
        num_pts_L = num_pts_L_list[i]
        num_pts_R = num_pts_R_list[i]
        v_x_val = v_x_val_list[i]
        num_time_steps = num_time_steps_list[-1]
        fish_system_model = run_fish_sim(num_pts_L=num_pts_L, num_pts_R=num_pts_R,num_time_steps=num_time_steps,
                    v_x_val=v_x_val, tail_frequency_val=0.35354, amp_max=0.15, 
                    num_period=num_period, run_opt=run_opt,problem_name=problem_name)
        np_ignore  = 1

        thrust = fish_system_model.declare_variable('thrust',shape=(num_time_steps,1))[int(num_time_steps/num_period)*np_ignore:,:]
        C_F = fish_system_model.declare_variable('C_F')
        area = fish_system_model.declare_variable('eel_s_panel',shape=(num_time_steps,int((num_pts_L-1)*(num_pts_R-1))))
        avg_area = csdl.sum(area)/num_time_steps
        density = fish_system_model.declare_variable('density',val=np.ones((num_time_steps,1))*997)
        avg_C_T = -csdl.sum(thrust)/(0.5*csdl.reshape(density[0,0],(1,))*v_x_val_list[i]**2*avg_area)/(num_time_steps-int(num_time_steps/num_period)*np_ignore)
        fish_system_model.register_output('avg_C_T', avg_C_T)

        simulator = Simulator(fish_system_model, display_scripts=True)
        simulator.run()
        avg_C_T = simulator["avg_C_T"]
        avg_C_T_list.append(avg_C_T)
        sim_list.append(simulator)


elif test == 'time_grid':
    for i in np.arange(len(num_time_steps_list)):
        num_time_steps = num_time_steps_list[i]
        print(num_time_steps)
        # exit()
        num_pts_L = 41
        num_pts_R = 5
        v_x_val = v_x_val_list[0]
        fish_system_model = run_fish_sim(num_pts_L=num_pts_L, num_pts_R=num_pts_R,num_time_steps=num_time_steps_list[i],
                    v_x_val=v_x_val, tail_frequency_val=0.35354, amp_max=0.15, 
                    num_period=num_period, run_opt=run_opt,problem_name=problem_name)
        np_ignore  = 1

        thrust = fish_system_model.declare_variable('thrust',shape=(num_time_steps,1))[int(num_time_steps/num_period)*np_ignore:,:]
        C_F = fish_system_model.declare_variable('C_F')
        area = fish_system_model.declare_variable('eel_s_panel',shape=(num_time_steps,int((num_pts_L-1)*(num_pts_R-1))))
        avg_area = csdl.sum(area)/num_time_steps
        density = fish_system_model.declare_variable('density',val=np.ones((num_time_steps,1))*997)
        avg_C_T = -csdl.sum(thrust)/(0.5*csdl.reshape(density[0,0],(1,))*v_x_val**2*avg_area)/(num_time_steps-int(num_time_steps/num_period)*np_ignore)
        fish_system_model.register_output('avg_C_T', avg_C_T)

        simulator = Simulator(fish_system_model, display_scripts=True)
        simulator.run()
        avg_C_T = simulator["avg_C_T"]
        avg_C_T_list.append(avg_C_T)
        sim_list.append(simulator)


plt.figure()
if test == 'mesh_grid':
    plt.plot(num_pts_L_list, avg_C_T_list,'.-')
    plt.xlabel('number of points in longitudinal direction')

else:
    plt.plot(num_time_steps_list, avg_C_T_list,'.-')
    plt.xlabel('number of time steps')
    
# use latex for the labels
plt.rcParams['text.usetex'] = False
plt.ylabel(r'average $C_T$')
plt.tight_layout()
plt.ylim([-0.06, -0.02])
# size of the figure
plt.rcParams["figure.figsize"] = (5,4)
plt.show()






