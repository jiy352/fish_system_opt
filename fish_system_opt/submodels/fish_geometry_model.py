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
            x = np.linspace(start_epsilon,1,num_pts_L) * L_expand
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

    import numpy as np
    import python_csdl_backend
    eel_geometry_model = EelGeometryModel(surface_name='eel',
                                        surface_shape=[num_pts_L,num_pts_R, 3],
                                        s_1_ind=s_1_ind,s_2_ind=s_2_ind)

    eel_geometry_model.create_input('L', val=L)
    eel_geometry_model.create_input('a_coeff', val=0.51)
    eel_geometry_model.create_input('b_coeff', val=0.08)
    simulator = python_csdl_backend.Simulator(eel_geometry_model, display_scripts=False)
    simulator.run()

    simulator.check_partials(compact_print=True)

    height = simulator['eel_height']
    x = np.linspace(0,L,num_pts_L)

    import matplotlib.pyplot as plt
    plt.rcParams['text.usetex'] = False


    plt.figure()
    # plt.plot(x, height, '.')
    # plt.title('Eel Height Profile')

    mesh = simulator['eel_rigid_mesh']
    # add two subplots veritcally
    plt.subplot(2,1,2)
    plt.plot(mesh[:,:,0],mesh[:,:,2]+0., '.-', color='black')
    plt.plot(mesh[:,:,0].T,mesh[:,:,2].T, '.-', color='black')
    # add x axis limit
    # plt.xlim([-0.1,1.1])
    plt.ylim([-0.15,0.15])
    plt.tight_layout()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.subplot(2,1,1)
    plt.plot(mesh[:,0,0],mesh[:,-1,2]+0., '.-', color='black')
    plt.ylim([-0.1,0.2])
    plt.xlabel('x (m)')
    plt.ylabel('Height (m)')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.tight_layout()
    plt.savefig('eel_geometry.pdf', dpi=400)

    plt.show()
