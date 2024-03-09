

# REV_: eel_height,eel_rigid_mesh,-->v0_L,v1_a_coeff,v2_b_coeff,

# REV_: eel_height,eel_rigid_mesh,-->v0_L,v1_a_coeff,v2_b_coeff,

# op _000B_indexed_passthrough_eval
# LANG: _000A, _000H --> eel_rigid_mesh
# SHAPES: (41, 5, 1), (41, 5, 1) --> (41, 5, 3)
# full namespace: 

# _000B_indexed_passthrough_eval_pv18_eel_rigid_mesh_pv24__000H
path_from_v18_eel_rigid_mesh_to_v21__000A = STD_MULT(r_seed_v18_eel_rigid_mesh,pv18_eel_rigid_mesh_pv21__000A)
path_from_v18_eel_rigid_mesh_to_v24__000H = STD_MULT(r_seed_v18_eel_rigid_mesh,pv18_eel_rigid_mesh_pv24__000H)

# op _000z reshape_eval
# LANG: _000w --> _000A
# SHAPES: (41, 5) --> (41, 5, 1)
# full namespace: 

# _000z reshape_eval_pv21__000A_pv19__000w
path_from_v18_eel_rigid_mesh_to_v19__000w = DIAG_MULT(path_from_v18_eel_rigid_mesh_to_v21__000A,pv21__000A_pv19__000w)
del path_from_v18_eel_rigid_mesh_to_v21__000A

# op _000G reshape_eval
# LANG: _000F --> _000H
# SHAPES: (41, 5) --> (41, 5, 1)
# full namespace: 

# _000G reshape_eval_pv24__000H_pv23__000F
path_from_v18_eel_rigid_mesh_to_v23__000F = DIAG_MULT(path_from_v18_eel_rigid_mesh_to_v24__000H,pv24__000H_pv23__000F)
del path_from_v18_eel_rigid_mesh_to_v24__000H

# op _000v expand_array_eval
# LANG: _000d --> _000w
# SHAPES: (41,) --> (41, 5)
# full namespace: 

# _000v expand_array_eval_pv19__000w_pv9__000d
path_from_v18_eel_rigid_mesh_to_v9__000d = STD_MULT(path_from_v18_eel_rigid_mesh_to_v19__000w,pv19__000w_pv9__000d)
del path_from_v18_eel_rigid_mesh_to_v19__000w

# op _000E_power_combination_eval
# LANG: _000D --> _000F
# SHAPES: (41, 5) --> (41, 5)
# full namespace: 

# _000E_power_combination_eval_pv23__000F_pv22__000D
temp_power = _000E_coeff_temp*1
pv23__000F_pv22__000D = temp_power.flatten()
path_from_v18_eel_rigid_mesh_to_v22__000D = DIAG_MULT(path_from_v18_eel_rigid_mesh_to_v23__000F,pv23__000F_pv22__000D)
del path_from_v18_eel_rigid_mesh_to_v23__000F
del pv23__000F_pv22__000D

# op _000C_power_combination_eval
# LANG: _000y --> _000D
# SHAPES: (41, 5) --> (41, 5)
# full namespace: 

# _000C_power_combination_eval_pv22__000D_pv20__000y
temp_power = _000C_coeff_temp*1
pv22__000D_pv20__000y = temp_power.flatten()
path_from_v18_eel_rigid_mesh_to_v20__000y = DIAG_MULT(path_from_v18_eel_rigid_mesh_to_v22__000D,pv22__000D_pv20__000y)
del pv22__000D_pv20__000y
del path_from_v18_eel_rigid_mesh_to_v22__000D

# op _000x expand_array_eval
# LANG: eel_height --> _000y
# SHAPES: (41,) --> (41, 5)
# full namespace: 

# _000x expand_array_eval_pv20__000y_pv17_eel_height
path_from_v18_eel_rigid_mesh_to_v17_eel_height = STD_MULT(path_from_v18_eel_rigid_mesh_to_v20__000y,pv20__000y_pv17_eel_height)
del path_from_v18_eel_rigid_mesh_to_v20__000y

# op _000s_power_combination_eval
# LANG: _000h, _000r --> eel_height
# SHAPES: (41,), (41,) --> (41,)
# full namespace: 

# _000s_power_combination_eval_pv17_eel_height_pv16__000r
temp_power = _000s_coeff_temp*1*(v16__000r)
pv17_eel_height_pv11__000h = temp_power.flatten()
temp_power = _000s_coeff_temp*(v11__000h)*1
pv17_eel_height_pv16__000r = temp_power.flatten()
path_from_v17_eel_height_to_v11__000h = DIAG_MULT(r_seed_v17_eel_height,pv17_eel_height_pv11__000h)
path_from_v17_eel_height_to_v16__000r = DIAG_MULT(r_seed_v17_eel_height,pv17_eel_height_pv16__000r)
path_from_v18_eel_rigid_mesh_to_v11__000h = DIAG_MULT(path_from_v18_eel_rigid_mesh_to_v17_eel_height,pv17_eel_height_pv11__000h)
path_from_v18_eel_rigid_mesh_to_v16__000r = DIAG_MULT(path_from_v18_eel_rigid_mesh_to_v17_eel_height,pv17_eel_height_pv16__000r)
del pv17_eel_height_pv11__000h
del path_from_v18_eel_rigid_mesh_to_v17_eel_height
del pv17_eel_height_pv16__000r

# op _000q_power_combination_eval
# LANG: _000p --> _000r
# SHAPES: (41,) --> (41,)
# full namespace: 

# _000q_power_combination_eval_pv16__000r_pv15__000p
temp_power = _000q_coeff_temp*0.5*(v15__000p**-0.5)
pv16__000r_pv15__000p = temp_power.flatten()
path_from_v17_eel_height_to_v15__000p = DIAG_MULT(path_from_v17_eel_height_to_v16__000r,pv16__000r_pv15__000p)
path_from_v18_eel_rigid_mesh_to_v15__000p = DIAG_MULT(path_from_v18_eel_rigid_mesh_to_v16__000r,pv16__000r_pv15__000p)
del path_from_v17_eel_height_to_v16__000r
del pv16__000r_pv15__000p
del path_from_v18_eel_rigid_mesh_to_v16__000r

# op _000g expand_scalar_eval
# LANG: _0009 --> _000h
# SHAPES: (1,) --> (41,)
# full namespace: 

# _000g expand_scalar_eval_pv11__000h_pv7__0009
path_from_v17_eel_height_to_v7__0009 = STD_MULT(path_from_v17_eel_height_to_v11__000h,pv11__000h_pv7__0009)
path_from_v18_eel_rigid_mesh_to_v7__0009 = STD_MULT(path_from_v18_eel_rigid_mesh_to_v11__000h,pv11__000h_pv7__0009)
del path_from_v17_eel_height_to_v11__000h
del path_from_v18_eel_rigid_mesh_to_v11__000h

# op _000o_linear_combination_eval
# LANG: _000n --> _000p
# SHAPES: (41,) --> (41,)
# full namespace: 

# _000o_linear_combination_eval_pv15__000p_pv14__000n
path_from_v17_eel_height_to_v14__000n = DIAG_MULT(path_from_v17_eel_height_to_v15__000p,pv15__000p_pv14__000n)
path_from_v18_eel_rigid_mesh_to_v14__000n = DIAG_MULT(path_from_v18_eel_rigid_mesh_to_v15__000p,pv15__000p_pv14__000n)
del path_from_v17_eel_height_to_v15__000p
del path_from_v18_eel_rigid_mesh_to_v15__000p

# op _0008_power_combination_eval
# LANG: b_coeff, L --> _0009
# SHAPES: (1,), (1,) --> (1,)
# full namespace: 

# _0008_power_combination_eval_pv7__0009_pv0_L
temp_power = _0008_coeff_temp*1*(v0_L)
pv7__0009_pv2_b_coeff = temp_power.flatten()
temp_power = _0008_coeff_temp*(v2_b_coeff)*1
pv7__0009_pv0_L = temp_power.flatten()
path_from_v17_eel_height_to_v2_b_coeff = DIAG_MULT(path_from_v17_eel_height_to_v7__0009,pv7__0009_pv2_b_coeff)
path_from_v17_eel_height_to_v0_L = DIAG_MULT(path_from_v17_eel_height_to_v7__0009,pv7__0009_pv0_L)
path_from_v18_eel_rigid_mesh_to_v2_b_coeff = DIAG_MULT(path_from_v18_eel_rigid_mesh_to_v7__0009,pv7__0009_pv2_b_coeff)
path_from_v18_eel_rigid_mesh_to_v0_L = DIAG_MULT(path_from_v18_eel_rigid_mesh_to_v7__0009,pv7__0009_pv0_L)
del path_from_v17_eel_height_to_v7__0009
del pv7__0009_pv0_L
del path_from_v18_eel_rigid_mesh_to_v7__0009
del pv7__0009_pv2_b_coeff

# op _000m_power_combination_eval
# LANG: _000l --> _000n
# SHAPES: (41,) --> (41,)
# full namespace: 

# _000m_power_combination_eval_pv14__000n_pv13__000l
temp_power = _000m_coeff_temp*2*(v13__000l)
pv14__000n_pv13__000l = temp_power.flatten()
path_from_v17_eel_height_to_v13__000l = DIAG_MULT(path_from_v17_eel_height_to_v14__000n,pv14__000n_pv13__000l)
path_from_v18_eel_rigid_mesh_to_v13__000l = DIAG_MULT(path_from_v18_eel_rigid_mesh_to_v14__000n,pv14__000n_pv13__000l)
del pv14__000n_pv13__000l
del path_from_v17_eel_height_to_v14__000n
del path_from_v18_eel_rigid_mesh_to_v14__000n

# op _000k_power_combination_eval
# LANG: _000j, _000f --> _000l
# SHAPES: (41,), (41,) --> (41,)
# full namespace: 

# _000k_power_combination_eval_pv13__000l_pv10__000f
temp_power = _000k_coeff_temp*1*(v10__000f**-1)
pv13__000l_pv12__000j = temp_power.flatten()
temp_power = _000k_coeff_temp*(v12__000j)*-1*(v10__000f**-2.0)
pv13__000l_pv10__000f = temp_power.flatten()
path_from_v17_eel_height_to_v12__000j = DIAG_MULT(path_from_v17_eel_height_to_v13__000l,pv13__000l_pv12__000j)
path_from_v17_eel_height_to_v10__000f = DIAG_MULT(path_from_v17_eel_height_to_v13__000l,pv13__000l_pv10__000f)
path_from_v18_eel_rigid_mesh_to_v12__000j = DIAG_MULT(path_from_v18_eel_rigid_mesh_to_v13__000l,pv13__000l_pv12__000j)
path_from_v18_eel_rigid_mesh_to_v10__000f = DIAG_MULT(path_from_v18_eel_rigid_mesh_to_v13__000l,pv13__000l_pv10__000f)
del pv13__000l_pv12__000j
del pv13__000l_pv10__000f
del path_from_v17_eel_height_to_v13__000l
del path_from_v18_eel_rigid_mesh_to_v13__000l

# op _000i_linear_combination_eval
# LANG: _000d, _000f --> _000j
# SHAPES: (41,), (41,) --> (41,)
# full namespace: 

# _000i_linear_combination_eval_pv12__000j_pv10__000f
path_from_v17_eel_height_to_v9__000d = DIAG_MULT(path_from_v17_eel_height_to_v12__000j,pv12__000j_pv9__000d)
path_from_v17_eel_height_to_v10__000f += DIAG_MULT(path_from_v17_eel_height_to_v12__000j,pv12__000j_pv10__000f)
path_from_v18_eel_rigid_mesh_to_v9__000d += DIAG_MULT(path_from_v18_eel_rigid_mesh_to_v12__000j,pv12__000j_pv9__000d)
path_from_v18_eel_rigid_mesh_to_v10__000f += DIAG_MULT(path_from_v18_eel_rigid_mesh_to_v12__000j,pv12__000j_pv10__000f)
del path_from_v17_eel_height_to_v12__000j
del path_from_v18_eel_rigid_mesh_to_v12__000j

# op _000e expand_scalar_eval
# LANG: _0007 --> _000f
# SHAPES: (1,) --> (41,)
# full namespace: 

# _000e expand_scalar_eval_pv10__000f_pv6__0007
path_from_v17_eel_height_to_v6__0007 = STD_MULT(path_from_v17_eel_height_to_v10__000f,pv10__000f_pv6__0007)
path_from_v18_eel_rigid_mesh_to_v6__0007 = STD_MULT(path_from_v18_eel_rigid_mesh_to_v10__000f,pv10__000f_pv6__0007)
del path_from_v18_eel_rigid_mesh_to_v10__000f
del path_from_v17_eel_height_to_v10__000f

# op _000c_power_combination_eval
# LANG: _000b --> _000d
# SHAPES: (41,) --> (41,)
# full namespace: 

# _000c_power_combination_eval_pv9__000d_pv8__000b
temp_power = _000c_coeff_temp*1
pv9__000d_pv8__000b = temp_power.flatten()
path_from_v17_eel_height_to_v8__000b = DIAG_MULT(path_from_v17_eel_height_to_v9__000d,pv9__000d_pv8__000b)
path_from_v18_eel_rigid_mesh_to_v8__000b = DIAG_MULT(path_from_v18_eel_rigid_mesh_to_v9__000d,pv9__000d_pv8__000b)
del path_from_v18_eel_rigid_mesh_to_v9__000d
del pv9__000d_pv8__000b
del path_from_v17_eel_height_to_v9__000d

# op _000a expand_scalar_eval
# LANG: L --> _000b
# SHAPES: (1,) --> (41,)
# full namespace: 

# _000a expand_scalar_eval_pv8__000b_pv0_L
path_from_v17_eel_height_to_v0_L += STD_MULT(path_from_v17_eel_height_to_v8__000b,pv8__000b_pv0_L)
path_from_v18_eel_rigid_mesh_to_v0_L += STD_MULT(path_from_v18_eel_rigid_mesh_to_v8__000b,pv8__000b_pv0_L)
del path_from_v18_eel_rigid_mesh_to_v8__000b
del path_from_v17_eel_height_to_v8__000b

# op _0006_power_combination_eval
# LANG: a_coeff, L --> _0007
# SHAPES: (1,), (1,) --> (1,)
# full namespace: 

# _0006_power_combination_eval_pv6__0007_pv0_L
temp_power = _0006_coeff_temp*1*(v0_L)
pv6__0007_pv1_a_coeff = temp_power.flatten()
temp_power = _0006_coeff_temp*(v1_a_coeff)*1
pv6__0007_pv0_L = temp_power.flatten()
path_from_v17_eel_height_to_v1_a_coeff = DIAG_MULT(path_from_v17_eel_height_to_v6__0007,pv6__0007_pv1_a_coeff)
path_from_v17_eel_height_to_v0_L += DIAG_MULT(path_from_v17_eel_height_to_v6__0007,pv6__0007_pv0_L)
path_from_v18_eel_rigid_mesh_to_v1_a_coeff = DIAG_MULT(path_from_v18_eel_rigid_mesh_to_v6__0007,pv6__0007_pv1_a_coeff)
path_from_v18_eel_rigid_mesh_to_v0_L += DIAG_MULT(path_from_v18_eel_rigid_mesh_to_v6__0007,pv6__0007_pv0_L)
del path_from_v18_eel_rigid_mesh_to_v6__0007
del path_from_v17_eel_height_to_v6__0007
del pv6__0007_pv0_L
del pv6__0007_pv1_a_coeff
dv17_eel_height_dv0_L = path_from_v17_eel_height_to_v0_L.copy()
dv17_eel_height_dv1_a_coeff = path_from_v17_eel_height_to_v1_a_coeff.copy()
dv17_eel_height_dv2_b_coeff = path_from_v17_eel_height_to_v2_b_coeff.copy()
dv18_eel_rigid_mesh_dv0_L = path_from_v18_eel_rigid_mesh_to_v0_L.copy()
dv18_eel_rigid_mesh_dv1_a_coeff = path_from_v18_eel_rigid_mesh_to_v1_a_coeff.copy()
dv18_eel_rigid_mesh_dv2_b_coeff = path_from_v18_eel_rigid_mesh_to_v2_b_coeff.copy()