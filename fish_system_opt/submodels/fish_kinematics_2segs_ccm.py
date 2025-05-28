import csdl
import math

import numpy as np


# which variables need to be stored in the model?
# trans are computed for the next segment, and visualization 
# having this model running today, try connecting tomorrow

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
        T_base_list = []
        T_dot_base_list = []
        T_dot_i_list = []

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
            theta_dot_var = self.declare_variable(theta_dot_var_name, shape=theta_dot_var_shape)

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

            # compute the R_dot = dR/dt = dR/dtheta * dtheta/dt = -L/theta^2 * dtheta/dt
            R_dot = -csdl.expand(L_var,theta_var.shape) / (theta_var**2) * theta_dot_var

            # compute tranformation matrix for each segment tip actually, 
            # if there are n segments, there are n-1 transition matrices, the last ones is not used
            # the transition matrix is a num_time_steps, 4, 4 matrix, 

            # compute the transformation matrix for each segment
            if i == num_segments-1:
                # if it is the last segment, we don't need to compute the transformation matrix
                pass
            else:
                tip_trans_matrix_name = var_name + '_tip_trans_matrix'
                tip_trans_matrix = self.create_output(tip_trans_matrix_name, shape=(num_time_steps, 4, 4), val=0)
                tip_trans_matrix = self._compute_transformation_matrix(tip_trans_matrix, R, theta_var)

            # compute theta for all the point in the segment
            theta_actuator_linspace = np.linspace(0, 1, num_pts_segments[i])
            # repeat theta_actuator_linspace to (num_time_steps, num_pts_segments[i]) with numpy
            theta_actuator_linspace_exp  = np.outer(np.ones(num_time_steps), theta_actuator_linspace)
            theta_actuator_shape = (num_time_steps, num_pts_segments[i])
            theta_actuator_var = theta_actuator_linspace_exp * self._expand_1D_to_2D(theta_var, theta_actuator_shape)
            print('theta_actuator_var:', theta_actuator_var.shape)

            #################################################################
            # 1.0 compute the all the point in the segment in local frame
            #################################################################
            R_expanded = self._expand_1D_to_2D(R, theta_actuator_shape)

            actuator_pts_local = self.create_output(var_name+'_actuator_pts_local', shape=(num_time_steps, num_pts_segments[i], 4), val=1)
            actuator_pts_local = self._compute_act_pts_local_frame(actuator_pts_local, theta_actuator_var, R_expanded)

            #################################################################
            # 1.1 transform the actuator points to the global frame
            #################################################################
            actuator_pts_global = self._tranform_segment_points_to_global_frame(actuator_pts_local,tip_trans_matrix_list)
            actuator_pts_global_name = var_name + '_actuator_pts_global'
            self.register_output(actuator_pts_global_name, actuator_pts_global)       


                

            ########################################################################
            # 2.0 compute velocity of all the point in the segment in local frame
            ########################################################################
            actuator_vel_local = self.create_output(var_name+'_actuator_vel_local', shape=(num_time_steps, num_pts_segments[i], 3), val=0)
            d_theta_i_d_theta_tip_i_diag_perts = np.linspace(0, num_pts_segments[i]-1, num_pts_segments[i])/(num_pts_segments[i]-1)
            d_theta_i_d_theta_tip_i_diag = np.tile(d_theta_i_d_theta_tip_i_diag_perts, (num_time_steps, 1))

            actuator_vel_local = self._compute_act_vel_local_frame(
                actuator_vel_local, theta_actuator_var, d_theta_i_d_theta_tip_i_diag, theta_dot_var, R, R_dot)
            
            # expand the actuator_vel_local to match the shape of actuator_pts_local
            actuator_vel_local_pad = self.create_output(
                var_name+'_actuator_vel_local_pad', shape=(num_time_steps, num_pts_segments[i], 4), val=0.0
            )
            actuator_vel_local_pad[:, :, :3] = actuator_vel_local

            
            #################################################################
            # 2.1 transform the actuator points velocity to the global frame
            #################################################################
            # T_base = self._compute_base_transformation(tip_trans_matrix_list,T_base_list)
            if i==0:
                v_global = actuator_vel_local_pad*1.
                self.register_output(var_name + '_actuator_vel_global', v_global)
                name = var_name + '_T_dot'
                T_dot = self.create_output(name, shape=(num_time_steps, 4, 4), val=0.0)
                self._compute_tip_trans_matrix_dot(T_dot,R, theta_var, R_dot, theta_dot_var)
                T_base_list.append(tip_trans_matrix)
                T_dot_base_list.append(T_dot)
                # T_base =tip_trans_matrix *1.
                
                
                # T_base is identity matrix for the first segment, the shape of T_base is (num_time_steps, 4, 4) 
                # T_base_name  = var_name + '_T_base'
                # T_dot_base_name = var_name + '_T_dot_base'  
                # T_base_prev = self.declare_variable(T_base_name, np.einsum('k,ij->kij', np.ones(num_time_steps), np.eye(4)))
                # T_dot_base_prev = self.declare_variable(T_dot_base_name, np.zeros((num_time_steps, 4, 4)))
                # T_dot_i_prev = self.declare_variable(T_dot_base_name, np.zeros((num_time_steps, 4, 4)))
            elif i==1:
                T_base = T_base_list[-1]
                T_dot_base = T_dot_base_list[-1]
                dt = 0.0060404
                T_dot_base_fd = self.create_output(var_name + '_T_dot_base_fd', shape=(num_time_steps, 4, 4), val=0.0)
                print('T_base:', T_dot_base_fd.name,)
                
                
                T_dot_base_fd[1:,:,:]  = (T_base[1:,:,:] - T_base[:num_time_steps -1 ,:,:])/dt 
                # finite difference to get the derivative of the base transformation matrix
                v_global = self._transform_velocity_to_global_frame(
                    actuator_pts_local,
                    actuator_vel_local_pad,
                    T_base,
                    T_dot_base_fd,
                    # name_prefix=var_name
                )
                self.register_output(var_name + '_actuator_vel_global', v_global)

                name = var_name + '_T_dot'

                T_dot = self.create_output(name, shape=(num_time_steps, 4, 4), val=0.0)
                self._compute_tip_trans_matrix_dot(T_dot,R, theta_var, R_dot, theta_dot_var) 
                T_dot_i_list.append(T_dot)               

            else:
                T_base_prev = T_base_list[-1] 
                T_dot_base_prev = T_dot_base_list[-1]
                

                # print('R:', R.shape, 'theta_actuator_var:', theta_actuator_var.shape, 'R_dot:', R_dot.shape, 'theta_dot_var:', theta_dot_var.shape)
                T_base = self._batched_matmul_4x4(T_base_prev, tip_trans_matrix)
                name = var_name + '_T_dot'
                T_dot = self.create_output(name, shape=(num_time_steps, 4, 4), val=0.0)
                self._compute_tip_trans_matrix_dot(T_dot,R, theta_var, R_dot, theta_dot_var)

                T_dot_base = self._update_base_transformation_dot(T_base_prev, T_dot_base_prev, tip_trans_matrix_list[-1], T_dot_i[-1])

                '''
                
                v_global = self._transform_velocity_to_global_frame(
                    actuator_pts_local,
                    actuator_vel_local_pad,
                    T_base,
                    T_dot_base,
                    # name_prefix=var_name
                )
                self.register_output(var_name + '_actuator_vel_global', v_global)
                '''
                T_base_list.append(T_base)
                T_dot_base_list.append(T_dot_base)
                T_dot_base_list.append(T_dot_base)
                T_dot_i_list.append(T_dot_i)
                print('T_base_list:', i, len(T_base_list))
            
            tip_trans_matrix_list.append(tip_trans_matrix) 
            
            
           
            



    def _tranform_segment_points_to_global_frame(self, actuator_pts_local, tip_trans_matrix_list):
        exp = csdl.expand
        actuator_pts_local_shape = actuator_pts_local.shape
        # global_trans_matrix shape is (num_time_steps, num_pts_segments[i], 4, 4)
        global_trans_matrix = np.outer(np.ones(actuator_pts_local_shape[:-1]), np.eye(4)).reshape(actuator_pts_local_shape+(4,))
        """Transform the actuator points to the global frame."""
        # if there are no previous segments, tip_trans_matrix_name_list is [], pass this function
        if tip_trans_matrix_list == []:
            print('entering if tip_trans_matrix_list == []')
            actuator_pts_global =  actuator_pts_local*1.
        else:
            if len(tip_trans_matrix_list)==1:
                # if there are previous segments, get the last tip_trans_matrix and multiply it with the current actuator_pts_local
                print('entering if tip_trans_matrix_list == 1')

                global_trans_matrix = tip_trans_matrix_list[0]*1.
            elif len(tip_trans_matrix_list)==2:
                print('entering if tip_trans_matrix_list == 2')
                global_trans_matrix_temp = exp(tip_trans_matrix_list[0], tip_trans_matrix_list[0].shape+(4,),'ijk->ijkl') *\
                     exp(tip_trans_matrix_list[1], tip_trans_matrix_list[0].shape+(4,),'ijk->iljk')
                global_trans_matrix = csdl.sum(global_trans_matrix_temp, axes=(2,))
            expanded_shape = actuator_pts_local.shape +(4,)
            # print('global_trans_matrix',global_trans_matrix.shape)
            # print('actuator_pts_local',actuator_pts_local.shape)
            print('len of tip_trans_matrix_list',len(tip_trans_matrix_list))
            actuator_pts_local_exp = csdl.expand(actuator_pts_local, shape=expanded_shape, indices='ijk->ijlk')
            global_trans_matrix_exp = csdl.expand(global_trans_matrix, shape=expanded_shape, indices='ijk->iljk')
            actuator_pts_global = csdl.sum(actuator_pts_local_exp*global_trans_matrix_exp, axes=(-1,))

            self.register_output('global_trans_matrix'+str(len(tip_trans_matrix_list)), global_trans_matrix)

        return actuator_pts_global


    def _compute_actuator_R(self, L_var, theta_var, R_var_name):
        L_var_exp = self._expand_1D_to_2D(L_var, theta_var.shape)

        R_var = L_var_exp / theta_var
        return R_var

    def _expand_1D_to_2D(self, var, shape):
        # print('var:', var.shape)
        return csdl.expand(var, shape=(shape),indices='i->ij')

    def _compute_transformation_matrix(self, trans_matrix, R, theta):
        """Create a transformation matrix for a segment with given rotation theta and length L."""
        shape = trans_matrix[:, 0, 0].shape
        # can this be fixed with new csdl?
        ones = self.create_input(name='ones', shape=(1,), val=1.0)    
        trans_matrix[:, 0, 0] = csdl.reshape(csdl.cos(theta), shape)
        trans_matrix[:, 0, 1] = csdl.reshape(-csdl.sin(theta), shape)
        trans_matrix[:, 0, 3] = csdl.reshape(R * csdl.sin(theta), shape)
        trans_matrix[:, 1, 0] = csdl.reshape(csdl.sin(theta), shape)
        trans_matrix[:, 1, 1] = csdl.reshape(csdl.cos(theta), shape)
        trans_matrix[:, 1, 3] = csdl.reshape(R * (1 - csdl.cos(theta)), shape)
        trans_matrix[:, 2, 2] = csdl.expand(ones, shape)
        trans_matrix[:, 3, 3] = csdl.expand(ones, shape)
        return trans_matrix

    # Define function to compute tip position in local frame
    def _compute_act_pts_local_frame(self, actuator_pts_local, theta, R):
        """Compute the tip position in the local frame."""
        shape = actuator_pts_local[:, :, 0].shape
        reshape = csdl.reshape
        actuator_pts_local[:, :, 0] = reshape(R * csdl.sin(theta), shape)
        actuator_pts_local[:, :, 1] = reshape(R * (1 - csdl.cos(theta)), shape)
        actuator_pts_local[:, :, 2] = reshape(R*0., shape)

        return actuator_pts_local

    def _compute_act_vel_local_frame(self, actuator_vel_local, theta, dtheta_dtheta_tip,theta_dot_tip,R,R_dot):

        """
        Computes dot{x}(t), dot{y}(t) of all points on a segment based on given variables.
        Parameters:
        - theta_tip: shape (N_ts,)
        - theta: shape (N_ts, N_pts)
        - dtheta_dtheta_tip: shape (N_ts, N_pts)
        - theta_dot_tip: shape (N_ts,)
        - r, r_dot: shape (N_ts, N_pts), note these should already be expanded to match the shape of theta, orginal r and r_dot are (N_ts,)
        Returns:
        - x_dot, y_dot: shape (N_ts, N_pts)
        """

        N_ts = theta.shape[0]
        N_pts = theta.shape[1]

        sin_theta = csdl.sin(theta)
        cos_theta = csdl.cos(theta)

        # expand theta_dot_tip to (N_ts, N_pts) from (N_ts,)
        theta_dot_tip_expanded = csdl.expand(theta_dot_tip, (N_ts, N_pts), 'i->ij')
        R_dot_expand = csdl.expand(R_dot, (N_ts, N_pts), 'i->ij')
        R_expand = csdl.expand(R, (N_ts, N_pts), 'i->ij')

        x_dot = R_dot_expand * sin_theta +\
             R_expand * dtheta_dtheta_tip * theta_dot_tip_expanded * cos_theta

        y_dot = R_dot_expand * (1 - cos_theta) +\
                R_expand * dtheta_dtheta_tip * theta_dot_tip_expanded * sin_theta

        actuator_vel_local[:, :, 0] = csdl.reshape(x_dot, (N_ts, N_pts,1))
        actuator_vel_local[:, :, 1] = csdl.reshape(y_dot, (N_ts, N_pts,1))

        return actuator_vel_local

    def _transform_velocity_to_global_frame(
        self, actuator_pts_local, actuator_vel_local_pad, T_base, T_dot_base
    ):
        """
        Transform local velocity to global frame using:
        v_global = Ṫ_base @ p_local + T_base @ v_local
        actuator_pts_local is T, N_ts, N_pts_segments, 4
        actuator_vel_local_pad is N_ts, N_pts_segments, 4
        T_base is N_ts, 4, 4
        T_dot_base is N_ts, 4, 4
        """
        num_time_steps, num_pts_segments = actuator_pts_local.shape[:2]
        # Expand T_base and T_dot_base to (T, N, 4, 4)
        T_base_exp = csdl.expand(T_base, shape=(num_time_steps, num_pts_segments, 4, 4), indices='ijk->iljk')
        T_dot_base_exp = csdl.expand(T_dot_base, shape=(num_time_steps, num_pts_segments, 4, 4), indices='ijk->iljk')

        # Matrix-vector multiplication using helper
        term1 = self._batched_matvec(T_dot_base_exp, actuator_pts_local)  # Ṫ_base @ p_local
        term2 = self._batched_matvec(T_base_exp, actuator_vel_local_pad)  # T_base @ v_local

        v_global = term1 + term2  # shape: (T, N, 4)
        return v_global[:, :, :3]  # drop the homogeneous coordinate
        
    def _update_base_transformation_dot(self, T_dot_base_prev, T_prev, T_base_prev, T_dot_prev):
        """
        Compute the derivative of the base transformation matrix:
            Ṫ_base^i = Ṫ_base^{i-1} @ T_{i-1} + T_base^{i-1} @ Ṫ_{i-1}

        Parameters
        ----------
        T_dot_base_prev : csdl array, shape (T, 4, 4)
            dot(T_base^{i-1})
        T_prev : csdl array, shape (T, 4, 4)
            T_{i-1}
        T_base_prev : csdl array, shape (T, 4, 4)
            T_base^{i-1}
        T_dot_prev : csdl array, shape (T, 4, 4)
            dot(T_{i-1})

        Returns
        -------
        T_dot_base_i : csdl array, shape (T, 4, 4)
        """
        term1 = self._batched_matmul_4x4(T_dot_base_prev, T_prev)
        term2 = self._batched_matmul_4x4(T_base_prev, T_dot_prev)
        return term1 + term2



    def _batched_matmul_4x4(self, A, B):
        """
        Performs batched (T, 4, 4) x (T, 4, 4) → (T, 4, 4) using expand + * + sum.
        ijk,ikl -> ijkl
        first step ijk->ijkl, ikl -> ijkl
        """
        A_exp = csdl.expand(A, shape=(A.shape[0], 4, 4, 4), indices='ijk->ijkl')
        B_exp = csdl.expand(B, shape=(B.shape[0], 4, 4, 4), indices='ikl->ijkl')
        product = A_exp * B_exp  # shape (T, 4, 4)
        result = csdl.sum(product, axes=(2,))  # shape (T, 4, 4)
        return result


    def _batched_matvec(self, matrix_4x4, vector_4):
        """
        Perform batched matrix-vector multiplication:
            output[i, j, k] = sum_l matrix[i, j, k, l] * vector[i, j, l]

        Parameters
        ----------
        matrix_4x4 : csdl array, shape (T, N, 4, 4)
            The batch of transformation matrices.
        vector_4 : csdl array, shape (T, N, 4)
            The batch of vectors to transform.
        name : str
            Name prefix for debugging outputs (optional).

        Returns
        -------
        output : csdl array, shape (T, N, 4)
            The transformed vectors.
        """
        T, N = vector_4.shape[0], vector_4.shape[1]

        # Expand vector_4 to (T, N, 4, 4)
        vector_exp = csdl.expand(vector_4, shape=(T, N, 4, 4), indices='ijl->ijlk')

        # Element-wise multiply and sum over last axis (l)
        product = matrix_4x4 * vector_exp
        result = csdl.sum(product, axes=(-1,))  # shape (T, N, 4)

        return result

    def _compute_tip_trans_matrix_dot(self, T_dot, R, theta, R_dot, theta_dot):
        """
        Compute time derivative of transformation matrix T_i for one segment.

        Parameters
        ----------
        R         : shape (T,)
        theta     : shape (T,)
        R_dot     : shape (T,)
        theta_dot : shape (T,)

        Returns
        -------
        T_dot     : shape (T, 4, 4)
        """
        
        T = theta.shape[0]
        

        sin_th = csdl.sin(theta)
        cos_th = csdl.cos(theta)

        T_dot[:, 0, 0] = csdl.reshape(-theta_dot * sin_th,(T, 1, 1))
        T_dot[:, 0, 1] = csdl.reshape(-theta_dot * cos_th,(T, 1, 1))
        T_dot[:, 0, 3] = csdl.reshape(R_dot * sin_th + R * theta_dot * cos_th,(T, 1, 1))

        T_dot[:, 1, 0] = csdl.reshape(theta_dot * cos_th,(T, 1, 1))
        T_dot[:, 1, 1] = csdl.reshape(-theta_dot * sin_th,(T, 1, 1))
        T_dot[:, 1, 3] = csdl.reshape(R_dot * (1 - cos_th) + R * theta_dot * sin_th,(T, 1, 1))

        # (2,2) and (3,3) are constant; time derivatives are 0
        return T_dot





if __name__ == '__main__':

    import numpy as np
    import csdl
    import python_csdl_backend
    import matplotlib.pyplot as plt
    from fish_actuation_pressure_multi_segs import EelAmplitudeModel
    plt.rcParams['text.usetex'] = False

    # Setup for two segments
    num_time_steps = 100
    num_pts_segments = 15
    seg_names = ['seg1', 'seg2']
    input_seg_shapes = [(num_time_steps,num_pts_segments), (num_time_steps,num_pts_segments)]
    NUM_PERIODS = 0.5

    # Create model and simulator
    model = csdl.Model()

    frequency_val = 1.0
    T = 1 / frequency_val
    time_vals = np.linspace(1e-3, NUM_PERIODS * T, num_time_steps)
    exit()

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

    np.set_printoptions(precision=4, suppress=False, floatmode='maxprec_equal')







# import matplotlib.pyplot as plt

# # How many time steps to skip between frames (adjust for clarity)
# plot_every_n = 10

# # Loop through selected time steps
# for t in range(0, num_time_steps, plot_every_n):
#     plt.figure(figsize=(8, 6))
#     plt.title(f"Actuator Points and Velocities (XY) at Time Step {t}")
#     plt.xlabel('X')
#     plt.ylabel('Y')
#     plt.grid(True)
#     plt.axis('equal')

#     for seg in seg_names:
#         # Extract global positions and local velocities (2D projection)
#         pts = sim[f"{seg}_actuator_pts_global"][t]  # (num_pts, 3)
#         vel = sim[f"{seg}_actuator_vel_local"][t]   # (num_pts, 3)

#         # Only use x and y
#         x, y = pts[:, 0], pts[:, 1]
#         u, v = vel[:, 0], vel[:, 1]

#         # Scatter plot for points
#         plt.scatter(x, y, label=f"{seg} points")

#         # Quiver plot for velocities
#         plt.quiver(x, y, u, v, angles='xy', scale_units='xy', scale=1, width=0.002)

#     plt.legend()
#     plt.tight_layout()
#     plt.show()

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(figsize=(8, 6))
ax.set_title("Actuator Points and Velocities Over Time (XY)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.grid(True)
ax.axis("equal")

# Limits (optional: adjust based on your data)
ax.set_xlim(-0.1, 0.5)
ax.set_ylim(-0.3, 0.3)

scatters = []
quivers = []
quivers_local = []

# Initialize plots for each segment
for seg in seg_names:
    scatter, = ax.plot([], [], 'o', label=f"{seg} points")
    quiver = ax.quiver([], [], [], [], angles='xy', scale_units='xy', scale=1, width=0.002)
    quiver_local = ax.quiver([], [], [], [], angles='xy', color='red', scale_units='xy', scale=1, width=0.002)
    scatters.append(scatter)
    quivers.append(quiver)
    quivers_local.append(quiver_local)

ax.legend()

def update(t):
    for i, seg in enumerate(seg_names):
        pts = sim[f"{seg}_actuator_pts_global"][t]  # shape (num_pts, 3)
        vel = sim[f"{seg}_actuator_vel_global"][t]   # shape (num_pts, 3)
        vel_local = sim[f"{seg}_actuator_vel_local"][t]

        x, y = pts[:, 0], pts[:, 1]
        u, v = vel[:, 0], vel[:, 1]
        u_local, v_local = vel_local[:, 0], vel_local[:, 1]

        # Update scatter plot
        scatters[i].set_data(x, y)

        # Remove the old quiver and draw a new one
        quivers[i].remove()
        # quivers_local[i].remove()

        quivers[i] = ax.quiver(x, y, u, v, angles='xy', scale_units='xy', scale=1, width=0.002)
        # quivers_local[i] = ax.quiver(x, y, u_local, v_local, angles='xy', color='red', scale_units='xy', scale=1, width=0.002)

    return scatters + quivers #+ quivers_local


ani = FuncAnimation(fig, update, frames=num_time_steps, interval=500, blit=False)

plt.tight_layout()
plt.show()
