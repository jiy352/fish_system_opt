import csdl

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
            CoM_x, CoM_z = self.compute_CoM(rigid_fish_mesh)
            self.register_output(surface_name+'_CoM_x', CoM_x)
            # self.register_output(surface_name+'_CoM_y', CoM_y)

    def compute_CoM(self, rigid_fish_mesh):
        nx = rigid_fish_mesh.shape[0]
        ny = rigid_fish_mesh.shape[1]
        # x_CoM = csdl.sum(rigid_fish_mesh[:,:,0], axes=(0,1))/(nx*ny)
        # z_CoM = csdl.sum(rigid_fish_mesh[:,:,2], axes=(0,1))/(nx*ny)
        ###########################################
        # compute the area of the panels
        ###########################################
        i = rigid_fish_mesh[:-1, 1:, :] - rigid_fish_mesh[1:, :-1, :]
        j = rigid_fish_mesh[:-1, :-1, :] - rigid_fish_mesh[1:, 1:, :]
        # compute the wetted area:
        normals = csdl.cross(i, j, axis=2)
        s_panels = (csdl.sum(normals**2, axes=(2, )))**0.5 * 0.5
        ###########################################
        # compute the center of each panel
        ###########################################
        x_center = (rigid_fish_mesh[:-1, 1:, 0] + rigid_fish_mesh[1:, :-1, 0] + rigid_fish_mesh[:-1, :-1, 0] + rigid_fish_mesh[1:, 1:, 0])/4
        z_center = (rigid_fish_mesh[:-1, 1:, 2] + rigid_fish_mesh[1:, :-1, 2] + rigid_fish_mesh[:-1, :-1, 2] + rigid_fish_mesh[1:, 1:, 2])/4
        ###########################################
        # compute the CoM
        ###########################################

        # print('s_panels', s_panels.shape)
        # print('x_center', x_center.shape)
        x_center_reshape = csdl.reshape(x_center,( (nx-1),(ny-1)))
        z_center_reshape = csdl.reshape(z_center, ((nx-1),(ny-1)))
        x_CoM = csdl.sum(x_center_reshape * s_panels)/csdl.sum(s_panels)
        z_CoM = csdl.sum(z_center_reshape * s_panels)/csdl.sum(s_panels)
        return x_CoM, z_CoM


if __name__ == '__main__':
    num_pts_R = 5
    num_pts_L = 41
    L = 1.0
    s_1_ind = 5
    s_2_ind = num_pts_L-3

    import numpy as np
    import python_csdl_backend
    from fish_system_opt.submodels.fish_geometry_model_bspline import EelGeometryModel

    model = csdl.Model()

    num_cp = 5
    a = 0.51
    b = 0.08

    x = np.linspace(1e-3, 1, num_cp)
    height =  b * np.sqrt(1 - ((x - a)/a)**2)
    model.create_input('control_points', val=height)

    eel_geometry_model = EelGeometryModel(surface_name='eel',
                                        surface_shape=[num_pts_L,num_pts_R, 3],
                                        num_cp=num_cp,
                                        s_1_ind=s_1_ind,s_2_ind=s_2_ind)
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


    import matplotlib.pyplot as plt
    plt.rcParams['text.usetex'] = False
    x = sim['eel_rigid_mesh'][:,:,0].flatten()
    z = sim['eel_rigid_mesh'][:,:,2].flatten()
    plt.plot(x, z, '.')
    # axes equal
    plt.axis('equal')
    plt.show()