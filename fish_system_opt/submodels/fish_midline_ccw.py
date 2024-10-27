# The fish mesh can be computed from Carling 1998, where the height profile of the fish is given by:
# height = b*(1-((x-a)/a)**2)**0.5

# the inputs are:
# L: length of the fish
# a: shifting parameter for the height profile
# b: scaling parameter for the height profile

# the parameters are:
# num_pts_L: number of points in the length direction
# num_pts_R: number of points in the radial direction
# s_1_ind: number of points for the head region
# s_2_ind: number of points for the tail region
# discretization: 'uniform' or 'cosine'
import csdl
import numpy as np
import scipy.sparse


class FishTurnCCW(csdl.Model):
    def initialize(self):
        self.parameters.declare('surface_name')
        self.parameters.declare('surface_shape') # note this is without number of nodes
        self.parameters.declare('num_period')
        self.parameters.declare('num_time_steps')


    def define(self):
        self.surface_name = self.parameters['surface_name']
        self.surface_shape = self.parameters['surface_shape']
        num_period = self.parameters['num_period']
        self.num_time_steps = self.parameters['num_time_steps']

        # declare the variables
        L = self.declare_variable('L', val=1.0)
        start_L = self.create_input('start_L', val=0.5)
        # this part is a hard coded part, where I assume the fish is turning but the front half is not bending

        # we assume theta is a cosine function starting from its maximum value
        theta_max = self.create_input('theta_max', val=np.pi/6)

        time_vector = csdl.linspace(0, num_period, self.num_time_steps)

        theta_profile = self.generate_theta_profile(theta_max, time_vector)
        theta_dot = self.generate_theta_dot(theta_max, time_vector)

        r_profile = self.generate_r_profile(L, start_L, time_vector)
        r_dot = self.generate_r_dot(L, start_L, time_vector)

        x = r_profile * csdl.sin(theta_profile)
        y = r_profile * (1-csdl.cos(theta_profile)) 

        x_dot = r_dot * csdl.sin(theta_profile) + r_profile * csdl.cos(theta_profile) * theta_dot
        y_dot = r_dot * (1-csdl.cos(theta_profile)) + r_profile * csdl.sin(theta_profile) * theta_dot

    def generate_theta_profile(self, theta_max, time_vector):
        pass
    def generate_theta_dot(self, theta_max, time_vector):
        pass
    def generate_r_profile(self, L, theta_profile):
        L_expanded  = self.expand_var_to_nt(L)
        return L_expanded/theta_profile

    def generate_r_dot(self, L, theta_profile, theta_dot):
        # r_dot = -L*theta_dot/(theta_profile**2)*theta_dot
        pass

    def expand_var_to_nt(self, var):
        var_expanded = csdl.expand_dims(var, axis=0, num_times=self.num_time_steps)
        return var_expanded

if __name__ == '__main__':
    from fish_geometry_model import EelGeometryModel
    num_pts_R = 5
    num_pts_L = 41
    L = 1.0
    s_1_ind = 5
    s_2_ind = num_pts_L-3
    num_time_steps = 50
    num_period = 2
    num_amp_cp = 6
    surface_shape = (num_pts_L,num_pts_R, 3)

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

    import numpy as np
    import python_csdl_backend
    eel_geometry_model = EelGeometryModel(surface_name='eel',
                                        surface_shape=surface_shape,
                                        s_1_ind=s_1_ind,s_2_ind=s_2_ind)
    eel_kinematics_model = EelKinematicsModel(surface_name='eel',
                                        surface_shape=surface_shape,
                                        num_period=num_period,
                                        num_time_steps=num_time_steps,
                                        num_amp_cp=num_amp_cp)
    eel_model = csdl.Model()
    eel_model.add(eel_geometry_model, name='EelGeometryModel')
    eel_model.add(eel_kinematics_model, name='EelKinematicsModel')
    eel_model.create_input('L', val=L)
    eel_model.create_input('a_coeff', val=0.55)
    eel_model.create_input('b_coeff', val=0.08)

    eel_model.create_input('tail_frequency',val=0.48)
    eel_model.create_input('wave_length',val=1.0)
    eel_model.create_input('amplitude_profile_coeff',val=0.03125)
    

    simulator = python_csdl_backend.Simulator(eel_model, display_scripts=False)
    simulator.run()
    # simulator.check_partials(compact_print=True)
    import matplotlib.pyplot as plt
    plt.rcParams['text.usetex'] = False
    exit()

    # simulator.check_partials(compact_print=True)


    height = simulator['eel_height']
    x = np.linspace(0,L,num_pts_L)

    import matplotlib.pyplot as plt
    plt.rcParams['text.usetex'] = False


    # plt.figure()
    # # plt.plot(x, height, '.')
    # plt.axis('equal')
    # plt.title('Eel Height Profile')

    # mesh = simulator['eel_rigid_mesh']
    # plt.plot(mesh[:,:,0],mesh[:,:,1]+0., '.')

    # plt.show()


    from mpl_toolkits.mplot3d import Axes3D
    import time

    # Example data: A list of arrays, where each array represents a time step
    # Replace this with your actual data
    
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
        filename = f'frame_{i}.png'
        plt.savefig(filename, dpi=200)
        filenames.append(filename)
    import imageio
    import os
    # Create a GIF
    with imageio.get_writer('my_animation.gif', mode='I', duration=0.1) as writer:
        for filename in filenames:
            image = imageio.imread(filename)
            writer.append_data(image)

    # Remove files
    for filename in filenames:
        os.remove(filename)

    plt.ioff()  # Turn off interactive mode
    plt.show()

    x_np = np.linspace(1e-3,1, num_amp_cp)
    control_points_inital = (x_np + 0.03) / (1+0.03) * 0.125
    x =  simulator['eel'][0,:,2,0]

    plt.figure()
    plt.plot(x_np, simulator['eel_amplitude_cp'],'.')
    plt.plot(x,simulator['amplitude'])
    plt.show()