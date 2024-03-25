

# REV_: du_dt,dudot_dt,-->v1559_u,v1560_u_dot,

# REV_: du_dt,dudot_dt,-->v1559_u,v1560_u_dot,

# op _00N1_indexed_passthrough_eval
# LANG: _00N0 --> dudot_dt
# SHAPES: (1, 30) --> (1, 30)
# full namespace: 

# _00N1_indexed_passthrough_eval_pv1578_dudot_dt_pv1593__00N0
path_from_v1578_dudot_dt_to_v1593__00N0 = STD_MULT(r_seed_v1578_dudot_dt,pv1578_dudot_dt_pv1593__00N0)

# op _00Mt_power_combination_eval
# LANG: u_dot --> du_dt
# SHAPES: (1, 30) --> (1, 30)
# full namespace: 

# _00Mt_power_combination_eval_pv1576_du_dt_pv1560_u_dot
temp_power = _00Mt_coeff_temp*1
pv1576_du_dt_pv1560_u_dot = temp_power.flatten()
path_from_v1576_du_dt_to_v1560_u_dot = DIAG_MULT(r_seed_v1576_du_dt,pv1576_du_dt_pv1560_u_dot)
del pv1576_du_dt_pv1560_u_dot

# op _00M_ reshape_eval
# LANG: _00MZ --> _00N0
# SHAPES: (30,) --> (1, 30)
# full namespace: 

# _00M_ reshape_eval_pv1593__00N0_pv1592__00MZ
path_from_v1578_dudot_dt_to_v1592__00MZ = DIAG_MULT(path_from_v1578_dudot_dt_to_v1593__00N0,pv1593__00N0_pv1592__00MZ)
del path_from_v1578_dudot_dt_to_v1593__00N0

# op _00MY reshape_eval
# LANG: _00MX --> _00MZ
# SHAPES: (30, 1) --> (30,)
# full namespace: 

# _00MY reshape_eval_pv1592__00MZ_pv1591__00MX
path_from_v1578_dudot_dt_to_v1591__00MX = DIAG_MULT(path_from_v1578_dudot_dt_to_v1592__00MZ,pv1592__00MZ_pv1591__00MX)
del path_from_v1578_dudot_dt_to_v1592__00MZ

# _00MW_solve_linear_system_eval_v1578_dudot_dt__00MW
_00MWv1591__00MX_path_tranposed = _00MWv1591__00MX_solve_transposed_system(v1589__00MT,path_from_v1578_dudot_dt_to_v1591__00MX)
_00MW_v1578_dudot_dt_v1589__00MT = _00MWv1591__00MX_accumulate_A(v1591__00MX,_00MWv1591__00MX_path_tranposed)
_00MW_v1578_dudot_dt_v1590__00MV = _00MWv1591__00MX_path_tranposed.T
path_from_v1578_dudot_dt_to_v1590__00MV = _00MW_v1578_dudot_dt_v1590__00MV
del path_from_v1578_dudot_dt_to_v1591__00MX

# op _00MU reshape_eval
# LANG: _00MR --> _00MV
# SHAPES: (30,) --> (30, 1)
# full namespace: 

# _00MU reshape_eval_pv1590__00MV_pv1588__00MR
path_from_v1578_dudot_dt_to_v1588__00MR = DIAG_MULT(path_from_v1578_dudot_dt_to_v1590__00MV,pv1590__00MV_pv1588__00MR)
del path_from_v1578_dudot_dt_to_v1590__00MV

# op _00MQ reshape_eval
# LANG: _00MP --> _00MR
# SHAPES: (1, 30) --> (30,)
# full namespace: 

# _00MQ reshape_eval_pv1588__00MR_pv1587__00MP
path_from_v1578_dudot_dt_to_v1587__00MP = DIAG_MULT(path_from_v1578_dudot_dt_to_v1588__00MR,pv1588__00MR_pv1587__00MP)
del path_from_v1578_dudot_dt_to_v1588__00MR

# op _00MO_linear_combination_eval
# LANG: _00MJ, _00MN --> _00MP
# SHAPES: (1, 30), (1, 30) --> (1, 30)
# full namespace: 

# _00MO_linear_combination_eval_pv1587__00MP_pv1586__00MN
path_from_v1578_dudot_dt_to_v1584__00MJ = DIAG_MULT(path_from_v1578_dudot_dt_to_v1587__00MP,pv1587__00MP_pv1584__00MJ)
path_from_v1578_dudot_dt_to_v1586__00MN = DIAG_MULT(path_from_v1578_dudot_dt_to_v1587__00MP,pv1587__00MP_pv1586__00MN)
del path_from_v1578_dudot_dt_to_v1587__00MP

# op _00MM_decompose_eval
# LANG: _00ML --> _00MN
# SHAPES: (1, 30) --> (1, 30)
# full namespace: 

# _00MM_decompose_eval_pv1586__00MN_pv1585__00ML
path_from_v1578_dudot_dt_to_v1585__00ML = STD_MULT(path_from_v1578_dudot_dt_to_v1586__00MN,pv1586__00MN_pv1585__00ML)
del path_from_v1578_dudot_dt_to_v1586__00MN

# op _00MI_linear_combination_eval
# LANG: _00MD, _00MH --> _00MJ
# SHAPES: (1, 30), (1, 30) --> (1, 30)
# full namespace: 

# _00MI_linear_combination_eval_pv1584__00MJ_pv1583__00MH
path_from_v1578_dudot_dt_to_v1583__00MH = DIAG_MULT(path_from_v1578_dudot_dt_to_v1584__00MJ,pv1584__00MJ_pv1583__00MH)
del path_from_v1578_dudot_dt_to_v1584__00MJ

# op _00MK einsum_eval
# LANG: _00Ms, u_dot --> _00ML
# SHAPES: (1, 30, 30), (1, 30) --> (1, 30)
# full namespace: 

# _00MK einsum_eval_pv1585__00ML_pv1560_u_dot
_00MK_temp_einsum = _00MK_partial_func(v1575__00Ms, v1560_u_dot)
pv1585__00ML_pv1575__00Ms = _00MK_temp_einsum[0]
pv1585__00ML_pv1560_u_dot = _00MK_temp_einsum[1]
path_from_v1578_dudot_dt_to_v1560_u_dot = STD_MULT(path_from_v1578_dudot_dt_to_v1585__00ML,pv1585__00ML_pv1560_u_dot)
del pv1585__00ML_pv1575__00Ms
del pv1585__00ML_pv1560_u_dot
del path_from_v1578_dudot_dt_to_v1585__00ML

# op _00MG_decompose_eval
# LANG: _00MF --> _00MH
# SHAPES: (1, 30) --> (1, 30)
# full namespace: 

# _00MG_decompose_eval_pv1583__00MH_pv1582__00MF
path_from_v1578_dudot_dt_to_v1582__00MF = STD_MULT(path_from_v1578_dudot_dt_to_v1583__00MH,pv1583__00MH_pv1582__00MF)
del path_from_v1578_dudot_dt_to_v1583__00MH

# op _00ME einsum_eval
# LANG: global_stiffness_matrix, u --> _00MF
# SHAPES: (1, 30, 30), (1, 30) --> (1, 30)
# full namespace: 

# _00ME einsum_eval_pv1582__00MF_pv1559_u
_00ME_temp_einsum = _00ME_partial_func(v1565_global_stiffness_matrix, v1559_u)
pv1582__00MF_pv1565_global_stiffness_matrix = _00ME_temp_einsum[0]
pv1582__00MF_pv1559_u = _00ME_temp_einsum[1]
path_from_v1578_dudot_dt_to_v1559_u = STD_MULT(path_from_v1578_dudot_dt_to_v1582__00MF,pv1582__00MF_pv1559_u)
del pv1582__00MF_pv1565_global_stiffness_matrix
del path_from_v1578_dudot_dt_to_v1582__00MF
del pv1582__00MF_pv1559_u
# dv1576_du_dt_dv1559_u = zero
dv1576_du_dt_dv1559_u = np.zeros((r_seed_v1576_du_dt.shape[0],30))
dv1576_du_dt_dv1560_u_dot = path_from_v1576_du_dt_to_v1560_u_dot.copy()
dv1578_dudot_dt_dv1559_u = path_from_v1578_dudot_dt_to_v1559_u.copy()
dv1578_dudot_dt_dv1560_u_dot = path_from_v1578_dudot_dt_to_v1560_u_dot.copy()