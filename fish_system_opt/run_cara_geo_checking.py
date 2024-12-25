import numpy as np

import csdl
from python_csdl_backend import Simulator
from fish_system_opt.submodels.fish_geometry_model_carangiform import FishGeometryModel
from fish_system_opt.submodels.fish_kinematics_model_poly import EelKinematicsModel
from fish_system_opt.submodels.fish_geometry_model import EelGeometryModel

from fish_system_opt.submodels.com_model import CoMModel
# from fish_system_opt.submodels.fish_kinematics_model import EelKinematicsModel

from VAST.core.submodels.friction_submodels.eel_viscous_force_3x import EelViscousModel
from VAST.core.vlm_llt.vlm_dynamic_old.VLM_prescribed_wake_solver import UVLMSolver
from VAST.core.submodels.output_submodels.vlm_post_processing.efficiency import EfficiencyModel


import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = False

def run_fish_sim(num_pts_L, num_pts_R,num_time_steps, v_x_val, tail_frequency_val, amp_max, num_period,num_points_list,run_opt=False, del_sim=False,problem_name='kin_opt'):
    #########################################
    # solver specific parameters
    #########################################
    surface_name = 'fish'
    L = 1.0

    surface_shape = (num_pts_L,num_pts_R, 3) # shape of the fish mesh

    # num_time_steps = 60
    # shape to input to the fish hydrodynamic solver model:
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
    # inputs to the sub fish_geometry_model
    #########################################
    fish_system_model.create_input('L', val=L)

    #########################################
    # inputs to the sub kinematics model
    #########################################
    tail_frequency_csdl = fish_system_model.declare_variable('tail_frequency',val=tail_frequency_val)
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
    fish_amplitude_cp_val  = np.array([0.02, -0.08, 0.16, 0])
    fish_system_model.create_input('fish_amplitude_cp', val=fish_amplitude_cp_val)
    fish_system_model.declare_variable('amplitude_max', val=amp_max)

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
    # fish_geometry_model = FishGeometryModel(surface_name=surface_name,
    #                                         surface_shape=surface_shape,
    #                                         num_points_list=num_points_list)
    s_1_ind = 5
    s_2_ind = num_pts_L-3    
    fish_geometry_model = EelGeometryModel(surface_name=surface_name,
                                            surface_shape=surface_shape,
                                            s_1_ind=s_1_ind,s_2_ind=s_2_ind)

    fish_system_model.add(fish_geometry_model, name='FishGeometryModel')

    #########################################
    # add CoM model
    #########################################
    fish_system_model.add(CoMModel(surface_names=[surface_name], surface_shapes=[surface_shape]), 'CoMModel')

    # # add kinematics model
    fish_kinematics_model = EelKinematicsModel(surface_name=surface_name,
                                                surface_shape=surface_shape,    
                                                num_period=num_period,
                                                num_time_steps=num_time_steps,
                                                num_amp_cp=fish_amplitude_cp_val.size)                                       
    fish_system_model.add(fish_kinematics_model, name='EelKinematicsModel')

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

    return fish_system_model


run_opt = True
v_x_val = 1.
num_time_steps = 70
problem_name = 'kinematics_opt_0213_24_v10_old_geo'

# tail_frequency_val = 0.227513  
# tail_frequency_val = 0.224355
tail_frequency_val = 1.098151

amp_max = 0.05

num_pts_R = 5
num_pts_L = 41
L = 1.0
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

model = csdl.Model()
tail_frequency_csdl = model.create_input('tail_frequency',val=tail_frequency_val)
amplitude_max =     model.create_input('amplitude_max', val=amp_max)


model.create_input('x1', val=x1_val)
model.create_input('h1', val=h1_val)
model.create_input('x2', val=x2_val)
model.create_input('h2', val=h2_val)
model.create_input('tail_width', val=tail_width_val)
fish_system_model= run_fish_sim(num_pts_L=num_pts_L, num_pts_R=num_pts_R,num_time_steps=num_time_steps,
                                            v_x_val=v_x_val, tail_frequency_val=tail_frequency_val, amp_max=amp_max, 
                                            num_period=num_period, num_points_list=num_points_list,
                                            run_opt=run_opt,problem_name=problem_name)

np_ignore  = 1

thrust = fish_system_model.declare_variable('thrust',shape=(num_time_steps,1))[int(num_time_steps/num_period)*np_ignore:,:]
C_F = fish_system_model.declare_variable('C_F')
area = fish_system_model.declare_variable('fish_s_panel',shape=(num_time_steps,int((num_pts_L-1)*(num_pts_R-1))))
avg_area = csdl.sum(area)/num_time_steps
density = fish_system_model.declare_variable('desity', shape=(num_time_steps,1))
v_x = fish_system_model.declare_variable('v_x')
avg_C_T = -csdl.sum(thrust)/(0.5*csdl.reshape(density[0,0],(1,))*v_x**2*avg_area)/(num_time_steps-int(num_time_steps/num_period)*np_ignore)
fish_system_model.register_output('avg_C_T', avg_C_T)
thrust_coeff_avr = (avg_C_T - C_F)**2    
fish_system_model.print_var(C_F)
fish_system_model.print_var(avg_C_T)

com_x = fish_system_model.declare_variable('fish_CoM_x')*1.

panel_total_power = fish_system_model.declare_variable('panel_total_power') * 1.
fish_system_model.register_output('sum_power', panel_total_power)



fish_system_model.register_output('thrust_coeff_avr', thrust_coeff_avr)
# fish_system_model.add_constraint('thrust_coeff_avr',equals=0.,scaler=1e2)
# fish_system_model.add_constraint('fish_CoM_x',upper=0.55,lower=0.45)
#########################################
fish_system_model.register_output('average_area', avg_area)
# fish_system_model.add_constraint('average_area',equals=0.13907782)
# fish_height = fish_system_model.declare_variable('fish_height',shape=(num_pts_L,))
# fish_system_model.register_output('tail_width', fish_height[-1])
#########################################
efficiency = fish_system_model.declare_variable('efficiency')
fish_system_model.print_var(efficiency)

model.add(fish_system_model, 'FishSystemModel')

model.add_design_variable('tail_frequency',upper=2.,lower=0.1)
model.add_design_variable('amplitude_max',upper=0.3,lower=0.01)

model.add_objective('sum_power')

model.add_constraint('thrust_coeff_avr',equals=0.,scaler=1e2)
model.add_constraint('fish_CoM_x',upper=0.55,lower=0.45)


simulator = Simulator(model, display_scripts=False)
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
        Major_step_limit=.5,
    )

    optimizer.solve()
    optimizer.print_results(summary_table=True)

