import csdl
import math

import numpy as np

class CCM(csdl.Model):
    """
    A model for computing the piecewise constant curvature motion of an actuator.

    Attributes
    ----------
    L: csdl.Array
        Array of segment lengths with shape (num_segments,)
    theta : csdl.Array
        Array of velocities with shape (num_time_steps, num_segments, ). 
    theta_dot : csdl.Array
        Array of normals with shape (num_time_steps, num_pts_segments, 3)

    Returns
    -------
    actuator_pos : csdl.Array
        Array of actuator positions with shape (num_time_steps, num_pts_total, 3)
    """

    def initialize(self):
        self.parameters.declare('seg_names', types=list)
        self.parameters.declare('input_seg_shapes', types=list)

    def define(self):
        seg_names = self.parameters['seg_names']
        input_seg_shapes = self.parameters['input_seg_shapes'] 
        # list of tuples with the shape of each segment:
        # [(num_time_steps, num_pts_segments),(...)]

        # constants
        num_segments = len(seg_names) # number of segments is the length of the input variable names
        num_time_steps = input_seg_shapes[0][0]
        num_pts_segments = [input_seg_shapes[i][1] for i in range(num_segments)] # number of points in each segment is the second dimension of the input variable shapes
        
        # predefine the transition matrix
        tip_trans_matrix_list = []

        # declare input variables for each segment
        for i, var_name in enumerate(seg_names):
            # declare the segment variable, var_name is the name of the segment variable
            
            ##########################
            # Input variables
            ##########################
            # 1. the segment length
            L_var_name = var_name + '_L' # the name of the L variable is the name of the segment variable with '_L' appended
            L_var_shape = (1,)
            # declare the L variable
            L_var = self.declare_variable(L_var_name, shape=L_var_shape)

            # 2. the segment angle profile (num_time_steps, )
            theta_var_name = var_name + '_theta'
            theta_var_shape = (num_time_steps, )
            # declare the theta variable
            theta_var = self.declare_variable(theta_var_name, shape=theta_var_shape)            

            # the name of the theta_dot variable is the name of the segment variable with '_theta_dot' appended
            theta_dot_var_name = var_name + '_theta_dot'
            theta_dot_var_shape = (num_time_steps,)
            # declare the theta_dot variable
            self.declare_variable(theta_dot_var_name, shape=theta_dot_var_shape)

            ##########################
            # computations
            ##########################

            # 1. compute the curvature
            # for each segment R = 1/kappa = L/theta
            R_var_name = var_name + '_R'
            R_var_shape = (num_time_steps, )
            # compute R for each segment
            R = self._compute_actuator_R(L_var, theta_var, R_var_name)
            self.register_output(R_var_name, R)


    def _compute_actuator_R(self, L_var, theta_var, R_var_name):
        L_var_exp = self._expand_1D_to_2D(L_var, theta_var.shape)

        R_var = L_var_exp / theta_var
        return R_var


    def _expand_1D_to_2D(self, var, shape):
        # print('var:', var.shape)
        return csdl.expand(var, shape=(shape),indices='i->ij')


if __name__ == '__main__':

    import numpy as np
    import csdl
    import python_csdl_backend
    import matplotlib.pyplot as plt
    from fish_actuation_pressure_multi_segs import EelAmplitudeModel
    plt.rcParams['text.usetex'] = False

    # Setup for two segments
    num_time_steps = 60
    num_pts_segments = 15
    seg_names = ['seg1', 'seg2']
    input_seg_shapes = [(num_time_steps,num_pts_segments), (num_time_steps,num_pts_segments)]
    NUM_PERIODS = 2

    # Create model and simulator
    model = csdl.Model()

    frequency_val = 1.0
    T = 1 / frequency_val
    time_vals = np.linspace(1e-3, NUM_PERIODS * T - 1e-3, num_time_steps)

    # # Segment names and phase shifts (e.g., segment_0 leads by π/2)
    # seg_names = ['seg_0', 'seg_1', 'seg_2']
    # phi = [np.pi/2, np.pi/4, 0]  # seg_0 leads seg_1 by π/2, seg_1 leads seg_2 by π/4

    # Segment names and phase shifts (e.g., segment_0 leads by π/2)
    seg_names = ['seg1', 'seg2']
    phi = [np.pi/2, 0]  # seg_0 leads seg_1 by π/2, seg_1 leads seg_2 by π/4
    # Create example inputs

    L1 = np.array([0.2])
    L2 = np.array([0.2])

    model.create_input('frequency', val=frequency_val)
    model.create_input('time_vector', val=time_vals)


    model.create_input('seg1_L', val=L1)
    # model.create_input('seg1_theta', val=theta_seg1)
    # model.create_input('seg1_theta_dot', val=theta_dot_seg1)
    model.create_input('seg2_L', val=L2)




    # Model
    model.add(
        EelAmplitudeModel(
            num_time_steps=num_time_steps,
            a_0=27.903,
            a_1=-6.430,
            seg_names=seg_names,
            phi=phi
        ),
        name='amplitude_model'
    )



    model.add(CCM(seg_names=seg_names, input_seg_shapes=input_seg_shapes), name='ccm_model')





    # model.create_input('seg2_theta', val=theta_seg2)
    # model.create_input('seg2_theta_dot', val=theta_dot_seg2)

    # Run simulator
    sim = python_csdl_backend.Simulator(model)
    sim.run()

    # Plot both curvature radii
    R1 = sim['seg1_R']
    R2 = sim['seg2_R']
    time = np.linspace(0, 1, num_time_steps)

    plt.figure(figsize=(10, 5))
    plt.plot(time, R1, label='seg1_R (L=0.3)')
    plt.plot(time, R2, label='seg2_R (L=0.4)')
    plt.xlabel('Time (normalized)')
    plt.ylabel('Curvature Radius R (m)')
    plt.title('Curvature Radius for Two Segments Over Time')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Plot results
    fig, axs = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
    for seg in seg_names:
        axs[0].plot(time_vals, sim[f'{seg}_theta'], label=f'{seg}_theta')
        axs[1].plot(time_vals, sim[f'{seg}_theta_dot'], label=f'{seg}_theta_dot')

    axs[0].set_ylabel('Angle (rad)')
    axs[1].set_ylabel('Angular Velocity (rad/s)')
    axs[1].set_xlabel('Time (s)')
    axs[0].legend()
    axs[1].legend()
    axs[0].grid(True)
    axs[1].grid(True)
    plt.tight_layout()
    plt.show()
