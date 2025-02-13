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

class FishGeometryModel(csdl.Model):
    def initialize(self):
        self.parameters.declare('surface_name')
        self.parameters.declare('surface_shape') # note this is without number of nodes

        self.parameters.declare('num_points_list')
        self.parameters.declare('start_epsilon',default=1e-6)

    def define(self):
        
        surface_name = self.parameters['surface_name']
        surface_shape = self.parameters['surface_shape']
        num_points_list = self.parameters['num_points_list']
        start_epsilon = self.parameters['start_epsilon']
        num_pts_R = surface_shape[1]
        num_pts_L = surface_shape[0]

        head_pts = int(num_points_list[0])
        body_pts = int(num_points_list[1])
        tail_pts = int(num_points_list[2])

        # declare variables for L, x1, h1, x2, h2, tail_width
        # TODO: L can probably be a constant for now
        L = 1.

        x1 = self.declare_variable('x1')
        h1 = self.declare_variable('h1')
        x2 = self.declare_variable('x2')
        h2 = self.declare_variable('h2')
        tail_width = self.declare_variable('tail_width')

        # coefficients for the head height as quadratic function of x_head
        a = -h1 /(x1**2) 
        b = -2*a*x1
        c = 0
        # coefficients for the body height as cubic function of x_body
        d = (-2*h1 + 2*h2)/(x1**3 - 3*x1**2*x2 + 3*x1*x2**2 - x2**3)
        e = (3*h1*x1 + 3*h1*x2 - 3*h2*x1 - 3*h2*x2)/(x1**3 - 3*x1**2*x2 + 3*x1*x2**2 - x2**3)
        f = (-6*h1*x1*x2 + 6*h2*x1*x2)/(x1**3 - 3*x1**2*x2 + 3*x1*x2**2 - x2**3)
        g = (3*h1*x1*x2**2 - h1*x2**3 + h2*x1**3 - 3*h2*x1**2*x2)/(x1**3 - 3*x1**2*x2 + 3*x1*x2**2 - x2**3)
        # coefficients for the tail height as quadratic function of x_tail
        h = (tail_width - h2)/(L**2 - 2*L*x2 + x2**2)
        i = (-2*tail_width*x2 + 2*h2*x2)/(L**2 - 2*L*x2 + x2**2)
        j = (L**2*h2 - 2*L*h2*x2 + tail_width*x2**2)/(L**2 - 2*L*x2 + x2**2)

        # self.register_output('a', a)
        # self.register_output('b', b)
        # self.register_output('d', d)
        # self.register_output('e', e)
        # self.register_output('f', f)
        # self.register_output('g', g)
        # self.register_output('h', h)
        # self.register_output('i', i)
        # self.register_output('j', j)

        x_head = np.linspace(start_epsilon, L, head_pts,endpoint=True) * csdl.expand(x1,shape=head_pts) # figure out whether this works
        x_body = np.linspace(0, L, body_pts,endpoint=True) * csdl.expand((x2 - x1),shape=body_pts) + csdl.expand(x1,shape=body_pts)
        x_tail = np.linspace(0, L, tail_pts) * csdl.expand((L - x2),shape=tail_pts) + csdl.expand(x2,shape=tail_pts)
        self.register_output('x_head', x_head)
        self.register_output('x_body', x_body)
        self.register_output('x_tail', x_tail)
        head_height_profile = self.compute_fish_head_profile(x_head, a,b)
        self.register_output('head_height_profile', head_height_profile)

        body_height_profile = self.compute_fish_body_profile(x_body, d,e,f,g)
        self.register_output('body_height_profile', body_height_profile)

        tail_height_profile = self.compute_fish_tail_profile(x_tail, h,i,j)
        self.register_output('tail_height_profile', tail_height_profile)
        head_height_profile_expand = csdl.expand(head_height_profile,shape=(head_pts,num_pts_R),indices='i->ijk')
        body_height_profile_expand = csdl.expand(body_height_profile,shape=(body_pts,num_pts_R),indices='i->ijk')
        tail_height_profile_expand = csdl.expand(tail_height_profile,shape=(tail_pts,num_pts_R),indices='i->ijk')

        rigid_fish_mesh = self.create_output(surface_name+'_rigid_mesh', val=np.zeros(surface_shape))
        rigid_fish_mesh[:head_pts,:,0] = csdl.expand(x_head,shape=(head_pts,num_pts_R,1),indices='i->ijk')
        rigid_fish_mesh[:head_pts,:,2] = csdl.reshape(np.outer(np.arange(num_pts_R) / (num_pts_R-1) - 1/2, np.ones(head_pts)).T * head_height_profile_expand *2, new_shape=(head_pts,num_pts_R,1))
        rigid_fish_mesh[head_pts:head_pts+body_pts,:,0] = csdl.expand(x_body,shape=(body_pts,num_pts_R,1),indices='i->ijk')
        rigid_fish_mesh[head_pts:head_pts+body_pts,:,2] = csdl.reshape(np.outer(np.arange(num_pts_R) / (num_pts_R-1) - 1/2, np.ones(body_pts)).T * body_height_profile_expand *2, new_shape=(body_pts,num_pts_R,1))
        rigid_fish_mesh[head_pts+body_pts:,:,0] = csdl.expand(x_tail,shape=(tail_pts,num_pts_R,1),indices='i->ijk')
        rigid_fish_mesh[head_pts+body_pts:,:,2] = csdl.reshape(np.outer(np.arange(num_pts_R) / (num_pts_R-1) - 1/2, np.ones(tail_pts)).T * tail_height_profile_expand *2, new_shape=(tail_pts,num_pts_R,1))

        # eel_height = self.compute_fish_height(x_head, x_body, x_tail, L,x1, h1, x2, h2, tail_width)

        # rigid_fish_mesh = self.create_output(surface_name+'_rigid_mesh', val=np.zeros(surface_shape))

        # self.compute_rigid_fish_mesh(x, eel_height,rigid_fish_mesh)

    def compute_fish_head_profile(self, x_head, a,b):
        a_expand = csdl.expand(a,shape=x_head.shape)
        b_expand = csdl.expand(b,shape=x_head.shape)
          
        head_height_profile = a_expand*x_head**2 + b_expand*x_head# + c
        return head_height_profile

    def compute_fish_body_profile(self, x_body, d,e,f,g):
        d_expand = csdl.expand(d,shape=x_body.shape)
        e_expand = csdl.expand(e,shape=x_body.shape)
        f_expand = csdl.expand(f,shape=x_body.shape)
        g_expand = csdl.expand(g,shape=x_body.shape)
          
        body_height_profile = d_expand*x_body**3 + e_expand*x_body**2 + f_expand*x_body + g_expand
        return body_height_profile

    def compute_fish_tail_profile(self, x_tail, h,i,j):
        h_expand = csdl.expand(h,shape=x_tail.shape)
        i_expand = csdl.expand(i,shape=x_tail.shape)
        j_expand = csdl.expand(j,shape=x_tail.shape)
          
        tail_height_profile = h_expand*x_tail**2 + i_expand*x_tail + j_expand
        return tail_height_profile



if __name__ == '__main__':
    num_pts_R = 5
    num_pts_L = 41
    L = 1.0
    
    # x1_val_list = [0.5627,0.54436,0.54337]
    # x2_val_list = [0.9,0.9,0.9]
    # h1_val_list = [0.13915,0.13708,0.13698]
    # h2_val_list = [0.0518,0.0592,0.05954]
    # tail_width_val_list = [0.14218215,0.14218215,0.14218215,]

    # x1_val_list = [0.5627,0.49282,0.2968]
    # x2_val_list = [0.9,0.88256,0.5859]
    # h1_val_list = [0.13915,0.11669,0.1036]
    # h2_val_list = [0.0518,0.0962,0.09339]
    # tail_width_val_list = [0.14218215,0.14218215,0.14218215,]

    # color_list = ['r','g','b'] 

    x1_val_list = [0.424]
    h1_val_list = [0.148]
    x2_val_list = [0.837]
    h2_val_list = [0.074]
    tail_width_val_list = [0.14218215]
    color_list = ['black'] * 3

    head_pts = int(num_pts_L * x1_val_list[0]*L / L)
    body_pts = int(num_pts_L * (x2_val_list[0]-x1_val_list[0])*L / L)
    tail_pts = num_pts_L - head_pts - body_pts

    num_points_list = [head_pts, body_pts, tail_pts]

    import numpy as np
    import python_csdl_backend
    for i in range(len(x1_val_list)):
        x1_val = x1_val_list[i]
        h1_val = h1_val_list[i]
        x2_val = x2_val_list[i]
        h2_val = h2_val_list[i]
        tail_width_val = tail_width_val_list[i]

        fish_geometry_model = csdl.Model()

        
        fish_geometry_model.create_input('x1', val=x1_val)
        fish_geometry_model.create_input('h1', val=h1_val)
        fish_geometry_model.create_input('x2', val=x2_val)
        fish_geometry_model.create_input('h2', val=h2_val)
        fish_geometry_model.create_input('tail_width', val=tail_width_val)


        model = FishGeometryModel(surface_name='fish',
                                            surface_shape=[num_pts_L,num_pts_R, 3],
                                            num_points_list=num_points_list)

        fish_geometry_model.add(model, 'FishGeometryModel')   


        simulator = python_csdl_backend.Simulator(fish_geometry_model, display_scripts=False)
        simulator.run()

        # simulator.check_partials(compact_print=True)

        # print('print inputs', simulator["x1"], simulator["h1"])
        # print('print head coefficients a', simulator["a"])
        # print('print head coefficients b', simulator["b"])
        # print('print body coefficients d', simulator["d"])
        # print('print body coefficients e', simulator["e"])
        # print('print body coefficients f', simulator["f"])
        # print('print body coefficients g', simulator["g"])
        # print('print tail coefficients h', simulator["h"])
        # print('print tail coefficients i', simulator["i"])
        # print('print tail coefficients j', simulator["j"])

        # print("print points along the fish")
        # print(simulator["x_head"])
        # print(simulator["x_body"])
        # print(simulator["x_tail"])
        def R(x, L=1):
            return 0.14 * np.sin(2 * np.pi * x / 1.6) + 0.0008 * L * (np.exp(2 * np.pi * x / 1.1) - 1)

        

        import matplotlib.pyplot as plt
        plt.rcParams['text.usetex'] = False
        from matplotlib.lines import Line2D

        # # plot head height profile
        # x_full = np.linspace(0, L, num_pts_L)
        x_head = simulator["x_head"]
        head_height_profile = simulator["head_height_profile"]
        x_body = simulator["x_body"]
        body_height_profile = simulator["body_height_profile"]
        x_tail = simulator["x_tail"]
        tail_height_profile = simulator["tail_height_profile"]


        # plt.figure(figsize=(6, 3))
        # plt.plot(x_full, R(x_full), label="Fish literature")
        # plt.plot(x_full, -R(x_full), label="Fish literature")
        # plt.plot(x_head, head_height_profile, '.-', label="Head quadratic")
        # plt.plot(x_body, body_height_profile, '.-', label="Body cubic")
        # plt.plot(x_tail, tail_height_profile, '.-', label="Tail quadratic")
        # plt.grid(True)
        # plt.axis('equal')
        # plt.legend()

        # plt.figure(figsize=(6, 3))
        # mesh = simulator['fish_rigid_mesh'].copy()
        mesh = simulator['fish_rigid_mesh'].copy()
        # print('mesh', mesh[:,-1,2])
        # add two subplots veritcally


        # plt.plot(mesh[:,:,0],mesh[:,:,2]+0., '.-', color='black')
        # plt.plot(mesh[:,:,0].T,mesh[:,:,2].T, '.-', color='black')

        plt.plot(mesh[:,:,0],mesh[:,:,2]+0., '.-',color=color_list[i],linewidth=0.4)
        plt.plot(mesh[:,:,0].T,mesh[:,:,2].T, '.-',color=color_list[i],linewidth=0.4)
        plt.axis('equal')

    # legend_handles = [
    #     Line2D([0], [0], color=color_list[0], lw=2, label='$V_x=0.3$ m/s'),
    #     Line2D([0], [0], color=color_list[1], lw=2, label='$V_x=0.6$ m/s'),
    #     Line2D([0], [0], color=color_list[2], lw=2, label='$V_x=0.9$ m/s')
    # ]  
    plt.plot(mesh[:,0,0], R(mesh[:,0,0]), color = 'blue',linewidth=3)
    plt.plot(x_head, head_height_profile,'o' ,markerfacecolor='none',label="Head quadratic",linewidth=3)
    plt.plot(x_body, body_height_profile, 'o',markerfacecolor='none',label="Body cubic",linewidth=3)
    plt.plot(x_tail, tail_height_profile,'o', markerfacecolor='none',label="Tail quadratic",linewidth=3)

    legend_handles = [
        Line2D([0], [0], color='blue', lw=2, label='Head quadratic function'),
        Line2D([0], [0], color='orange', lw=2, label='Head quadratic function'),
        Line2D([0], [0], color='green', lw=2, label='Head quadratic function'),
        Line2D([0], [0], color='blue', lw=2, label='Fish height profile from [33]'),
        # Line2D([0], [0], color=colsor_list[2], lw=2, label='$V_x=0.9$ m/s')
    ] 

    plt.legend(handles=legend_handles, loc='best', fontsize=12)  

# plt.figure(figsize=(6, 3))
# plt.plot(x_head, head_height_profile, '.-', label="Head quadratic")
# plt.plot(x_body, body_height_profile, '.-', label="Body cubic")
# plt.plot(x_tail, tail_height_profile, '.-', label="Tail quadratic")
# plt.show()

# # mesh = simulator['fish_rigid_mesh'].copy()
# mesh = simulator['fish_system_model_0.eel_rigid_mesh'].copy()
# # print('mesh', mesh[:,-1,2])
# # add two subplots veritcally


# # plt.plot(mesh[:,:,0],mesh[:,:,2]+0., '.-', color='black')
# # plt.plot(mesh[:,:,0].T,mesh[:,:,2].T, '.-', color='black')
# plt.plot(mesh[:,:,0],mesh[:,:,2]+0., '.-',color='black',linewidth=0.4)
# plt.plot(mesh[:,:,0].T,mesh[:,:,2].T, '.-',color='black',linewidth=0.4)
# plt.axis('equal')
# plt.show()


x_top_profile = mesh[:,-1,0]
z_top_profile = mesh[:,-1,2]

x_bottom_profile = mesh[:,0,0]
z_bottom_profile = mesh[:,0,2]


plt.figure(figsize=(8, 4))
plt.plot(x_top_profile[:head_pts], z_top_profile[:head_pts], 'r-',linewidth=1)        # top edge
plt.plot(x_bottom_profile[:head_pts], z_bottom_profile[:head_pts], 'r-',linewidth=1)  # bottom edge

plt.plot(x_top_profile[head_pts:head_pts+body_pts], z_top_profile[head_pts:head_pts+body_pts], 'grey',linewidth=1)        # top edge
plt.plot(x_bottom_profile[head_pts:head_pts+body_pts], z_bottom_profile[head_pts:head_pts+body_pts], 'grey',linewidth=1)  # bottom edge

plt.plot(x_top_profile[head_pts+body_pts:], z_top_profile[head_pts+body_pts:], 'b-',linewidth=1)        # top edge
plt.plot(x_bottom_profile[head_pts+body_pts:], z_bottom_profile[head_pts+body_pts:], 'b-',linewidth=1)  # bottom edge

plt.plot(mesh[:,0,0], R(mesh[:,0,0])+0.06,'--', color = 'black',markerfacecolor='none',linewidth=1.5)
plt.plot(x_head[0], head_height_profile[0],'o',color ='black' ,markerfacecolor='none',linewidth=3)
plt.plot(x_head[-1], head_height_profile[-1],'o',color ='black' ,markerfacecolor='none',label="Head quadratic",linewidth=3)
# plt.plot(x_body[0], body_height_profile[0], 'o', markerfacecolor='none',linewidth=3)
plt.plot(x_body[-1], body_height_profile[-1],'o',color ='black',markerfacecolor='none',label="Body cubic",linewidth=3)
plt.plot(x_tail[0], tail_height_profile[0],'o',color ='black',markerfacecolor='none',label="Tail quadratic",linewidth=3)
plt.plot(x_tail[-1], tail_height_profile[-1],'o',color ='black',markerfacecolor='none',label="Tail quadratic",linewidth=3)


# "Fill" between them
plt.fill_between(
    x_top_profile[:head_pts], 
    z_top_profile[:head_pts], 
    z_bottom_profile[:head_pts],
    color='red', alpha=0.3
)
plt.fill_between(
    x_top_profile[head_pts:head_pts+body_pts], 
    z_top_profile[head_pts:head_pts+body_pts], 
    z_bottom_profile[head_pts:head_pts+body_pts],
    color='gray', alpha=0.3
)
plt.fill_between(
    x_top_profile[head_pts+body_pts:], 
    z_top_profile[head_pts+body_pts:], 
    z_bottom_profile[head_pts+body_pts:],
    color='blue', alpha=0.3,
    # label='Tail quadratic curve',
)

plt.ylim(-0.25,0.25)

plt.axis('equal')
legend_handles = [
    Line2D([0], [0], color='red', lw=2, label='Head'),
    Line2D([0], [0], color='grey', lw=2, label='Body'),
    Line2D([0], [0], color='blue', lw=2, label='Tail'),
    Line2D([0], [0], color='black', linestyle='--',lw=2, label='Ref. [33]'),
    # Line2D([0], [0], color=colsor_list[2], lw=2, label='$V_x=0.9$ m/s')
] 
plt.xlabel('x (m)',fontsize=12)
plt.ylabel('Height (m)',fontsize=12)
plt.tight_layout()
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(handles=legend_handles, loc='best', fontsize=12, ncol=4) 
plt.show()
