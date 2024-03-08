

# REV_: eel_height,-->v0_L,v1_a_coeff,v2_b_coeff,

# REV_: eel_height,-->v0_L,v1_a_coeff,v2_b_coeff,

# op _000p_power_combination_eval
# LANG: _000e, _000o --> eel_height
# SHAPES: (41,), (41,) --> (41,)
# full namespace: 

# _000p_power_combination_eval_pv14_eel_height_pv13__000o
temp_power = _000p_coeff_temp*1*(v13__000o)
pv14_eel_height_pv8__000e = temp_power.flatten()
temp_power = _000p_coeff_temp*(v8__000e)*1
pv14_eel_height_pv13__000o = temp_power.flatten()
path_from_v14_eel_height_to_v8__000e = DIAG_MULT(r_seed_v14_eel_height,pv14_eel_height_pv8__000e)
path_from_v14_eel_height_to_v13__000o = DIAG_MULT(r_seed_v14_eel_height,pv14_eel_height_pv13__000o)
del pv14_eel_height_pv13__000o
del pv14_eel_height_pv8__000e

# op _000n_power_combination_eval
# LANG: _000m --> _000o
# SHAPES: (41,) --> (41,)
# full namespace: 

# _000n_power_combination_eval_pv13__000o_pv12__000m
temp_power = _000n_coeff_temp*0.5*(v12__000m**-0.5)
pv13__000o_pv12__000m = temp_power.flatten()
path_from_v14_eel_height_to_v12__000m = DIAG_MULT(path_from_v14_eel_height_to_v13__000o,pv13__000o_pv12__000m)
del pv13__000o_pv12__000m
del path_from_v14_eel_height_to_v13__000o

# op _000d expand_scalar_eval
# LANG: _0006 --> _000e
# SHAPES: (1,) --> (41,)
# full namespace: 

# _000d expand_scalar_eval_pv8__000e_pv4__0006
path_from_v14_eel_height_to_v4__0006 = STD_MULT(path_from_v14_eel_height_to_v8__000e,pv8__000e_pv4__0006)
del path_from_v14_eel_height_to_v8__000e

# op _000l_linear_combination_eval
# LANG: _000k --> _000m
# SHAPES: (41,) --> (41,)
# full namespace: 

# _000l_linear_combination_eval_pv12__000m_pv11__000k
path_from_v14_eel_height_to_v11__000k = DIAG_MULT(path_from_v14_eel_height_to_v12__000m,pv12__000m_pv11__000k)
del path_from_v14_eel_height_to_v12__000m

# op _0005_power_combination_eval
# LANG: b_coeff, L --> _0006
# SHAPES: (1,), (1,) --> (1,)
# full namespace: 

# _0005_power_combination_eval_pv4__0006_pv0_L
temp_power = _0005_coeff_temp*1*(v0_L)
pv4__0006_pv2_b_coeff = temp_power.flatten()
temp_power = _0005_coeff_temp*(v2_b_coeff)*1
pv4__0006_pv0_L = temp_power.flatten()
path_from_v14_eel_height_to_v2_b_coeff = DIAG_MULT(path_from_v14_eel_height_to_v4__0006,pv4__0006_pv2_b_coeff)
path_from_v14_eel_height_to_v0_L = DIAG_MULT(path_from_v14_eel_height_to_v4__0006,pv4__0006_pv0_L)
del pv4__0006_pv0_L
del path_from_v14_eel_height_to_v4__0006
del pv4__0006_pv2_b_coeff

# op _000j_power_combination_eval
# LANG: _000i --> _000k
# SHAPES: (41,) --> (41,)
# full namespace: 

# _000j_power_combination_eval_pv11__000k_pv10__000i
temp_power = _000j_coeff_temp*2*(v10__000i)
pv11__000k_pv10__000i = temp_power.flatten()
path_from_v14_eel_height_to_v10__000i = DIAG_MULT(path_from_v14_eel_height_to_v11__000k,pv11__000k_pv10__000i)
del pv11__000k_pv10__000i
del path_from_v14_eel_height_to_v11__000k

# op _000h_power_combination_eval
# LANG: _000g, _000c --> _000i
# SHAPES: (41,), (41,) --> (41,)
# full namespace: 

# _000h_power_combination_eval_pv10__000i_pv7__000c
temp_power = _000h_coeff_temp*1*(v7__000c**-1)
pv10__000i_pv9__000g = temp_power.flatten()
temp_power = _000h_coeff_temp*(v9__000g)*-1*(v7__000c**-2.0)
pv10__000i_pv7__000c = temp_power.flatten()
path_from_v14_eel_height_to_v9__000g = DIAG_MULT(path_from_v14_eel_height_to_v10__000i,pv10__000i_pv9__000g)
path_from_v14_eel_height_to_v7__000c = DIAG_MULT(path_from_v14_eel_height_to_v10__000i,pv10__000i_pv7__000c)
del pv10__000i_pv9__000g
del path_from_v14_eel_height_to_v10__000i
del pv10__000i_pv7__000c

# op _000f_linear_combination_eval
# LANG: _000a, _000c --> _000g
# SHAPES: (41,), (41,) --> (41,)
# full namespace: 

# _000f_linear_combination_eval_pv9__000g_pv7__000c
path_from_v14_eel_height_to_v6__000a = DIAG_MULT(path_from_v14_eel_height_to_v9__000g,pv9__000g_pv6__000a)
path_from_v14_eel_height_to_v7__000c += DIAG_MULT(path_from_v14_eel_height_to_v9__000g,pv9__000g_pv7__000c)
del path_from_v14_eel_height_to_v9__000g

# op _000b expand_scalar_eval
# LANG: _0004 --> _000c
# SHAPES: (1,) --> (41,)
# full namespace: 

# _000b expand_scalar_eval_pv7__000c_pv3__0004
path_from_v14_eel_height_to_v3__0004 = STD_MULT(path_from_v14_eel_height_to_v7__000c,pv7__000c_pv3__0004)
del path_from_v14_eel_height_to_v7__000c

# op _0009_power_combination_eval
# LANG: _0008 --> _000a
# SHAPES: (41,) --> (41,)
# full namespace: 

# _0009_power_combination_eval_pv6__000a_pv5__0008
temp_power = _0009_coeff_temp*1
pv6__000a_pv5__0008 = temp_power.flatten()
path_from_v14_eel_height_to_v5__0008 = DIAG_MULT(path_from_v14_eel_height_to_v6__000a,pv6__000a_pv5__0008)
del path_from_v14_eel_height_to_v6__000a
del pv6__000a_pv5__0008

# op _0007 expand_scalar_eval
# LANG: L --> _0008
# SHAPES: (1,) --> (41,)
# full namespace: 

# _0007 expand_scalar_eval_pv5__0008_pv0_L
path_from_v14_eel_height_to_v0_L += STD_MULT(path_from_v14_eel_height_to_v5__0008,pv5__0008_pv0_L)
del path_from_v14_eel_height_to_v5__0008

# op _0003_power_combination_eval
# LANG: a_coeff, L --> _0004
# SHAPES: (1,), (1,) --> (1,)
# full namespace: 

# _0003_power_combination_eval_pv3__0004_pv0_L
temp_power = _0003_coeff_temp*1*(v0_L)
pv3__0004_pv1_a_coeff = temp_power.flatten()
temp_power = _0003_coeff_temp*(v1_a_coeff)*1
pv3__0004_pv0_L = temp_power.flatten()
path_from_v14_eel_height_to_v1_a_coeff = DIAG_MULT(path_from_v14_eel_height_to_v3__0004,pv3__0004_pv1_a_coeff)
path_from_v14_eel_height_to_v0_L += DIAG_MULT(path_from_v14_eel_height_to_v3__0004,pv3__0004_pv0_L)
del pv3__0004_pv1_a_coeff
del path_from_v14_eel_height_to_v3__0004
del pv3__0004_pv0_L
dv14_eel_height_dv0_L = path_from_v14_eel_height_to_v0_L.copy()
dv14_eel_height_dv1_a_coeff = path_from_v14_eel_height_to_v1_a_coeff.copy()
dv14_eel_height_dv2_b_coeff = path_from_v14_eel_height_to_v2_b_coeff.copy()