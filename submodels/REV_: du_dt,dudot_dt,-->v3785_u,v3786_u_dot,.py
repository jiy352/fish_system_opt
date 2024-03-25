

# REV_: du_dt,dudot_dt,-->v3785_u,v3786_u_dot,

# REV_: du_dt,dudot_dt,-->v3785_u,v3786_u_dot,

# op _01SF_indexed_passthrough_eval
# LANG: _01SE --> dudot_dt
# SHAPES: (1, 66) --> (1, 66)
# full namespace: 

# _01SF_indexed_passthrough_eval_pv3804_dudot_dt_pv3818__01SE
path_from_v3804_dudot_dt_to_v3818__01SE = STD_MULT(r_seed_v3804_dudot_dt,pv3804_dudot_dt_pv3818__01SE)

# op _01S8_power_combination_eval
# LANG: u_dot --> du_dt
# SHAPES: (1, 66) --> (1, 66)
# full namespace: 

# _01S8_power_combination_eval_pv3802_du_dt_pv3786_u_dot
temp_power = _01S8_coeff_temp*1
pv3802_du_dt_pv3786_u_dot = temp_power.flatten()
path_from_v3802_du_dt_to_v3786_u_dot = DIAG_MULT(r_seed_v3802_du_dt,pv3802_du_dt_pv3786_u_dot)
del pv3802_du_dt_pv3786_u_dot

# op _01SD reshape_eval
# LANG: _01SC --> _01SE
# SHAPES: (66,) --> (1, 66)
# full namespace: 

# _01SD reshape_eval_pv3818__01SE_pv3817__01SC
path_from_v3804_dudot_dt_to_v3817__01SC = DIAG_MULT(path_from_v3804_dudot_dt_to_v3818__01SE,pv3818__01SE_pv3817__01SC)
del path_from_v3804_dudot_dt_to_v3818__01SE

# op _01SB reshape_eval
# LANG: _01SA --> _01SC
# SHAPES: (66, 1) --> (66,)
# full namespace: 

# _01SB reshape_eval_pv3817__01SC_pv3816__01SA
path_from_v3804_dudot_dt_to_v3816__01SA = DIAG_MULT(path_from_v3804_dudot_dt_to_v3817__01SC,pv3817__01SC_pv3816__01SA)
del path_from_v3804_dudot_dt_to_v3817__01SC

# _01Sz_solve_linear_system_eval_v3804_dudot_dt__01Sz
_01Szv3816__01SA_path_tranposed = _01Szv3816__01SA_solve_transposed_system(v3806__01Sg,path_from_v3804_dudot_dt_to_v3816__01SA)
_01Sz_v3804_dudot_dt_v3806__01Sg = _01Szv3816__01SA_accumulate_A(v3816__01SA,_01Szv3816__01SA_path_tranposed)
_01Sz_v3804_dudot_dt_v3815__01Sy = _01Szv3816__01SA_path_tranposed.T
path_from_v3804_dudot_dt_to_v3815__01Sy = _01Sz_v3804_dudot_dt_v3815__01Sy
del path_from_v3804_dudot_dt_to_v3816__01SA

# op _01Sx reshape_eval
# LANG: _01Sw --> _01Sy
# SHAPES: (66,) --> (66, 1)
# full namespace: 

# _01Sx reshape_eval_pv3815__01Sy_pv3814__01Sw
path_from_v3804_dudot_dt_to_v3814__01Sw = DIAG_MULT(path_from_v3804_dudot_dt_to_v3815__01Sy,pv3815__01Sy_pv3814__01Sw)
del path_from_v3804_dudot_dt_to_v3815__01Sy

# op _01Sv reshape_eval
# LANG: _01Su --> _01Sw
# SHAPES: (1, 66) --> (66,)
# full namespace: 

# _01Sv reshape_eval_pv3814__01Sw_pv3813__01Su
path_from_v3804_dudot_dt_to_v3813__01Su = DIAG_MULT(path_from_v3804_dudot_dt_to_v3814__01Sw,pv3814__01Sw_pv3813__01Su)
del path_from_v3804_dudot_dt_to_v3814__01Sw

# op _01St_linear_combination_eval
# LANG: _01So, _01Ss --> _01Su
# SHAPES: (1, 66), (1, 66) --> (1, 66)
# full namespace: 

# _01St_linear_combination_eval_pv3813__01Su_pv3812__01Ss
path_from_v3804_dudot_dt_to_v3810__01So = DIAG_MULT(path_from_v3804_dudot_dt_to_v3813__01Su,pv3813__01Su_pv3810__01So)
path_from_v3804_dudot_dt_to_v3812__01Ss = DIAG_MULT(path_from_v3804_dudot_dt_to_v3813__01Su,pv3813__01Su_pv3812__01Ss)
del path_from_v3804_dudot_dt_to_v3813__01Su

# op _01Sr_decompose_eval
# LANG: _01Sq --> _01Ss
# SHAPES: (1, 66) --> (1, 66)
# full namespace: 

# _01Sr_decompose_eval_pv3812__01Ss_pv3811__01Sq
path_from_v3804_dudot_dt_to_v3811__01Sq = STD_MULT(path_from_v3804_dudot_dt_to_v3812__01Ss,pv3812__01Ss_pv3811__01Sq)
del path_from_v3804_dudot_dt_to_v3812__01Ss

# op _01Sn_linear_combination_eval
# LANG: _01Si, _01Sm --> _01So
# SHAPES: (1, 66), (1, 66) --> (1, 66)
# full namespace: 

# _01Sn_linear_combination_eval_pv3810__01So_pv3809__01Sm
path_from_v3804_dudot_dt_to_v3809__01Sm = DIAG_MULT(path_from_v3804_dudot_dt_to_v3810__01So,pv3810__01So_pv3809__01Sm)
del path_from_v3804_dudot_dt_to_v3810__01So

# op _01Sp einsum_eval
# LANG: _01S7, u_dot --> _01Sq
# SHAPES: (1, 66, 66), (1, 66) --> (1, 66)
# full namespace: 

# _01Sp einsum_eval_pv3811__01Sq_pv3786_u_dot
_01Sp_temp_einsum = _01Sp_partial_func(v3801__01S7, v3786_u_dot)
pv3811__01Sq_pv3801__01S7 = _01Sp_temp_einsum[0]
pv3811__01Sq_pv3786_u_dot = _01Sp_temp_einsum[1]
path_from_v3804_dudot_dt_to_v3786_u_dot = STD_MULT(path_from_v3804_dudot_dt_to_v3811__01Sq,pv3811__01Sq_pv3786_u_dot)
del pv3811__01Sq_pv3786_u_dot
del path_from_v3804_dudot_dt_to_v3811__01Sq
del pv3811__01Sq_pv3801__01S7

# op _01Sl_decompose_eval
# LANG: _01Sk --> _01Sm
# SHAPES: (1, 66) --> (1, 66)
# full namespace: 

# _01Sl_decompose_eval_pv3809__01Sm_pv3808__01Sk
path_from_v3804_dudot_dt_to_v3808__01Sk = STD_MULT(path_from_v3804_dudot_dt_to_v3809__01Sm,pv3809__01Sm_pv3808__01Sk)
del path_from_v3804_dudot_dt_to_v3809__01Sm

# op _01Sj einsum_eval
# LANG: global_stiffness_matrix, u --> _01Sk
# SHAPES: (1, 66, 66), (1, 66) --> (1, 66)
# full namespace: 

# _01Sj einsum_eval_pv3808__01Sk_pv3785_u
_01Sj_temp_einsum = _01Sj_partial_func(v3791_global_stiffness_matrix, v3785_u)
pv3808__01Sk_pv3791_global_stiffness_matrix = _01Sj_temp_einsum[0]
pv3808__01Sk_pv3785_u = _01Sj_temp_einsum[1]
path_from_v3804_dudot_dt_to_v3785_u = STD_MULT(path_from_v3804_dudot_dt_to_v3808__01Sk,pv3808__01Sk_pv3785_u)
del pv3808__01Sk_pv3791_global_stiffness_matrix
del path_from_v3804_dudot_dt_to_v3808__01Sk
del pv3808__01Sk_pv3785_u
# dv3802_du_dt_dv3785_u = zero
dv3802_du_dt_dv3785_u = np.zeros((r_seed_v3802_du_dt.shape[0],66))
dv3802_du_dt_dv3786_u_dot = path_from_v3802_du_dt_to_v3786_u_dot.copy()
dv3804_dudot_dt_dv3785_u = path_from_v3804_dudot_dt_to_v3785_u.copy()
dv3804_dudot_dt_dv3786_u_dot = path_from_v3804_dudot_dt_to_v3786_u_dot.copy()