import csdl
import numpy as np

class CoMModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('surface_names')
        self.parameters.declare('surface_shapes') # note this is without number of nodes

    def define(self):
        surface_names = self.parameters['surface_names']
        surface_shapes = self.parameters['surface_shapes']
        
        for i in range(len(surface_names)):
            surface_name = surface_names[i]
            surface_shape = surface_shapes[i]
            print(surface_name)
            print(surface_shape)
            rigid_fish_mesh = self.declare_variable(surface_name+'_rigid_mesh', shape=surface_shape)
            x_com = self.compute_CoM(rigid_fish_mesh)
            self.register_output(surface_name+'_CoM_x', x_com)
            # self.register_output(surface_name+'_CoM_y', CoM_y)

    def compute_CoM(self, rigid_fish_mesh):
        nx = rigid_fish_mesh.shape[0]
        ny = rigid_fish_mesh.shape[1]

        x = csdl.reshape(rigid_fish_mesh[:,-1,0],(nx,)) # x-coordinates of top edge, here we just take the first column because mesh is the same at all columns
        # here the shape is (nx, 1, 1) , reshaped it to (nx,)
        half_height = csdl.reshape(rigid_fish_mesh[:,-1,2],(nx,))
        # z-coordinates of top edge, here we just take the first column because it is the half_height of the fish

        # we use the naca0012 profile to compute the half thickness
        # https://turbmodels.larc.nasa.gov/naca0012_val.html
        c = 1.0 # chord length this is temperal and the same as length of fish
        half_thickness = 0.594689181 * (0.298222773 * (x / c)**0.5 
                        - 0.127125232 * (x / c) 
                        - 0.357907906 * (x / c)**2 
                        + 0.291984971 * (x / c)**3 
                        - 0.105174606 * (x / c)**4)
        # compute volume of each panel using trapezoidal rule
        vol = np.pi * (x[1:]-x[:-1]) * 0.5* (half_height[:-1]+half_height[1:]) * 0.5* (half_thickness[:-1]+half_thickness[1:])
        # compute total volume
        total_vol = csdl.sum(vol)
        mass = 997*total_vol
        self.register_output('half_height', half_height)
        self.register_output('half_thickness', half_thickness)
        self.register_output('mass', mass)
        # self.register_output('total_vol', total_vol)
        # self.register_output('vol', total_vol)
        # compute the CoM
        x_com = csdl.sum(0.5*(x[:-1]+x[1:]) * vol) / total_vol
        return x_com


if __name__ == '__main__':
    num_pts_R = 5
    num_pts_L = 41
    L = 1.0
    s_1_ind = 5
    s_2_ind = num_pts_L-3

    import numpy as np
    import python_csdl_backend
    from fish_system_opt.submodels.fish_geometry_model_carangiform import FishGeometryModel

    model = csdl.Model()


    L = 1.0
    num_pts_L = 41
    num_pts_R = 5
    num_period = 2
    x1_val = 0.424
    h1_val = 0.148
    x2_val = 0.837
    h2_val = 0.074
    tail_width_val = 0.14218215

    head_pts = int(num_pts_L * x1_val*L / L)
    body_pts = int(num_pts_L * (x2_val-x1_val)*L / L)
    tail_pts = num_pts_L - head_pts - body_pts
    num_points_list = [head_pts, body_pts, tail_pts]

    model.create_input('x1', val=x1_val)
    model.create_input('h1', val=h1_val)
    model.create_input('x2', val=x2_val)
    model.create_input('h2', val=h2_val)
    model.create_input('tail_width', val=tail_width_val)

    eel_geometry_model = FishGeometryModel(surface_name='eel',
                                        surface_shape=[num_pts_L,num_pts_R, 3],
                                        num_points_list=num_points_list)
    model.add(eel_geometry_model, 'EelGeometryModel')


    eel_com_model = CoMModel(surface_names=['eel'],
                            surface_shapes=[(num_pts_L,num_pts_R, 3)])    
    model.add(eel_com_model, 'CoMModel')

    sim = python_csdl_backend.Simulator(model, display_scripts=False)


    # eel_geometry_model.create_input('L', val=L)
    # # eel_geometry_model.create_input('a_coeff', val=0.55)
    # # eel_geometry_model.create_input('b_coeff', val=0.08)
    # # eel_geometry_model.create_input('control_points', val=np.array([[0.005, 0.10996615, 0.12, 0.12, 0.02146652, 0.005, 0.00671981, 0.12]]))
    # simulator = python_csdl_backend.Simulator(eel_geometry_model, display_scripts=False)
    sim.run()       

    print('eel_CoM_x', sim['eel_CoM_x']) 


    # import matplotlib.pyplot as plt
    # plt.rcParams['text.usetex'] = False
    # x = sim['eel_rigid_mesh'][:,:,0].flatten()
    # z = sim['eel_rigid_mesh'][:,:,2].flatten()
    # plt.plot(x, z, '.')
    # # axes equal
    # plt.axis('equal')

    # plt.figure()
    # plt.plot(sim['eel_rigid_mesh'][:,0,0],sim['half_thickness'], label='half_thickness')
    # plt.plot(sim['eel_rigid_mesh'][:,0,0],sim['half_height'], label='half_height')
    # plt.axis('equal')
    # plt.legend()
    # plt.show()