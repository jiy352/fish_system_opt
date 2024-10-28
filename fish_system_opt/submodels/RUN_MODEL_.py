

# RUN_MODEL_

# system evaluation block

# op _000b_power_combination_eval
# LANG: L, a_coeff --> _000c
# SHAPES: (1,), (1,) --> (1,)
# full namespace: EelGeometryModel
v9__000c = (v7_a_coeff)*(v57_L)
v9__000c = v9__000c.reshape((1,))

# op _000f expand_scalar_eval
# LANG: L --> _000g
# SHAPES: (1,) --> (41,)
# full namespace: EelGeometryModel
v11__000g = np.empty((41,))
v11__000g.fill(v57_L.item())

# op _000h_power_combination_eval
# LANG: _000g --> _000i
# SHAPES: (41,) --> (41,)
# full namespace: EelGeometryModel
v12__000i = (v11__000g)
v12__000i = (v12__000i*_000h_coeff).reshape((41,))

# op _000j expand_scalar_eval
# LANG: _000c --> _000k
# SHAPES: (1,) --> (41,)
# full namespace: EelGeometryModel
v13__000k = np.empty((41,))
v13__000k.fill(v9__000c.item())

# op _001C expand_scalar_eval
# LANG: theta_max --> _001D
# SHAPES: (1,) --> (71,)
# full namespace: EelKinematicsModel.FishTurnCCModel
v62__001D = np.empty((71,))
v62__001D.fill(v59_theta_max.item())

# op _001G_power_combination_eval
# LANG: time_vector --> _001H
# SHAPES: (71,) --> (71,)
# full namespace: EelKinematicsModel.FishTurnCCModel
v64__001H = (v60_time_vector)
v64__001H = (v64__001H*_001G_coeff).reshape((71,))

# op _000n_linear_combination_eval
# LANG: _000i, _000k --> _000o
# SHAPES: (41,), (41,) --> (41,)
# full namespace: EelGeometryModel
v15__000o = v12__000i+-1*v13__000k

# op _001E_linear_combination_eval
# LANG: _001D --> _001F
# SHAPES: (71,) --> (71,)
# full namespace: EelKinematicsModel.FishTurnCCModel
v63__001F = -1*v62__001D

# op _001I_cos_eval
# LANG: _001H --> _001J
# SHAPES: (71,) --> (71,)
# full namespace: EelKinematicsModel.FishTurnCCModel
v65__001J = np.cos(v64__001H)

# op _001Q expand_scalar_eval
# LANG: theta_max --> _001R
# SHAPES: (1,) --> (71,)
# full namespace: EelKinematicsModel.FishTurnCCModel
v69__001R = np.empty((71,))
v69__001R.fill(v59_theta_max.item())

# op _000p_power_combination_eval
# LANG: _000o, _000k --> _000q
# SHAPES: (41,), (41,) --> (41,)
# full namespace: EelGeometryModel
v16__000q = (v15__000o)*(v13__000k**-1)
v16__000q = v16__000q.reshape((41,))

# op _001K_power_combination_eval
# LANG: _001F, _001J --> _001L
# SHAPES: (71,), (71,) --> (71,)
# full namespace: EelKinematicsModel.FishTurnCCModel
v66__001L = (v63__001F)*(v65__001J)
v66__001L = v66__001L.reshape((71,))

# op _001O expand_scalar_eval
# LANG: tail_frequency --> _001P
# SHAPES: (1,) --> (71,)
# full namespace: EelKinematicsModel.FishTurnCCModel
v68__001P = np.empty((71,))
v68__001P.fill(v61_tail_frequency.item())

# op _001S_power_combination_eval
# LANG: _001R --> _001T
# SHAPES: (71,) --> (71,)
# full namespace: EelKinematicsModel.FishTurnCCModel
v70__001T = (v69__001R)
v70__001T = (v70__001T*_001S_coeff).reshape((71,))

# op _001W_power_combination_eval
# LANG: time_vector --> _001X
# SHAPES: (71,) --> (71,)
# full namespace: EelKinematicsModel.FishTurnCCModel
v72__001X = (v60_time_vector)
v72__001X = (v72__001X*_001W_coeff).reshape((71,))

# op _000r_power_combination_eval
# LANG: _000q --> _000s
# SHAPES: (41,) --> (41,)
# full namespace: EelGeometryModel
v17__000s = (v16__000q**2)
v17__000s = v17__000s.reshape((41,))

# op _001M_linear_combination_eval
# LANG: _001L, _001D --> theta_profile
# SHAPES: (71,), (71,) --> (71,)
# full namespace: EelKinematicsModel.FishTurnCCModel
v67_theta_profile = v66__001L+v62__001D

# op _001U_power_combination_eval
# LANG: _001T, _001P --> _001V
# SHAPES: (71,), (71,) --> (71,)
# full namespace: EelKinematicsModel.FishTurnCCModel
v71__001V = (v70__001T)*(v68__001P)
v71__001V = v71__001V.reshape((71,))

# op _001Y_sin_eval
# LANG: _001X --> _001Z
# SHAPES: (71,) --> (71,)
# full namespace: EelKinematicsModel.FishTurnCCModel
v73__001Z = np.sin(v72__001X)

# op _0025 expand_scalar_eval
# LANG: L --> _0026
# SHAPES: (1,) --> (71,)
# full namespace: EelKinematicsModel.FishTurnCCModel
v77__0026 = np.empty((71,))
v77__0026.fill(v57_L.item())

# op _000d_power_combination_eval
# LANG: L, b_coeff --> _000e
# SHAPES: (1,), (1,) --> (1,)
# full namespace: EelGeometryModel
v10__000e = (v8_b_coeff)*(v57_L)
v10__000e = v10__000e.reshape((1,))

# op _000t_linear_combination_eval
# LANG: _000s --> _000u
# SHAPES: (41,) --> (41,)
# full namespace: EelGeometryModel
v18__000u = _000t_constant+-1*v17__000s

# op _001__power_combination_eval
# LANG: _001V, _001Z --> theta_dot
# SHAPES: (71,), (71,) --> (71,)
# full namespace: EelKinematicsModel.FishTurnCCModel
v74_theta_dot = (v71__001V)*(v73__001Z)
v74_theta_dot = v74_theta_dot.reshape((71,))

# op _0021 expand_scalar_eval
# LANG: L --> _0022
# SHAPES: (1,) --> (71,)
# full namespace: EelKinematicsModel.FishTurnCCModel
v75__0022 = np.empty((71,))
v75__0022.fill(v57_L.item())

# op _0027_linear_combination_eval
# LANG: _0026 --> _0028
# SHAPES: (71,) --> (71,)
# full namespace: EelKinematicsModel.FishTurnCCModel
v78__0028 = -1*v77__0026

# op _002P expand_array_eval
# LANG: theta_profile --> _002Q
# SHAPES: (71,) --> (71, 41)
# full namespace: EelKinematicsModel.FishTurnCCModel
v100__002Q = np.einsum('a,b->ab', v67_theta_profile.reshape((71,)) ,np.ones((41,))).reshape((71, 41))

# op _000l expand_scalar_eval
# LANG: _000e --> _000m
# SHAPES: (1,) --> (41,)
# full namespace: EelGeometryModel
v14__000m = np.empty((41,))
v14__000m.fill(v10__000e.item())

# op _000v_power_combination_eval
# LANG: _000u --> _000w
# SHAPES: (41,) --> (41,)
# full namespace: EelGeometryModel
v19__000w = (v18__000u**0.5)
v19__000w = v19__000w.reshape((41,))

# op _0023_power_combination_eval
# LANG: theta_profile, _0022 --> _0024
# SHAPES: (71,), (71,) --> (71,)
# full namespace: EelKinematicsModel.FishTurnCCModel
v76__0024 = (v75__0022)*(v67_theta_profile**-1)
v76__0024 = v76__0024.reshape((71,))

# op _0029_power_combination_eval
# LANG: theta_dot, _0028 --> _002a
# SHAPES: (71,), (71,) --> (71,)
# full namespace: EelKinematicsModel.FishTurnCCModel
v79__002a = (v78__0028)*(v74_theta_dot)
v79__002a = v79__002a.reshape((71,))

# op _002T_power_combination_eval
# LANG: _002Q --> _002U
# SHAPES: (71, 41) --> (71, 41)
# full namespace: EelKinematicsModel.FishTurnCCModel
v102__002U = (v100__002Q)
v102__002U = (v102__002U*_002T_coeff).reshape((71, 41))

# op _002b_power_combination_eval
# LANG: theta_profile --> _002c
# SHAPES: (71,) --> (71,)
# full namespace: EelKinematicsModel.FishTurnCCModel
v80__002c = (v67_theta_profile**2)
v80__002c = v80__002c.reshape((71,))

# op _000x_power_combination_eval
# LANG: _000m, _000w --> eel_height
# SHAPES: (41,), (41,) --> (41,)
# full namespace: EelGeometryModel
v20_eel_height = (v14__000m)*(v19__000w)
v20_eel_height = v20_eel_height.reshape((41,))

# op _002d_power_combination_eval
# LANG: _002a, _002c --> _002e
# SHAPES: (71,), (71,) --> (71,)
# full namespace: EelKinematicsModel.FishTurnCCModel
v81__002e = (v79__002a)*(v80__002c**-1)
v81__002e = v81__002e.reshape((71,))

# op _0036 expand_array_eval
# LANG: _0024 --> _0037
# SHAPES: (71,) --> (71, 41)
# full namespace: EelKinematicsModel.FishTurnCCModel
v109__0037 = np.einsum('a,b->ab', v76__0024.reshape((71,)) ,np.ones((41,))).reshape((71, 41))

# op _0038 expand_array_eval
# LANG: theta_dot --> _0039
# SHAPES: (71,) --> (71, 41)
# full namespace: EelKinematicsModel.FishTurnCCModel
v110__0039 = np.einsum('a,b->ab', v74_theta_dot.reshape((71,)) ,np.ones((41,))).reshape((71, 41))

# op _003g_cos_eval
# LANG: _002U --> _003h
# SHAPES: (71, 41) --> (71, 41)
# full namespace: EelKinematicsModel.FishTurnCCModel
v114__003h = np.cos(v102__002U)

# op _003o_cos_eval
# LANG: _002U --> _003p
# SHAPES: (71, 41) --> (71, 41)
# full namespace: EelKinematicsModel.FishTurnCCModel
v118__003p = np.cos(v102__002U)

# op _003u_sin_eval
# LANG: _002U --> _003v
# SHAPES: (71, 41) --> (71, 41)
# full namespace: EelKinematicsModel.FishTurnCCModel
v121__003v = np.sin(v102__002U)

# op _000C expand_array_eval
# LANG: eel_height --> _000D
# SHAPES: (41,) --> (41, 5)
# full namespace: EelGeometryModel
v23__000D = np.einsum('a,b->ab', v20_eel_height.reshape((41,)) ,np.ones((5,))).reshape((41, 5))

# op _0034 expand_array_eval
# LANG: _002e --> _0035
# SHAPES: (71,) --> (71, 41)
# full namespace: EelKinematicsModel.FishTurnCCModel
v108__0035 = np.einsum('a,b->ab', v81__002e.reshape((71,)) ,np.ones((41,))).reshape((71, 41))

# op _003a_sin_eval
# LANG: _002U --> _003b
# SHAPES: (71, 41) --> (71, 41)
# full namespace: EelKinematicsModel.FishTurnCCModel
v111__003b = np.sin(v102__002U)

# op _003e_power_combination_eval
# LANG: _0039 --> _003f
# SHAPES: (71, 41) --> (71, 41)
# full namespace: EelKinematicsModel.FishTurnCCModel
v113__003f = (v110__0039)
v113__003f = (v113__003f*_003e_coeff).reshape((71, 41))

# op _003i_power_combination_eval
# LANG: _0037, _003h --> _003j
# SHAPES: (71, 41), (71, 41) --> (71, 41)
# full namespace: EelKinematicsModel.FishTurnCCModel
v115__003j = (v109__0037)*(v114__003h)
v115__003j = v115__003j.reshape((71, 41))

# op _003q_linear_combination_eval
# LANG: _003p --> _003r
# SHAPES: (71, 41) --> (71, 41)
# full namespace: EelKinematicsModel.FishTurnCCModel
v119__003r = _003q_constant+-1*v118__003p

# op _003w_power_combination_eval
# LANG: _0037, _003v --> _003x
# SHAPES: (71, 41), (71, 41) --> (71, 41)
# full namespace: EelKinematicsModel.FishTurnCCModel
v122__003x = (v109__0037)*(v121__003v)
v122__003x = v122__003x.reshape((71, 41))

# op _000H_power_combination_eval
# LANG: _000D --> _000I
# SHAPES: (41, 5) --> (41, 5)
# full namespace: EelGeometryModel
v25__000I = (v23__000D)
v25__000I = (v25__000I*_000H_coeff).reshape((41, 5))

# op _003c_power_combination_eval
# LANG: _0035, _003b --> _003d
# SHAPES: (71, 41), (71, 41) --> (71, 41)
# full namespace: EelKinematicsModel.FishTurnCCModel
v112__003d = (v108__0035)*(v111__003b)
v112__003d = v112__003d.reshape((71, 41))

# op _003k_power_combination_eval
# LANG: _003f, _003j --> _003l
# SHAPES: (71, 41), (71, 41) --> (71, 41)
# full namespace: EelKinematicsModel.FishTurnCCModel
v116__003l = (v115__003j)*(v113__003f)
v116__003l = v116__003l.reshape((71, 41))

# op _003s_power_combination_eval
# LANG: _0035, _003r --> _003t
# SHAPES: (71, 41), (71, 41) --> (71, 41)
# full namespace: EelKinematicsModel.FishTurnCCModel
v120__003t = (v108__0035)*(v119__003r)
v120__003t = v120__003t.reshape((71, 41))

# op _003y_power_combination_eval
# LANG: _003x, _003f --> _003z
# SHAPES: (71, 41), (71, 41) --> (71, 41)
# full namespace: EelKinematicsModel.FishTurnCCModel
v123__003z = (v122__003x)*(v113__003f)
v123__003z = v123__003z.reshape((71, 41))

# op _000A expand_array_eval
# LANG: _000i --> _000B
# SHAPES: (41,) --> (41, 5)
# full namespace: EelGeometryModel
v22__000B = np.einsum('a,b->ab', v12__000i.reshape((41,)) ,np.ones((5,))).reshape((41, 5))

# op _000J_power_combination_eval
# LANG: _000I --> _000K
# SHAPES: (41, 5) --> (41, 5)
# full namespace: EelGeometryModel
v26__000K = (v25__000I)
v26__000K = (v26__000K*_000J_coeff).reshape((41, 5))

# op _003A_linear_combination_eval
# LANG: _003t, _003z --> y_dot
# SHAPES: (71, 41), (71, 41) --> (71, 41)
# full namespace: EelKinematicsModel.FishTurnCCModel
v124_y_dot = v120__003t+v123__003z

# op _003m_linear_combination_eval
# LANG: _003d, _003l --> x_dot
# SHAPES: (71, 41), (71, 41) --> (71, 41)
# full namespace: EelKinematicsModel.FishTurnCCModel
v117_x_dot = v112__003d+v116__003l

# op _000E reshape_eval
# LANG: _000B --> _000F
# SHAPES: (41, 5) --> (41, 5, 1)
# full namespace: EelGeometryModel
v24__000F = v22__000B.reshape((41, 5, 1))

# op _000L reshape_eval
# LANG: _000K --> _000M
# SHAPES: (41, 5) --> (41, 5, 1)
# full namespace: EelGeometryModel
v27__000M = v26__000K.reshape((41, 5, 1))

# op _0014 expand_array_eval
# LANG: x_dot --> _0015
# SHAPES: (71, 41) --> (71, 41, 4, 1)
# full namespace: EelKinematicsModel
v41__0015 = np.einsum('ab,cd->abcd', v117_x_dot.reshape((71, 41)) ,np.ones((4, 1))).reshape((71, 41, 4, 1))

# op _0016 expand_array_eval
# LANG: y_dot --> _0017
# SHAPES: (71, 41) --> (71, 41, 4, 1)
# full namespace: EelKinematicsModel
v42__0017 = np.einsum('ab,cd->abcd', v124_y_dot.reshape((71, 41)) ,np.ones((4, 1))).reshape((71, 41, 4, 1))

# op _002Z_cos_eval
# LANG: _002U --> _002_
# SHAPES: (71, 41) --> (71, 41)
# full namespace: EelKinematicsModel.FishTurnCCModel
v105__002_ = np.cos(v102__002U)

# op _000G_indexed_passthrough_eval
# LANG: _000F, _000M --> eel_rigid_mesh
# SHAPES: (41, 5, 1), (41, 5, 1) --> (41, 5, 3)
# full namespace: EelGeometryModel
v44_eel_rigid_mesh__temp[i_v24__000F__000G_indexed_passthrough_eval] = v24__000F.flatten()
v44_eel_rigid_mesh = v44_eel_rigid_mesh__temp.copy()
v44_eel_rigid_mesh__temp[i_v27__000M__000G_indexed_passthrough_eval] = v27__000M.flatten()
v44_eel_rigid_mesh = v44_eel_rigid_mesh__temp.copy()

# op _001i_decompose_eval
# LANG: _0015 --> _001k, _001j
# SHAPES: (71, 41, 4, 1) --> (71, 40, 4, 1), (71, 40, 4, 1)
# full namespace: EelKinematicsModel
v49__001j = ((v41__0015.flatten())[src_indices__001j__001i]).reshape((71, 40, 4, 1))
v50__001k = ((v41__0015.flatten())[src_indices__001k__001i]).reshape((71, 40, 4, 1))

# op _001q_decompose_eval
# LANG: _0017 --> _001s, _001r
# SHAPES: (71, 41, 4, 1) --> (71, 40, 4, 1), (71, 40, 4, 1)
# full namespace: EelKinematicsModel
v53__001r = ((v42__0017.flatten())[src_indices__001r__001q]).reshape((71, 40, 4, 1))
v54__001s = ((v42__0017.flatten())[src_indices__001s__001q]).reshape((71, 40, 4, 1))

# op _002B_cos_eval
# LANG: theta_profile --> _002C
# SHAPES: (71,) --> (71,)
# full namespace: EelKinematicsModel.FishTurnCCModel
v93__002C = np.cos(v67_theta_profile)

# op _002H_sin_eval
# LANG: theta_profile --> _002I
# SHAPES: (71,) --> (71,)
# full namespace: EelKinematicsModel.FishTurnCCModel
v96__002I = np.sin(v67_theta_profile)

# op _002R expand_array_eval
# LANG: _0024 --> _002S
# SHAPES: (71,) --> (71, 41)
# full namespace: EelKinematicsModel.FishTurnCCModel
v101__002S = np.einsum('a,b->ab', v76__0024.reshape((71,)) ,np.ones((41,))).reshape((71, 41))

# op _002V_sin_eval
# LANG: _002U --> _002W
# SHAPES: (71, 41) --> (71, 41)
# full namespace: EelKinematicsModel.FishTurnCCModel
v103__002W = np.sin(v102__002U)

# op _002t_cos_eval
# LANG: theta_profile --> _002u
# SHAPES: (71,) --> (71,)
# full namespace: EelKinematicsModel.FishTurnCCModel
v89__002u = np.cos(v67_theta_profile)

# op _0030_linear_combination_eval
# LANG: _002_ --> _0031
# SHAPES: (71, 41) --> (71, 41)
# full namespace: EelKinematicsModel.FishTurnCCModel
v106__0031 = _0030_constant+-1*v105__002_

# op _001b expand_array_eval
# LANG: eel_rigid_mesh --> _001c
# SHAPES: (41, 5, 3) --> (71, 41, 5, 3)
# full namespace: EelKinematicsModel
v45__001c = np.einsum('bcd,a->abcd', v44_eel_rigid_mesh.reshape((41, 5, 3)) ,np.ones((71,))).reshape((71, 41, 5, 3))

# op _001l_linear_combination_eval
# LANG: _001j, _001k --> _001m
# SHAPES: (71, 40, 4, 1), (71, 40, 4, 1) --> (71, 40, 4, 1)
# full namespace: EelKinematicsModel
v51__001m = v49__001j+v50__001k

# op _001t_linear_combination_eval
# LANG: _001r, _001s --> _001u
# SHAPES: (71, 40, 4, 1), (71, 40, 4, 1) --> (71, 40, 4, 1)
# full namespace: EelKinematicsModel
v55__001u = v53__001r+v54__001s

# op _002D_linear_combination_eval
# LANG: _002C --> _002E
# SHAPES: (71,) --> (71,)
# full namespace: EelKinematicsModel.FishTurnCCModel
v94__002E = _002D_constant+-1*v93__002C

# op _002J_power_combination_eval
# LANG: _0024, _002I --> _002K
# SHAPES: (71,), (71,) --> (71,)
# full namespace: EelKinematicsModel.FishTurnCCModel
v97__002K = (v76__0024)*(v96__002I)
v97__002K = v97__002K.reshape((71,))

# op _002X_power_combination_eval
# LANG: _002S, _002W --> x
# SHAPES: (71, 41), (71, 41) --> (71, 41)
# full namespace: EelKinematicsModel.FishTurnCCModel
v104_x = (v101__002S)*(v103__002W)
v104_x = v104_x.reshape((71, 41))

# op _002j_cos_eval
# LANG: theta_profile --> _002k
# SHAPES: (71,) --> (71,)
# full namespace: EelKinematicsModel.FishTurnCCModel
v84__002k = np.cos(v67_theta_profile)

# op _002p_sin_eval
# LANG: theta_profile --> _002q
# SHAPES: (71,) --> (71,)
# full namespace: EelKinematicsModel.FishTurnCCModel
v87__002q = np.sin(v67_theta_profile)

# op _002v_power_combination_eval
# LANG: _0024, _002u --> _002w
# SHAPES: (71,), (71,) --> (71,)
# full namespace: EelKinematicsModel.FishTurnCCModel
v90__002w = (v76__0024)*(v89__002u)
v90__002w = v90__002w.reshape((71,))

# op _0032_power_combination_eval
# LANG: _002S, _0031 --> y
# SHAPES: (71, 41), (71, 41) --> (71, 41)
# full namespace: EelKinematicsModel.FishTurnCCModel
v107_y = (v101__002S)*(v106__0031)
v107_y = v107_y.reshape((71, 41))

# op _0010 expand_array_eval
# LANG: x --> _0011
# SHAPES: (71, 41) --> (71, 41, 5, 1)
# full namespace: EelKinematicsModel
v39__0011 = np.einsum('ab,cd->abcd', v104_x.reshape((71, 41)) ,np.ones((5, 1))).reshape((71, 41, 5, 1))

# op _0012 expand_array_eval
# LANG: y --> _0013
# SHAPES: (71, 41) --> (71, 41, 5, 1)
# full namespace: EelKinematicsModel
v40__0013 = np.einsum('ab,cd->abcd', v107_y.reshape((71, 41)) ,np.ones((5, 1))).reshape((71, 41, 5, 1))

# op _001f_decompose_eval
# LANG: _001c --> _001g
# SHAPES: (71, 41, 5, 3) --> (71, 41, 5, 1)
# full namespace: EelKinematicsModel
v47__001g = ((v45__001c.flatten())[src_indices__001g__001f]).reshape((71, 41, 5, 1))

# op _001n_power_combination_eval
# LANG: _001m --> _001o
# SHAPES: (71, 40, 4, 1) --> (71, 40, 4, 1)
# full namespace: EelKinematicsModel
v52__001o = (v51__001m)
v52__001o = (v52__001o*_001n_coeff).reshape((71, 40, 4, 1))

# op _001v_power_combination_eval
# LANG: _001u --> _001w
# SHAPES: (71, 40, 4, 1) --> (71, 40, 4, 1)
# full namespace: EelKinematicsModel
v56__001w = (v55__001u)
v56__001w = (v56__001w*_001v_coeff).reshape((71, 40, 4, 1))

# op _002F_power_combination_eval
# LANG: _002e, _002E --> _002G
# SHAPES: (71,), (71,) --> (71,)
# full namespace: EelKinematicsModel.FishTurnCCModel
v95__002G = (v81__002e)*(v94__002E)
v95__002G = v95__002G.reshape((71,))

# op _002L_power_combination_eval
# LANG: theta_dot, _002K --> _002M
# SHAPES: (71,), (71,) --> (71,)
# full namespace: EelKinematicsModel.FishTurnCCModel
v98__002M = (v97__002K)*(v74_theta_dot)
v98__002M = v98__002M.reshape((71,))

# op _002f_sin_eval
# LANG: theta_profile --> _002g
# SHAPES: (71,) --> (71,)
# full namespace: EelKinematicsModel.FishTurnCCModel
v82__002g = np.sin(v67_theta_profile)

# op _002l_linear_combination_eval
# LANG: _002k --> _002m
# SHAPES: (71,) --> (71,)
# full namespace: EelKinematicsModel.FishTurnCCModel
v85__002m = _002l_constant+-1*v84__002k

# op _002r_power_combination_eval
# LANG: _002e, _002q --> _002s
# SHAPES: (71,), (71,) --> (71,)
# full namespace: EelKinematicsModel.FishTurnCCModel
v88__002s = (v81__002e)*(v87__002q)
v88__002s = v88__002s.reshape((71,))

# op _002x_power_combination_eval
# LANG: theta_dot, _002w --> _002y
# SHAPES: (71,), (71,) --> (71,)
# full namespace: EelKinematicsModel.FishTurnCCModel
v91__002y = (v90__002w)*(v74_theta_dot)
v91__002y = v91__002y.reshape((71,))

# op _001e_indexed_passthrough_eval
# LANG: _0011, _0013, _001g --> eel
# SHAPES: (71, 41, 5, 1), (71, 41, 5, 1), (71, 41, 5, 1) --> (71, 41, 5, 3)
# full namespace: EelKinematicsModel
v46_eel__temp[i_v39__0011__001e_indexed_passthrough_eval] = v39__0011.flatten()
v46_eel = v46_eel__temp.copy()
v46_eel__temp[i_v40__0013__001e_indexed_passthrough_eval] = v40__0013.flatten()
v46_eel = v46_eel__temp.copy()
v46_eel__temp[i_v47__001g__001e_indexed_passthrough_eval] = v47__001g.flatten()
v46_eel = v46_eel__temp.copy()

# op _001p_indexed_passthrough_eval
# LANG: _001o, _001w --> eel_coll_vel
# SHAPES: (71, 40, 4, 1), (71, 40, 4, 1) --> (71, 40, 4, 3)
# full namespace: EelKinematicsModel
v48_eel_coll_vel__temp[i_v52__001o__001p_indexed_passthrough_eval] = v52__001o.flatten()
v48_eel_coll_vel = v48_eel_coll_vel__temp.copy()
v48_eel_coll_vel__temp[i_v56__001w__001p_indexed_passthrough_eval] = v56__001w.flatten()
v48_eel_coll_vel = v48_eel_coll_vel__temp.copy()

# op _002N_linear_combination_eval
# LANG: _002G, _002M --> y_dot_tip
# SHAPES: (71,), (71,) --> (71,)
# full namespace: EelKinematicsModel.FishTurnCCModel
v99_y_dot_tip = v95__002G+v98__002M

# op _002h_power_combination_eval
# LANG: _0024, _002g --> x_tip
# SHAPES: (71,), (71,) --> (71,)
# full namespace: EelKinematicsModel.FishTurnCCModel
v83_x_tip = (v76__0024)*(v82__002g)
v83_x_tip = v83_x_tip.reshape((71,))

# op _002n_power_combination_eval
# LANG: _0024, _002m --> y_tip
# SHAPES: (71,), (71,) --> (71,)
# full namespace: EelKinematicsModel.FishTurnCCModel
v86_y_tip = (v76__0024)*(v85__002m)
v86_y_tip = v86_y_tip.reshape((71,))

# op _002z_linear_combination_eval
# LANG: _002s, _002y --> x_dot_tip
# SHAPES: (71,), (71,) --> (71,)
# full namespace: EelKinematicsModel.FishTurnCCModel
v92_x_dot_tip = v88__002s+v91__002y