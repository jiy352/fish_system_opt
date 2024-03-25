import numpy as np
import csdl
import python_csdl_backend
from aframe.core.beam_model import BeamModel
from aframe.core.dataclass import Beam, BoundaryCondition, Joint, Material
from aframe.utils.plot import plot_box, plot_circle
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from ozone.api import ODEProblem
plt.rcParams.update(plt.rcParamsDefault)



num_nodes = 11
aluminum = Material(name='aluminum', E=69E9, G=26E9, rho=2700, v=0.33)
wing = Beam(name='eel', num_nodes=num_nodes, material=aluminum, cs='ellipse')
boundary_condition_1 = BoundaryCondition(beam=wing, node=5)
eta_M = 0.
eta_K = 0.

class ODEFunction(csdl.Model):

    def initialize(self):
        self.parameters.declare('num_nodes')

    def define(self):
        num_nodes = self.parameters['num_nodes']
        num_beam_nodes = 11
        beam_name = 'eel'

        # states: u and u dot
        u = self.declare_variable('u', shape=(num_nodes, num_beam_nodes * 6))
        udot = self.create_input('u_dot', shape=(num_nodes, num_beam_nodes *  6))

        beam_F_val = self.create_input(beam_name+'_force_torque', shape=(num_nodes, num_beam_nodes ,6))

        # input to ode: torque as a function of time
        nodel_force = beam_F_val[:, :, :3]
        self.register_output(beam_name+'_forces',nodel_force)
        # self.print_var(beam_F_val)
        # self.print_var(nodel_force)


        beam_mesh = self.create_input(beam_name+'_mesh',  shape=(num_beam_nodes, 3))

        aluminum = Material(name='aluminum', E=69E9, G=26E9, rho=2700, v=0.33)
        wing = Beam(name=beam_name, num_nodes=num_beam_nodes, material=aluminum, cs='ellipse')
        # fuselage = Beam(name='fuselage', num_nodes=num_nodes, material=aluminum, cs='tube')
        boundary_condition_1 = BoundaryCondition(beam=wing, node=5)
        


        global_mass_matrix = self.create_input('global_mass_matrix', shape=(num_nodes, num_beam_nodes * 6, num_beam_nodes * 6))
        global_stiffness_matrix = self.create_input('global_stiffness_matrix', shape=(num_nodes, num_beam_nodes * 6, num_beam_nodes * 6))

        test_u = csdl.solve(csdl.reshape(global_stiffness_matrix[0,:,:],(num_beam_nodes*6,num_beam_nodes*6)),
         csdl.reshape(beam_F_val[0,:,:],(num_beam_nodes*6)))
        # self.print_var(test_u)
        C = eta_M * global_mass_matrix + eta_K * global_stiffness_matrix
        # self.print_var(global_mass_matrix)

        # states time derivative
        self.register_output('du_dt', udot*1.0)

        nodel_force_reshape = csdl.reshape(beam_F_val, (num_nodes, num_beam_nodes * 6))
        indices_str = 'ijk,ik->ij'
        u_ddot = self.create_output('dudot_dt', shape=(num_nodes, num_beam_nodes * 6))

        for i in range(num_nodes):
            MTX = csdl.reshape(global_mass_matrix[i,:,:], (num_beam_nodes * 6, num_beam_nodes * 6))
            b = nodel_force_reshape[i,:] - csdl.einsum(global_stiffness_matrix, u, subscripts=indices_str)[i,:] - csdl.einsum(C, udot,  subscripts=indices_str)[i,:]
            b_reshaped = csdl.reshape(b, MTX.shape[1])
            u_ddot[i,:] = csdl.reshape(csdl.solve(MTX, b_reshaped), u_ddot.shape)
        # self.print_var(u)
        # self.print_var(u_ddot)


# The parent model containing the optimization problem
class IntegratorModel(csdl.Model):

    def define(self):
        num_timepoints = 50  # number of time points for integration (includes initial condition)
        num_beam_nodes = 11  # number of nodes for the beam
        beam_name = 'eel'  # name of the beam

        # set initial conditions
        # self.create_input('initial_u', val=np.array([ 0.          ,  0.          ,  2.0667076668, -0.1476219762,  0.          ,  0.          ,  0.          ,  0.          ,  0.6889025556, -0.118097581 ,  0.          ,  0.          ,  0.          ,  0.          ,  0.          ,  0.          ,  0.          ,  0.          ,  0.          ,  0.          ,  0.6889025556,  0.118097581 ,  0.          ,  0.          ,  0.          ,  0.          ,  2.0667076668,  0.1476219762,  0.          ,  0.          ]))
        self.create_input('initial_u', val=np.zeros((num_beam_nodes * 6)))
        self.create_input('initial_udot', val=np.zeros((num_beam_nodes * 6)))

        # set torque as an control input to the pendulum ode for every timepoint


        # ---VARIABLE TIME---:
        # to specify the ode integration timespan, we give a vector of timesteps.
        # for example, if we want to integrate from 0 ~ 1 seconds with 5 timesteps, we will give
        # np.array([0.2, 0.2, 0.2, 0.2, 0.2]) as the timestep vector.
        # If we set this variable as a design variable, it will automatically change them appropriately.
        val = np.ones(num_timepoints-1)*0.5
        timestep_vector = self.create_input('timestep_vector', val)
        # the final time to minimize is the sum of the timesteps
        self.register_output('final_time', csdl.sum(timestep_vector))

        # adding the ODE solver to this model
        # ode = ODEProblem('ForwardEuler', 'time-marching', num_timepoints)
        ode = ODEProblem('BackwardEuler', 'time-marching', num_timepoints)
        # ode = ODEProblem('RK4', 'time-marching', num_timepoints)
        ode.add_state('u', 'du_dt', output='solved_u', initial_condition_name='initial_u',shape=(num_beam_nodes * 6))
        ode.add_state('u_dot', 'dudot_dt', output='solved_udot', initial_condition_name='initial_udot',shape=(num_beam_nodes * 6))
        ode.add_parameter(beam_name+'_mesh', dynamic=False, shape=(num_beam_nodes, 3))
        ode.add_parameter(beam_name+'_force_torque', dynamic=True, shape=(num_timepoints, num_beam_nodes, 6))
        ode.add_times(step_vector='timestep_vector')  # here we give the timestep vector
        ode.add_parameter('global_mass_matrix', dynamic=False, shape=(num_beam_nodes * 6, num_beam_nodes * 6))
        ode.add_parameter('global_stiffness_matrix', dynamic=False, shape=(num_beam_nodes * 6, num_beam_nodes * 6))
        ode.set_ode_system(ODEFunction, display_scripts=True)  # this is the model containing the ode
        
        self.add(ode.create_solver_model())




if __name__ == '__main__':
    num_beam_nodes = 11
    num_time_steps = 50
    model = csdl.Model()
    
    eel_mesh = np.zeros((num_beam_nodes, 3))
    eel_mesh[:, 1] = np.linspace(-20, 20, num_beam_nodes)
    model.create_input('eel_mesh', val=eel_mesh)  
    model.create_input('eel_semi_major_axis', shape=(wing.num_elements), val=0.5)
    model.create_input('eel_semi_minor_axis', shape=(wing.num_elements), val=0.05)
    beam_F_val = np.zeros((num_time_steps, num_beam_nodes, 6)) 
    beam_F_val[:, :, 2] = 2000
    beam_F_val[:, 5, 2] = 0 # zero out the middle node for boundary condition
    # beam_F_val[:, 2, 2] = 0 # zero out the middle node for boundary condition
    beam_F = model.create_input('eel'+'_force_torque', val=beam_F_val)
    nodel_force = beam_F_val[0, :, :3]
    model.create_input('eel'+'_forces',nodel_force)    

    model.add(BeamModel(beams=[wing,],
                    boundary_conditions=[boundary_condition_1],)) 
    model.add(IntegratorModel(), name='IntegratorModel')

    sim = python_csdl_backend.Simulator(model)
    sim.run()

    undeformed_eel_mesh = sim['eel_mesh']
    deformation = sim['solved_u'] 
    deformed_eel_mesh = undeformed_eel_mesh + deformation.reshape(num_time_steps, num_beam_nodes, 6)[:,:,:3]#[-1]

    # eel_stress = sim['eel_stress']
    # eel_semi_major_axis = sim['eel_semi_major_axis']
    # eel_semi_minor_axis = sim['eel_semi_minor_axis']

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    # ax.view_init(elev=35, azim=-10)
    # ax.set_box_aspect((1, 2, 1))

    # ax.scatter(undeformed_eel_mesh[:,0], undeformed_eel_mesh[:,1], undeformed_eel_mesh[:,2], color='yellow', edgecolor='black', s=50)
    # ax.plot(undeformed_eel_mesh[:,0], undeformed_eel_mesh[:,1], undeformed_eel_mesh[:,2])
    # # fix the aspect ratio
    # ax.set_box_aspect([np.ptp(deformed_eel_mesh[:,:,0]), np.ptp(deformed_eel_mesh[:,:,1]), np.ptp(deformed_eel_mesh[:,:,2])])


    def update_graph(num):
        ax.clear()
        ax.view_init(elev=35, azim=-10)
        ax.set_box_aspect((1, 2, 1))
        
        # Plot the undeformed mesh (yellow)
        ax.scatter(undeformed_eel_mesh[:, 0], undeformed_eel_mesh[:, 1], undeformed_eel_mesh[:, 2], color='yellow', edgecolor='black', s=50)
        ax.plot(undeformed_eel_mesh[:, 0], undeformed_eel_mesh[:, 1], undeformed_eel_mesh[:, 2])
        
        # Plot the deformed mesh for the current time step (blue)
        ax.scatter(deformed_eel_mesh[num, :, 0], deformed_eel_mesh[num, :, 1], deformed_eel_mesh[num, :, 2], color='blue', s=50)
        ax.plot(deformed_eel_mesh[num, :, 0], deformed_eel_mesh[num, :, 1], deformed_eel_mesh[num, :, 2], color='blue')
        # add a title with the current time step
        ax.set_title(f'Current time is {num*0.5:.1f}')

        # fix the x, y, z range
        ax.set_xlim(-1, 1)
        ax.set_ylim(-20, 20)
        ax.set_zlim(-3, 3)


    for i in range(num_time_steps):
        update_graph(i)
        plt.pause(0.1)
        plt.savefig(f'frame_{i}.png', dpi=200)
    plt.show()

    # make a gif
    import imageio
    with imageio.get_writer('eel.gif', mode='I') as writer:
        for i in range(num_time_steps):
            image = imageio.imread(f'frame_{i}.png')
            writer.append_data(image)
        

    

    # ax.scatter(undeformed_fuselage_mesh[:,0], undeformed_fuselage_mesh[:,1], undeformed_fuselage_mesh[:,2], color='red', s=50)
    # ax.plot(undeformed_fuselage_mesh[:,0], undeformed_fuselage_mesh[:,1], undeformed_fuselage_mesh[:,2])
    # ax.scatter(deformed_fuselage_mesh[:,0], deformed_fuselage_mesh[:,1], deformed_fuselage_mesh[:,2], color='green', s=50)
    # ax.plot(deformed_fuselage_mesh[:,0], deformed_fuselage_mesh[:,1], deformed_fuselage_mesh[:,2], color='green')

    # vertices = plot_circle(undeformed_eel_mesh, eel_radius*5, num_circle=20)
    # for i in range(wing.num_elements):
    #     ax.add_collection3d(Poly3DCollection(vertices[i], facecolors='black', linewidths=1, edgecolors='red', alpha=0.4))

    # deformed_vertices = plot_circle(deformed_eel_mesh, eel_radius*5, num_circle=20)
    # for i in range(wing.num_elements):
    #     ax.add_collection3d(Poly3DCollection(deformed_vertices[i], facecolors='cyan', linewidths=1, edgecolors='red', alpha=0.4))

    # plot deformation

    ax.axis('equal')
    plt.axis('off')
    plt.show()

    # plt.plot(eel_stress)
    plt.show()

    np.set_printoptions(edgeitems=30, linewidth=100000,precision=10,suppress=True)
    print(sim['global_mass_matrix'])
    print(sim['global_stiffness_matrix'].shape)

    #  [𝐶]=𝜂𝑀[𝑀]+𝜂𝐾[𝐾]

    eta_M = 0.1
    eta_K = 0.1
    M = sim['global_mass_matrix']
    K = sim['global_stiffness_matrix']
    C = eta_M * M + eta_K * K

    u = np.linalg.inv(K)@(sim['eel_force_torque'][0,:,:].reshape(-1))
    u.reshape(-1,6)[:,:3]



    deformation = deformed_eel_mesh - undeformed_eel_mesh
    plt.plot(deformation[:,2], color='blue')
    plt.show()
