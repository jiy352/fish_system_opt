import numpy as np

import csdl
from python_csdl_backend import Simulator
from submodels.fish_geometry_model import EelGeometryModel
from submodels.fish_kinematics_model import EelKinematicsModel

from VAST.core.submodels.friction_submodels.eel_viscous_force import EelViscousModel
from VAST.core.vlm_llt.vlm_dynamic_old.VLM_prescribed_wake_solver import UVLMSolver
from VAST.core.submodels.output_submodels.vlm_post_processing.efficiency import EfficiencyModel


# script for the optimization of the fish system (try to finish within 100-150 lines)

# [optimizer] -> optimization variables
# -> [geometry, kinematics]-> fish mesh, mesh velocity
# -> [hydrodynamics (VLM), viscous drag] -> forces ->powers
# -> [elasticity] -> elastic energy
# -> [battery sizing]
# -> [power estimation]->efficiency
run_opt = True
#########################################
# solver specific parameters
#########################################
surface_name = 'eel'
num_pts_L = 51
num_pts_R = 5
L = 2.0
s_1_ind = 5
s_2_ind = num_pts_L-3
tail_frequency_val = 0.48
v_x_val = .5

num_period = 2
surface_shape = (num_pts_L,num_pts_R, 3) # shape of the fish mesh

num_time_steps = 70
# shape to input to the fish hydrodynamic solver model:
surface_shapes = [(num_time_steps, num_pts_L, num_pts_R, 3)] 
surface_properties_dict = {'surface_names':[surface_name],
                            'surface_shapes':[surface_shape],
                            'frame':'wing_fixed',}
ode_surface_shapes = [(num_time_steps, ) + surface_shape]
    
# default all nessary states to zero, except for u, which is expanded from v_x
state_names = ['v', 'w', 'p', 'q', 'r', 'theta', 'psi', 'x', 'y', 'z', 'phiw', 'gamma', 'psiw']
states_dict = {state: np.zeros((num_time_steps, 1)) for state in state_names}

# TODO: check if this work, also for how v_x is given to the hydrodynamic model
h_stepsize = num_period/ tail_frequency_val / (num_time_steps-1)
print('h_stepsize is',h_stepsize)
#######################################################################################

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
fish_system_model.create_input('a_coeff', val=0.51)
fish_system_model.create_input('b_coeff', val=0.08)

#########################################
# inputs to the sub kinematics model
#########################################
fish_system_model.create_input('tail_amplitude',val=0.125)
fish_system_model.create_input('tail_frequency',val=tail_frequency_val)
fish_system_model.create_input('wave_length',val=1.)
fish_system_model.create_input('amplitude_profile_coeff',val=0.03125)

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

# add kinematics model
eel_kinematics_model = EelKinematicsModel(surface_name=surface_name,
                                            surface_shape=surface_shape,    
                                            num_period=num_period,
                                            num_time_steps=num_time_steps)
fish_system_model.add(eel_kinematics_model, name='EelKinematicsModel')

#########################################
# add hydrodynamics model
#########################################

fish_system_model.add(UVLMSolver(num_times=num_time_steps,h_stepsize=h_stepsize,states_dict=states_dict,
                                    surface_properties_dict=surface_properties_dict), 'fish_model')
fish_system_model.add(EfficiencyModel(surface_names=[surface_name], surface_shapes=ode_surface_shapes,
                                        n_ignore=int(num_time_steps/num_period)),name='EfficiencyModel')
fish_system_model.add(EelViscousModel(surface_shapes=ode_surface_shapes),name='EelViscousModel')

#########################################
if run_opt == True:
    fish_system_model.add_design_variable('tail_amplitude',upper=0.4,lower=0.05)
    fish_system_model.add_design_variable('tail_frequency',upper=2.,lower=0.1)
    fish_system_model.add_design_variable('v_x',upper=v_x_val,lower=v_x_val)
    fish_system_model.add_design_variable('wave_length',upper=2,lower=0.5)
    fish_system_model.add_design_variable('amplitude_profile_coeff',upper=0.03125*3,lower=0.03125*0.5)
    fish_system_model.add_design_variable('L',upper=3,lower=0.3)
    fish_system_model.add_design_variable('a_coeff',upper=0.51*1.5,lower=0.51*1)
    fish_system_model.add_design_variable('b_coeff',upper=0.08*5,lower=0.08*0.2)
    # add objective
    fish_system_model.add_objective('efficiency',scaler=-1)
    # add constraint
    #########################################sim[]

    thrust = fish_system_model.declare_variable('thrust',shape=(num_time_steps,1))
    C_F = fish_system_model.declare_variable('C_F')
    area = fish_system_model.declare_variable('eel_s_panel',shape=(num_time_steps,int((num_pts_L-1)*(num_pts_R-1))))
    avg_area = csdl.sum(area)/num_time_steps
    avg_C_T = -csdl.sum(thrust)/(0.5*csdl.reshape(density[0,0],(1,))*v_x**2*avg_area)/num_time_steps
    fish_system_model.register_output('avg_C_T', avg_C_T)
    thrust_coeff_avr = (avg_C_T - C_F)**2    
    fish_system_model.print_var(avg_area)

    fish_system_model.register_output('thrust_coeff_avr', thrust_coeff_avr)
    fish_system_model.add_constraint('thrust_coeff_avr',equals=0.)
    #########################################
    fish_system_model.register_output('average_area', avg_area)
    fish_system_model.add_constraint('average_area',equals=0.134)
    #########################################

    simulator = Simulator(fish_system_model, display_scripts=False)
    simulator.run()

    #####################
    # optimizaton
    #####################
    from modopt.csdl_library import CSDLProblem

    from modopt.snopt_library import SNOPT
    # Define problem for the optimization
    prob = CSDLProblem(
        problem_name='eel_full_system_optimization',
        simulator=simulator,
    )
    # optimizer = SLSQP(prob, maxiter=1)
    optimizer = SNOPT(
        prob, 
        Major_iterations=30,
        # Major_optimality=1e-6,
        Major_optimality=1e-7,
        # Major_feasibility=1e-5,
        Major_feasibility=1e-4,
        append2file=True,
        Major_step_limit=.1,
    )

    optimizer.solve()
    optimizer.print_results(summary_table=True)
#########################################
else:
    #########################################
    # attach fish system model to simulator
    #########################################
    simulator = Simulator(fish_system_model, display_scripts=False)
    simulator.run()
    # simulator.check_partials(compact_print=True)
    #########################################

# fish_system_model.add(FishHydrodynamicsModel, name='fish_hydrodynamics')
# fish_system_model.add(FishElasticityModel, name='fish_elasticity')
# fish_system_model.add(FishBatteryModel, name='fish_battery')
# fish_system_model.add(FishPowerModel, name='fish_power')

# exit()

print('################### optimizaton results ######################')
print('efficiency is',simulator['efficiency'])

print('v_x is',simulator['v_x'])
print('tail amplitude is',simulator['tail_amplitude'])
print('tail frequency is',simulator['tail_frequency'])
print('wave length is',simulator['wave_length'])
print('a coeff is',simulator['a_coeff'])
print('b coeff is',simulator['b_coeff'])
print('L is',simulator['L'])
print('amplitude profile coeff is',simulator['amplitude_profile_coeff'])

#########################################
# plot the fish mesh and the velocity
#########################################

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
plt.rcParams['text.usetex'] = False
from utils.plots import axis_equal,plot3d

plt.ion()  # Turn on interactive mode
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

plot3d(ax, simulator['eel'], simulator['eel_coll_vel'], ax)

