import csdl
import numpy as np

import csdl
import numpy as np

import csdl
import numpy as np

class AnalyticalCCMVelocity(csdl.Model):
    def initialize(self):
        self.parameters.declare('seg_names', types=list)
        self.parameters.declare('input_seg_shapes', types=list)

    def define(self):
        seg_names = self.parameters['seg_names']
        input_seg_shapes = self.parameters['input_seg_shapes'] 

        num_segments = len(seg_names)
        num_time_steps = input_seg_shapes[0][0]
        num_pts_segments = [input_seg_shapes[i][1] for i in range(num_segments)]

        for i, var_name in enumerate(seg_names):        
            L_var = self.declare_variable(var_name + '_L', shape=(1,))            
            theta = self.declare_variable(var_name + '_theta', shape=(num_time_steps,))
            theta_dot = self.declare_variable(var_name + '_theta_dot', shape=(num_time_steps,))
            if i < 2:
                alpha_frac = self.create_input(var_name + '_alpha_frac', val=np.linspace(0, 1, num_pts_segments[i],endpoint=False))
            else:
                alpha_frac = self.create_input(var_name + '_alpha_frac', val=np.linspace(0.0667, 1, num_pts_segments[i],endpoint=True))
            alpha_frac_exp = csdl.expand(alpha_frac, (num_time_steps, num_pts_segments[i]), 'j->ij')
            alpha = csdl.expand(theta, (num_time_steps, num_pts_segments[i]), 'i->ij') * alpha_frac_exp

            r = csdl.expand(L_var, (num_time_steps,)) / theta
            r_exp = csdl.expand(r, (num_time_steps, num_pts_segments[i]), 'i->ij')
            r_dot = -csdl.expand(L_var, (num_time_steps,)) / (theta**2) * theta_dot
            r_dot_exp = csdl.expand(r_dot, (num_time_steps, num_pts_segments[i]), 'i->ij')

            sin_alpha = csdl.sin(alpha)
            cos_alpha = csdl.cos(alpha)
            theta_dot_exp = csdl.expand(theta_dot, (num_time_steps, num_pts_segments[i]), 'i->ij')

            if i == 0:
                # Segment 1: compute position and velocity in local frame
                x = r_exp * sin_alpha
                y = r_exp * (1 - cos_alpha)
                x_dot = r_dot_exp * sin_alpha + r_exp * theta_dot_exp * alpha_frac_exp * cos_alpha
                y_dot = r_dot_exp * (1 - cos_alpha) + r_exp * theta_dot_exp * alpha_frac_exp * sin_alpha
                p_global = self.create_output(var_name + '_p_global', shape=(num_time_steps, num_pts_segments[i], 3), val=0.0)
                v_global = self.create_output(var_name + '_v_global', shape=(num_time_steps, num_pts_segments[i], 3), val=0.0)

                p_global[:, :, 0] = csdl.reshape(x, p_global[:, :, 0].shape)
                p_global[:, :, 1] = csdl.reshape(y, p_global[:, :, 1].shape)
                v_global[:, :, 0] = csdl.reshape(x_dot, v_global[:, :, 0].shape)
                v_global[:, :, 1] = csdl.reshape(y_dot, v_global[:, :, 1].shape)

            elif i == 1:
                # Segment 2: contributions from three terms:
                # Term A: tip motion of segment 1
                # Term B: motion due to rotation of local frame (Jacobian from theta1)
                # Term C: motion due to its own deformation (Jacobian from theta2)

                ###########################
                # Term A: v_tip from segment 1
                ###########################
                theta1 = self.declare_variable('seg1_theta', shape=(num_time_steps,))
                theta1_dot = self.declare_variable('seg1_theta_dot', shape=(num_time_steps,))
                L1 = self.declare_variable('seg1_L', shape=(1,))

                r1 = csdl.expand(L1, (num_time_steps,)) / theta1
                sin_th1 = csdl.sin(theta1)
                cos_th1 = csdl.cos(theta1)
                p1_tip_x = r1 * sin_th1
                p1_tip_y = r1 * (1 - cos_th1)

                v_global_seg1 = self.declare_variable('seg1_v_global', shape=(num_time_steps, num_pts_segments[0], 3))
                tip_x_dot_seg1 = csdl.expand(csdl.reshape(v_global_seg1[:, -1, 0], (num_time_steps,)), (num_time_steps, num_pts_segments[i]), 'i->ij')
                tip_y_dot_seg1 = csdl.expand(csdl.reshape(v_global_seg1[:, -1, 1], (num_time_steps,)), (num_time_steps, num_pts_segments[i]), 'i->ij')

                ###########################
                # Term B: Frame rotation effect from dR/dtheta1 * p2_local
                ###########################
                x_local = r_exp * sin_alpha
                y_local = r_exp * (1 - cos_alpha)

                cos_th1_exp = csdl.expand(cos_th1, (num_time_steps, num_pts_segments[i]), 'i->ij')
                sin_th1_exp = csdl.expand(sin_th1, (num_time_steps, num_pts_segments[i]), 'i->ij')
                p1_tip_x_exp = csdl.expand(csdl.reshape(p1_tip_x, (num_time_steps,)), (num_time_steps, num_pts_segments[i]), 'i->ij')
                p1_tip_y_exp = csdl.expand(csdl.reshape(p1_tip_y, (num_time_steps,)), (num_time_steps, num_pts_segments[i]), 'i->ij')

                x = cos_th1_exp * x_local - sin_th1_exp * y_local + p1_tip_x_exp
                y = sin_th1_exp * x_local + cos_th1_exp * y_local + p1_tip_y_exp

                Jx_rot = -sin_th1_exp * x_local - cos_th1_exp * y_local
                Jy_rot =  cos_th1_exp * x_local - sin_th1_exp * y_local
                theta1_dot_exp = csdl.expand(theta1_dot, (num_time_steps, num_pts_segments[i]), 'i->ij')
                vx_rot = Jx_rot * theta1_dot_exp
                vy_rot = Jy_rot * theta1_dot_exp

                ###########################
                # Term C: local deformation from R*d(p2_local)/dtheta2*theta2_dot
                ###########################
                alpha_2 = csdl.expand(theta, (num_time_steps, num_pts_segments[i]), 'i->ij') * alpha_frac_exp
                sin_alpha2 = csdl.sin(alpha_2)
                cos_alpha2 = csdl.cos(alpha_2)
                theta_exp = csdl.expand(theta, (num_time_steps, num_pts_segments[i]), 'i->ij')
                theta_dot_exp = csdl.expand(theta_dot, (num_time_steps, num_pts_segments[i]), 'i->ij')
                L_exp = csdl.expand(L_var, (num_time_steps, num_pts_segments[i]), 'i->ij')

                dx_local_dtheta2 = -L_exp / (theta_exp**2) * sin_alpha2 + (L_exp * alpha_frac_exp / theta_exp) * cos_alpha2
                dy_local_dtheta2 = -L_exp / (theta_exp**2) * (1 - cos_alpha2) + (L_exp * alpha_frac_exp / theta_exp) * sin_alpha2

                vx_local_def = dx_local_dtheta2 * theta_dot_exp
                vy_local_def = dy_local_dtheta2 * theta_dot_exp

                vx_rot_def = cos_th1_exp * vx_local_def - sin_th1_exp * vy_local_def
                vy_rot_def = sin_th1_exp * vx_local_def + cos_th1_exp * vy_local_def

                ###########################
                # Combine all terms:
                # v_seg2 = v_tip(seg1) + dR/dtheta1*p2_local*theta1_dot + R*d(p2_local)/dtheta2*theta2_dot
                ###########################
                x_dot =   vx_rot + vx_rot_def + tip_x_dot_seg1
                y_dot =   vy_rot + vy_rot_def + tip_y_dot_seg1

                # Create output variables
                p_global = self.create_output(var_name + '_p_global', shape=(num_time_steps, num_pts_segments[i], 3), val=0.0)
                v_global = self.create_output(var_name + '_v_global', shape=(num_time_steps, num_pts_segments[i], 3), val=0.0)

                p_global[:, :, 0] = csdl.reshape(x, p_global[:, :, 0].shape)
                p_global[:, :, 1] = csdl.reshape(y, p_global[:, :, 1].shape)
                v_global[:, :, 0] = csdl.reshape(x_dot, v_global[:, :, 0].shape)
                v_global[:, :, 1] = csdl.reshape(y_dot, v_global[:, :, 1].shape)

            elif i == 2:
                # Segment 3: straight rigid link after seg2
                theta1 = self.declare_variable('seg1_theta', shape=(num_time_steps,))
                theta2 = self.declare_variable('seg2_theta', shape=(num_time_steps,))
                theta1_dot = self.declare_variable('seg1_theta_dot', shape=(num_time_steps,))
                theta2_dot = self.declare_variable('seg2_theta_dot', shape=(num_time_steps,))

                v_global_seg2 = self.declare_variable('seg2_v_global', shape=(num_time_steps, num_pts_segments[1], 3))
                p_global_seg2 = self.declare_variable('seg2_p_global', shape=(num_time_steps, num_pts_segments[1], 3))

                tip_x_seg2 = csdl.expand(csdl.reshape(p_global_seg2[:, -1, 0], (num_time_steps,)), (num_time_steps, num_pts_segments[i]), 'i->ij')
                tip_y_seg2 = csdl.expand(csdl.reshape(p_global_seg2[:, -1, 1], (num_time_steps,)), (num_time_steps, num_pts_segments[i]), 'i->ij')
                tip_x_dot_seg2 = csdl.expand(csdl.reshape(v_global_seg2[:, -1, 0], (num_time_steps,)), (num_time_steps, num_pts_segments[i]), 'i->ij')
                tip_y_dot_seg2 = csdl.expand(csdl.reshape(v_global_seg2[:, -1, 1], (num_time_steps,)), (num_time_steps, num_pts_segments[i]), 'i->ij')

                theta12 = theta1 + theta2
                theta12_dot = theta1_dot + theta2_dot

                theta12_exp = csdl.expand(theta12, (num_time_steps, num_pts_segments[i]), 'i->ij')
                theta12_dot_exp = csdl.expand(theta12_dot, (num_time_steps, num_pts_segments[i]), 'i->ij')

                L_exp = csdl.expand(L_var, (num_time_steps, num_pts_segments[i]), 'i->ij')
                s = alpha_frac_exp * L_exp
                cos_theta12 = csdl.cos(theta12_exp)
                sin_theta12 = csdl.sin(theta12_exp)

                x = tip_x_seg2 + s * cos_theta12
                y = tip_y_seg2 + s * sin_theta12
                x_dot = tip_x_dot_seg2 - s * sin_theta12 * theta12_dot_exp
                y_dot = tip_y_dot_seg2 + s * cos_theta12 * theta12_dot_exp


                # Create output variables
                p_global = self.create_output(var_name + '_p_global', shape=(num_time_steps, num_pts_segments[i], 3), val=0.0)
                v_global = self.create_output(var_name + '_v_global', shape=(num_time_steps, num_pts_segments[i], 3), val=0.0)

                p_global[:, :, 0] = csdl.reshape(x, p_global[:, :, 0].shape)
                p_global[:, :, 1] = csdl.reshape(y, p_global[:, :, 1].shape)
                v_global[:, :, 0] = csdl.reshape(x_dot, v_global[:, :, 0].shape)
                v_global[:, :, 1] = csdl.reshape(y_dot, v_global[:, :, 1].shape)
                
if __name__ == '__main__':

    import numpy as np
    import csdl
    import python_csdl_backend
    import matplotlib.pyplot as plt
    from fish_actuation_pressure_multi_segs import EelAmplitudeModel
    from matplotlib.animation import FuncAnimation 

    plt.rcParams['text.usetex'] = False



    # ======================
    # Simulation Parameters
    # ======================
    num_time_steps = 84
    num_pts_segments = 15
    seg_names = ['seg1', 'seg2', 'seg3']  # Segment names
    input_seg_shapes = [(num_time_steps, num_pts_segments)] * len(seg_names)
    NUM_PERIODS = 2
    frequency_val = 1.5
    T = 1 / frequency_val
    time_vals = np.linspace(1.1e-3, NUM_PERIODS * T - 1.1e-3, num_time_steps)
    dt =( time_vals[1] - time_vals[0]) *1000

    # ==========================
    # Create and configure model
    # ==========================
    model = csdl.Model()

    # Input values
    model.create_input('frequency', val=frequency_val)
    model.create_input('time_vector', val=time_vals)
    model.create_input('seg1_L', val=np.array([0.1]))
    model.create_input('seg2_L', val=np.array([0.1]))
    model.create_input('seg3_L', val=np.array([0.1]))

    # Phase offsets for segments
    phi = [np.pi / 2, 0]

    # Add amplitude model (generates theta and theta_dot per segment)
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

    # Add kinematics model to compute positions and velocities
    model.add(
        AnalyticalCCMVelocity(
            seg_names=seg_names,
            input_seg_shapes=input_seg_shapes
        ),
        name='ccm_model'
    )

    # ====================
    # Run simulation
    # ====================
    sim = python_csdl_backend.Simulator(model)
    sim.run()
    sim.check_partials(compact_print=True)

    # ====================
    # Extract output data
    # ====================
    p_seg1 = sim['seg1_p_global']
    v_seg1 = sim['seg1_v_global']
    p_seg2 = sim['seg2_p_global']
    v_seg2 = sim['seg2_v_global']
    p_seg3 = sim['seg3_p_global']
    v_seg3 = sim['seg3_v_global']

    # ====================
    # Animate motion
    # ====================
    # fig, ax = plt.subplots(figsize=(8, 6))
    fig, ax = plt.subplots()
    ax.set_xlim(-0.1, 0.4)
    ax.set_ylim(-1, 1)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Segments 1 and 2 Position and Velocity Over Time')
    ax.grid(True)
    ax.set_aspect('equal')
    ax.legend()

    # Initialize plots
    scatter1 = ax.plot([], [], 'ro-', label='Segment 1')[0]
    scatter2 = ax.plot([], [], 'go-', label='Segment 2')[0]
    scatter3 = ax.plot([], [], 'bo-', label='Segment 3')[0]
    quiver_container1 = {'obj': None}
    quiver_container2 = {'obj': None}
    quiver_container3 = {'obj': None}

    # Frame update function
    def update(frame):
        for container in [quiver_container1, quiver_container2, quiver_container3]:
            if container['obj'] is not None:
                container['obj'].remove()

        # Segment 1
        x1, y1 = p_seg1[frame, :, 0], p_seg1[frame, :, 1]
        u1, v1 = v_seg1[frame, :, 0], v_seg1[frame, :, 1]
        scatter1.set_data(x1, y1)
        quiver_container1['obj'] = ax.quiver(x1, y1, u1, v1, angles='xy', scale_units='xy', scale=2.5, color='r')

        # Segment 2
        x2, y2 = p_seg2[frame, :, 0], p_seg2[frame, :, 1]
        u2, v2 = v_seg2[frame, :, 0], v_seg2[frame, :, 1]
        scatter2.set_data(x2, y2)
        quiver_container2['obj'] = ax.quiver(x2, y2, u2, v2, angles='xy', scale_units='xy', scale=2.5, color='green')

        # Segment 3
        x3, y3 = p_seg3[frame, :, 0], p_seg3[frame, :, 1]
        u3, v3 = v_seg3[frame, :, 0], v_seg3[frame, :, 1]
        scatter3.set_data(x3, y3)
        quiver_container3['obj'] = ax.quiver(x3, y3, u3, v3, angles='xy', scale_units='xy', scale=2.5, color='b')

        return scatter1, scatter2, scatter3, quiver_container1['obj'], quiver_container2['obj'], quiver_container3['obj']
    ani = FuncAnimation(fig, update, frames=num_time_steps, interval=dt, blit=False)
    plt.show()
