
from beam_dyamic_model import *

beam_name = 'eel'
num_beam_nodes = 5

eta_M = 0.2
eta_K = 0.02
# fixed_node = int(num_beam_nodes / 2)
fixed_node = 0
aluminum = Material(name='custom', E=69E9, G=26E9, rho=2700, v=0.33)
# aluminum = Material(name='custom', E=5E7, G=16.78E6, rho=1150, v=0.49)

wing = Beam(name=beam_name, num_nodes=num_beam_nodes, material=aluminum, cs='ellipse')
boundary_condition_1 = BoundaryCondition(beam=wing, node=fixed_node)


num_time_steps = 70
model = csdl.Model()

eel_mesh = np.zeros((num_beam_nodes, 3))
eel_mesh[:, 1] = np.linspace(-20, 20, num_beam_nodes)
model.create_input('eel_mesh', val=eel_mesh)  
model.create_input('eel_semi_major_axis', shape=(wing.num_elements), val=0.5)
model.create_input('eel_semi_minor_axis', shape=(wing.num_elements), val=0.05)
beam_F_val = np.zeros((num_time_steps, num_beam_nodes, 6)) 
beam_F_val[:5, :, 2] = 500
beam_F_val[:, fixed_node, 2] = 0 # zero out the middle node for boundary condition
# beam_F_val[:, 2, 2] = 0 # zero out the middle node for boundary condition
beam_F = model.create_input('eel'+'_force_torque', val=beam_F_val)
nodel_force = beam_F_val[0, :, :3]
model.create_input('eel'+'_forces',nodel_force)    

model.add(BeamModel(beams=[wing,],
                boundary_conditions=[boundary_condition_1],)) 
model.add(IntegratorModel(
    num_time_points=num_time_steps, beam_name=beam_name, num_beam_nodes=num_beam_nodes,
    eta_M=eta_M, eta_K=eta_K),
    name='IntegratorModel')

sim = python_csdl_backend.Simulator(model)
sim.run()

undeformed_eel_mesh = sim['eel_mesh']
deformation = sim['solved_u'] 
deformed_eel_mesh = undeformed_eel_mesh + deformation.reshape(num_time_steps, num_beam_nodes, 6)[:,:,:3]#[-1]

# eel_stress = sim['eel_stress']
# eel_semi_major_axis = sim['eel_semi_major_axis']
# eel_semi_minor_axis = sim['eel_semi_minor_axis']

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
# ax.view_init(elev=35, azim=-10)
# ax.set_box_aspect((1, 2, 1))


def update_graph(num):
    ax.clear()
    ax.view_init(elev=35, azim=-10)
    ax.set_box_aspect((1, 2, 1))
    
    # Plot the undeformed mesh (yellow)
    ax.scatter(undeformed_eel_mesh[:, 0], undeformed_eel_mesh[:, 1], undeformed_eel_mesh[:, 2], color='yellow', edgecolor='black', s=50)
    ax.plot(undeformed_eel_mesh[:, 0], undeformed_eel_mesh[:, 1], undeformed_eel_mesh[:, 2])
    
    # Plot the deformed mesh for the current time step (blue)
    ax.scatter(deformed_eel_mesh[num, :, 0], deformed_eel_mesh[num, :, 1], deformed_eel_mesh[num, :, 2], color='blue', s=50)
    ax.plot(deformed_eel_mesh[num, :, 0], deformed_eel_mesh[num, :, 1], deformed_eel_mesh[num, :, 2], color='blue')
    # add a title with the current time step
    ax.set_title(f'Current time is {num*0.5:.1f}')

    # fix the x, y, z range
    ax.set_xlim(-1, 1)
    ax.set_ylim(-20, 20)
    ax.set_zlim(-3, 3)

filenames = []
for i in range(num_time_steps):
    update_graph(i)
    plt.pause(0.1)
    plt.savefig(f'frame_{i}.png', dpi=200)
    filenames.append(f'frame_{i}.png')
plt.show()

# make a gif
import imageio.v2 as imageio
with imageio.get_writer('eel.gif', mode='I') as writer:
    for i in range(num_time_steps):
        image = imageio.imread(filenames[i])
        writer.append_data(image)
    
# Remove files
import os
for filename in filenames:
    os.remove(filename)


ax.axis('equal')
plt.axis('off')
plt.show()

# plt.plot(eel_stress)
plt.show()

np.set_printoptions(edgeitems=30, linewidth=100000,precision=10,suppress=True)
# print(sim['global_mass_matrix'])
# print(sim['global_stiffness_matrix'].shape)

#  [𝐶]=𝜂𝑀[𝑀]+𝜂𝐾[𝐾]


M = sim['global_mass_matrix']
K = sim['global_stiffness_matrix']
C = eta_M * M + eta_K * K

u = np.linalg.inv(K)@(sim['eel_force_torque'][0,:,:].reshape(-1))
u.reshape(-1,6)[:,:3]



deformation = deformed_eel_mesh - undeformed_eel_mesh
plt.plot(deformation[:,-1, 2], color='blue')
plt.show()
