import csdl
import numpy as np

import csdl
import numpy as np

class CombineSegmentsAndGenerateMesh(csdl.Model):
    def initialize(self):
        self.parameters.declare('seg_names', types=list)
        self.parameters.declare('input_seg_shapes', types=list)
        self.parameters.declare('surface_shape', types=tuple)

    def define(self):
        seg_names = self.parameters['seg_names']
        input_seg_shapes = self.parameters['input_seg_shapes']
        surface_shape = self.parameters['surface_shape']

        num_time_steps = input_seg_shapes[0][0]
        num_pts_L = surface_shape[0]
        num_pts_R = surface_shape[1]
        total_pts_L = sum([input_seg_shapes[i][1] for i in range(len(seg_names))])

        combined_midline = self.create_output('fish_midline', shape=(num_time_steps, total_pts_L, 2), val=0.0)
        combined_velocity = self.create_output('fish_midline_velocity', shape=(num_time_steps, total_pts_L, 2), val=0.0)

        start_idx = 0
        for i, name in enumerate(seg_names):
            seg_len = input_seg_shapes[i][1]
            midline = self.declare_variable(name + '_p_global', shape=(num_time_steps, seg_len, 3))[:, :, 0:2]
            velocity = self.declare_variable(name + '_v_global', shape=(num_time_steps, seg_len, 3))[:, :, 0:2]
            combined_midline[:, start_idx:start_idx+seg_len, :] = midline
            combined_velocity[:, start_idx:start_idx+seg_len, :] = velocity
            start_idx += seg_len

        # Total fish length
        L_total = (self.declare_variable('seg1_L') + 
                   self.declare_variable('seg2_L') + 
                   self.declare_variable('seg3_L'))

        # Rigid mesh
        x_rest_np = np.linspace(0, 1, num_pts_L)
        x_rest_input = self.create_input('x_rest_line', val=x_rest_np)
        L_total_exp = csdl.expand(L_total, (num_pts_L,), '->j')
        x_rest_scaled = x_rest_input * L_total_exp
        x_rest_exp = csdl.expand(x_rest_scaled, (num_time_steps, num_pts_L, num_pts_R, 1), 'j->ijkl')

        z_vals_np = np.linspace(-0.04, 0.04, num_pts_R)
        z_vals_input = self.create_input('z_vals', val=z_vals_np)
        z_coords = csdl.expand(z_vals_input, (num_time_steps, num_pts_L, num_pts_R, 1), 'k->ijkl')

        fish_rigid_mesh = self.create_output('fish_rigid_mesh', shape=(num_time_steps, num_pts_L, num_pts_R, 3), val=0.0)
        fish_rigid_mesh[:, :, :, 0] = x_rest_exp[:, :, :, 0]
        # fish_rigid_mesh[:, :, :, 1] = 0.0
        fish_rigid_mesh[:, :, :, 2] = z_coords[:, :, :, 0]

        # Deformed mesh
        midline_x = csdl.expand(combined_midline[:, :, 0], (num_time_steps, num_pts_L, num_pts_R, 1), 'ijl->ijkl')
        midline_y = csdl.expand(combined_midline[:, :, 1], (num_time_steps, num_pts_L, num_pts_R, 1), 'ijl->ijkl')

        fish = self.create_output('fish', shape=(num_time_steps, num_pts_L, num_pts_R, 3))
        fish[:, :, :, 0] = midline_x[:, :, :, 0]
        fish[:, :, :, 1] = midline_y[:, :, :, 0]
        fish[:, :, :, 2] = z_coords[:, :, :, 0]

        # Collocation velocities
        x_y_velocity = csdl.expand(combined_velocity[:, :, 0:2], (num_time_steps, num_pts_L, num_pts_R, 2), 'ijl->ijkl')
        fish_collocation_pts_velocity = self.create_output('fish_coll_vel', val=np.zeros((num_time_steps, num_pts_L - 1, num_pts_R - 1, 3)))
        fish_collocation_pts_velocity[:, :, :, :2] = 0.25 * (
            x_y_velocity[:, :-1, :-1, :] +
            x_y_velocity[:, :-1, 1:, :] +
            x_y_velocity[:, 1:, :-1, :] +
            x_y_velocity[:, 1:, 1:, :]
        )

if __name__ == '__main__':

    import numpy as np
    import csdl
    import python_csdl_backend
    import matplotlib.pyplot as plt
    from fish_actuation_pressure_multi_segs import EelAmplitudeModel
    from fish_kinematics_3segs_analytical import AnalyticalCCMVelocity
    from matplotlib.animation import FuncAnimation 

    plt.rcParams['text.usetex'] = False

    # ======================
    # Simulation Parameters
    # ======================
    num_time_steps = 84
    num_pts_segments = 15
    seg_names = ['seg1', 'seg2', 'seg3']
    input_seg_shapes = [(num_time_steps, num_pts_segments)] * len(seg_names)
    surface_shape = (45, 5)  # e.g. for mesh resolution (L_pts, R_pts)
    frequency_val = 1.5
    T = 1 / frequency_val
    time_vals = np.linspace(1.1e-3, 2 * T - 1.1e-3, num_time_steps)
    dt = (time_vals[1] - time_vals[0]) * 1000

    # ==========================
    # Create and configure model
    # ==========================
    model = csdl.Model()
    model.create_input('frequency', val=frequency_val)
    model.create_input('time_vector', val=time_vals)
    model.create_input('seg1_L', val=np.array([0.1]))
    model.create_input('seg2_L', val=np.array([0.1]))
    model.create_input('seg3_L', val=np.array([0.1]))

    model.create_input('fish_total_length', val=0.3)
    model.create_input('a_coeff', val=0.3)
    model.create_input('b_coeff', val=0.04)

    phi = [np.pi / 2, 0]

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

    model.add(
        AnalyticalCCMVelocity(
            seg_names=seg_names,
            input_seg_shapes=input_seg_shapes
        ),
        name='ccm_model'
    )

    model.add(
        CombineSegmentsAndGenerateMesh(
            seg_names=seg_names,
            input_seg_shapes=input_seg_shapes,
            surface_shape=surface_shape
        ),
        name='mesh_model'
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
    fig, ax = plt.subplots()
    ax.set_xlim(-0.1, 0.4)
    ax.set_ylim(-1, 1)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Segments Position and Velocity Over Time')
    ax.grid(True)
    ax.set_aspect('equal')
    ax.legend()

    scatter1 = ax.plot([], [], 'ro-', label='Segment 1')[0]
    scatter2 = ax.plot([], [], 'go-', label='Segment 2')[0]
    scatter3 = ax.plot([], [], 'bo-', label='Segment 3')[0]
    quiver_container1 = {'obj': None}
    quiver_container2 = {'obj': None}
    quiver_container3 = {'obj': None}

    def update(frame):
        for container in [quiver_container1, quiver_container2, quiver_container3]:
            if container['obj'] is not None:
                container['obj'].remove()

        x1, y1 = p_seg1[frame, :, 0], p_seg1[frame, :, 1]
        u1, v1 = v_seg1[frame, :, 0], v_seg1[frame, :, 1]
        scatter1.set_data(x1, y1)
        quiver_container1['obj'] = ax.quiver(x1, y1, u1, v1, angles='xy', scale_units='xy', scale=2.5, color='r')

        x2, y2 = p_seg2[frame, :, 0], p_seg2[frame, :, 1]
        u2, v2 = v_seg2[frame, :, 0], v_seg2[frame, :, 1]
        scatter2.set_data(x2, y2)
        quiver_container2['obj'] = ax.quiver(x2, y2, u2, v2, angles='xy', scale_units='xy', scale=2.5, color='g')

        x3, y3 = p_seg3[frame, :, 0], p_seg3[frame, :, 1]
        u3, v3 = v_seg3[frame, :, 0], v_seg3[frame, :, 1]
        scatter3.set_data(x3, y3)
        quiver_container3['obj'] = ax.quiver(x3, y3, u3, v3, angles='xy', scale_units='xy', scale=2.5, color='b')

        return scatter1, scatter2, scatter3, quiver_container1['obj'], quiver_container2['obj'], quiver_container3['obj']

    ani = FuncAnimation(fig, update, frames=num_time_steps, interval=dt, blit=False)
    plt.show()



from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

# Extract 3D mesh: (T, L, R, 3)
fish_mesh = sim['fish']
num_time_steps, num_pts_L, num_pts_R, _ = fish_mesh.shape

# Get global bounds
x_min, x_max = fish_mesh[:, :, :, 0].min(), fish_mesh[:, :, :, 0].max()
y_min, y_max = fish_mesh[:, :, :, 1].min(), fish_mesh[:, :, :, 1].max()
z_min, z_max = fish_mesh[:, :, :, 2].min(), fish_mesh[:, :, :, 2].max()

# Compute range for consistent scaling
max_range = max(x_max - x_min, y_max - y_min, z_max - z_min) / 2
mid_x = (x_max + x_min) / 2
mid_y = (y_max + y_min) / 2
mid_z = (z_max + z_min) / 2

# Set up 3D figure
fig_3d = plt.figure()
ax_3d = fig_3d.add_subplot(111, projection='3d')

# Animation update function
surf_plot = [None]  # mutable container to hold the surface plot

def update_3d(frame):
    ax_3d.clear()
    mesh = fish_mesh[frame]
    x = mesh[:, :, 0]
    y = mesh[:, :, 1]
    z = mesh[:, :, 2]

    surf_plot[0] = ax_3d.plot_surface(x, y, z, color='deepskyblue', edgecolor='k', rstride=1, cstride=1, linewidth=0.1, alpha=0.9)

    ax_3d.set_xlim(mid_x - max_range, mid_x + max_range)
    ax_3d.set_ylim(mid_y - max_range, mid_y + max_range)
    ax_3d.set_zlim(mid_z - max_range, mid_z + max_range)

    ax_3d.set_xlabel('X')
    ax_3d.set_ylabel('Y')
    ax_3d.set_zlabel('Z')
    ax_3d.set_title(f'Fish Body at t={frame}')
    return surf_plot[0],

# Create animation with loop
ani3d = FuncAnimation(fig_3d, update_3d, frames=num_time_steps, interval=dt, blit=False, repeat=True)

plt.show()


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Extract data
fish_mesh = sim['fish_rigid_mesh']  # shape: (T, total_pts_L, num_pts_R, 3)
time_vals = sim['time_vector']
t_target = 0.1
frame_idx = np.argmin(np.abs(time_vals - t_target))

# Segment structure
seg_lengths = [shape[1] for shape in input_seg_shapes]  # e.g. [15, 15, 15]
seg_colors = ['red', 'green', 'blue']
seg_start = np.cumsum([0] + seg_lengths[:-1])
seg_end = np.cumsum(seg_lengths)

# Prepare plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title(f'Fish Mesh Points at t = {time_vals[frame_idx]:.3f} s')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Plot segment by segment
mesh_frame = fish_mesh[frame_idx]

for i in range(3):
    mesh_seg = mesh_frame[seg_start[i]:seg_end[i], :, :]  # shape: (L_seg, R, 3)
    x = mesh_seg[:, :, 0].flatten()
    y = mesh_seg[:, :, 1].flatten()
    z = mesh_seg[:, :, 2].flatten()
    ax.scatter(x, y, z, color=seg_colors[i], s=5, label=f'Segment {i+1}')

# Fix axis scaling
def axis_equal(ax, x, y, z):
    max_range = np.array([x.max()-x.min(), y.max()-y.min(), z.max()-z.min()]).max() / 2.0
    mid_x = (x.max()+x.min()) * 0.5
    mid_y = (y.max()+y.min()) * 0.5
    mid_z = (z.max()+z.min()) * 0.5
    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)

# All points for scaling
x_all = fish_mesh[frame_idx, :, :, 0].flatten()
y_all = fish_mesh[frame_idx, :, :, 1].flatten()
z_all = fish_mesh[frame_idx, :, :, 2].flatten()
axis_equal(ax, x_all, y_all, z_all)

ax.legend()
plt.tight_layout()
plt.show()
