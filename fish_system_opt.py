import csdl
from python_csdl_backend import Simulator

# script for the optimization of the fish system (try to finish within 100-150 lines)

# [optimizer] -> optimization variables
# -> [geometry, kinematics]-> fish mesh, mesh velocity
# -> [hydrodynamics (VLM), viscous drag] -> forces ->powers
# -> [elasticity] -> elastic energy
# -> [battery sizing]
# -> [power estimation]->efficiency

# set up a fish system model
fish_system_model = csdl.Model()

# add geometry and kinematics model
# generate initial rigid fish mesh

fish_system_model.add(FishGeomeryKinematicsModel, name='fish_geom_kinematics')


# fish_system_model.add(FishHydrodynamicsModel, name='fish_hydrodynamics')
# fish_system_model.add(FishElasticityModel, name='fish_elasticity')
# fish_system_model.add(FishBatteryModel, name='fish_battery')
# fish_system_model.add(FishPowerModel, name='fish_power')
