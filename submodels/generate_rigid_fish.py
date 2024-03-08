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
        self.parameters.declare('start_epsilon',default=1e-3)
    def define(self):
        surface_name = self.parameters['surface_name']
        surface_shape = self.parameters['surface_shape']

        eel_height = self.compute_eel_height()
        self.register_output('eel_height', eel_height)

    def compute_eel_height(self):
        s_1_ind = self.parameters['s_1_ind']
        s_2_ind = self.parameters['s_2_ind']
        discretization = self.parameters['discretization']
        num_pts_L = self.parameters['surface_shape'][0]
        num_pts_R = self.parameters['surface_shape'][1]
        start_epsilon = self.parameters['start_epsilon']

        L = self.declare_variable('L',val=1.0)
        a_coeff = self.declare_variable('a_coeff',val=0.55)
        b_coeff = self.declare_variable('b_coeff',val=0.08)

        a = a_coeff * L
        b = b_coeff * L

        L_expand = csdl.expand(L,shape=(num_pts_L,))

        if discretization == 'uniform':
            x = np.linspace(start_epsilon,1,num_pts_L) * L_expand
        a_expand = csdl.expand(a,shape=x.shape)
        b_expand = csdl.expand(b,shape=x.shape)

        height = b_expand*(1-((x-a_expand)/a_expand)**2)**0.5
        return height





if __name__ == '__main__':
    num_pts_R = 5
    num_pts_L = 41
    L = 1.0
    s_1_ind = 5
    s_2_ind = num_pts_L-3

    import numpy as np
    import python_csdl_backend
    eel_geometry_model = EelGeometryModel(surface_name='eel',
                                        surface_shape=[num_pts_L,num_pts_R, 3],
                                        s_1_ind=s_1_ind,s_2_ind=s_2_ind)

    simulator = python_csdl_backend.Simulator(eel_geometry_model, display_scripts=True)
    simulator.run()

    simulator.check_partials(compact_print=True)

    height = simulator['eel_height']
    x = np.linspace(0,L,num_pts_L)

    
    import matplotlib.pyplot as plt
    plt.rcParams['text.usetex'] = False


    plt.figure()


    plt.plot(x, height, '.')
    plt.axis('equal')
    plt.title('Eel Height Profile')

    plt.show()

