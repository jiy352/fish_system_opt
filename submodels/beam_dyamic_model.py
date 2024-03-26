import numpy as np
import csdl
import python_csdl_backend
from aframe.core.beam_model import BeamModel
from aframe.core.dataclass import Beam, BoundaryCondition, Joint, Material
import matplotlib.pyplot as plt
from ozone.api import ODEProblem
plt.rcParams.update(plt.rcParamsDefault)




class ODEFunction(csdl.Model):

    def initialize(self):
        self.parameters.declare('num_nodes')
        self.parameters.declare('eta_M')
        self.parameters.declare('eta_K')
        self.parameters.declare('beam_name')
        self.parameters.declare('num_beam_nodes')

    def define(self):
        num_nodes = self.parameters['num_nodes']
        num_beam_nodes = self.parameters['num_beam_nodes']
        beam_name = self.parameters['beam_name']

        eta_M = self.parameters['eta_M']
        eta_K = self.parameters['eta_K']

        # states: u and u dot
        u = self.create_input('u', shape=(num_nodes, num_beam_nodes * 6))
        udot = self.create_input('u_dot', shape=(num_nodes, num_beam_nodes *  6))

        beam_F_val = self.create_input(beam_name+'_force_torque', shape=(num_nodes, num_beam_nodes ,6))

        # input to ode: torque as a function of time
        nodel_force = beam_F_val[:, :, :3]
        self.register_output(beam_name+'_forces',nodel_force)

        beam_mesh = self.create_input(beam_name+'_mesh',  shape=(num_nodes, num_beam_nodes, 3))

        global_mass_matrix = self.declare_variable('global_mass_matrix', shape=(num_nodes, num_beam_nodes * 6, num_beam_nodes * 6))
        global_stiffness_matrix = self.declare_variable('global_stiffness_matrix', shape=(num_nodes, num_beam_nodes * 6, num_beam_nodes * 6))

        C = eta_M * global_mass_matrix + eta_K * global_stiffness_matrix

        # states time derivative
        # first state is the displacement
        self.register_output('du_dt', udot*1.0)

        nodel_force_reshape = csdl.reshape(beam_F_val, (num_nodes, num_beam_nodes * 6))
        # second state is the velocity
        u_ddot = self.create_output('dudot_dt', shape=(num_nodes, num_beam_nodes * 6))

        indices_str = 'ijk,ik->ij'
        for i in range(num_nodes):
            MTX = csdl.reshape(global_mass_matrix[i,:,:], (num_beam_nodes * 6, num_beam_nodes * 6))
            b = nodel_force_reshape[i,:] - csdl.einsum(global_stiffness_matrix, u, subscripts=indices_str)[i,:] - csdl.einsum(C, udot,  subscripts=indices_str)[i,:]
            b_reshaped = csdl.reshape(b, MTX.shape[1])
            u_ddot[i,:] = csdl.reshape(csdl.solve(MTX, b_reshaped), u_ddot.shape)


# The parent model containing the optimization problem
class IntegratorModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('num_time_points')
        self.parameters.declare('num_beam_nodes')
        self.parameters.declare('beam_name')
        self.parameters.declare('eta_M')
        self.parameters.declare('eta_K')


    def define(self):
        num_time_points = self.parameters['num_time_points']  # number of time points for integration (includes initial condition)
        num_beam_nodes = self.parameters['num_beam_nodes']  # number of nodes for the beam
        beam_name = self.parameters['beam_name']  # name of the beam
        eta_M = self.parameters['eta_M']
        eta_K = self.parameters['eta_K']

        # set initial conditions
        self.create_input('initial_u', val=np.zeros((num_beam_nodes * 6)))
        self.create_input('initial_udot', val=np.zeros((num_beam_nodes * 6)))

        # ---VARIABLE TIME---:
        # to specify the ode integration timespan, we give a vector of timesteps.
        # for example, if we want to integrate from 0 ~ 1 seconds with 5 timesteps, we will give
        # np.array([0.2, 0.2, 0.2, 0.2, 0.2]) as the timestep vector.
        # If we set this variable as a design variable, it will automatically change them appropriately.
        val = np.ones(num_time_points-1)*0.5
        timestep_vector = self.create_input('timestep_vector', val)
        # the final time to minimize is the sum of the timesteps
        self.register_output('final_time', csdl.sum(timestep_vector))

        # adding the ODE solver to this model
        # ode = ODEProblem('ForwardEuler', 'time-marching', num_time_points)
        ode = ODEProblem('BackwardEuler', 'time-marching checkpointing', num_time_points)
        # ode = ODEProblem('ImplicitMidpoint', 'time-marching', num_time_points)
        # ode = ODEProblem('RK4', 'time-marching', num_time_points)
        ode.add_state('u', 'du_dt', output='solved_u', initial_condition_name='initial_u',shape=(num_beam_nodes * 6))
        ode.add_state('u_dot', 'dudot_dt', output='solved_udot', initial_condition_name='initial_udot',shape=(num_beam_nodes * 6))
        ode.add_parameter(beam_name+'_mesh', dynamic=False, shape=(num_beam_nodes, 3))
        ode.add_parameter(beam_name+'_force_torque', dynamic=True, shape=(num_time_points, num_beam_nodes, 6))
        ode.add_times(step_vector='timestep_vector')  # here we give the timestep vector
        ode.add_parameter('global_mass_matrix', dynamic=False, shape=(num_beam_nodes * 6, num_beam_nodes * 6))
        ode.add_parameter('global_stiffness_matrix', dynamic=False, shape=(num_beam_nodes * 6, num_beam_nodes * 6))
        ode.set_ode_system(ODEFunction)  # this is the model containing the ode


        ode_para_dict = {'eta_M': eta_M,
                         'eta_K': eta_K,
                         'beam_name': beam_name,
                         'num_beam_nodes': num_beam_nodes,}
        
        self.add(ode.create_solver_model(ODE_parameters=ode_para_dict))




