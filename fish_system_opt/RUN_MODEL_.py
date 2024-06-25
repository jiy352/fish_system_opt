

# RUN_MODEL_

# system evaluation block

# op _000d expand_scalar_eval
# LANG: L --> _000e
# SHAPES: (1,) --> (51,)
# full namespace: EelGeometryModel
v11__000e = np.empty((51,))
v11__000e.fill(v9_L.item())

# op _000h_matvec_eval
# LANG: control_points --> _000i
# SHAPES: (5,) --> (51,)
# full namespace: EelGeometryModel
v13__000i = _000h_matvec_eval_A.dot(v10_control_points)

# op _000j_power_combination_eval
# LANG: _000e, _000i --> eel_height
# SHAPES: (51,), (51,) --> (51,)
# full namespace: EelGeometryModel
v14_eel_height = (v13__000i)*(v11__000e)
v14_eel_height = v14_eel_height.reshape((51,))

# op _000o expand_array_eval
# LANG: eel_height --> _000p
# SHAPES: (51,) --> (51, 5)
# full namespace: EelGeometryModel
v17__000p = np.einsum('a,b->ab', v14_eel_height.reshape((51,)) ,np.ones((5,))).reshape((51, 5))

# op _000f_power_combination_eval
# LANG: _000e --> _000g
# SHAPES: (51,) --> (51,)
# full namespace: EelGeometryModel
v12__000g = (v11__000e)
v12__000g = (v12__000g*_000f_coeff).reshape((51,))

# op _000t_power_combination_eval
# LANG: _000p --> _000u
# SHAPES: (51, 5) --> (51, 5)
# full namespace: EelGeometryModel
v19__000u = (v17__000p)
v19__000u = (v19__000u*_000t_coeff).reshape((51, 5))

# op _000m expand_array_eval
# LANG: _000g --> _000n
# SHAPES: (51,) --> (51, 5)
# full namespace: EelGeometryModel
v16__000n = np.einsum('a,b->ab', v12__000g.reshape((51,)) ,np.ones((5,))).reshape((51, 5))

# op _000v_power_combination_eval
# LANG: _000u --> _000w
# SHAPES: (51, 5) --> (51, 5)
# full namespace: EelGeometryModel
v20__000w = (v19__000u)
v20__000w = (v20__000w*_000v_coeff).reshape((51, 5))

# op _000q reshape_eval
# LANG: _000n --> _000r
# SHAPES: (51, 5) --> (51, 5, 1)
# full namespace: EelGeometryModel
v18__000r = v16__000n.reshape((51, 5, 1))

# op _000x reshape_eval
# LANG: _000w --> _000y
# SHAPES: (51, 5) --> (51, 5, 1)
# full namespace: EelGeometryModel
v21__000y = v20__000w.reshape((51, 5, 1))

# op _0007 expand_scalar_eval
# LANG: v_x --> u
# SHAPES: (1,) --> (70, 1)
# full namespace: 
v7_u = np.empty((70, 1))
v7_u.fill(v6_v_x.item())

# op _000s_indexed_passthrough_eval
# LANG: _000r, _000y --> eel_rigid_mesh
# SHAPES: (51, 5, 1), (51, 5, 1) --> (51, 5, 3)
# full namespace: EelGeometryModel
v15_eel_rigid_mesh__temp[i_v18__000r__000s_indexed_passthrough_eval] = v18__000r.flatten()
v15_eel_rigid_mesh = v15_eel_rigid_mesh__temp.copy()
v15_eel_rigid_mesh__temp[i_v21__000y__000s_indexed_passthrough_eval] = v21__000y.flatten()
v15_eel_rigid_mesh = v15_eel_rigid_mesh__temp.copy()