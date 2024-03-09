import csdl
from python_csdl_backend import Simulator
from submodels.fish_geometry_model import EelGeometryModel

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
surface_shape = (num_pts_L,num_pts_R, 3) # shape of the fish mesh

num_time_steps = 100
# shape to input to the fish hydrodynamic solver model:
surface_shapes = [(num_time_steps, num_pts_L, num_pts_R, 3)] 
#######################################################################################

#######################################################################################
# set up a fish system model
fish_system_model = csdl.Model()

# add geometry and kinematics model
# generate initial rigid fish mesh
eel_geometry_model = EelGeometryModel(surface_name=surface_name,
                                     surface_shape=surface_shape,
                                     s_1_ind=s_1_ind,s_2_ind=s_2_ind)
fish_system_model.add(eel_geometry_model, name='EelGeometryModel')
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
fish_system_model.create_input('L', val=L)
fish_system_model.create_input('a_coeff', val=0.55)
fish_system_model.create_input('b_coeff', val=0.08)

#########################################
# attach fish system model to simulator
#########################################
simulator = Simulator(fish_system_model, display_scripts=False)
simulator.run()
#########################################

# fish_system_model.add(FishHydrodynamicsModel, name='fish_hydrodynamics')
# fish_system_model.add(FishElasticityModel, name='fish_elasticity')
# fish_system_model.add(FishBatteryModel, name='fish_battery')
# fish_system_model.add(FishPowerModel, name='fish_power')


import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = False
plt.figure()
# plt.plot(x, height, '.')
plt.axis('equal')
plt.title('Eel Height Profile')

mesh = simulator['eel_rigid_mesh']
plt.plot(mesh[:,:,0],mesh[:,:,1]+0., '.')

plt.show()