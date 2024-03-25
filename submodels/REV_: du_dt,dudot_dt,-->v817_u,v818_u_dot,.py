

# REV_: du_dt,dudot_dt,-->v817_u,v818_u_dot,

# REV_: du_dt,dudot_dt,-->v817_u,v818_u_dot,

# op _00q6_indexed_passthrough_eval
# LANG: _00q5 --> dudot_dt
# SHAPES: (1, 18) --> (1, 18)
# full namespace: 

# _00q6_indexed_passthrough_eval_pv836_dudot_dt_pv850__00q5
path_from_v836_dudot_dt_to_v850__00q5 = STD_MULT(r_seed_v836_dudot_dt,pv836_dudot_dt_pv850__00q5)

# op _00pA_power_combination_eval
# LANG: u_dot --> du_dt
# SHAPES: (1, 18) --> (1, 18)
# full namespace: 

# _00pA_power_combination_eval_pv834_du_dt_pv818_u_dot
temp_power = _00pA_coeff_temp*1
pv834_du_dt_pv818_u_dot = temp_power.flatten()
path_from_v834_du_dt_to_v818_u_dot = DIAG_MULT(r_seed_v834_du_dt,pv834_du_dt_pv818_u_dot)
del pv834_du_dt_pv818_u_dot

# op _00q4 reshape_eval
# LANG: _00q3 --> _00q5
# SHAPES: (18,) --> (1, 18)
# full namespace: 

# _00q4 reshape_eval_pv850__00q5_pv849__00q3
path_from_v836_dudot_dt_to_v849__00q3 = DIAG_MULT(path_from_v836_dudot_dt_to_v850__00q5,pv850__00q5_pv849__00q3)
del path_from_v836_dudot_dt_to_v850__00q5

# op _00q2 reshape_eval
# LANG: _00q1 --> _00q3
# SHAPES: (18, 1) --> (18,)
# full namespace: 

# _00q2 reshape_eval_pv849__00q3_pv848__00q1
path_from_v836_dudot_dt_to_v848__00q1 = DIAG_MULT(path_from_v836_dudot_dt_to_v849__00q3,pv849__00q3_pv848__00q1)
del path_from_v836_dudot_dt_to_v849__00q3

# _00q0_solve_linear_system_eval_v836_dudot_dt__00q0
_00q0v848__00q1_path_tranposed = _00q0v848__00q1_solve_transposed_system(v838__00pI,path_from_v836_dudot_dt_to_v848__00q1)
_00q0_v836_dudot_dt_v838__00pI = _00q0v848__00q1_accumulate_A(v848__00q1,_00q0v848__00q1_path_tranposed)
_00q0_v836_dudot_dt_v847__00p_ = _00q0v848__00q1_path_tranposed.T
path_from_v836_dudot_dt_to_v847__00p_ = _00q0_v836_dudot_dt_v847__00p_
del path_from_v836_dudot_dt_to_v848__00q1

# op _00pZ reshape_eval
# LANG: _00pY --> _00p_
# SHAPES: (18,) --> (18, 1)
# full namespace: 

# _00pZ reshape_eval_pv847__00p__pv846__00pY
path_from_v836_dudot_dt_to_v846__00pY = DIAG_MULT(path_from_v836_dudot_dt_to_v847__00p_,pv847__00p__pv846__00pY)
del path_from_v836_dudot_dt_to_v847__00p_

# op _00pX reshape_eval
# LANG: _00pW --> _00pY
# SHAPES: (1, 18) --> (18,)
# full namespace: 

# _00pX reshape_eval_pv846__00pY_pv845__00pW
path_from_v836_dudot_dt_to_v845__00pW = DIAG_MULT(path_from_v836_dudot_dt_to_v846__00pY,pv846__00pY_pv845__00pW)
del path_from_v836_dudot_dt_to_v846__00pY

# op _00pV_linear_combination_eval
# LANG: _00pQ, _00pU --> _00pW
# SHAPES: (1, 18), (1, 18) --> (1, 18)
# full namespace: 

# _00pV_linear_combination_eval_pv845__00pW_pv844__00pU
path_from_v836_dudot_dt_to_v842__00pQ = DIAG_MULT(path_from_v836_dudot_dt_to_v845__00pW,pv845__00pW_pv842__00pQ)
path_from_v836_dudot_dt_to_v844__00pU = DIAG_MULT(path_from_v836_dudot_dt_to_v845__00pW,pv845__00pW_pv844__00pU)
del path_from_v836_dudot_dt_to_v845__00pW

# op _00pT_decompose_eval
# LANG: _00pS --> _00pU
# SHAPES: (1, 18) --> (1, 18)
# full namespace: 

# _00pT_decompose_eval_pv844__00pU_pv843__00pS
path_from_v836_dudot_dt_to_v843__00pS = STD_MULT(path_from_v836_dudot_dt_to_v844__00pU,pv844__00pU_pv843__00pS)
del path_from_v836_dudot_dt_to_v844__00pU

# op _00pP_linear_combination_eval
# LANG: _00pK, _00pO --> _00pQ
# SHAPES: (1, 18), (1, 18) --> (1, 18)
# full namespace: 

# _00pP_linear_combination_eval_pv842__00pQ_pv841__00pO
path_from_v836_dudot_dt_to_v841__00pO = DIAG_MULT(path_from_v836_dudot_dt_to_v842__00pQ,pv842__00pQ_pv841__00pO)
del path_from_v836_dudot_dt_to_v842__00pQ

# op _00pR einsum_eval
# LANG: _00pz, u_dot --> _00pS
# SHAPES: (1, 18, 18), (1, 18) --> (1, 18)
# full namespace: 

# _00pR einsum_eval_pv843__00pS_pv818_u_dot
_00pR_temp_einsum = _00pR_partial_func(v833__00pz, v818_u_dot)
pv843__00pS_pv833__00pz = _00pR_temp_einsum[0]
pv843__00pS_pv818_u_dot = _00pR_temp_einsum[1]
path_from_v836_dudot_dt_to_v818_u_dot = STD_MULT(path_from_v836_dudot_dt_to_v843__00pS,pv843__00pS_pv818_u_dot)
del pv843__00pS_pv818_u_dot
del pv843__00pS_pv833__00pz
del path_from_v836_dudot_dt_to_v843__00pS

# op _00pN_decompose_eval
# LANG: _00pM --> _00pO
# SHAPES: (1, 18) --> (1, 18)
# full namespace: 

# _00pN_decompose_eval_pv841__00pO_pv840__00pM
path_from_v836_dudot_dt_to_v840__00pM = STD_MULT(path_from_v836_dudot_dt_to_v841__00pO,pv841__00pO_pv840__00pM)
del path_from_v836_dudot_dt_to_v841__00pO

# op _00pL einsum_eval
# LANG: global_stiffness_matrix, u --> _00pM
# SHAPES: (1, 18, 18), (1, 18) --> (1, 18)
# full namespace: 

# _00pL einsum_eval_pv840__00pM_pv817_u
_00pL_temp_einsum = _00pL_partial_func(v823_global_stiffness_matrix, v817_u)
pv840__00pM_pv823_global_stiffness_matrix = _00pL_temp_einsum[0]
pv840__00pM_pv817_u = _00pL_temp_einsum[1]
path_from_v836_dudot_dt_to_v817_u = STD_MULT(path_from_v836_dudot_dt_to_v840__00pM,pv840__00pM_pv817_u)
del pv840__00pM_pv817_u
del pv840__00pM_pv823_global_stiffness_matrix
del path_from_v836_dudot_dt_to_v840__00pM
# dv834_du_dt_dv817_u = zero
dv834_du_dt_dv817_u = np.zeros((r_seed_v834_du_dt.shape[0],18))
dv834_du_dt_dv818_u_dot = path_from_v834_du_dt_to_v818_u_dot.copy()
dv836_dudot_dt_dv817_u = path_from_v836_dudot_dt_to_v817_u.copy()
dv836_dudot_dt_dv818_u_dot = path_from_v836_dudot_dt_to_v818_u_dot.copy()