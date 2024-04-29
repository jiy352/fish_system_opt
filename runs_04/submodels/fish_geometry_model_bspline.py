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
import scipy.sparse
# from get_b_spline_mtx import get_bspline_mtx

def get_bspline_mtx(num_cp, num_pt, order=4):
    order = min(order, num_cp)

    knots = np.zeros(num_cp + order)
    knots[order-1:num_cp+1] = np.linspace(0, 1, num_cp - order + 2)
    knots[num_cp+1:] = 1.0

    t_vec = np.linspace(0, 1, num_pt)

    basis = np.zeros(order)
    arange = np.arange(order)
    data = np.zeros((num_pt, order))
    rows = np.zeros((num_pt, order), int)
    cols = np.zeros((num_pt, order), int)

    for ipt in range(num_pt):
        t = t_vec[ipt]

        i0 = -1
        for ind in range(order, num_cp+1):
            if (knots[ind-1] <= t) and (t < knots[ind]):
                i0 = ind - order
        if t == knots[-1]:
            i0 = num_cp - order

        basis[:] = 0.
        basis[-1] = 1.

        for i in range(2, order+1):
            l = i - 1
            j1 = order - l
            j2 = order
            n = i0 + j1
            if knots[n+l] != knots[n]:
                basis[j1-1] = (knots[n+l] - t) / \
                              (knots[n+l] - knots[n]) * basis[j1]
            else:
                basis[j1-1] = 0.
            for j in range(j1+1, j2):
                n = i0 + j
                if knots[n+l-1] != knots[n-1]:
                    basis[j-1] = (t - knots[n-1]) / \
                                (knots[n+l-1] - knots[n-1]) * basis[j-1]
                else:
                    basis[j-1] = 0.
                if knots[n+l] != knots[n]:
                    basis[j-1] += (knots[n+l] - t) / \
                                  (knots[n+l] - knots[n]) * basis[j]
            n = i0 + j2
            if knots[n+l-1] != knots[n-1]:
                basis[j2-1] = (t - knots[n-1]) / \
                              (knots[n+l-1] - knots[n-1]) * basis[j2-1]
            else:
                basis[j2-1] = 0.

        data[ipt, :] = basis
        rows[ipt, :] = ipt
        cols[ipt, :] = i0 + arange

    data, rows, cols = data.flatten(), rows.flatten(), cols.flatten()

    return scipy.sparse.csr_matrix(
        (data, (rows, cols)), 
        shape=(num_pt, num_cp),
    )


class EelGeometryModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('surface_name')
        self.parameters.declare('surface_shape') # note this is without number of nodes
        self.parameters.declare('num_cp')
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
        num_cp = self.parameters['num_cp']

        L = self.declare_variable('L',val=1.0)


        a = 0.51
        b = 0.08
        x_np = np.linspace(0,1,num_cp)
        control_points_inital = b * np.sqrt(1 - ((x_np - a)/a)**2)

        control_points = self.declare_variable('control_points',val=control_points_inital)
        # a_coeff = self.declare_variable('a_coeff',val=0.51)
        # b_coeff = self.declare_variable('b_coeff',val=0.08)

        # a = a_coeff * L
        # b = b_coeff * L
        L_expand = csdl.expand(L,shape=(num_pts_L,))
        if discretization == 'uniform':
            x = np.linspace(start_epsilon,1,num_pts_L) * L_expand 
        elif discretization == 'cosine':
            raise NotImplementedError

        # a_expand = csdl.expand(a,shape=x.shape)
        # b_expand = csdl.expand(b,shape=x.shape)
        height = csdl.matvec(get_bspline_mtx(num_cp, num_pts_L, 4), control_points) * L_expand
        # the height is scaling with L right now

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
    num_pts_L = 41
    L = 1.0
    s_1_ind = 5
    s_2_ind = num_pts_L-3

    import numpy as np
    import python_csdl_backend
    eel_geometry_model = EelGeometryModel(surface_name='eel',
                                        surface_shape=[num_pts_L,num_pts_R, 3],
                                        s_1_ind=s_1_ind,s_2_ind=s_2_ind)

    eel_geometry_model.create_input('L', val=L)
    # eel_geometry_model.create_input('a_coeff', val=0.55)
    # eel_geometry_model.create_input('b_coeff', val=0.08)
    # eel_geometry_model.create_input('control_points', val=np.array([[0.005, 0.10996615, 0.12, 0.12, 0.02146652, 0.005, 0.00671981, 0.12]]))
    simulator = python_csdl_backend.Simulator(eel_geometry_model, display_scripts=False)
    simulator.run()

    simulator.check_partials(compact_print=True)

    height = simulator['eel_height']
    x = np.linspace(0,L,num_pts_L)

    import matplotlib.pyplot as plt
    plt.rcParams['text.usetex'] = False


    plt.figure()
    # plt.plot(x, height, '.')
    plt.axis('equal')
    plt.title('Eel Height Profile')

    mesh = simulator['eel_rigid_mesh']
    plt.plot(mesh[:,:,0],mesh[:,:,2]+0., '.')

    plt.show()
