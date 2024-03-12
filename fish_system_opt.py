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

#########################################
# solver specific parameters
#########################################
surface_name = 'eel'
num_pts_L = 41
num_pts_R = 5
L = 1.0
s_1_ind = 5
s_2_ind = num_pts_L-3
tail_frequency_val = 0.48
v_x_val = 0.2

num_period = 2
surface_shape = (num_pts_L,num_pts_R, 3) # shape of the fish mesh

num_time_steps = 50
# shape to input to the fish hydrodynamic solver model:
surface_shapes = [(num_time_steps, num_pts_L, num_pts_R, 3)] 
surface_properties_dict = {'surface_names':[surface_name],
                            'surface_shapes':[surface_shape],
                            'frame':'wing_fixed',}
states_dict = {
    'v': np.zeros((num_time_steps, 1)), 'w': np.ones((num_time_steps, 1))*v_x_val,
    'p': np.zeros((num_time_steps, 1)), 'q': np.zeros((num_time_steps, 1)), 'r': np.zeros((num_time_steps, 1)),
    'theta': np.zeros((num_time_steps, 1)), 'psi': np.zeros((num_time_steps, 1)),
    'x': np.zeros((num_time_steps, 1)), 'y': np.zeros((num_time_steps, 1)), 'z': np.zeros((num_time_steps, 1)),
    'phiw': np.zeros((num_time_steps, 1)), 'gamma': np.zeros((num_time_steps, 1)),'psiw': np.zeros((num_time_steps, 1)),
}

# TODO: check if this work, also for how v_x is given to the hydrodynamic model
h_stepsize = tail_frequency_val * num_period / (num_time_steps-1)
#######################################################################################

#######################################################################################
# set up a fish system model
fish_system_model = csdl.Model()

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
fish_system_model.add(EelViscousModel(),name='EelViscousModel')

fish_system_model.add(UVLMSolver(num_times=num_time_steps,h_stepsize=h_stepsize,states_dict=states_dict,
                                    surface_properties_dict=surface_properties_dict), 'fish_model')
ode_surface_shapes = [(num_time_steps, ) + surface_shape]
fish_system_model.add(EfficiencyModel(surface_names=[surface_name], surface_shapes=ode_surface_shapes,n_ignore=int(num_time_steps/num_period)),name='EfficiencyModel')

#######################################################################################
# inputs to the fish_system_model
#######################################################################################

#########################################
# inputs to the sub eel_geometry_model
#########################################
fish_system_model.create_input('L', val=L)
fish_system_model.create_input('a_coeff', val=0.55)
fish_system_model.create_input('b_coeff', val=0.08)

#########################################
# inputs to the sub kinematics model
#########################################
fish_system_model.create_input('tail_amplitude',val=0.125)
fish_system_model.create_input('tail_frequency',val=tail_frequency_val)
fish_system_model.create_input('wave_length',val=1.0)
fish_system_model.create_input('amplitude_profile_coeff',val=0.03125)

#########################################
# inputs to viscous model
#########################################
fish_system_model.create_input('v_x',val=v_x_val)

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

exit()
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

