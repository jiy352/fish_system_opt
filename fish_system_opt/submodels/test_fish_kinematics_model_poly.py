from fish_geometry_model import EelGeometryModel
from fish_kinematics_model_poly import EelKinematicsModel
import csdl
import numpy as np


num_pts_R = 5
num_pts_L = 41
L = 1.0
s_1_ind = 5
s_2_ind = num_pts_L-3
num_time_steps = 20
num_period = 2
num_amp_cp = 3
surface_shape = (num_pts_L,num_pts_R, 3)



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

coeffs = np.array([0.02, -0.08, 0.16])

eel_model.create_input('tail_frequency',val=0.48)
eel_model.create_input('wave_length',val=1.0)
eel_model.create_input('amplitude_max',val=0.1)
eel_model.create_input('eel_amplitude_cp',val=coeffs)


simulator = python_csdl_backend.Simulator(eel_model, display_scripts=False)
simulator.run()
# simulator.check_partials(compact_print=True)
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = False
diff = (simulator['eel'][1:,20,1,1]-simulator['eel'][:-1,20,1,1])
dt = (simulator['time_vector'][1]-simulator['time_vector'][0])/0.48
plt.figure()
plt.plot(diff/dt)
plt.plot(simulator['eel_lateral_velocity'][:,20,1].flatten())

# exit()

# simulator.check_partials(compact_print=True)


height = simulator['eel_height']
x = np.linspace(0,L,num_pts_L)

import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = False

plt.figure()
x = np.linspace(0,L,num_pts_L)
plt.plot(x, simulator['amplitude'])
plt.title('Amplitude')
plt.xlim([0,1])
plt.ylim([0,0.1])

plt.figure()
x = np.linspace(0,L,num_pts_L)
for i in range(num_time_steps):
    plt.plot(x, simulator['eel_amplitude_along_body'][i,:,0,0])

plt.title('Amplitude along body at different time steps')
plt.xlim([0,1])
plt.ylim([-0.1,0.1])
plt.show()

exit()

###############################################################################################
###############################################################################################
###############################################################################################
###############################################################################################
###############################################################################################

from mpl_toolkits.mplot3d import Axes3D
import time

# Example data: A list of arrays, where each array represents a time step
# Replace this with your actual data

plt.ion()  # Turn on interactive mode
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

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