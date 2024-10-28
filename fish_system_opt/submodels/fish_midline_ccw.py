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


class FishTurnCCModel(csdl.Model):
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

        # declare the variables: L, start_L, theta_max, time_vector, tail_frequency
        L = self.declare_variable('L', val=1.0)
        start_L = self.declare_variable('start_L', val=0.5)
        # this part is a hard coded part, where I assume the fish is turning but the front half is not bending

        # we assume theta is a cosine function starting from its maximum value
        theta_max = self.declare_variable('theta_max')
        # this is half of the theta_max!!!!!!!

        time_vector_val = np.linspace(0, num_period, self.num_time_steps)
        time_vector = self.declare_variable('time_vector', val=time_vector_val)
        # this is essentially the T/t, which is from 0 to num_period
        frequency = self.declare_variable('tail_frequency', val=1.)
        # this is the frequency of the tail

        # theta_profile = self.generate_theta_profile_cos(theta_max, time_vector)
        theta_profile = self.generate_theta_profile_2(theta_max, time_vector)
        self.register_output('theta_profile', theta_profile)
        # theta_dot = self.generate_theta_dot(theta_max, frequency, time_vector)
        theta_dot = self.generate_theta_dot_2(theta_max, frequency, time_vector)
        self.register_output('theta_dot', theta_dot)

        # r = L/theta_{tip}
        r_profile = self.generate_r_profile(L, theta_profile)
        # self.register_output('r_profile', r_profile)
        r_dot = self.generate_r_dot(L, theta_profile, theta_dot)
        # self.register_output('r_dot', r_dot)

        x_tip = r_profile * csdl.sin(theta_profile)
        y_tip = r_profile * (1-csdl.cos(theta_profile)) 

        
        self.register_output('x_tip', x_tip)
        self.register_output('y_tip', y_tip)

        x_dot_tip = r_dot * csdl.sin(theta_profile) + r_profile * csdl.cos(theta_profile) * theta_dot
        y_dot_tip = r_dot * (1-csdl.cos(theta_profile)) + r_profile * csdl.sin(theta_profile) * theta_dot
        self.register_output('x_dot_tip', x_dot_tip)
        self.register_output('y_dot_tip', y_dot_tip)

        num_pts_actuator = self.surface_shape[0]
        theta_actutator_normalized = np.linspace(0, 1, num_pts_actuator) # this is a np array!
        

        # compute the x and y of the actuator
        x, y, theta_actutator = self.compute_actuator_position(theta_profile, theta_actutator_normalized,r_profile)
        self.register_output('x', x)
        self.register_output('y', y)

        # compute the nodal velocity of the actuator
        x_dot, y_dot = self.compute_actuator_velocity(theta_actutator_normalized,r_profile, r_dot, theta_actutator,theta_dot)
        self.register_output('x_dot', x_dot)
        self.register_output('y_dot', y_dot)


    def generate_theta_profile_cos(self, theta_max, time_vector):
        theta_max_expanded = self.expand_var_to_nt(theta_max)
        theta = theta_max_expanded * csdl.cos(2*np.pi*time_vector) + theta_max_expanded
        return theta

    def generate_theta_profile_2(self, theta_max, time_vector):
        theta_max_expanded = self.expand_var_to_nt(theta_max)
        theta = -theta_max_expanded * csdl.cos(2*np.pi*time_vector) + theta_max_expanded
        return theta

    def generate_theta_dot(self, theta_max, f, time_vector):
        f_expanded = self.expand_var_to_nt(f)
        theta_max_expanded = self.expand_var_to_nt(theta_max)
        theta_dot = -2*np.pi*theta_max_expanded * f_expanded * csdl.sin(2*np.pi*time_vector)
        return theta_dot
    
    def generate_theta_dot_2(self, theta_max, f, time_vector):
        f_expanded = self.expand_var_to_nt(f)
        theta_max_expanded = self.expand_var_to_nt(theta_max)
        theta_dot = 2*np.pi*theta_max_expanded * f_expanded * csdl.sin(2*np.pi*time_vector)
        return theta_dot


    def generate_r_profile(self, L, theta_profile):
        L_expanded  = self.expand_var_to_nt(L)
        return L_expanded/theta_profile

    def generate_r_dot(self, L, theta_profile, theta_dot):
        L_expanded  = self.expand_var_to_nt(L)
        r_dot = -L_expanded*theta_dot/(theta_profile**2)

        return r_dot
    
    def compute_actuator_position(self, theta_profile, theta_actutator_normalized,r_profile):
        # this function computes the x and y of the actuator
        # theta_profile: the angle profile tip of the fish
        # theta_actutator_normalized: the normalized angle of the actuator
        # x, y: the x and y of the actuator

        # x = r * sin(theta_actuator)
        # y = r * (1-cos(theta_actuator))

        # first we need to expand the variables theta_profile and r_profile to the number of nodes in the actuator
        theta_profile_expanded = self.expand_nt_var_to_ntnx(theta_profile)
        r_profile_expanded = self.expand_nt_var_to_ntnx(r_profile)

        # then, we expand the numpy var of the theta_actutator_normalized to the number of time steps
        theta_actutator_normalized_ntnx = np.einsum('i,j->ij', np.ones(self.num_time_steps),theta_actutator_normalized)
        theta_actutator = theta_profile_expanded * theta_actutator_normalized_ntnx # this is the csdl variable of the angle along the actuator

        # then we compute the x and y of the actuator
        x = r_profile_expanded * csdl.sin(theta_actutator)
        y = r_profile_expanded * (1-csdl.cos(theta_actutator))

        return x, y, theta_actutator

    def compute_actuator_velocity(self, theta_actutator_normalized, r_profile, r_dot,theta_actutator, theta_dot):
        # this function computes the nodal velocity of the actuator
        # theta_profile: the angle profile tip of the fish

        # x_dot = r_dot * sin(theta_actuator) + r * cos(theta_actuator) * theta_actuator_dot
        # theta_actuator_dot = d theta_actuator / d theta_tip * theta_tip_dot

        # y_dot = r_dot * (1-cos(theta_actuator)) + r * sin(theta_actuator) * theta_actuator_dot

        # expand the variables from nt to ntnx
        r_dot_expanded = self.expand_nt_var_to_ntnx(r_dot) # tip r dot expanded
        r_profile_expanded = self.expand_nt_var_to_ntnx(r_profile) # tip r expanded
        theta_dot_expanded = self.expand_nt_var_to_ntnx(theta_dot) # tip theta dot expanded

        # first we compute the x_dot
        x_dot_t1 = r_dot_expanded * csdl.sin(theta_actutator) # this is the first term of x_dot
        theta_actutator_normalized_ntnx = np.einsum('i,j->ij', np.ones(self.num_time_steps),theta_actutator_normalized)
        theta_actutator_dot = theta_actutator_normalized_ntnx * theta_dot_expanded
        x_dot_t2 = r_profile_expanded * csdl.cos(theta_actutator) * theta_actutator_dot # this is the second term of x_dot

        x_dot = x_dot_t1 + x_dot_t2

        # then we compute the y_dot
        y_dot_t1 = r_dot_expanded * (1-csdl.cos(theta_actutator)) # this is the first term of y_dot
        y_dot_t2 = r_profile_expanded * csdl.sin(theta_actutator) * theta_actutator_dot # this is the second term of y_dot

        y_dot = y_dot_t1 + y_dot_t2

        return x_dot, y_dot




    def expand_nt_var_to_ntnx(self, var):
        num_nodes_x = self.surface_shape[0]
        var_expanded = csdl.expand(var, shape=(self.num_time_steps, num_nodes_x), indices='i->ij')
        return var_expanded

    def expand_var_to_nt(self, var):
        var_expanded = csdl.expand(var, shape=(self.num_time_steps,))
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
    eel_kinematics_model = FishTurnCCModel(surface_name='eel',
                                        surface_shape=surface_shape,
                                        num_period=num_period,
                                        num_time_steps=num_time_steps)
    eel_model = csdl.Model()
    eel_model.add(eel_geometry_model, name='EelGeometryModel')
    eel_model.add(eel_kinematics_model, name='EelKinematicsModel')
    eel_model.create_input('L', val=L)
    eel_model.create_input('a_coeff', val=0.55)
    eel_model.create_input('b_coeff', val=0.08)

    eel_model.create_input('tail_frequency',val=1)
    eel_model.create_input('wave_length',val=1.0)
    eel_model.create_input('amplitude_profile_coeff',val=0.03125)
    

    simulator = python_csdl_backend.Simulator(eel_model, display_scripts=False)
    simulator.run()
    simulator.check_partials(compact_print=True)

    # exit()
    import matplotlib.pyplot as plt
    plt.rcParams['text.usetex'] = False
    fig = plt.figure()
    theta_profile = np.rad2deg(simulator["theta_profile"])
    time_vector = simulator['time_vector']
    theta_dot = np.rad2deg(simulator['theta_dot'])

    plt.plot(time_vector, theta_profile, label='theta')
    plt.plot(time_vector, theta_dot, label='theta_dot')
    plt.xlabel('time')
    plt.ylabel('theta')
    plt.legend()

    plt.figure()
    x_tip = simulator['x_tip']
    y_tip = simulator['y_tip']
    
    plt.plot(x_tip, y_tip,'o')
    plt.xlabel('x_tip')
    plt.ylabel('y_tip')

    # plot the position of the actuator
    x = simulator['x']
    y = simulator['y']
    for i in range(num_time_steps):
        plt.plot(x[i,:], y[i,:],'-')
    # axis equal
    plt.axis('equal')
    plt.xlim(0,1)
    plt.ylim(0,1)
    plt.show()
    exit()

    # simulator.check_partials(compact_print=True)


