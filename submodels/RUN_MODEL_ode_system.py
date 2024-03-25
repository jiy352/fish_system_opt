

# RUN_MODEL_ode_system

# system evaluation block

# op _01S2_power_combination_eval
# LANG: global_mass_matrix --> _01S3
# SHAPES: (1, 66, 66) --> (1, 66, 66)
# full namespace: 
v3799__01S3 = (v3790_global_mass_matrix)
v3799__01S3 = (v3799__01S3*_01S2_coeff).reshape((1, 66, 66))

# op _01S4_power_combination_eval
# LANG: global_stiffness_matrix --> _01S5
# SHAPES: (1, 66, 66) --> (1, 66, 66)
# full namespace: 
v3800__01S5 = (v3791_global_stiffness_matrix)
v3800__01S5 = (v3800__01S5*_01S4_coeff).reshape((1, 66, 66))

# op _01S6_linear_combination_eval
# LANG: _01S3, _01S5 --> _01S7
# SHAPES: (1, 66, 66), (1, 66, 66) --> (1, 66, 66)
# full namespace: 
v3801__01S7 = v3799__01S3+v3800__01S5

# op _01Sa reshape_eval
# LANG: eel_force_torque --> _01Sb
# SHAPES: (1, 11, 6) --> (1, 66)
# full namespace: 
v3803__01Sb = v3787_eel_force_torque.reshape((1, 66))

# op _01Sj einsum_eval
# LANG: global_stiffness_matrix, u --> _01Sk
# SHAPES: (1, 66, 66), (1, 66) --> (1, 66)
# full namespace: 
v3808__01Sk = np.einsum('ijk,ik->ij' , v3791_global_stiffness_matrix, v3785_u)

# op _01Sh_decompose_eval
# LANG: _01Sb --> _01Si
# SHAPES: (1, 66) --> (1, 66)
# full namespace: 
v3807__01Si = ((v3803__01Sb.flatten())[src_indices__01Si__01Sh]).reshape((1, 66))

# op _01Sl_decompose_eval
# LANG: _01Sk --> _01Sm
# SHAPES: (1, 66) --> (1, 66)
# full namespace: 
v3809__01Sm = ((v3808__01Sk.flatten())[src_indices__01Sm__01Sl]).reshape((1, 66))

# op _01Sp einsum_eval
# LANG: _01S7, u_dot --> _01Sq
# SHAPES: (1, 66, 66), (1, 66) --> (1, 66)
# full namespace: 
v3811__01Sq = np.einsum('ijk,ik->ij' , v3801__01S7, v3786_u_dot)

# op _01Sn_linear_combination_eval
# LANG: _01Si, _01Sm --> _01So
# SHAPES: (1, 66), (1, 66) --> (1, 66)
# full namespace: 
v3810__01So = v3807__01Si+-1*v3809__01Sm

# op _01Sr_decompose_eval
# LANG: _01Sq --> _01Ss
# SHAPES: (1, 66) --> (1, 66)
# full namespace: 
v3812__01Ss = ((v3811__01Sq.flatten())[src_indices__01Ss__01Sr]).reshape((1, 66))

# op _01St_linear_combination_eval
# LANG: _01So, _01Ss --> _01Su
# SHAPES: (1, 66), (1, 66) --> (1, 66)
# full namespace: 
v3813__01Su = v3810__01So+-1*v3812__01Ss

# op _01Sd_decompose_eval
# LANG: global_mass_matrix --> _01Se
# SHAPES: (1, 66, 66) --> (1, 66, 66)
# full namespace: 
v3805__01Se = ((v3790_global_mass_matrix.flatten())[src_indices__01Se__01Sd]).reshape((1, 66, 66))

# op _01Sv reshape_eval
# LANG: _01Su --> _01Sw
# SHAPES: (1, 66) --> (66,)
# full namespace: 
v3814__01Sw = v3813__01Su.reshape((66,))

# op _01Sf reshape_eval
# LANG: _01Se --> _01Sg
# SHAPES: (1, 66, 66) --> (66, 66)
# full namespace: 
v3806__01Sg = v3805__01Se.reshape((66, 66))

# op _01Sx reshape_eval
# LANG: _01Sw --> _01Sy
# SHAPES: (66,) --> (66, 1)
# full namespace: 
v3815__01Sy = v3814__01Sw.reshape((66, 1))

# op _01Sz_solve_linear_system_eval
# LANG: _01Sg, _01Sy --> _01SA
# SHAPES: (66, 66), (66, 1) --> (66, 1)
# full namespace: 
v3816__01SA = _01Szv3816__01SA_solver(v3806__01Sg, v3815__01Sy, False)

# op _01SB reshape_eval
# LANG: _01SA --> _01SC
# SHAPES: (66, 1) --> (66,)
# full namespace: 
v3817__01SC = v3816__01SA.reshape((66,))

# op _01SD reshape_eval
# LANG: _01SC --> _01SE
# SHAPES: (66,) --> (1, 66)
# full namespace: 
v3818__01SE = v3817__01SC.reshape((1, 66))

# op _01RL_decompose_eval
# LANG: eel_force_torque --> eel_forces, _01RU
# SHAPES: (1, 11, 6) --> (1, 11, 3), (1, 11, 6)
# full namespace: 
v3788_eel_forces = ((v3787_eel_force_torque.flatten())[src_indices_eel_forces__01RL]).reshape((1, 11, 3))
v3794__01RU = ((v3787_eel_force_torque.flatten())[src_indices__01RU__01RL]).reshape((1, 11, 6))

# op _01S8_power_combination_eval
# LANG: u_dot --> du_dt
# SHAPES: (1, 66) --> (1, 66)
# full namespace: 
v3802_du_dt = (v3786_u_dot)
v3802_du_dt = v3802_du_dt.reshape((1, 66))

# op _01SF_indexed_passthrough_eval
# LANG: _01SE --> dudot_dt
# SHAPES: (1, 66) --> (1, 66)
# full namespace: 
v3804_dudot_dt__temp[i_v3818__01SE__01SF_indexed_passthrough_eval] = v3818__01SE.flatten()
v3804_dudot_dt = v3804_dudot_dt__temp.copy()