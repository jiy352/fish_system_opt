

# RUN_MODEL_ode_system

# system evaluation block

# op _00pA_power_combination_eval
# LANG: global_mass_matrix --> _00pB
# SHAPES: (1, 18, 18) --> (1, 18, 18)
# full namespace: 
v834__00pB = (v825_global_mass_matrix)
v834__00pB = (v834__00pB*_00pA_coeff).reshape((1, 18, 18))

# op _00pC_power_combination_eval
# LANG: global_stiffness_matrix --> _00pD
# SHAPES: (1, 18, 18) --> (1, 18, 18)
# full namespace: 
v835__00pD = (v826_global_stiffness_matrix)
v835__00pD = (v835__00pD*_00pC_coeff).reshape((1, 18, 18))

# op _00pE_linear_combination_eval
# LANG: _00pB, _00pD --> _00pF
# SHAPES: (1, 18, 18), (1, 18, 18) --> (1, 18, 18)
# full namespace: 
v836__00pF = v834__00pB+v835__00pD

# op _00pI reshape_eval
# LANG: eel_force_torque --> _00pJ
# SHAPES: (1, 3, 6) --> (1, 18)
# full namespace: 
v838__00pJ = v820_eel_force_torque.reshape((1, 18))

# op _00pR einsum_eval
# LANG: global_stiffness_matrix, u --> _00pS
# SHAPES: (1, 18, 18), (1, 18) --> (1, 18)
# full namespace: 
v843__00pS = np.einsum('ijk,ik->ij' , v826_global_stiffness_matrix, v818_u)

# op _00pP_decompose_eval
# LANG: _00pJ --> _00pQ
# SHAPES: (1, 18) --> (1, 18)
# full namespace: 
v842__00pQ = ((v838__00pJ.flatten())[src_indices__00pQ__00pP]).reshape((1, 18))

# op _00pT_decompose_eval
# LANG: _00pS --> _00pU
# SHAPES: (1, 18) --> (1, 18)
# full namespace: 
v844__00pU = ((v843__00pS.flatten())[src_indices__00pU__00pT]).reshape((1, 18))

# op _00pX einsum_eval
# LANG: _00pF, u_dot --> _00pY
# SHAPES: (1, 18, 18), (1, 18) --> (1, 18)
# full namespace: 
v846__00pY = np.einsum('ijk,ik->ij' , v836__00pF, v819_u_dot)

# op _00pV_linear_combination_eval
# LANG: _00pQ, _00pU --> _00pW
# SHAPES: (1, 18), (1, 18) --> (1, 18)
# full namespace: 
v845__00pW = v842__00pQ+-1*v844__00pU

# op _00pZ_decompose_eval
# LANG: _00pY --> _00p_
# SHAPES: (1, 18) --> (1, 18)
# full namespace: 
v847__00p_ = ((v846__00pY.flatten())[src_indices__00p___00pZ]).reshape((1, 18))

# op _00q0_linear_combination_eval
# LANG: _00pW, _00p_ --> _00q1
# SHAPES: (1, 18), (1, 18) --> (1, 18)
# full namespace: 
v848__00q1 = v845__00pW+-1*v847__00p_

# op _00pL_decompose_eval
# LANG: global_mass_matrix --> _00pM
# SHAPES: (1, 18, 18) --> (1, 18, 18)
# full namespace: 
v840__00pM = ((v825_global_mass_matrix.flatten())[src_indices__00pM__00pL]).reshape((1, 18, 18))

# op _00q2 reshape_eval
# LANG: _00q1 --> _00q3
# SHAPES: (1, 18) --> (18,)
# full namespace: 
v849__00q3 = v848__00q1.reshape((18,))

# op _00pN reshape_eval
# LANG: _00pM --> _00pO
# SHAPES: (1, 18, 18) --> (18, 18)
# full namespace: 
v841__00pO = v840__00pM.reshape((18, 18))

# op _00q4 reshape_eval
# LANG: _00q3 --> _00q5
# SHAPES: (18,) --> (18, 1)
# full namespace: 
v850__00q5 = v849__00q3.reshape((18, 1))

# op _00q6_solve_linear_system_eval
# LANG: _00pO, _00q5 --> _00q7
# SHAPES: (18, 18), (18, 1) --> (18, 1)
# full namespace: 
v851__00q7 = _00q6v851__00q7_solver(v841__00pO, v850__00q5, False)

# op _00q8 reshape_eval
# LANG: _00q7 --> _00q9
# SHAPES: (18, 1) --> (18,)
# full namespace: 
v852__00q9 = v851__00q7.reshape((18,))

# op _00pe_decompose_eval
# LANG: eel_force_torque --> eel_forces, _00pr
# SHAPES: (1, 3, 6) --> (1, 3, 3), (1, 3, 6)
# full namespace: 
v821_eel_forces = ((v820_eel_force_torque.flatten())[src_indices_eel_forces__00pe]).reshape((1, 3, 3))
v829__00pr = ((v820_eel_force_torque.flatten())[src_indices__00pr__00pe]).reshape((1, 3, 6))

# op _00qa reshape_eval
# LANG: _00q9 --> _00qb
# SHAPES: (18,) --> (1, 18)
# full namespace: 
v853__00qb = v852__00q9.reshape((1, 18))

# op _00pG_power_combination_eval
# LANG: u_dot --> du_dt
# SHAPES: (1, 18) --> (1, 18)
# full namespace: 
v837_du_dt = (v819_u_dot)
v837_du_dt = v837_du_dt.reshape((1, 18))

# op _00pg_print_var_eval
# LANG: eel_force_torque --> eel_force_torque_print
# SHAPES: (1, 3, 6) --> (1, 3, 6)
# full namespace: 
print()
print('printing ', 'v820_eel_force_torque (eel_force_torque)')
print(v820_eel_force_torque)

# op _00pi_print_var_eval
# LANG: eel_forces --> eel_forces_print
# SHAPES: (1, 3, 3) --> (1, 3, 3)
# full namespace: 
print()
print('printing ', 'v821_eel_forces (eel_forces)')
print(v821_eel_forces)

# op _00qc_indexed_passthrough_eval
# LANG: _00qb --> dudot_dt
# SHAPES: (1, 18) --> (1, 18)
# full namespace: 
v839_dudot_dt__temp[i_v853__00qb__00qc_indexed_passthrough_eval] = v853__00qb.flatten()
v839_dudot_dt = v839_dudot_dt__temp.copy()