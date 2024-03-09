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
        self.parameters.declare('time_vector')

    def define(self):
        self.surface_name = self.parameters['surface_name']
        self.surface_shape = self.parameters['surface_shape']
        self.num_time_steps = self.parameters['time_vector'].size

        swimming_fish_mesh, swimming_fish_velocity = self.compute_swimming_fish_kinematics()

    def compute_swimming_fish_kinematics(self):
        surface_shape = self.parameters['surface_shape']

        tail_amplitude = self.declare_variable('tail_amplitude')
        tail_frequency = self.declare_variable('tail_frequency')
        wave_number = self.declare_variable('wave_number')
        amplitude_profile_coeff = self.declare_variable('amplitude_profile_coeff')
        L = self.declare_variable('L')

        self.num_pts_L = self.parameters['surface_shape'][0]
        self.num_pts_R = self.parameters['surface_shape'][1]
        ############################################
        # prepare the variables to the correct shape
        ############################################
        # use helper function to expand the variables to the correct shape

        L_expand = self.prepare_scaler_variables_to_nnnxny(L)
        tail_amplitude_expand = self.prepare_scaler_variables_to_nnnxny(tail_amplitude)
        amplitude_profile_coeff_expand = self.prepare_scaler_variables_to_nnnxny(amplitude_profile_coeff_expand)
        shape = (self.num_pts_L, self.num_pts_R, 1)
        time_vector_expand = np.einsum('i->ijkl',np.ones(shape),self.parameters['time_vector'])
        rigid_fish_mesh = self.declare_variable(surface_name+'_rigid_mesh', shape=surface_shape)
        rigid_fish_mesh_expand = csdl.expand(rigid_fish_mesh,shape=(self.num_time_steps,self.num_pts_L,self.num_pts_R,3),indices='jkl->ijkl')
        s_expand = rigid_fish_mesh_expand[:,:,:,0]
        # s is defined as the discritization in the length direction

        # check this 1:
        '''
        amplitude_growth_profile = (s_expand/L_expand + amplitude_profile_coeff_expand) / (1+amplitude_profile_coeff_expand)

        amplitude_along_body = tail_amplitude_expand * amplitude_growth_profile * csdl.sin(2*np.pi*(s_expand/L_expand - time_vector_expand))

        swimming_fish_mesh = self.create_output(self.surface_name, shape=(self.num_time_steps,self.num_pts_L,self.num_pts_R,1))
        swimming_fish_mesh[:,:,:,0] = rigid_fish_mesh[:,:,:,0]
        swimming_fish_mesh[:,:,:,1] = amplitude_along_body
        swimming_fish_mesh[:,:,:,2] = rigid_fish_mesh[:,:,:,2]
        # lateral velocity is defined as the derivative of the lateral position with respect to time (tail_amplitude_expand * amplitude_growth_profile * csdl.sin(2*np.pi*(s_expand/L_expand - time_vector_expand)))
        lateral_velocity = tail_amplitude_expand * amplitude_growth_profile * csdl.cos(2*np.pi*(s_expand/L_expand - time_vector_expand))
        fish_collocation_pts_velocity = self.create_output(self.surface_name+'_velocity', val=np.zeros((self.num_time_steps,self.num_pts_L-1,self.num_pts_R-1,3)))
        fish_velocity[:,:,:,1] = 0.25(lateral_velocity[:,:-1,:-1]+lateral_velocity[:,:-1,1:]+lateral_velocity[:,1:,:-1]+lateral_velocity[:,1:,1:])
        return swimming_fish_mesh, fish_velocity
        '''


        # * np.sin(wave_number * x - tail_frequency * t)

    def prepare_scaler_variables_to_nnnxny(self, var):
        shape = (self.num_time_steps, self.num_pts_L, self.num_pts_R, 1)
        return csdl.expand(var,shape=shape)


if __name__ == '__main__':
    num_pts_R = 5
    num_pts_L = 41
    L = 1.0
    s_1_ind = 5
    s_2_ind = num_pts_L-3

    import numpy as np
    import python_csdl_backend
    eel_geometry_model = EelGeometryModel(surface_name='eel',
                                        surface_shape=[num_pts_L,num_pts_R, 3],
                                        s_1_ind=s_1_ind,s_2_ind=s_2_ind)

    eel_geometry_model.create_input('L', val=L)
    eel_geometry_model.create_input('a_coeff', val=0.55)
    eel_geometry_model.create_input('b_coeff', val=0.08)
    simulator = python_csdl_backend.Simulator(eel_geometry_model, display_scripts=False)
    simulator.run()

    simulator.check_partials(compact_print=True)

    height = simulator['eel_height']
    x = np.linspace(0,L,num_pts_L)

    import matplotlib.pyplot as plt
    plt.rcParams['text.usetex'] = False


    plt.figure()
    # plt.plot(x, height, '.')
    plt.axis('equal')
    plt.title('Eel Height Profile')

    mesh = simulator['eel_rigid_mesh']
    plt.plot(mesh[:,:,0],mesh[:,:,1]+0., '.')

    plt.show()
