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

class EelKinematicsModel(csdl.Model):
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

        tail_amplitude = self.declare_variable('tail_amplitude')
        tail_frequency = self.declare_variable('tail_frequency')
        wave_length = self.declare_variable('wave_length')
        amplitude_profile_coeff = self.declare_variable('amplitude_profile_coeff')

        time_steps_normalized = np.linspace(0, num_period, self.num_time_steps)
        # time_vector = csdl.expand(tail_frequency, (time_steps_normalized.shape)) * time_steps_normalized
        # self.register_output('time_vector', time_vector)
        time_vector = self.create_input('time_vector', val=time_steps_normalized)
        print('time_vector',time_vector.shape)
        print('time_steps_normalized',time_steps_normalized.shape)

        L = self.declare_variable('L')        

        # swimming_fish_mesh, swimming_fish_velocsity = self.compute_swimming_fish_kinematics()
        self.compute_swimming_fish_kinematics(L, tail_amplitude, tail_frequency, wave_length, amplitude_profile_coeff, time_vector)

    def compute_swimming_fish_kinematics(self, L, tail_amplitude, tail_frequency, wave_length, amplitude_profile_coeff, time_vector):
        surface_shape = self.parameters['surface_shape']

        self.num_pts_L = self.parameters['surface_shape'][0]
        self.num_pts_R = self.parameters['surface_shape'][1]
        ############################################
        # prepare the variables to the correct shape
        ############################################
        # use helper function to expand the variables to the correct shape

        L_expand = self.prepare_scaler_variables_to_nnnxny(L)
        tail_amplitude_expand = self.prepare_scaler_variables_to_nnnxny(tail_amplitude)
        amplitude_profile_coeff_expand = self.prepare_scaler_variables_to_nnnxny(amplitude_profile_coeff)
        wave_length_expand = self.prepare_scaler_variables_to_nnnxny(wave_length)
        tail_frequency_expand = self.prepare_scaler_variables_to_nnnxny(tail_frequency)

        time_vector_size = time_vector.size
        shape = (time_vector_size,)+(self.num_pts_L, self.num_pts_R, 1)
        time_vector_expand = csdl.expand(time_vector,shape=shape,indices='i->ijkl')
        rigid_fish_mesh = self.declare_variable(self.surface_name+'_rigid_mesh', shape=surface_shape)
        rigid_fish_mesh_expand = csdl.expand(rigid_fish_mesh,shape=(self.num_time_steps,self.num_pts_L,self.num_pts_R,3),indices='jkl->ijkl')
        s_expand = rigid_fish_mesh_expand[:,:,:,0]
        # s is defined as the discritization in the length direction

        # check this 1:
        
        amplitude_growth_profile = (s_expand/L_expand + amplitude_profile_coeff_expand) / (1+amplitude_profile_coeff_expand)
        print('amplitude_growth_profile',amplitude_growth_profile.shape)
        print('tail_amplitude_expand',tail_amplitude_expand.shape)
        print('time_vector_expand',time_vector_expand.shape)

        amplitude_along_body = tail_amplitude_expand * amplitude_growth_profile * csdl.sin(2*np.pi*(s_expand/L_expand / wave_length_expand - time_vector_expand))
        self.register_output(self.surface_name+'_amplitude_along_body', amplitude_along_body)
        self.register_output(self.surface_name+'_amplitude_growth_profile', amplitude_growth_profile)

        swimming_fish_mesh = self.create_output(self.surface_name, shape=(self.num_time_steps,self.num_pts_L,self.num_pts_R, 3))
        swimming_fish_mesh[:,:,:,0] = rigid_fish_mesh_expand[:,:,:,0]
        swimming_fish_mesh[:,:,:,1] = amplitude_along_body +  rigid_fish_mesh_expand[:,:,:,1]
        # swimming_fish_mesh[:,:,:,1] = rigid_fish_mesh_expand[:,:,:,1]
        swimming_fish_mesh[:,:,:,2] = rigid_fish_mesh_expand[:,:,:,2]
        # self.register_output(self.surface_name, swimming_fish_mesh)
        
        
        # lateral velocity is defined as the derivative of the lateral position with respect to time (tail_amplitude_expand * amplitude_growth_profile * csdl.sin(2*np.pi*(s_expand/L_expand - time_vector_expand)))
        lateral_velocity = tail_amplitude_expand * amplitude_growth_profile * (-2*np.pi*tail_frequency_expand) * csdl.cos(2*np.pi*(s_expand/L_expand / wave_length_expand - time_vector_expand))
        fish_collocation_pts_velocity = self.create_output(self.surface_name+'_velocity', val=np.zeros((self.num_time_steps,self.num_pts_L-1,self.num_pts_R-1,3)))
        fish_collocation_pts_velocity[:,:,:,1] = 0.25*(lateral_velocity[:,:-1,:-1,:]+lateral_velocity[:,:-1,1:,:]+lateral_velocity[:,1:,:-1,:]+lateral_velocity[:,1:,1:,:])



        # * np.sin(wave_length * x - tail_frequency * t)

    def prepare_scaler_variables_to_nnnxny(self, var):
        shape = (self.num_time_steps, self.num_pts_L, self.num_pts_R, 1)
        return csdl.expand(var,shape=shape)


if __name__ == '__main__':
    from fish_geometry_model import EelGeometryModel
    num_pts_R = 5
    num_pts_L = 41
    L = 1.0
    s_1_ind = 5
    s_2_ind = num_pts_L-3
    num_time_steps = 50
    num_period = 2
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
                                        num_time_steps=num_time_steps)
    eel_model = csdl.Model()
    eel_model.add(eel_geometry_model, name='EelGeometryModel')
    eel_model.add(eel_kinematics_model, name='EelKinematicsModel')
    eel_model.create_input('L', val=L)
    eel_model.create_input('a_coeff', val=0.55)
    eel_model.create_input('b_coeff', val=0.08)

    eel_model.create_input('tail_amplitude',val=0.125)
    eel_model.create_input('tail_frequency',val=0.48)
    eel_model.create_input('wave_length',val=1.0)
    eel_model.create_input('amplitude_profile_coeff',val=0.03125)
    

    simulator = python_csdl_backend.Simulator(eel_model, display_scripts=False)
    simulator.run()
    # exit()

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

        velocity_data = simulator['eel_velocity'][i]
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