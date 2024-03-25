

# REV_: du_dt,dudot_dt,-->v1559_u,v1560_u_dot,v1561_eel_force_torque,v1563_eel_mesh,v1564_global_mass_matrix,v1565_global_stiffness_matrix,

# REV_: du_dt,dudot_dt,-->v1559_u,v1560_u_dot,v1561_eel_force_torque,v1563_eel_mesh,v1564_global_mass_matrix,v1565_global_stiffness_matrix,

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
path_from_v1578_dudot_dt_to_v1589__00MT = _00MW_v1578_dudot_dt_v1589__00MT
path_from_v1578_dudot_dt_to_v1590__00MV = _00MW_v1578_dudot_dt_v1590__00MV
del path_from_v1578_dudot_dt_to_v1591__00MX

# op _00MU reshape_eval
# LANG: _00MR --> _00MV
# SHAPES: (30,) --> (30, 1)
# full namespace: 

# _00MU reshape_eval_pv1590__00MV_pv1588__00MR
path_from_v1578_dudot_dt_to_v1588__00MR = DIAG_MULT(path_from_v1578_dudot_dt_to_v1590__00MV,pv1590__00MV_pv1588__00MR)
del path_from_v1578_dudot_dt_to_v1590__00MV

# op _00MS_power_combination_eval
# LANG: _00MB --> _00MT
# SHAPES: (30, 30) --> (30, 30)
# full namespace: 

# _00MS_power_combination_eval_pv1589__00MT_pv1580__00MB
temp_power = _00MS_coeff_temp*1
pv1589__00MT_pv1580__00MB = temp_power.flatten()
path_from_v1578_dudot_dt_to_v1580__00MB = DIAG_MULT(path_from_v1578_dudot_dt_to_v1589__00MT,pv1589__00MT_pv1580__00MB)
del path_from_v1578_dudot_dt_to_v1589__00MT
del pv1589__00MT_pv1580__00MB

# op _00MQ reshape_eval
# LANG: _00MP --> _00MR
# SHAPES: (1, 30) --> (30,)
# full namespace: 

# _00MQ reshape_eval_pv1588__00MR_pv1587__00MP
path_from_v1578_dudot_dt_to_v1587__00MP = DIAG_MULT(path_from_v1578_dudot_dt_to_v1588__00MR,pv1588__00MR_pv1587__00MP)
del path_from_v1578_dudot_dt_to_v1588__00MR

# op _00MA reshape_eval
# LANG: _00Mz --> _00MB
# SHAPES: (1, 30, 30) --> (30, 30)
# full namespace: 

# _00MA reshape_eval_pv1580__00MB_pv1579__00Mz
path_from_v1578_dudot_dt_to_v1579__00Mz = DIAG_MULT(path_from_v1578_dudot_dt_to_v1580__00MB,pv1580__00MB_pv1579__00Mz)
del path_from_v1578_dudot_dt_to_v1580__00MB

# op _00My_decompose_eval
# LANG: global_mass_matrix --> _00Mz
# SHAPES: (1, 30, 30) --> (1, 30, 30)
# full namespace: 

# _00My_decompose_eval_pv1579__00Mz_pv1564_global_mass_matrix
path_from_v1578_dudot_dt_to_v1564_global_mass_matrix = STD_MULT(path_from_v1578_dudot_dt_to_v1579__00Mz,pv1579__00Mz_pv1564_global_mass_matrix)
del path_from_v1578_dudot_dt_to_v1579__00Mz

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
path_from_v1578_dudot_dt_to_v1581__00MD = DIAG_MULT(path_from_v1578_dudot_dt_to_v1584__00MJ,pv1584__00MJ_pv1581__00MD)
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
path_from_v1578_dudot_dt_to_v1575__00Ms = STD_MULT(path_from_v1578_dudot_dt_to_v1585__00ML,pv1585__00ML_pv1575__00Ms)
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

# op _00MC_decompose_eval
# LANG: _00Mw --> _00MD
# SHAPES: (1, 30) --> (1, 30)
# full namespace: 

# _00MC_decompose_eval_pv1581__00MD_pv1577__00Mw
path_from_v1578_dudot_dt_to_v1577__00Mw = STD_MULT(path_from_v1578_dudot_dt_to_v1581__00MD,pv1581__00MD_pv1577__00Mw)
del path_from_v1578_dudot_dt_to_v1581__00MD

# op _00Mv reshape_eval
# LANG: eel_force_torque --> _00Mw
# SHAPES: (1, 5, 6) --> (1, 30)
# full namespace: 

# _00Mv reshape_eval_pv1577__00Mw_pv1561_eel_force_torque
path_from_v1578_dudot_dt_to_v1561_eel_force_torque = DIAG_MULT(path_from_v1578_dudot_dt_to_v1577__00Mw,pv1577__00Mw_pv1561_eel_force_torque)
del path_from_v1578_dudot_dt_to_v1577__00Mw

# op _00Mr_linear_combination_eval
# LANG: _00Mo, _00Mq --> _00Ms
# SHAPES: (1, 30, 30), (1, 30, 30) --> (1, 30, 30)
# full namespace: 

# _00Mr_linear_combination_eval_pv1575__00Ms_pv1574__00Mq
path_from_v1578_dudot_dt_to_v1573__00Mo = DIAG_MULT(path_from_v1578_dudot_dt_to_v1575__00Ms,pv1575__00Ms_pv1573__00Mo)
path_from_v1578_dudot_dt_to_v1574__00Mq = DIAG_MULT(path_from_v1578_dudot_dt_to_v1575__00Ms,pv1575__00Ms_pv1574__00Mq)
del path_from_v1578_dudot_dt_to_v1575__00Ms

# op _00ME einsum_eval
# LANG: global_stiffness_matrix, u --> _00MF
# SHAPES: (1, 30, 30), (1, 30) --> (1, 30)
# full namespace: 

# _00ME einsum_eval_pv1582__00MF_pv1559_u
_00ME_temp_einsum = _00ME_partial_func(v1565_global_stiffness_matrix, v1559_u)
pv1582__00MF_pv1565_global_stiffness_matrix = _00ME_temp_einsum[0]
pv1582__00MF_pv1559_u = _00ME_temp_einsum[1]
path_from_v1578_dudot_dt_to_v1565_global_stiffness_matrix = STD_MULT(path_from_v1578_dudot_dt_to_v1582__00MF,pv1582__00MF_pv1565_global_stiffness_matrix)
path_from_v1578_dudot_dt_to_v1559_u = STD_MULT(path_from_v1578_dudot_dt_to_v1582__00MF,pv1582__00MF_pv1559_u)
del pv1582__00MF_pv1565_global_stiffness_matrix
del path_from_v1578_dudot_dt_to_v1582__00MF
del pv1582__00MF_pv1559_u

# op _00Mp_power_combination_eval
# LANG: global_stiffness_matrix --> _00Mq
# SHAPES: (1, 30, 30) --> (1, 30, 30)
# full namespace: 

# _00Mp_power_combination_eval_pv1574__00Mq_pv1565_global_stiffness_matrix
temp_power = _00Mp_coeff_temp*1
pv1574__00Mq_pv1565_global_stiffness_matrix = temp_power.flatten()
path_from_v1578_dudot_dt_to_v1565_global_stiffness_matrix += DIAG_MULT(path_from_v1578_dudot_dt_to_v1574__00Mq,pv1574__00Mq_pv1565_global_stiffness_matrix)
del pv1574__00Mq_pv1565_global_stiffness_matrix
del path_from_v1578_dudot_dt_to_v1574__00Mq

# op _00Mn_power_combination_eval
# LANG: global_mass_matrix --> _00Mo
# SHAPES: (1, 30, 30) --> (1, 30, 30)
# full namespace: 

# _00Mn_power_combination_eval_pv1573__00Mo_pv1564_global_mass_matrix
temp_power = _00Mn_coeff_temp*1
pv1573__00Mo_pv1564_global_mass_matrix = temp_power.flatten()
path_from_v1578_dudot_dt_to_v1564_global_mass_matrix += DIAG_MULT(path_from_v1578_dudot_dt_to_v1573__00Mo,pv1573__00Mo_pv1564_global_mass_matrix)
del path_from_v1578_dudot_dt_to_v1573__00Mo
del pv1573__00Mo_pv1564_global_mass_matrix
# dv1576_du_dt_dv1559_u = zero
dv1576_du_dt_dv1559_u = np.zeros((r_seed_v1576_du_dt.shape[0],30))
dv1576_du_dt_dv1560_u_dot = path_from_v1576_du_dt_to_v1560_u_dot.copy()
# dv1576_du_dt_dv1561_eel_force_torque = zero
dv1576_du_dt_dv1561_eel_force_torque = np.zeros((r_seed_v1576_du_dt.shape[0],30))
# dv1576_du_dt_dv1563_eel_mesh = zero
dv1576_du_dt_dv1563_eel_mesh = np.zeros((r_seed_v1576_du_dt.shape[0],15))
# dv1576_du_dt_dv1564_global_mass_matrix = zero
dv1576_du_dt_dv1564_global_mass_matrix = sp.csr_array((r_seed_v1576_du_dt.shape[0], 900))
# dv1576_du_dt_dv1565_global_stiffness_matrix = zero
dv1576_du_dt_dv1565_global_stiffness_matrix = sp.csr_array((r_seed_v1576_du_dt.shape[0], 900))
dv1578_dudot_dt_dv1559_u = path_from_v1578_dudot_dt_to_v1559_u.copy()
dv1578_dudot_dt_dv1560_u_dot = path_from_v1578_dudot_dt_to_v1560_u_dot.copy()
dv1578_dudot_dt_dv1561_eel_force_torque = path_from_v1578_dudot_dt_to_v1561_eel_force_torque.copy()
# dv1578_dudot_dt_dv1563_eel_mesh = zero
dv1578_dudot_dt_dv1563_eel_mesh = np.zeros((r_seed_v1578_dudot_dt.shape[0],15))
dv1578_dudot_dt_dv1564_global_mass_matrix = path_from_v1578_dudot_dt_to_v1564_global_mass_matrix.copy()
dv1578_dudot_dt_dv1565_global_stiffness_matrix = path_from_v1578_dudot_dt_to_v1565_global_stiffness_matrix.copy()