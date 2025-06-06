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
# from get_b_spline_mtx import get_bspline_mtx

def get_bspline_mtx(num_cp, num_pt, order=4):
    order = min(order, num_cp)

    knots = np.zeros(num_cp + order)
    knots[order-1:num_cp+1] = np.linspace(0, 1, num_cp - order + 2)
    knots[num_cp+1:] = 1.0

    t_vec = np.linspace(0, 1, num_pt)

    basis = np.zeros(order)
    arange = np.arange(order)
    data = np.zeros((num_pt, order))
    rows = np.zeros((num_pt, order), int)
    cols = np.zeros((num_pt, order), int)

    for ipt in range(num_pt):
        t = t_vec[ipt]

        i0 = -1
        for ind in range(order, num_cp+1):
            if (knots[ind-1] <= t) and (t < knots[ind]):
                i0 = ind - order
        if t == knots[-1]:
            i0 = num_cp - order

        basis[:] = 0.
        basis[-1] = 1.

        for i in range(2, order+1):
            l = i - 1
            j1 = order - l
            j2 = order
            n = i0 + j1
            if knots[n+l] != knots[n]:
                basis[j1-1] = (knots[n+l] - t) / \
                              (knots[n+l] - knots[n]) * basis[j1]
            else:
                basis[j1-1] = 0.
            for j in range(j1+1, j2):
                n = i0 + j
                if knots[n+l-1] != knots[n-1]:
                    basis[j-1] = (t - knots[n-1]) / \
                                (knots[n+l-1] - knots[n-1]) * basis[j-1]
                else:
                    basis[j-1] = 0.
                if knots[n+l] != knots[n]:
                    basis[j-1] += (knots[n+l] - t) / \
                                  (knots[n+l] - knots[n]) * basis[j]
            n = i0 + j2
            if knots[n+l-1] != knots[n-1]:
                basis[j2-1] = (t - knots[n-1]) / \
                              (knots[n+l-1] - knots[n-1]) * basis[j2-1]
            else:
                basis[j2-1] = 0.

        data[ipt, :] = basis
        rows[ipt, :] = ipt
        cols[ipt, :] = i0 + arange

    data, rows, cols = data.flatten(), rows.flatten(), cols.flatten()

    return scipy.sparse.csr_matrix(
        (data, (rows, cols)), 
        shape=(num_pt, num_cp),
    )

class EelKinematicsModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('surface_name')
        self.parameters.declare('surface_shape') # note this is without number of nodes
        self.parameters.declare('num_period')
        self.parameters.declare('num_time_steps')
        self.parameters.declare('num_amp_cp')

    def define(self):
        self.surface_name = self.parameters['surface_name']
        self.surface_shape = self.parameters['surface_shape']
        num_period = self.parameters['num_period']
        self.num_time_steps = self.parameters['num_time_steps']

        tail_frequency = self.declare_variable('tail_frequency')
        wave_length = self.declare_variable('wave_length')

        time_steps_normalized = np.linspace(0, num_period, self.num_time_steps)
        # time_vector = csdl.expand(tail_frequency, (time_steps_normalized.shape)) * time_steps_normalized
        # self.register_output('time_vector', time_vector)
        time_vector = self.create_input('time_vector', val=time_steps_normalized)
        # print('time_vector',time_vector.shape)
        # print('time_steps_normalized',time_steps_normalized[1])

        L = self.declare_variable('L')        

        # swimming_fish_mesh, swimming_fish_velocsity = self.compute_swimming_fish_kinematics()
        self.compute_swimming_fish_kinematics(L, tail_frequency, wave_length, time_vector)

    def compute_swimming_fish_kinematics(self, L, tail_frequency, wave_length, time_vector):
        surface_shape = self.parameters['surface_shape']
        num_amp_cp = self.parameters['num_amp_cp']

        self.num_pts_L = self.parameters['surface_shape'][0]
        self.num_pts_R = self.parameters['surface_shape'][1]
        ############################################
        # prepare the variables to the correct shape
        ############################################
        # use helper function to expand the variables to the correct shape

        L_expand = self.prepare_scaler_variables_to_nnnxny(L)
        wave_length_expand = self.prepare_scaler_variables_to_nnnxny(wave_length)
        tail_frequency_expand = self.prepare_scaler_variables_to_nnnxny(tail_frequency)

        time_vector_size = time_vector.size
        shape = (time_vector_size,)+(self.num_pts_L, self.num_pts_R, 1)
        time_vector_expand = csdl.expand(time_vector,shape=shape,indices='i->ijkl')
        rigid_fish_mesh = self.declare_variable(self.surface_name+'_rigid_mesh', shape=surface_shape)
        rigid_fish_mesh_expand = csdl.expand(rigid_fish_mesh,shape=(self.num_time_steps,self.num_pts_L,self.num_pts_R,3),indices='jkl->ijkl')
        s_expand = rigid_fish_mesh_expand[:,:,:,0]
        s = csdl.reshape(rigid_fish_mesh[:,0,0],(self.num_pts_L,))
        # s is defined as the discritization in the length direction

        # x_np = np.linspace(0,1, num_amp_cp)
        # control_points_inital = (x_np + 0.03) / (1+0.03) * 0.125

        amplitude_cp = self.declare_variable(self.surface_name+'_amplitude_cp',shape=(num_amp_cp,))
        coeff_05s = amplitude_cp[0]
        coeff_s = amplitude_cp[1]
        coeff_2s = amplitude_cp[2]
        # CHANGE Oct 12 2024, change the kinematics to mimic switch between carangiform and anguilliform
        coeff_exp = amplitude_cp[3]

        # print('coeff_05s',coeff_05s.shape)
        coeff_05s_expand = csdl.expand(coeff_05s,shape=(s.shape))
        coeff_s_expand = csdl.expand(coeff_s,shape=(s.shape))
        coeff_2s_expand = csdl.expand(coeff_2s,shape=(s.shape))
        coeff_exp_expand = csdl.expand(coeff_exp,shape=(s.shape))

        amplitude_max = self.declare_variable('amplitude_max')
        amplitude_max_expand = csdl.expand(amplitude_max,shape=(s.shape))   
        # print('coeff_05s_expand',coeff_05s_expand.shape)
        '''CHANGE 0926/2024 change the kinematics to mimic carangform'''
        # amplitude = amplitude_max_expand*(coeff_05s_expand* s**0.5 + coeff_s_expand * s + coeff_2s_expand * s**2)/(coeff_05s_expand + coeff_s_expand + coeff_2s_expand)
        # amplitude = amplitude_max_expand*(coeff_05s_expand + coeff_s_expand * s + coeff_2s_expand * s**2)/(coeff_05s_expand + coeff_s_expand + coeff_2s_expand)
        amplitude_carang = amplitude_max_expand*(coeff_05s_expand + coeff_s_expand * s + coeff_2s_expand * s**2)/(coeff_05s_expand + coeff_s_expand + coeff_2s_expand)
        amplitude_angui = amplitude_max_expand*(csdl.exp(s-1.))
        amplitude = amplitude_carang * (1-coeff_exp_expand) + amplitude_angui * coeff_exp_expand
        self.register_output('amplitude', amplitude)

        amplitude_expand_temp = csdl.expand(amplitude,shape=(s_expand.shape),indices='j->ijkl')
        beta = 0.3
        amplitude_expand = amplitude_expand_temp 
        # num_nodes, num_pts_L, num_pts_R, 1

        print('time_vector_expand',time_vector_expand.shape)

        

        amplitude_along_body_temp = amplitude_expand  * csdl.sin(2*np.pi*(s_expand/L_expand / wave_length_expand - time_vector_expand)) 
        bias_factor_scalar = self.declare_variable('bias_factor')
        bias_factor = csdl.expand(bias_factor_scalar,shape=(amplitude_along_body_temp[1:19,:,:,0].shape))
        # this is a hard coded version of the amplitude along the body
        amplitude_along_body = self.create_output(self.surface_name+'_amplitude_along_body', shape=(self.num_time_steps,self.num_pts_L,self.num_pts_R, 1))
        amplitude_along_body[0,:,:,0] = amplitude_along_body_temp[0,:,:,0]
        amplitude_along_body[1:19,:,:,0] = amplitude_along_body_temp[1:19,:,:,0] * bias_factor
        amplitude_along_body[19:37,:,:,0] = amplitude_along_body_temp[19:37,:,:,0] 
        amplitude_along_body[37:55,:,:,0] = amplitude_along_body_temp[37:55,:,:,0] * bias_factor
        amplitude_along_body[55:73,:,:,0] = amplitude_along_body_temp[55:73,:,:,0]

        # self.register_output(self.surface_name+'_amplitude_along_body', amplitude_along_body)

        swimming_fish_mesh = self.create_output(self.surface_name, shape=(self.num_time_steps,self.num_pts_L,self.num_pts_R, 3))
        swimming_fish_mesh[:,:,:,0] = rigid_fish_mesh_expand[:,:,:,0]
        swimming_fish_mesh[:,:,:,1] = amplitude_along_body +  rigid_fish_mesh_expand[:,:,:,1]
        # swimming_fish_mesh[:,:,:,1] = rigid_fish_mesh_expand[:,:,:,1]
        swimming_fish_mesh[:,:,:,2] = rigid_fish_mesh_expand[:,:,:,2]
        # self.register_output(self.surface_name, swimming_fish_mesh)
        
        lateral_velocity_temp = amplitude_expand  * (-2*np.pi*tail_frequency_expand) * csdl.cos(2*np.pi*(s_expand/L_expand / wave_length_expand - time_vector_expand))
        # self.register_output(self.surface_name+'_lateral_velocity', lateral_velocity)
        lateral_velocity = self.create_output(self.surface_name+'_lateral_velocity', shape=(self.num_time_steps,self.num_pts_L,self.num_pts_R, 1))

        lateral_velocity[0,:,:,0] = lateral_velocity_temp[0,:,:,0] 
        lateral_velocity[1:19,:,:,0] = lateral_velocity_temp[1:19,:,:,0] * bias_factor
        lateral_velocity[19:37,:,:,0] = lateral_velocity_temp[19:37,:,:,0]
        lateral_velocity[37:55,:,:,0] = lateral_velocity_temp[37:55,:,:,0] * bias_factor
        lateral_velocity[55:73,:,:,0] = lateral_velocity_temp[55:73,:,:,0]

        fish_collocation_pts_velocity = self.create_output(self.surface_name+'_coll_vel', val=np.zeros((self.num_time_steps,self.num_pts_L-1,self.num_pts_R-1,3)))
        fish_collocation_pts_velocity[:,:,:,1] = 0.25*(lateral_velocity[:,:-1,:-1,:]+lateral_velocity[:,:-1,1:,:]+lateral_velocity[:,1:,:-1,:]+lateral_velocity[:,1:,1:,:])


    def prepare_scaler_variables_to_nnnxny(self, var):
        shape = (self.num_time_steps, self.num_pts_L, self.num_pts_R, 1)
        return csdl.expand(var,shape=shape)

    def prepare_vector_variables_to_nx(self, var):
        shape = (self.num_pts_L, )
        return csdl.expand(var,shape=shape)


if __name__ == '__main__':
    from fish_geometry_model import EelGeometryModel
    num_pts_R = 5
    num_pts_L = 41
    L = 1.0
    s_1_ind = 5
    s_2_ind = num_pts_L-3
    num_time_steps = 73
    num_period = 2
    num_amp_cp = 4

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
    coeffs = np.array([0.02, -0.08, 0.16, 0.])

    eel_model.create_input('bias_factor',val=0.2)
    eel_model.create_input('tail_frequency',val=0.48)
    eel_model.create_input('wave_length',val=1.0)
    eel_model.create_input('amplitude_max',val=0.2)
    eel_model.create_input('eel_amplitude_cp',val=coeffs)
    

    simulator = python_csdl_backend.Simulator(eel_model, display_scripts=False)
    simulator.run()

    import matplotlib.pyplot as plt
    plt.rcParams['text.usetex'] = False

    eel_amplitude_along_body_mod = simulator['eel_amplitude_along_body'].copy()
    eel_amplitude_along_body_mod[0:14] = simulator['eel_amplitude_along_body'].copy()[0:14]#*0.5
    eel_amplitude_along_body_mod[27:40] = simulator['eel_amplitude_along_body'].copy()[27:40]#*0.5


    plt.figure()
    # plot head motion
    head_motion = eel_amplitude_along_body_mod[:,0,0,0]
    plt.plot(simulator['time_vector'], head_motion,'.-' ,label='Head')
    # plot tail motion
    tail_motion = eel_amplitude_along_body_mod[:,-1,0,0]
    plt.plot(simulator['time_vector'], tail_motion, '.-' ,label='Tail')
    # plot mid body motion
    mid_body_motion = eel_amplitude_along_body_mod[:,21,0,0]
    plt.plot(simulator['time_vector'], mid_body_motion, '.-' ,label='Mid Body')
    # draw a line where y = 0
    plt.axhline(y=0, color='r', linestyle='--')
    plt.legend()
    plt.title('Eel Amplitude Along Body')
    plt.show()




    # exit()
    # simulator.check_partials(compact_print=True)

    diff = (simulator['eel'][1:,20,1,1]-simulator['eel'][:-1,20,1,1])
    dt = (simulator['time_vector'][1]-simulator['time_vector'][0])/0.48
    plt.figure()
    plt.plot(diff/dt)
    plt.plot(simulator['eel_lateral_velocity'][:,20,1].flatten())
    plt.title('Lateral Velocity')


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
        ax.view_init(90, -90)


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
    with imageio.get_writer('my_animation_ca.gif', mode='I', duration=0.1) as writer:
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