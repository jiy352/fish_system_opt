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

class EelGeometryModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('surface_name')
        self.parameters.declare('surface_shape') # note this is without number of nodes
        self.parameters.declare('s_1_ind')
        self.parameters.declare('s_2_ind')
        self.parameters.declare('discretization',default='uniform')
        self.parameters.declare('start_epsilon',default=1e-10)
    def define(self):
        surface_name = self.parameters['surface_name']
        surface_shape = self.parameters['surface_shape']

        x, eel_height = self.compute_eel_height()
        self.register_output(surface_name+'_height', eel_height)

        rigid_fish_mesh = self.create_output(surface_name+'_rigid_mesh', val=np.zeros(surface_shape))

        self.compute_rigid_fish_mesh(x, eel_height,rigid_fish_mesh)

    def compute_eel_height(self):
        s_1_ind = self.parameters['s_1_ind']
        s_2_ind = self.parameters['s_2_ind']
        discretization = self.parameters['discretization']
        num_pts_L = self.parameters['surface_shape'][0]
        num_pts_R = self.parameters['surface_shape'][1]
        start_epsilon = self.parameters['start_epsilon']

        L = self.declare_variable('L',val=1.0)
        a_coeff = self.declare_variable('a_coeff',val=0.51)
        b_coeff = self.declare_variable('b_coeff',val=0.08)

        a = a_coeff * L
        b = b_coeff * L
        L_expand = csdl.expand(L,shape=(num_pts_L,))
        if discretization == 'uniform':
            print('uniform')
            print(num_pts_L)
            x = np.linspace(start_epsilon,1,int(num_pts_L)) * L_expand
        elif discretization == 'cosine':
            raise NotImplementedError

        a_expand = csdl.expand(a,shape=x.shape)
        b_expand = csdl.expand(b,shape=x.shape)
        height = b_expand*(1-((x-a_expand)/a_expand)**2)**0.5
        # this height is scaling with L right now

        return x, height

    def compute_rigid_fish_mesh(self, x, height,rigid_fish_mesh):
        s_1_ind = self.parameters['s_1_ind']
        s_2_ind = self.parameters['s_2_ind']
        discretization = self.parameters['discretization']
        num_pts_L = self.parameters['surface_shape'][0]
        num_pts_R = self.parameters['surface_shape'][1]
        start_epsilon = self.parameters['start_epsilon']

        x_expand_2d = csdl.expand(x,shape=(num_pts_L,num_pts_R), indices='i->ij')
        height_expand = csdl.expand(height,shape=(num_pts_L,num_pts_R), indices='i->ij')
        rigid_fish_mesh[:,:,0] = csdl.reshape(x_expand_2d,new_shape=(num_pts_L,num_pts_R,1))
        rigid_fish_mesh[:,:,2] = csdl.reshape(np.outer(np.arange(num_pts_R) / (num_pts_R-1) - 1/2, np.ones(num_pts_L)).T * height_expand *2, new_shape=(num_pts_L,num_pts_R,1))
        # times 2 since the height is half axis length

        return rigid_fish_mesh



if __name__ == '__main__':
    num_pts_R = 5
    num_pts_L = 51
    L = 1.0
    s_1_ind = 5
    s_2_ind = num_pts_L-3

    # a = 0.508
    # b = 0.082
    # a = 0.551
    # b = 0.078
    # a = 0.654
    # b = 0.077
    a_list = [0.508, 0.551, 0.654]
    b_list = [0.082, 0.078, 0.077]
    color_list = ['r','g','b']  

    # Data
    

    vx_0_3 = [
        0.0092, 0.0083, 0.0075, 0.0069, 0.0065, 0.0061, 0.0059, 0.0058, 0.0058,
        0.0059, 0.0060, 0.0062, 0.0065, 0.0068, 0.0071, 0.0075, 0.0079, 0.0084,
        0.0088, 0.0093, 0.0099, 0.0105, 0.0111, 0.0118, 0.0126, 0.0133, 0.0142,
        0.0151, 0.0160, 0.0170, 0.0180, 0.0190, 0.0200, 0.0211, 0.0221, 0.0230,
        0.0239, 0.0248, 0.0256, 0.0263, 0.0270
    ]

    vx_0_6 = [
        0.0146, 0.0132, 0.0122, 0.0115, 0.0112, 0.0111, 0.0112, 0.0116, 0.0122,
        0.0130, 0.0139, 0.0150, 0.0161, 0.0173, 0.0186, 0.0198, 0.0211, 0.0224,
        0.0236, 0.0249, 0.0261, 0.0273, 0.0284, 0.0295, 0.0305, 0.0314, 0.0322,
        0.0330, 0.0336, 0.0341, 0.0346, 0.0350, 0.0353, 0.0356, 0.0358, 0.0360,
        0.0362, 0.0363, 0.0365, 0.0367, 0.0369
    ]

    vx_0_9 = [
        0.0200, 0.0181, 0.0166, 0.0155, 0.0148, 0.0144, 0.0143, 0.0145, 0.0149,
        0.0156, 0.0164, 0.0174, 0.0184, 0.0196, 0.0208, 0.0220, 0.0233, 0.0246,
        0.0258, 0.0271, 0.0283, 0.0295, 0.0306, 0.0317, 0.0327, 0.0336, 0.0345,
        0.0352, 0.0358, 0.0364, 0.0368, 0.0372, 0.0376, 0.0379, 0.0381, 0.0384,
        0.0386, 0.0389, 0.0391, 0.0394, 0.0397
    ]


    import numpy as np
    import python_csdl_backend

    import matplotlib.pyplot as plt
    plt.rcParams['text.usetex'] = False
    from matplotlib.lines import Line2D


    # plt.figure(figsize=(12, 6))
    fig, axs = plt.subplots(2, 1, figsize=(10, 4.5))

    for i in np.arange(len(a_list)):
    # for i in np.arange(1):
        eel_geometry_model = EelGeometryModel(surface_name='eel',
                                            surface_shape=[num_pts_L,num_pts_R, 3],
                                            s_1_ind=s_1_ind,s_2_ind=s_2_ind)

        eel_geometry_model.create_input('L', val=L)
        # eel_geometry_model.create_input('a_coeff', val=0.51)
        # eel_geometry_model.create_input('b_coeff', val=0.08)
        eel_geometry_model.create_input('a_coeff', val=a_list[i])
        eel_geometry_model.create_input('b_coeff', val=b_list[i])
        simulator = python_csdl_backend.Simulator(eel_geometry_model, display_scripts=False)
        simulator.run()

        # simulator.check_partials(compact_print=True)

        height = simulator['eel_height']
        x = np.linspace(0,L,num_pts_L)


        # plt.plot(x, height, '.')
        # plt.title('Eel Height Profile')

        mesh = simulator['eel_rigid_mesh'].copy()
        # print('mesh', mesh[:,-1,2])
        # add two subplots veritcally
        
        plt.subplot(2,1,2)
        print('i', i)
        # plt.plot(mesh[:,:,0],mesh[:,:,2]+0., '.-', color='black')
        # plt.plot(mesh[:,:,0].T,mesh[:,:,2].T, '.-', color='black')
        axs[1].plot(mesh[:,:,0],mesh[:,:,2]+0., '.-',color=color_list[i],linewidth=0.4)
        axs[1].plot(mesh[:,:,0].T,mesh[:,:,2].T, '.-',color=color_list[i],linewidth=0.4)
        # add x axis limit
        # plt.xlim([-0.1,1.1])
        # axs[0].ylim([-0.15,0.3])
        # axs[0].tight_layout()
        # axs[0].gca().set_aspect('equal', adjustable='box')
        axs[1].set_xlabel('x (m)\n (b)', fontsize=12)
        axs[1].set_ylabel('Height (m)', fontsize=12)
        '''
        plt.subplot(2,1,1)

        # plt.plot(mesh[:,0,0],mesh[:,-1,2]+0., '.-', color='black')
        plt.plot(mesh[:,0,0],mesh[:,-1,2]+0., '.-', color=color_list[i])
        plt.ylim([-0.1,0.2])
        plt.xlabel('x (m)')
        plt.ylabel('Height (m)')
        plt.gca().set_aspect('equal', adjustable='box')
        plt.tight_layout()
        '''
    x = [
        0.0000, 0.0250, 0.0500, 0.0750, 0.1000, 0.1250, 0.1500, 0.1750, 0.2000,
        0.2250, 0.2500, 0.2750, 0.3000, 0.3250, 0.3500, 0.3750, 0.4000, 0.4250,
        0.4500, 0.4750, 0.5000, 0.5250, 0.5500, 0.5750, 0.6000, 0.6250, 0.6500,
        0.6750, 0.7000, 0.7250, 0.7500, 0.7750, 0.8000, 0.8250, 0.8500, 0.8750,
        0.9000, 0.9250, 0.9500, 0.9750, 1.0000
    ]
    axs[0].plot(x, vx_0_3, label="$V_x=0.3$ m/s", linewidth=2, color="red")
    axs[0].plot(x, vx_0_6, label="$V_x=0.6$ m/s", linewidth=2, color="green")
    axs[0].plot(x, vx_0_9, label="$V_x=0.9$ m/s", linewidth=2, color="blue")
    axs[1].set_aspect('equal', adjustable='box')
    # axs[0].set_aspect('equal', adjustable='box')

    # Create custom legend handles with the desired colors
    legend_handles = [
        Line2D([0], [0], color=color_list[0], lw=2, label='$V_x=0.3$ m/s'),
        Line2D([0], [0], color=color_list[1], lw=2, label='$V_x=0.6$ m/s'),
        Line2D([0], [0], color=color_list[2], lw=2, label='$V_x=0.9$ m/s')
    ]

    # Add the legend to the plot
    axs[0].legend(handles=legend_handles, loc='best', fontsize=12)
    # set x and y labels
    axs[0].set_xlabel('x (m)\n (a)', fontsize=12)
    axs[0].set_ylabel('Amplitude (m)', fontsize=12)
    plt.tight_layout()
    plt.savefig('eel_geometry.pdf', dpi=400)

    plt.show()
