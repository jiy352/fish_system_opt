

# RUN_MODEL_

# system evaluation block

# op _0003_power_combination_eval
# LANG: a_coeff, L --> _0004
# SHAPES: (1,), (1,) --> (1,)
# full namespace: 
v3__0004 = (v1_a_coeff)*(v0_L)
v3__0004 = v3__0004.reshape((1,))

# op _0007 expand_scalar_eval
# LANG: L --> _0008
# SHAPES: (1,) --> (41,)
# full namespace: 
v5__0008 = np.empty((41,))
v5__0008.fill(v0_L.item())

# op _0009_power_combination_eval
# LANG: _0008 --> _000a
# SHAPES: (41,) --> (41,)
# full namespace: 
v6__000a = (v5__0008)
v6__000a = (v6__000a*_0009_coeff).reshape((41,))

# op _000b expand_scalar_eval
# LANG: _0004 --> _000c
# SHAPES: (1,) --> (41,)
# full namespace: 
v7__000c = np.empty((41,))
v7__000c.fill(v3__0004.item())

# op _000f_linear_combination_eval
# LANG: _000a, _000c --> _000g
# SHAPES: (41,), (41,) --> (41,)
# full namespace: 
v9__000g = v6__000a+-1*v7__000c

# op _000h_power_combination_eval
# LANG: _000g, _000c --> _000i
# SHAPES: (41,), (41,) --> (41,)
# full namespace: 
v10__000i = (v9__000g)*(v7__000c**-1)
v10__000i = v10__000i.reshape((41,))

# op _000j_power_combination_eval
# LANG: _000i --> _000k
# SHAPES: (41,) --> (41,)
# full namespace: 
v11__000k = (v10__000i**2)
v11__000k = v11__000k.reshape((41,))

# op _0005_power_combination_eval
# LANG: b_coeff, L --> _0006
# SHAPES: (1,), (1,) --> (1,)
# full namespace: 
v4__0006 = (v2_b_coeff)*(v0_L)
v4__0006 = v4__0006.reshape((1,))

# op _000l_linear_combination_eval
# LANG: _000k --> _000m
# SHAPES: (41,) --> (41,)
# full namespace: 
v12__000m = _000l_constant+-1*v11__000k

# op _000d expand_scalar_eval
# LANG: _0006 --> _000e
# SHAPES: (1,) --> (41,)
# full namespace: 
v8__000e = np.empty((41,))
v8__000e.fill(v4__0006.item())

# op _000n_power_combination_eval
# LANG: _000m --> _000o
# SHAPES: (41,) --> (41,)
# full namespace: 
v13__000o = (v12__000m**0.5)
v13__000o = v13__000o.reshape((41,))

# op _000p_power_combination_eval
# LANG: _000e, _000o --> eel_height
# SHAPES: (41,), (41,) --> (41,)
# full namespace: 
v14_eel_height = (v8__000e)*(v13__000o)
v14_eel_height = v14_eel_height.reshape((41,))