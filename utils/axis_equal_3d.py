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


def plot3d(mesh_all_ts):
    num_time_steps = mesh_all_ts.shape[0]
    for i in range(num_time_steps):
        ax.clear()  # Clear previous points
        axis_equal(ax, num_time_steps[:,:,:,0], num_time_steps[:,:,:,1], num_time_steps[:,:,:,2])
        data = num_time_steps[i]
        x = data[:,:,0].flatten()
        y = data[:,:,1].flatten()
        z = data[:,:,2].flatten()

        ax.scatter(x, y, z)
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
        plt.draw()
        plt.pause(0.01)  # Pause to update the plot
        time.sleep(0.01)  # Adjust as per your time step's actual duration

    plt.ioff()  # Turn off interactive mode
    plt.show()