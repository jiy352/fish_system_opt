# The fish mesh can be computed from Carling 1998, where the height profile of the fish is given by:
# height = b*(1-((x-a)/a)**2)**0.5

# the inputs are:
# L: length of the fish

# the parameters are:
# num_pts_L: number of points in the length direction
# num_pts_R: number of points in the radial direction
# s_1_ind: number of points for the head region
# s_2_ind: number of points for the tail region
# discretization: 'uniform' or 'cosine'

import numpy as np
import matplotlib.pyplot as plt
def generate_eel_carling(num_pts_L,num_pts_R,L,s_1_ind,s_2_ind, discretization='cosine', a_coeff = 0.55, b_coeff = 0.08):


    s1 = 0.04 * L
    s2 = 0.95 * L

    a = a_coeff * L
    b = b_coeff * L

    width = np.zeros(num_pts_L)
    height = np.zeros(num_pts_L)
    if discretization == 'uniform':
        x = np.linspace(0,L,num_pts_L) 

    elif discretization == 'cosine':
        x_1 = (1-np.cos(np.linspace(0, np.pi/2,s_1_ind,endpoint=False)))/1*s1
        x_2 = np.linspace(s1, s2, int(s_2_ind-s_1_ind),endpoint=False)
        x_3 = np.linspace(s2, L, int(num_pts_L-s_2_ind))

        x = np.concatenate((x_1,x_2,x_3))

    height = b*(1-((x-a)/a)**2)**0.5

    print('height',height.shape)

    mesh = np.zeros((num_pts_R, num_pts_L, 3))
    mesh[:, :, 0] = (np.outer(x, np.ones(num_pts_R))).T * L
    mesh[:, :, 1] = np.outer((np.arange(num_pts_R) / (num_pts_R-1) - 1/2), np.ones(num_pts_L)*height) 
    mesh[:, :, 2] = 0.

    return x,height, mesh


if __name__ == '__main__':
    num_pts_R = 5
    num_pts_L = 41
    L = 1.0
    s_1_ind = 5
    s_2_ind = num_pts_L-3


    x, height, mesh = generate_eel_carling(num_pts_L,num_pts_R,L,s_1_ind,s_2_ind,b_coeff=0.05)
    # plt.plot(x,width)
    # plt.plot(x,height)

    plt.plot(mesh[:,:,0],mesh[:,:,1]+0.5, '.')
    for i in range(num_pts_R):
        plt.plot(mesh[i,:,0],mesh[i,:,1]+0.5, '-k')

    x, height, mesh_1 = generate_eel_carling(num_pts_L,num_pts_R,L,s_1_ind,s_2_ind, b_coeff=0.08)
    # plt.plot(x,width)
    # plt.plot(x,height)

    plt.plot(mesh_1[:,:,0],mesh_1[:,:,1]+0.25, '.')
    for i in range(num_pts_R):
        plt.plot(mesh_1[i,:,0],mesh_1[i,:,1]+0.25, '-k')

    x, height, mesh_2 = generate_eel_carling(num_pts_L,num_pts_R,L,s_1_ind,s_2_ind, b_coeff=0.11)
    # plt.plot(x,width)
    # plt.plot(x,height)

    plt.plot(mesh_2[:,:,0],mesh_2[:,:,1]+0., '.')
    for i in range(num_pts_R):
        plt.plot(mesh_2[i,:,0],mesh_2[i,:,1]+0., '-k')

    x, height, mesh_3 = generate_eel_carling(num_pts_L,num_pts_R,L,s_1_ind,s_2_ind, b_coeff=.14)
    # plt.plot(x,width)
    # plt.plot(x,height)

    plt.plot(mesh_3[:,:,0],mesh_3[:,:,1]-0.25, '.')
    for i in range(num_pts_R):
        plt.plot(mesh_3[i,:,0],mesh_3[i,:,1]-0.25, '-k')

    # x, height, mesh_2 = generate_eel_carling(num_pts_L,num_pts_R,L*2,s_1_ind,s_2_ind)
    # plt.plot(mesh_2[:,:,0],mesh_2[:,:,1], '.')
    # # plot wireframe of the fish
    # for i in range(num_pts_R):
    #     plt.plot(mesh_2[i,:,0],mesh_2[i,:,1], '-k')

    # x, height, mesh_2 = generate_eel_carling(num_pts_L,num_pts_R,L*0.5,s_1_ind,s_2_ind)
    # plt.plot(mesh_2[:,:,0],mesh_2[:,:,1]-.5, '.')
    # # plot wireframe of the fish
    # for i in range(num_pts_R):
    #     plt.plot(mesh_2[i,:,0],mesh_2[i,:,1]-.5, '-k')

    # aixs equal
    plt.axis('equal')

    plt.show()