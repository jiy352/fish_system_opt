

# RUN_MODEL_

# system evaluation block

# op _0006_power_combination_eval
# LANG: a_coeff, L --> _0007
# SHAPES: (1,), (1,) --> (1,)
# full namespace: 
v6__0007 = (v1_a_coeff)*(v0_L)
v6__0007 = v6__0007.reshape((1,))

# op _000a expand_scalar_eval
# LANG: L --> _000b
# SHAPES: (1,) --> (41,)
# full namespace: 
v8__000b = np.empty((41,))
v8__000b.fill(v0_L.item())

# op _000c_power_combination_eval
# LANG: _000b --> _000d
# SHAPES: (41,) --> (41,)
# full namespace: 
v9__000d = (v8__000b)
v9__000d = (v9__000d*_000c_coeff).reshape((41,))

# op _000e expand_scalar_eval
# LANG: _0007 --> _000f
# SHAPES: (1,) --> (41,)
# full namespace: 
v10__000f = np.empty((41,))
v10__000f.fill(v6__0007.item())

# op _000i_linear_combination_eval
# LANG: _000d, _000f --> _000j
# SHAPES: (41,), (41,) --> (41,)
# full namespace: 
v12__000j = v9__000d+-1*v10__000f

# op _000k_power_combination_eval
# LANG: _000j, _000f --> _000l
# SHAPES: (41,), (41,) --> (41,)
# full namespace: 
v13__000l = (v12__000j)*(v10__000f**-1)
v13__000l = v13__000l.reshape((41,))

# op _000m_power_combination_eval
# LANG: _000l --> _000n
# SHAPES: (41,) --> (41,)
# full namespace: 
v14__000n = (v13__000l**2)
v14__000n = v14__000n.reshape((41,))

# op _0008_power_combination_eval
# LANG: b_coeff, L --> _0009
# SHAPES: (1,), (1,) --> (1,)
# full namespace: 
v7__0009 = (v2_b_coeff)*(v0_L)
v7__0009 = v7__0009.reshape((1,))

# op _000o_linear_combination_eval
# LANG: _000n --> _000p
# SHAPES: (41,) --> (41,)
# full namespace: 
v15__000p = _000o_constant+-1*v14__000n

# op _000g expand_scalar_eval
# LANG: _0009 --> _000h
# SHAPES: (1,) --> (41,)
# full namespace: 
v11__000h = np.empty((41,))
v11__000h.fill(v7__0009.item())

# op _000q_power_combination_eval
# LANG: _000p --> _000r
# SHAPES: (41,) --> (41,)
# full namespace: 
v16__000r = (v15__000p**0.5)
v16__000r = v16__000r.reshape((41,))

# op _000s_power_combination_eval
# LANG: _000h, _000r --> eel_height
# SHAPES: (41,), (41,) --> (41,)
# full namespace: 
v17_eel_height = (v11__000h)*(v16__000r)
v17_eel_height = v17_eel_height.reshape((41,))

# op _000x expand_array_eval
# LANG: eel_height --> _000y
# SHAPES: (41,) --> (41, 5)
# full namespace: 
v20__000y = np.einsum('a,b->ab', v17_eel_height.reshape((41,)) ,np.ones((5,))).reshape((41, 5))

# op _000C_power_combination_eval
# LANG: _000y --> _000D
# SHAPES: (41, 5) --> (41, 5)
# full namespace: 
v22__000D = (v20__000y)
v22__000D = (v22__000D*_000C_coeff).reshape((41, 5))

# op _000E_power_combination_eval
# LANG: _000D --> _000F
# SHAPES: (41, 5) --> (41, 5)
# full namespace: 
v23__000F = (v22__000D)
v23__000F = (v23__000F*_000E_coeff).reshape((41, 5))

# op _000v expand_array_eval
# LANG: _000d --> _000w
# SHAPES: (41,) --> (41, 5)
# full namespace: 
v19__000w = np.einsum('a,b->ab', v9__000d.reshape((41,)) ,np.ones((5,))).reshape((41, 5))

# op _000G reshape_eval
# LANG: _000F --> _000H
# SHAPES: (41, 5) --> (41, 5, 1)
# full namespace: 
v24__000H = v23__000F.reshape((41, 5, 1))

# op _000z reshape_eval
# LANG: _000w --> _000A
# SHAPES: (41, 5) --> (41, 5, 1)
# full namespace: 
v21__000A = v19__000w.reshape((41, 5, 1))

# op _000B_indexed_passthrough_eval
# LANG: _000A, _000H --> eel_rigid_mesh
# SHAPES: (41, 5, 1), (41, 5, 1) --> (41, 5, 3)
# full namespace: 
v18_eel_rigid_mesh__temp[i_v21__000A__000B_indexed_passthrough_eval] = v21__000A.flatten()
v18_eel_rigid_mesh = v18_eel_rigid_mesh__temp.copy()
v18_eel_rigid_mesh__temp[i_v24__000H__000B_indexed_passthrough_eval] = v24__000H.flatten()
v18_eel_rigid_mesh = v18_eel_rigid_mesh__temp.copy()