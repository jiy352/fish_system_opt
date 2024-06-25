

# RUN_MODEL_ode_system

# system evaluation block

# op _004G_linear_combination_eval
# LANG: u --> _004H
# SHAPES: (1, 1) --> (1, 1)
# full namespace: adapter_comp
v180__004H = -1*v156_u

# op _004J_linear_combination_eval
# LANG: w --> _004K
# SHAPES: (1, 1) --> (1, 1)
# full namespace: adapter_comp
v181__004K = -1*v192_w

# op _004I_indexed_passthrough_eval
# LANG: _004H, _004K --> frame_vel
# SHAPES: (1, 1), (1, 1) --> (1, 3)
# full namespace: adapter_comp
v621_frame_vel__temp[i_v180__004H__004I_indexed_passthrough_eval] = v180__004H.flatten()
v621_frame_vel = v621_frame_vel__temp.copy()
v621_frame_vel__temp[i_v181__004K__004I_indexed_passthrough_eval] = v181__004K.flatten()
v621_frame_vel = v621_frame_vel__temp.copy()

# op _0052_decompose_eval
# LANG: frame_vel --> _0057, _0053
# SHAPES: (1, 3) --> (1, 1), (1, 1)
# full namespace: MeshPreprocessing_comp
v194__0053 = ((v621_frame_vel.flatten())[src_indices__0053__0052]).reshape((1, 1))
v196__0057 = ((v621_frame_vel.flatten())[src_indices__0057__0052]).reshape((1, 1))

# op _0054_linear_combination_eval
# LANG: _0053 --> _0055
# SHAPES: (1, 1) --> (1, 1)
# full namespace: MeshPreprocessing_comp
v195__0055 = -1*v194__0053

# op _0058_linear_combination_eval
# LANG: _0057 --> _0059
# SHAPES: (1, 1) --> (1, 1)
# full namespace: MeshPreprocessing_comp
v197__0059 = -1*v196__0057

# op _004Q_decompose_eval
# LANG: eel --> _005q, _004R, _004U, _005g, _005j, _005k, _005p, _005I, _005J, _006e, _006h, _006m
# SHAPES: (1, 51, 5, 3) --> (1, 50, 4, 3), (1, 50, 5, 3), (1, 50, 5, 3), (1, 1, 5, 3), (1, 50, 4, 3), (1, 50, 4, 3), (1, 50, 4, 3), (1, 51, 4, 3), (1, 51, 4, 3), (1, 50, 4, 3), (1, 50, 4, 3), (1, 50, 4, 3)
# full namespace: MeshPreprocessing_comp
v186__004R = ((v309_eel.flatten())[src_indices__004R__004Q]).reshape((1, 50, 5, 3))
v188__004U = ((v309_eel.flatten())[src_indices__004U__004Q]).reshape((1, 50, 5, 3))
v201__005g = ((v309_eel.flatten())[src_indices__005g__004Q]).reshape((1, 1, 5, 3))
v203__005j = ((v309_eel.flatten())[src_indices__005j__004Q]).reshape((1, 50, 4, 3))
v204__005k = ((v309_eel.flatten())[src_indices__005k__004Q]).reshape((1, 50, 4, 3))
v207__005p = ((v309_eel.flatten())[src_indices__005p__004Q]).reshape((1, 50, 4, 3))
v208__005q = ((v309_eel.flatten())[src_indices__005q__004Q]).reshape((1, 50, 4, 3))
v218__005I = ((v309_eel.flatten())[src_indices__005I__004Q]).reshape((1, 51, 4, 3))
v219__005J = ((v309_eel.flatten())[src_indices__005J__004Q]).reshape((1, 51, 4, 3))
v238__006e = ((v309_eel.flatten())[src_indices__006e__004Q]).reshape((1, 50, 4, 3))
v240__006h = ((v309_eel.flatten())[src_indices__006h__004Q]).reshape((1, 50, 4, 3))
v243__006m = ((v309_eel.flatten())[src_indices__006m__004Q]).reshape((1, 50, 4, 3))

# op _0056_indexed_passthrough_eval
# LANG: _0055, _0059, w --> fs
# SHAPES: (1, 1), (1, 1), (1, 1) --> (1, 3)
# full namespace: MeshPreprocessing_comp
v193_fs__temp[i_v195__0055__0056_indexed_passthrough_eval] = v195__0055.flatten()
v193_fs = v193_fs__temp.copy()
v193_fs__temp[i_v197__0059__0056_indexed_passthrough_eval] = v197__0059.flatten()
v193_fs = v193_fs__temp.copy()
v193_fs__temp[i_v192_w__0056_indexed_passthrough_eval] = v192_w.flatten()
v193_fs = v193_fs__temp.copy()

# op _007B_decompose_eval
# LANG: eel_wake_coords --> _007C
# SHAPES: (1, 69, 5, 3) --> (1, 1, 5, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group
v287__007C = ((v285_eel_wake_coords.flatten())[src_indices__007C__007B]).reshape((1, 1, 5, 3))

# op _005a_power_combination_eval
# LANG: fs --> _005b
# SHAPES: (1, 3) --> (1, 3)
# full namespace: MeshPreprocessing_comp
v198__005b = (v193_fs)
v198__005b = (v198__005b*_005a_coeff).reshape((1, 3))

# op _005l_linear_combination_eval
# LANG: _005j, _005k --> _005m
# SHAPES: (1, 50, 4, 3), (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: MeshPreprocessing_comp
v205__005m = v203__005j+v204__005k

# op _005r_linear_combination_eval
# LANG: _005q, _005p --> _005s
# SHAPES: (1, 50, 4, 3), (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: MeshPreprocessing_comp
v209__005s = v207__005p+v208__005q

# op _007D_power_combination_eval
# LANG: _007C --> _007E
# SHAPES: (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group
v288__007E = (v287__007C)
v288__007E = v288__007E.reshape((1, 1, 5, 3))

# op _005c_power_combination_eval
# LANG: _005b --> _005d
# SHAPES: (1, 3) --> (1, 3)
# full namespace: MeshPreprocessing_comp
v199__005d = (v198__005b)
v199__005d = (v199__005d*_005c_coeff).reshape((1, 3))

# op _005n_power_combination_eval
# LANG: _005m --> _005o
# SHAPES: (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: MeshPreprocessing_comp
v206__005o = (v205__005m)
v206__005o = (v206__005o*_005n_coeff).reshape((1, 50, 4, 3))

# op _005t_power_combination_eval
# LANG: _005s --> _005u
# SHAPES: (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: MeshPreprocessing_comp
v210__005u = (v209__005s)
v210__005u = (v210__005u*_005t_coeff).reshape((1, 50, 4, 3))

# op _007A_indexed_passthrough_eval
# LANG: _007E, eel_wake_coords --> eel_TE_wake_coords
# SHAPES: (1, 1, 5, 3), (1, 69, 5, 3) --> (1, 70, 5, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group
v333_eel_TE_wake_coords__temp[i_v285_eel_wake_coords__007A_indexed_passthrough_eval] = v285_eel_wake_coords.flatten()
v333_eel_TE_wake_coords = v333_eel_TE_wake_coords__temp.copy()
v333_eel_TE_wake_coords__temp[i_v288__007E__007A_indexed_passthrough_eval] = v288__007E.flatten()
v333_eel_TE_wake_coords = v333_eel_TE_wake_coords__temp.copy()

# op _004S_power_combination_eval
# LANG: _004R --> _004T
# SHAPES: (1, 50, 5, 3) --> (1, 50, 5, 3)
# full namespace: MeshPreprocessing_comp
v187__004T = (v186__004R)
v187__004T = (v187__004T*_004S_coeff).reshape((1, 50, 5, 3))

# op _004V_power_combination_eval
# LANG: _004U --> _004W
# SHAPES: (1, 50, 5, 3) --> (1, 50, 5, 3)
# full namespace: MeshPreprocessing_comp
v189__004W = (v188__004U)
v189__004W = (v189__004W*_004V_coeff).reshape((1, 50, 5, 3))

# op _005e expand_array_eval
# LANG: _005d --> _005f
# SHAPES: (1, 3) --> (1, 1, 5, 3)
# full namespace: MeshPreprocessing_comp
v200__005f = np.einsum('ad,bc->abcd', v199__005d.reshape((1, 3)) ,np.ones((1, 5))).reshape((1, 1, 5, 3))

# op _005v_linear_combination_eval
# LANG: _005o, _005u --> eel_coll_pts_coords
# SHAPES: (1, 50, 4, 3), (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: MeshPreprocessing_comp
v511_eel_coll_pts_coords = v206__005o+v210__005u

# op _008R_decompose_eval
# LANG: eel_TE_wake_coords --> _008S, _008T, _008U, _008V
# SHAPES: (1, 70, 5, 3) --> (1, 69, 4, 3), (1, 69, 4, 3), (1, 69, 4, 3), (1, 69, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v334__008S = ((v333_eel_TE_wake_coords.flatten())[src_indices__008S__008R]).reshape((1, 69, 4, 3))
v335__008T = ((v333_eel_TE_wake_coords.flatten())[src_indices__008T__008R]).reshape((1, 69, 4, 3))
v336__008U = ((v333_eel_TE_wake_coords.flatten())[src_indices__008U__008R]).reshape((1, 69, 4, 3))
v337__008V = ((v333_eel_TE_wake_coords.flatten())[src_indices__008V__008R]).reshape((1, 69, 4, 3))

# op _004X_linear_combination_eval
# LANG: _004T, _004W --> _004Y
# SHAPES: (1, 50, 5, 3), (1, 50, 5, 3) --> (1, 50, 5, 3)
# full namespace: MeshPreprocessing_comp
v190__004Y = v187__004T+v189__004W

# op _005h_linear_combination_eval
# LANG: _005g, _005f --> _005i
# SHAPES: (1, 1, 5, 3), (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: MeshPreprocessing_comp
v202__005i = v201__005g+v200__005f

# op _008W reshape_eval
# LANG: eel_coll_pts_coords --> _008X
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v338__008X = v511_eel_coll_pts_coords.reshape((1, 200, 3))

# op _0091 reshape_eval
# LANG: _008S --> _0092
# SHAPES: (1, 69, 4, 3) --> (1, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v341__0092 = v334__008S.reshape((1, 276, 3))

# op _009F reshape_eval
# LANG: _008U --> _009G
# SHAPES: (1, 69, 4, 3) --> (1, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v361__009G = v336__008U.reshape((1, 276, 3))

# op _009f reshape_eval
# LANG: eel_coll_pts_coords --> _009g
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v348__009g = v511_eel_coll_pts_coords.reshape((1, 200, 3))

# op _009l reshape_eval
# LANG: _008T --> _009m
# SHAPES: (1, 69, 4, 3) --> (1, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v351__009m = v335__008T.reshape((1, 276, 3))

# op _009z reshape_eval
# LANG: eel_coll_pts_coords --> _009A
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v358__009A = v511_eel_coll_pts_coords.reshape((1, 200, 3))

# op _004Z_indexed_passthrough_eval
# LANG: _004Y, _005i --> eel_bd_vtx_coords
# SHAPES: (1, 50, 5, 3), (1, 1, 5, 3) --> (1, 51, 5, 3)
# full namespace: MeshPreprocessing_comp
v512_eel_bd_vtx_coords__temp[i_v190__004Y__004Z_indexed_passthrough_eval] = v190__004Y.flatten()
v512_eel_bd_vtx_coords = v512_eel_bd_vtx_coords__temp.copy()
v512_eel_bd_vtx_coords__temp[i_v202__005i__004Z_indexed_passthrough_eval] = v202__005i.flatten()
v512_eel_bd_vtx_coords = v512_eel_bd_vtx_coords__temp.copy()

# op _008Y expand_array_eval
# LANG: _008X --> _008Z
# SHAPES: (1, 200, 3) --> (1, 200, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v339__008Z = np.einsum('abd,c->abcd', v338__008X.reshape((1, 200, 3)) ,np.ones((276,))).reshape((1, 200, 276, 3))

# op _0093 expand_array_eval
# LANG: _0092 --> _0094
# SHAPES: (1, 276, 3) --> (1, 200, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v342__0094 = np.einsum('acd,b->abcd', v341__0092.reshape((1, 276, 3)) ,np.ones((200,))).reshape((1, 200, 276, 3))

# op _009B expand_array_eval
# LANG: _009A --> _009C
# SHAPES: (1, 200, 3) --> (1, 200, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v359__009C = np.einsum('abd,c->abcd', v358__009A.reshape((1, 200, 3)) ,np.ones((276,))).reshape((1, 200, 276, 3))

# op _009H expand_array_eval
# LANG: _009G --> _009I
# SHAPES: (1, 276, 3) --> (1, 200, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v362__009I = np.einsum('acd,b->abcd', v361__009G.reshape((1, 276, 3)) ,np.ones((200,))).reshape((1, 200, 276, 3))

# op _009T reshape_eval
# LANG: eel_coll_pts_coords --> _009U
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v368__009U = v511_eel_coll_pts_coords.reshape((1, 200, 3))

# op _009Z reshape_eval
# LANG: _008V --> _009_
# SHAPES: (1, 69, 4, 3) --> (1, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v371__009_ = v337__008V.reshape((1, 276, 3))

# op _009h expand_array_eval
# LANG: _009g --> _009i
# SHAPES: (1, 200, 3) --> (1, 200, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v349__009i = np.einsum('abd,c->abcd', v348__009g.reshape((1, 200, 3)) ,np.ones((276,))).reshape((1, 200, 276, 3))

# op _009n expand_array_eval
# LANG: _009m --> _009o
# SHAPES: (1, 276, 3) --> (1, 200, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v352__009o = np.einsum('acd,b->abcd', v351__009m.reshape((1, 276, 3)) ,np.ones((200,))).reshape((1, 200, 276, 3))

# op _008_ reshape_eval
# LANG: _008Z --> _0090
# SHAPES: (1, 200, 276, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v340__0090 = v339__008Z.reshape((1, 55200, 3))

# op _0095 reshape_eval
# LANG: _0094 --> _0096
# SHAPES: (1, 200, 276, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v343__0096 = v342__0094.reshape((1, 55200, 3))

# op _009D reshape_eval
# LANG: _009C --> _009E
# SHAPES: (1, 200, 276, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v360__009E = v359__009C.reshape((1, 55200, 3))

# op _009J reshape_eval
# LANG: _009I --> _009K
# SHAPES: (1, 200, 276, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v363__009K = v362__009I.reshape((1, 55200, 3))

# op _009V expand_array_eval
# LANG: _009U --> _009W
# SHAPES: (1, 200, 3) --> (1, 200, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v369__009W = np.einsum('abd,c->abcd', v368__009U.reshape((1, 200, 3)) ,np.ones((276,))).reshape((1, 200, 276, 3))

# op _009j reshape_eval
# LANG: _009i --> _009k
# SHAPES: (1, 200, 276, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v350__009k = v349__009i.reshape((1, 55200, 3))

# op _009p reshape_eval
# LANG: _009o --> _009q
# SHAPES: (1, 200, 276, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v353__009q = v352__009o.reshape((1, 55200, 3))

# op _00a0 expand_array_eval
# LANG: _009_ --> _00a1
# SHAPES: (1, 276, 3) --> (1, 200, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v372__00a1 = np.einsum('acd,b->abcd', v371__009_.reshape((1, 276, 3)) ,np.ones((200,))).reshape((1, 200, 276, 3))

# op _00eo_decompose_eval
# LANG: eel_bd_vtx_coords --> _00ep, _00eq, _00er, _00es
# SHAPES: (1, 51, 5, 3) --> (1, 50, 4, 3), (1, 50, 4, 3), (1, 50, 4, 3), (1, 50, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v513__00ep = ((v512_eel_bd_vtx_coords.flatten())[src_indices__00ep__00eo]).reshape((1, 50, 4, 3))
v514__00eq = ((v512_eel_bd_vtx_coords.flatten())[src_indices__00eq__00eo]).reshape((1, 50, 4, 3))
v515__00er = ((v512_eel_bd_vtx_coords.flatten())[src_indices__00er__00eo]).reshape((1, 50, 4, 3))
v516__00es = ((v512_eel_bd_vtx_coords.flatten())[src_indices__00es__00eo]).reshape((1, 50, 4, 3))

# op _0097_linear_combination_eval
# LANG: _0090, _0096 --> _0098
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v344__0098 = v340__0090+-1*v343__0096

# op _009L_linear_combination_eval
# LANG: _009E, _009K --> _009M
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v364__009M = v360__009E+-1*v363__009K

# op _009X reshape_eval
# LANG: _009W --> _009Y
# SHAPES: (1, 200, 276, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v370__009Y = v369__009W.reshape((1, 55200, 3))

# op _009r_linear_combination_eval
# LANG: _009k, _009q --> _009s
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v354__009s = v350__009k+-1*v353__009q

# op _00a2 reshape_eval
# LANG: _00a1 --> _00a3
# SHAPES: (1, 200, 276, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v373__00a3 = v372__00a1.reshape((1, 55200, 3))

# op _00eN reshape_eval
# LANG: eel_coll_pts_coords --> _00eO
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v527__00eO = v511_eel_coll_pts_coords.reshape((1, 200, 3))

# op _00eT reshape_eval
# LANG: _00eq --> _00eU
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v530__00eU = v514__00eq.reshape((1, 200, 3))

# op _00et reshape_eval
# LANG: eel_coll_pts_coords --> _00eu
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v517__00eu = v511_eel_coll_pts_coords.reshape((1, 200, 3))

# op _00ez reshape_eval
# LANG: _00ep --> _00eA
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v520__00eA = v513__00ep.reshape((1, 200, 3))

# op _00f6 reshape_eval
# LANG: eel_coll_pts_coords --> _00f7
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v537__00f7 = v511_eel_coll_pts_coords.reshape((1, 200, 3))

# op _00fc reshape_eval
# LANG: _00er --> _00fd
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v540__00fd = v515__00er.reshape((1, 200, 3))

# op _0099_power_combination_eval
# LANG: _0098 --> _009a
# SHAPES: (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v345__009a = (v344__0098**2)
v345__009a = v345__009a.reshape((1, 55200, 3))

# op _009N_power_combination_eval
# LANG: _009M --> _009O
# SHAPES: (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v365__009O = (v364__009M**2)
v365__009O = v365__009O.reshape((1, 55200, 3))

# op _009t_power_combination_eval
# LANG: _009s --> _009u
# SHAPES: (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v355__009u = (v354__009s**2)
v355__009u = v355__009u.reshape((1, 55200, 3))

# op _00a4_linear_combination_eval
# LANG: _009Y, _00a3 --> _00a5
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v374__00a5 = v370__009Y+-1*v373__00a3

# op _00eB expand_array_eval
# LANG: _00eA --> _00eC
# SHAPES: (1, 200, 3) --> (1, 200, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v521__00eC = np.einsum('acd,b->abcd', v520__00eA.reshape((1, 200, 3)) ,np.ones((200,))).reshape((1, 200, 200, 3))

# op _00eP expand_array_eval
# LANG: _00eO --> _00eQ
# SHAPES: (1, 200, 3) --> (1, 200, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v528__00eQ = np.einsum('abd,c->abcd', v527__00eO.reshape((1, 200, 3)) ,np.ones((200,))).reshape((1, 200, 200, 3))

# op _00eV expand_array_eval
# LANG: _00eU --> _00eW
# SHAPES: (1, 200, 3) --> (1, 200, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v531__00eW = np.einsum('acd,b->abcd', v530__00eU.reshape((1, 200, 3)) ,np.ones((200,))).reshape((1, 200, 200, 3))

# op _00ev expand_array_eval
# LANG: _00eu --> _00ew
# SHAPES: (1, 200, 3) --> (1, 200, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v518__00ew = np.einsum('abd,c->abcd', v517__00eu.reshape((1, 200, 3)) ,np.ones((200,))).reshape((1, 200, 200, 3))

# op _00f8 expand_array_eval
# LANG: _00f7 --> _00f9
# SHAPES: (1, 200, 3) --> (1, 200, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v538__00f9 = np.einsum('abd,c->abcd', v537__00f7.reshape((1, 200, 3)) ,np.ones((200,))).reshape((1, 200, 200, 3))

# op _00fe expand_array_eval
# LANG: _00fd --> _00ff
# SHAPES: (1, 200, 3) --> (1, 200, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v541__00ff = np.einsum('acd,b->abcd', v540__00fd.reshape((1, 200, 3)) ,np.ones((200,))).reshape((1, 200, 200, 3))

# op _00fq reshape_eval
# LANG: eel_coll_pts_coords --> _00fr
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v547__00fr = v511_eel_coll_pts_coords.reshape((1, 200, 3))

# op _00fw reshape_eval
# LANG: _00es --> _00fx
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v550__00fx = v516__00es.reshape((1, 200, 3))

# op _009P_single_tensor_sum_with_axis_eval
# LANG: _009O --> _009Q
# SHAPES: (1, 55200, 3) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v366__009Q = np.sum(v365__009O, axis = (2,)).reshape((1, 55200))

# op _009b_single_tensor_sum_with_axis_eval
# LANG: _009a --> _009c
# SHAPES: (1, 55200, 3) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v346__009c = np.sum(v345__009a, axis = (2,)).reshape((1, 55200))

# op _009v_single_tensor_sum_with_axis_eval
# LANG: _009u --> _009w
# SHAPES: (1, 55200, 3) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v356__009w = np.sum(v355__009u, axis = (2,)).reshape((1, 55200))

# op _00a6_power_combination_eval
# LANG: _00a5 --> _00a7
# SHAPES: (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v375__00a7 = (v374__00a5**2)
v375__00a7 = v375__00a7.reshape((1, 55200, 3))

# op _00eD reshape_eval
# LANG: _00eC --> _00eE
# SHAPES: (1, 200, 200, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v522__00eE = v521__00eC.reshape((1, 40000, 3))

# op _00eR reshape_eval
# LANG: _00eQ --> _00eS
# SHAPES: (1, 200, 200, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v529__00eS = v528__00eQ.reshape((1, 40000, 3))

# op _00eX reshape_eval
# LANG: _00eW --> _00eY
# SHAPES: (1, 200, 200, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v532__00eY = v531__00eW.reshape((1, 40000, 3))

# op _00ex reshape_eval
# LANG: _00ew --> _00ey
# SHAPES: (1, 200, 200, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v519__00ey = v518__00ew.reshape((1, 40000, 3))

# op _00fa reshape_eval
# LANG: _00f9 --> _00fb
# SHAPES: (1, 200, 200, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v539__00fb = v538__00f9.reshape((1, 40000, 3))

# op _00fg reshape_eval
# LANG: _00ff --> _00fh
# SHAPES: (1, 200, 200, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v542__00fh = v541__00ff.reshape((1, 40000, 3))

# op _00fs expand_array_eval
# LANG: _00fr --> _00ft
# SHAPES: (1, 200, 3) --> (1, 200, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v548__00ft = np.einsum('abd,c->abcd', v547__00fr.reshape((1, 200, 3)) ,np.ones((200,))).reshape((1, 200, 200, 3))

# op _00fy expand_array_eval
# LANG: _00fx --> _00fz
# SHAPES: (1, 200, 3) --> (1, 200, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v551__00fz = np.einsum('acd,b->abcd', v550__00fx.reshape((1, 200, 3)) ,np.ones((200,))).reshape((1, 200, 200, 3))

# op _009R_power_combination_eval
# LANG: _009Q --> _009S
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v367__009S = (v366__009Q**0.5)
v367__009S = v367__009S.reshape((1, 55200))

# op _009d_power_combination_eval
# LANG: _009c --> _009e
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v347__009e = (v346__009c**0.5)
v347__009e = v347__009e.reshape((1, 55200))

# op _009x_power_combination_eval
# LANG: _009w --> _009y
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v357__009y = (v356__009w**0.5)
v357__009y = v357__009y.reshape((1, 55200))

# op _00a8_single_tensor_sum_with_axis_eval
# LANG: _00a7 --> _00a9
# SHAPES: (1, 55200, 3) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v376__00a9 = np.sum(v375__00a7, axis = (2,)).reshape((1, 55200))

# op _00eF_linear_combination_eval
# LANG: _00ey, _00eE --> _00eG
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v523__00eG = v519__00ey+-1*v522__00eE

# op _00eZ_linear_combination_eval
# LANG: _00eS, _00eY --> _00e_
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v533__00e_ = v529__00eS+-1*v532__00eY

# op _00fA reshape_eval
# LANG: _00fz --> _00fB
# SHAPES: (1, 200, 200, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v552__00fB = v551__00fz.reshape((1, 40000, 3))

# op _00fi_linear_combination_eval
# LANG: _00fb, _00fh --> _00fj
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v543__00fj = v539__00fb+-1*v542__00fh

# op _00fu reshape_eval
# LANG: _00ft --> _00fv
# SHAPES: (1, 200, 200, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v549__00fv = v548__00ft.reshape((1, 40000, 3))

# op _00aS_power_combination_eval
# LANG: _009e --> _00aT
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v399__00aT = (v347__009e)
v399__00aT = (v399__00aT*_00aS_coeff).reshape((1, 55200))

# op _00aa_power_combination_eval
# LANG: _00a9 --> _00ab
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v377__00ab = (v376__00a9**0.5)
v377__00ab = v377__00ab.reshape((1, 55200))

# op _00ag_power_combination_eval
# LANG: _0098, _009s --> _00ah
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v380__00ah = (v344__0098)*(v354__009s)
v380__00ah = v380__00ah.reshape((1, 55200, 3))

# op _00ak_power_combination_eval
# LANG: _009e --> _00al
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v382__00al = (v347__009e**2)
v382__00al = v382__00al.reshape((1, 55200))

# op _00am_power_combination_eval
# LANG: _009y --> _00an
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v383__00an = (v357__009y**2)
v383__00an = v383__00an.reshape((1, 55200))

# op _00bP_power_combination_eval
# LANG: _009y --> _00bQ
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v429__00bQ = (v357__009y)
v429__00bQ = (v429__00bQ*_00bP_coeff).reshape((1, 55200))

# op _00bd_power_combination_eval
# LANG: _009M, _009s --> _00be
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v410__00be = (v354__009s)*(v364__009M)
v410__00be = v410__00be.reshape((1, 55200, 3))

# op _00bh_power_combination_eval
# LANG: _009y --> _00bi
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v412__00bi = (v357__009y**2)
v412__00bi = v412__00bi.reshape((1, 55200))

# op _00bj_power_combination_eval
# LANG: _009S --> _00bk
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v413__00bk = (v367__009S**2)
v413__00bk = v413__00bk.reshape((1, 55200))

# op _00eH_power_combination_eval
# LANG: _00eG --> _00eI
# SHAPES: (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v524__00eI = (v523__00eG**2)
v524__00eI = v524__00eI.reshape((1, 40000, 3))

# op _00f0_power_combination_eval
# LANG: _00e_ --> _00f1
# SHAPES: (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v534__00f1 = (v533__00e_**2)
v534__00f1 = v534__00f1.reshape((1, 40000, 3))

# op _00fC_linear_combination_eval
# LANG: _00fv, _00fB --> _00fD
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v553__00fD = v549__00fv+-1*v552__00fB

# op _00fk_power_combination_eval
# LANG: _00fj --> _00fl
# SHAPES: (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v544__00fl = (v543__00fj**2)
v544__00fl = v544__00fl.reshape((1, 40000, 3))

# op _00aA_linear_combination_eval
# LANG: _00an --> _00aB
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v390__00aB = _00aA_constant+v383__00an

# op _00aQ_linear_combination_eval
# LANG: _00al, _00an --> _00aR
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v398__00aR = v382__00al+v383__00an

# op _00aU_power_combination_eval
# LANG: _009y, _00aT --> _00aV
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v400__00aV = (v399__00aT)*(v357__009y)
v400__00aV = v400__00aV.reshape((1, 55200))

# op _00ai_single_tensor_sum_with_axis_eval
# LANG: _00ah --> _00aj
# SHAPES: (1, 55200, 3) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v381__00aj = np.sum(v380__00ah, axis = (2,)).reshape((1, 55200))

# op _00aq_linear_combination_eval
# LANG: _00al --> _00ar
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v385__00ar = _00aq_constant+v382__00al

# op _00bN_linear_combination_eval
# LANG: _00bi, _00bk --> _00bO
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v428__00bO = v412__00bi+v413__00bk

# op _00bR_power_combination_eval
# LANG: _009S, _00bQ --> _00bS
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v430__00bS = (v429__00bQ)*(v367__009S)
v430__00bS = v430__00bS.reshape((1, 55200))

# op _00bf_single_tensor_sum_with_axis_eval
# LANG: _00be --> _00bg
# SHAPES: (1, 55200, 3) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v411__00bg = np.sum(v410__00be, axis = (2,)).reshape((1, 55200))

# op _00bn_linear_combination_eval
# LANG: _00bi --> _00bo
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v415__00bo = _00bn_constant+v412__00bi

# op _00bx_linear_combination_eval
# LANG: _00bk --> _00by
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v420__00by = _00bx_constant+v413__00bk

# op _00cM_power_combination_eval
# LANG: _009S --> _00cN
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v459__00cN = (v367__009S)
v459__00cN = (v459__00cN*_00cM_coeff).reshape((1, 55200))

# op _00ca_power_combination_eval
# LANG: _00a5, _009M --> _00cb
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v440__00cb = (v364__009M)*(v374__00a5)
v440__00cb = v440__00cb.reshape((1, 55200, 3))

# op _00ce_power_combination_eval
# LANG: _009S --> _00cf
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v442__00cf = (v367__009S**2)
v442__00cf = v442__00cf.reshape((1, 55200))

# op _00cg_power_combination_eval
# LANG: _00ab --> _00ch
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v443__00ch = (v377__00ab**2)
v443__00ch = v443__00ch.reshape((1, 55200))

# op _00eJ_single_tensor_sum_with_axis_eval
# LANG: _00eI --> _00eK
# SHAPES: (1, 40000, 3) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v525__00eK = np.sum(v524__00eI, axis = (2,)).reshape((1, 40000))

# op _00f2_single_tensor_sum_with_axis_eval
# LANG: _00f1 --> _00f3
# SHAPES: (1, 40000, 3) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v535__00f3 = np.sum(v534__00f1, axis = (2,)).reshape((1, 40000))

# op _00fE_power_combination_eval
# LANG: _00fD --> _00fF
# SHAPES: (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v554__00fF = (v553__00fD**2)
v554__00fF = v554__00fF.reshape((1, 40000, 3))

# op _00fm_single_tensor_sum_with_axis_eval
# LANG: _00fl --> _00fn
# SHAPES: (1, 40000, 3) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v545__00fn = np.sum(v544__00fl, axis = (2,)).reshape((1, 40000))

# op _00aC_linear_combination_eval
# LANG: _00aB --> _00aD
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v391__00aD = _00aC_constant+v390__00aB

# op _00aK_power_combination_eval
# LANG: _00al, _00an --> _00aL
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v395__00aL = (v382__00al)*(v383__00an)
v395__00aL = v395__00aL.reshape((1, 55200))

# op _00aM_power_combination_eval
# LANG: _00aj --> _00aN
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v396__00aN = (v381__00aj**2)
v396__00aN = v396__00aN.reshape((1, 55200))

# op _00aW_linear_combination_eval
# LANG: _00aR, _00aV --> _00aX
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v401__00aX = v398__00aR+-1*v400__00aV

# op _00as_linear_combination_eval
# LANG: _00ar --> _00at
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v386__00at = _00as_constant+v385__00ar

# op _00bH_power_combination_eval
# LANG: _00bi, _00bk --> _00bI
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v425__00bI = (v412__00bi)*(v413__00bk)
v425__00bI = v425__00bI.reshape((1, 55200))

# op _00bJ_power_combination_eval
# LANG: _00bg --> _00bK
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v426__00bK = (v411__00bg**2)
v426__00bK = v426__00bK.reshape((1, 55200))

# op _00bT_linear_combination_eval
# LANG: _00bO, _00bS --> _00bU
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v431__00bU = v428__00bO+-1*v430__00bS

# op _00bp_linear_combination_eval
# LANG: _00bo --> _00bq
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v416__00bq = _00bp_constant+v415__00bo

# op _00bz_linear_combination_eval
# LANG: _00by --> _00bA
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v421__00bA = _00bz_constant+v420__00by

# op _00cK_linear_combination_eval
# LANG: _00cf, _00ch --> _00cL
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v458__00cL = v442__00cf+v443__00ch

# op _00cO_power_combination_eval
# LANG: _00ab, _00cN --> _00cP
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v460__00cP = (v459__00cN)*(v377__00ab)
v460__00cP = v460__00cP.reshape((1, 55200))

# op _00cc_single_tensor_sum_with_axis_eval
# LANG: _00cb --> _00cd
# SHAPES: (1, 55200, 3) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v441__00cd = np.sum(v440__00cb, axis = (2,)).reshape((1, 55200))

# op _00ck_linear_combination_eval
# LANG: _00cf --> _00cl
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v445__00cl = _00ck_constant+v442__00cf

# op _00cu_linear_combination_eval
# LANG: _00ch --> _00cv
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v450__00cv = _00cu_constant+v443__00ch

# op _00d7_power_combination_eval
# LANG: _00a5, _0098 --> _00d8
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v470__00d8 = (v374__00a5)*(v344__0098)
v470__00d8 = v470__00d8.reshape((1, 55200, 3))

# op _00dJ_power_combination_eval
# LANG: _00ab --> _00dK
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v489__00dK = (v377__00ab)
v489__00dK = (v489__00dK*_00dJ_coeff).reshape((1, 55200))

# op _00db_power_combination_eval
# LANG: _00ab --> _00dc
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v472__00dc = (v377__00ab**2)
v472__00dc = v472__00dc.reshape((1, 55200))

# op _00dd_power_combination_eval
# LANG: _009e --> _00de
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v473__00de = (v347__009e**2)
v473__00de = v473__00de.reshape((1, 55200))

# op _00eL_power_combination_eval
# LANG: _00eK --> _00eM
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v526__00eM = (v525__00eK**0.5)
v526__00eM = v526__00eM.reshape((1, 40000))

# op _00f4_power_combination_eval
# LANG: _00f3 --> _00f5
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v536__00f5 = (v535__00f3**0.5)
v536__00f5 = v536__00f5.reshape((1, 40000))

# op _00fG_single_tensor_sum_with_axis_eval
# LANG: _00fF --> _00fH
# SHAPES: (1, 40000, 3) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v555__00fH = np.sum(v554__00fF, axis = (2,)).reshape((1, 40000))

# op _00fO_power_combination_eval
# LANG: _00eG, _00e_ --> _00fP
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v559__00fP = (v523__00eG)*(v533__00e_)
v559__00fP = v559__00fP.reshape((1, 40000, 3))

# op _00fo_power_combination_eval
# LANG: _00fn --> _00fp
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v546__00fp = (v545__00fn**0.5)
v546__00fp = v546__00fp.reshape((1, 40000))

# op _00gd_power_combination_eval
# LANG: _00fj, _00e_ --> _00ge
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v572__00ge = (v533__00e_)*(v543__00fj)
v572__00ge = v572__00ge.reshape((1, 40000, 3))

# op _00aE_power_combination_eval
# LANG: _00aD --> _00aF
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v392__00aF = (v391__00aD**0.5)
v392__00aF = v392__00aF.reshape((1, 55200))

# op _00aO_linear_combination_eval
# LANG: _00aL, _00aN --> _00aP
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v397__00aP = v395__00aL+-1*v396__00aN

# op _00aY_power_combination_eval
# LANG: _00aX --> _00aZ
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v402__00aZ = (v401__00aX)
v402__00aZ = (v402__00aZ*_00aY_coeff).reshape((1, 55200))

# op _00ao_linear_combination_eval
# LANG: _00al, _00aj --> _00ap
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v384__00ap = v382__00al+-1*v381__00aj

# op _00au_power_combination_eval
# LANG: _00at --> _00av
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v387__00av = (v386__00at**0.5)
v387__00av = v387__00av.reshape((1, 55200))

# op _00ay_linear_combination_eval
# LANG: _00an, _00aj --> _00az
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v389__00az = v383__00an+-1*v381__00aj

# op _00bB_power_combination_eval
# LANG: _00bA --> _00bC
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v422__00bC = (v421__00bA**0.5)
v422__00bC = v422__00bC.reshape((1, 55200))

# op _00bL_linear_combination_eval
# LANG: _00bI, _00bK --> _00bM
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v427__00bM = v425__00bI+-1*v426__00bK

# op _00bV_power_combination_eval
# LANG: _00bU --> _00bW
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v432__00bW = (v431__00bU)
v432__00bW = (v432__00bW*_00bV_coeff).reshape((1, 55200))

# op _00bl_linear_combination_eval
# LANG: _00bi, _00bg --> _00bm
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v414__00bm = v412__00bi+-1*v411__00bg

# op _00br_power_combination_eval
# LANG: _00bq --> _00bs
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v417__00bs = (v416__00bq**0.5)
v417__00bs = v417__00bs.reshape((1, 55200))

# op _00bv_linear_combination_eval
# LANG: _00bk, _00bg --> _00bw
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v419__00bw = v413__00bk+-1*v411__00bg

# op _00cE_power_combination_eval
# LANG: _00cf, _00ch --> _00cF
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v455__00cF = (v442__00cf)*(v443__00ch)
v455__00cF = v455__00cF.reshape((1, 55200))

# op _00cG_power_combination_eval
# LANG: _00cd --> _00cH
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v456__00cH = (v441__00cd**2)
v456__00cH = v456__00cH.reshape((1, 55200))

# op _00cQ_linear_combination_eval
# LANG: _00cL, _00cP --> _00cR
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v461__00cR = v458__00cL+-1*v460__00cP

# op _00cm_linear_combination_eval
# LANG: _00cl --> _00cn
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v446__00cn = _00cm_constant+v445__00cl

# op _00cw_linear_combination_eval
# LANG: _00cv --> _00cx
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v451__00cx = _00cw_constant+v450__00cv

# op _00d9_single_tensor_sum_with_axis_eval
# LANG: _00d8 --> _00da
# SHAPES: (1, 55200, 3) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v471__00da = np.sum(v470__00d8, axis = (2,)).reshape((1, 55200))

# op _00dH_linear_combination_eval
# LANG: _00dc, _00de --> _00dI
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v488__00dI = v472__00dc+v473__00de

# op _00dL_power_combination_eval
# LANG: _00dK, _009e --> _00dM
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v490__00dM = (v489__00dK)*(v347__009e)
v490__00dM = v490__00dM.reshape((1, 55200))

# op _00dh_linear_combination_eval
# LANG: _00dc --> _00di
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v475__00di = _00dh_constant+v472__00dc

# op _00dr_linear_combination_eval
# LANG: _00de --> _00ds
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v480__00ds = _00dr_constant+v473__00de

# op _00fI_power_combination_eval
# LANG: _00fH --> _00fJ
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v556__00fJ = (v555__00fH**0.5)
v556__00fJ = v556__00fJ.reshape((1, 40000))

# op _00fQ_single_tensor_sum_with_axis_eval
# LANG: _00fP --> _00fR
# SHAPES: (1, 40000, 3) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v560__00fR = np.sum(v559__00fP, axis = (2,)).reshape((1, 40000))

# op _00fS_power_combination_eval
# LANG: _00eM, _00f5 --> _00fT
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v561__00fT = (v526__00eM)*(v536__00f5)
v561__00fT = v561__00fT.reshape((1, 40000))

# op _00gD_power_combination_eval
# LANG: _00fD, _00fj --> _00gE
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v585__00gE = (v543__00fj)*(v553__00fD)
v585__00gE = v585__00gE.reshape((1, 40000, 3))

# op _00gf_single_tensor_sum_with_axis_eval
# LANG: _00ge --> _00gg
# SHAPES: (1, 40000, 3) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v573__00gg = np.sum(v572__00ge, axis = (2,)).reshape((1, 40000))

# op _00gh_power_combination_eval
# LANG: _00fp, _00f5 --> _00gi
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v574__00gi = (v536__00f5)*(v546__00fp)
v574__00gi = v574__00gi.reshape((1, 40000))

# op _008e_decompose_eval
# LANG: eel --> _008k, _008f, _008g, _008j
# SHAPES: (1, 51, 5, 3) --> (1, 50, 4, 3), (1, 50, 4, 3), (1, 50, 4, 3), (1, 50, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal
v310__008f = ((v309_eel.flatten())[src_indices__008f__008e]).reshape((1, 50, 4, 3))
v311__008g = ((v309_eel.flatten())[src_indices__008g__008e]).reshape((1, 50, 4, 3))
v313__008j = ((v309_eel.flatten())[src_indices__008j__008e]).reshape((1, 50, 4, 3))
v314__008k = ((v309_eel.flatten())[src_indices__008k__008e]).reshape((1, 50, 4, 3))

# op _00aG_power_combination_eval
# LANG: _00az, _00aF --> _00aH
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v393__00aH = (v389__00az)*(v392__00aF**-1)
v393__00aH = v393__00aH.reshape((1, 55200))

# op _00a__linear_combination_eval
# LANG: _00aP, _00aZ --> _00b0
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v403__00b0 = v397__00aP+v402__00aZ

# op _00aw_power_combination_eval
# LANG: _00ap, _00av --> _00ax
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v388__00ax = (v384__00ap)*(v387__00av**-1)
v388__00ax = v388__00ax.reshape((1, 55200))

# op _00bD_power_combination_eval
# LANG: _00bw, _00bC --> _00bE
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v423__00bE = (v419__00bw)*(v422__00bC**-1)
v423__00bE = v423__00bE.reshape((1, 55200))

# op _00bX_linear_combination_eval
# LANG: _00bM, _00bW --> _00bY
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v433__00bY = v427__00bM+v432__00bW

# op _00bt_power_combination_eval
# LANG: _00bm, _00bs --> _00bu
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v418__00bu = (v414__00bm)*(v417__00bs**-1)
v418__00bu = v418__00bu.reshape((1, 55200))

# op _00cI_linear_combination_eval
# LANG: _00cF, _00cH --> _00cJ
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v457__00cJ = v455__00cF+-1*v456__00cH

# op _00cS_power_combination_eval
# LANG: _00cR --> _00cT
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v462__00cT = (v461__00cR)
v462__00cT = (v462__00cT*_00cS_coeff).reshape((1, 55200))

# op _00ci_linear_combination_eval
# LANG: _00cf, _00cd --> _00cj
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v444__00cj = v442__00cf+-1*v441__00cd

# op _00co_power_combination_eval
# LANG: _00cn --> _00cp
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v447__00cp = (v446__00cn**0.5)
v447__00cp = v447__00cp.reshape((1, 55200))

# op _00cs_linear_combination_eval
# LANG: _00ch, _00cd --> _00ct
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v449__00ct = v443__00ch+-1*v441__00cd

# op _00cy_power_combination_eval
# LANG: _00cx --> _00cz
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v452__00cz = (v451__00cx**0.5)
v452__00cz = v452__00cz.reshape((1, 55200))

# op _00dB_power_combination_eval
# LANG: _00dc, _00de --> _00dC
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v485__00dC = (v472__00dc)*(v473__00de)
v485__00dC = v485__00dC.reshape((1, 55200))

# op _00dD_power_combination_eval
# LANG: _00da --> _00dE
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v486__00dE = (v471__00da**2)
v486__00dE = v486__00dE.reshape((1, 55200))

# op _00dN_linear_combination_eval
# LANG: _00dI, _00dM --> _00dO
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v491__00dO = v488__00dI+-1*v490__00dM

# op _00dj_linear_combination_eval
# LANG: _00di --> _00dk
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v476__00dk = _00dj_constant+v475__00di

# op _00dt_linear_combination_eval
# LANG: _00ds --> _00du
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v481__00du = _00dt_constant+v480__00ds

# op _00fU_linear_combination_eval
# LANG: _00fT, _00fR --> _00fV
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v562__00fV = v561__00fT+v560__00fR

# op _00fY_power_combination_eval
# LANG: _00eM --> _00fZ
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v564__00fZ = (v526__00eM**-1)
v564__00fZ = v564__00fZ.reshape((1, 40000))

# op _00f__power_combination_eval
# LANG: _00f5 --> _00g0
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v565__00g0 = (v536__00f5**-1)
v565__00g0 = v565__00g0.reshape((1, 40000))

# op _00gF_single_tensor_sum_with_axis_eval
# LANG: _00gE --> _00gG
# SHAPES: (1, 40000, 3) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v586__00gG = np.sum(v585__00gE, axis = (2,)).reshape((1, 40000))

# op _00gH_power_combination_eval
# LANG: _00fJ, _00fp --> _00gI
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v587__00gI = (v546__00fp)*(v556__00fJ)
v587__00gI = v587__00gI.reshape((1, 40000))

# op _00gj_linear_combination_eval
# LANG: _00gi, _00gg --> _00gk
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v575__00gk = v574__00gi+v573__00gg

# op _00gn_power_combination_eval
# LANG: _00f5 --> _00go
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v577__00go = (v536__00f5**-1)
v577__00go = v577__00go.reshape((1, 40000))

# op _00gp_power_combination_eval
# LANG: _00fp --> _00gq
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v578__00gq = (v546__00fp**-1)
v578__00gq = v578__00gq.reshape((1, 40000))

# op _00h2_power_combination_eval
# LANG: _00fD, _00eG --> _00h3
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v598__00h3 = (v553__00fD)*(v523__00eG)
v598__00h3 = v598__00h3.reshape((1, 40000, 3))

# op _008h_linear_combination_eval
# LANG: _008f, _008g --> _008i
# SHAPES: (1, 50, 4, 3), (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal
v312__008i = v310__008f+-1*v311__008g

# op _008l_linear_combination_eval
# LANG: _008j, _008k --> _008m
# SHAPES: (1, 50, 4, 3), (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal
v315__008m = v313__008j+-1*v314__008k

# op _00aI_linear_combination_eval
# LANG: _00ax, _00aH --> _00aJ
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v394__00aJ = v388__00ax+v393__00aH

# op _00b1_linear_combination_eval
# LANG: _00b0 --> _00b2
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v404__00b2 = _00b1_constant+v403__00b0

# op _00bF_linear_combination_eval
# LANG: _00bu, _00bE --> _00bG
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v424__00bG = v418__00bu+v423__00bE

# op _00bZ_linear_combination_eval
# LANG: _00bY --> _00b_
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v434__00b_ = _00bZ_constant+v433__00bY

# op _00cA_power_combination_eval
# LANG: _00ct, _00cz --> _00cB
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v453__00cB = (v449__00ct)*(v452__00cz**-1)
v453__00cB = v453__00cB.reshape((1, 55200))

# op _00cU_linear_combination_eval
# LANG: _00cJ, _00cT --> _00cV
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v463__00cV = v457__00cJ+v462__00cT

# op _00cq_power_combination_eval
# LANG: _00cj, _00cp --> _00cr
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v448__00cr = (v444__00cj)*(v447__00cp**-1)
v448__00cr = v448__00cr.reshape((1, 55200))

# op _00dF_linear_combination_eval
# LANG: _00dC, _00dE --> _00dG
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v487__00dG = v485__00dC+-1*v486__00dE

# op _00dP_power_combination_eval
# LANG: _00dO --> _00dQ
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v492__00dQ = (v491__00dO)
v492__00dQ = (v492__00dQ*_00dP_coeff).reshape((1, 55200))

# op _00df_linear_combination_eval
# LANG: _00dc, _00da --> _00dg
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v474__00dg = v472__00dc+-1*v471__00da

# op _00dl_power_combination_eval
# LANG: _00dk --> _00dm
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v477__00dm = (v476__00dk**0.5)
v477__00dm = v477__00dm.reshape((1, 55200))

# op _00dp_linear_combination_eval
# LANG: _00de, _00da --> _00dq
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v479__00dq = v473__00de+-1*v471__00da

# op _00dv_power_combination_eval
# LANG: _00du --> _00dw
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v482__00dw = (v481__00du**0.5)
v482__00dw = v482__00dw.reshape((1, 55200))

# op _00fW_power_combination_eval
# LANG: _00fV --> _00fX
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v563__00fX = (v562__00fV**-1)
v563__00fX = v563__00fX.reshape((1, 40000))

# op _00g1_linear_combination_eval
# LANG: _00fZ, _00g0 --> _00g2
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v566__00g2 = v564__00fZ+v565__00g0

# op _00gJ_linear_combination_eval
# LANG: _00gI, _00gG --> _00gK
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v588__00gK = v587__00gI+v586__00gG

# op _00gN_power_combination_eval
# LANG: _00fp --> _00gO
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v590__00gO = (v546__00fp**-1)
v590__00gO = v590__00gO.reshape((1, 40000))

# op _00gP_power_combination_eval
# LANG: _00fJ --> _00gQ
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v591__00gQ = (v556__00fJ**-1)
v591__00gQ = v591__00gQ.reshape((1, 40000))

# op _00gl_power_combination_eval
# LANG: _00gk --> _00gm
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v576__00gm = (v575__00gk**-1)
v576__00gm = v576__00gm.reshape((1, 40000))

# op _00gr_linear_combination_eval
# LANG: _00go, _00gq --> _00gs
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v579__00gs = v577__00go+v578__00gq

# op _00h4_single_tensor_sum_with_axis_eval
# LANG: _00h3 --> _00h5
# SHAPES: (1, 40000, 3) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v599__00h5 = np.sum(v598__00h3, axis = (2,)).reshape((1, 40000))

# op _00h6_power_combination_eval
# LANG: _00eM, _00fJ --> _00h7
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v600__00h7 = (v556__00fJ)*(v526__00eM)
v600__00h7 = v600__00h7.reshape((1, 40000))

# op _008n cross_product_eval
# LANG: _008i, _008m --> _008o
# SHAPES: (1, 50, 4, 3), (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal
v316__008o = np.cross(v312__008i, v315__008m, axisa = 3, axisb = 3, axisc = 3)

# op _00ac cross_product_eval
# LANG: _0098, _009s --> _00ad
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v378__00ad = np.cross(v344__0098, v354__009s, axisa = 2, axisb = 2, axisc = 2)

# op _00b3_power_combination_eval
# LANG: _00aJ, _00b2 --> _00b4
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v405__00b4 = (v394__00aJ)*(v404__00b2**-1)
v405__00b4 = v405__00b4.reshape((1, 55200))

# op _00b9 cross_product_eval
# LANG: _009M, _009s --> _00ba
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v408__00ba = np.cross(v354__009s, v364__009M, axisa = 2, axisb = 2, axisc = 2)

# op _00c0_power_combination_eval
# LANG: _00bG, _00b_ --> _00c1
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v435__00c1 = (v424__00bG)*(v434__00b_**-1)
v435__00c1 = v435__00c1.reshape((1, 55200))

# op _00cC_linear_combination_eval
# LANG: _00cr, _00cB --> _00cD
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v454__00cD = v448__00cr+v453__00cB

# op _00cW_linear_combination_eval
# LANG: _00cV --> _00cX
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v464__00cX = _00cW_constant+v463__00cV

# op _00dR_linear_combination_eval
# LANG: _00dG, _00dQ --> _00dS
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v493__00dS = v487__00dG+v492__00dQ

# op _00dn_power_combination_eval
# LANG: _00dg, _00dm --> _00do
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v478__00do = (v474__00dg)*(v477__00dm**-1)
v478__00do = v478__00do.reshape((1, 55200))

# op _00dx_power_combination_eval
# LANG: _00dq, _00dw --> _00dy
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v483__00dy = (v479__00dq)*(v482__00dw**-1)
v483__00dy = v483__00dy.reshape((1, 55200))

# op _00fK cross_product_eval
# LANG: _00eG, _00e_ --> _00fL
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v557__00fL = np.cross(v523__00eG, v533__00e_, axisa = 2, axisb = 2, axisc = 2)

# op _00g3_power_combination_eval
# LANG: _00fX, _00g2 --> _00g4
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v567__00g4 = (v563__00fX)*(v566__00g2)
v567__00g4 = v567__00g4.reshape((1, 40000))

# op _00g9 cross_product_eval
# LANG: _00fj, _00e_ --> _00ga
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v570__00ga = np.cross(v533__00e_, v543__00fj, axisa = 2, axisb = 2, axisc = 2)

# op _00gL_power_combination_eval
# LANG: _00gK --> _00gM
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v589__00gM = (v588__00gK**-1)
v589__00gM = v589__00gM.reshape((1, 40000))

# op _00gR_linear_combination_eval
# LANG: _00gO, _00gQ --> _00gS
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v592__00gS = v590__00gO+v591__00gQ

# op _00gt_power_combination_eval
# LANG: _00gm, _00gs --> _00gu
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v580__00gu = (v576__00gm)*(v579__00gs)
v580__00gu = v580__00gu.reshape((1, 40000))

# op _00h8_linear_combination_eval
# LANG: _00h7, _00h5 --> _00h9
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v601__00h9 = v600__00h7+v599__00h5

# op _00hc_power_combination_eval
# LANG: _00fJ --> _00hd
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v603__00hd = (v556__00fJ**-1)
v603__00hd = v603__00hd.reshape((1, 40000))

# op _00he_power_combination_eval
# LANG: _00eM --> _00hf
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v604__00hf = (v526__00eM**-1)
v604__00hf = v604__00hf.reshape((1, 40000))

# op _007Q_indexed_passthrough_eval
# LANG: p, q, r --> ang_vel
# SHAPES: (1, 1), (1, 1), (1, 1) --> (1, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp
v295_ang_vel__temp[i_v292_p__007Q_indexed_passthrough_eval] = v292_p.flatten()
v295_ang_vel = v295_ang_vel__temp.copy()
v295_ang_vel__temp[i_v293_q__007Q_indexed_passthrough_eval] = v293_q.flatten()
v295_ang_vel = v295_ang_vel__temp.copy()
v295_ang_vel__temp[i_v294_r__007Q_indexed_passthrough_eval] = v294_r.flatten()
v295_ang_vel = v295_ang_vel__temp.copy()

# op _007T expand_array_eval
# LANG: eel_rot_ref --> _007U
# SHAPES: (1, 3) --> (1, 50, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp
v298__007U = np.einsum('ad,bc->abcd', v297_eel_rot_ref.reshape((1, 3)) ,np.ones((50, 4))).reshape((1, 50, 4, 3))

# op _008p_power_combination_eval
# LANG: _008o --> _008q
# SHAPES: (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal
v317__008q = (v316__008o**2)
v317__008q = v317__008q.reshape((1, 50, 4, 3))

# op _00ae_power_combination_eval
# LANG: _00ad --> _00af
# SHAPES: (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v379__00af = (v378__00ad)
v379__00af = (v379__00af*_00ae_coeff).reshape((1, 55200, 3))

# op _00b5 expand_array_eval
# LANG: _00b4 --> _00b6
# SHAPES: (1, 55200) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v406__00b6 = np.einsum('ab,c->abc', v405__00b4.reshape((1, 55200)) ,np.ones((3,))).reshape((1, 55200, 3))

# op _00bb_power_combination_eval
# LANG: _00ba --> _00bc
# SHAPES: (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v409__00bc = (v408__00ba)
v409__00bc = (v409__00bc*_00bb_coeff).reshape((1, 55200, 3))

# op _00c2 expand_array_eval
# LANG: _00c1 --> _00c3
# SHAPES: (1, 55200) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v436__00c3 = np.einsum('ab,c->abc', v435__00c1.reshape((1, 55200)) ,np.ones((3,))).reshape((1, 55200, 3))

# op _00c6 cross_product_eval
# LANG: _00a5, _009M --> _00c7
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v438__00c7 = np.cross(v364__009M, v374__00a5, axisa = 2, axisb = 2, axisc = 2)

# op _00cY_power_combination_eval
# LANG: _00cD, _00cX --> _00cZ
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v465__00cZ = (v454__00cD)*(v464__00cX**-1)
v465__00cZ = v465__00cZ.reshape((1, 55200))

# op _00dT_linear_combination_eval
# LANG: _00dS --> _00dU
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v494__00dU = _00dT_constant+v493__00dS

# op _00dz_linear_combination_eval
# LANG: _00do, _00dy --> _00dA
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v484__00dA = v478__00do+v483__00dy

# op _00fM_power_combination_eval
# LANG: _00fL --> _00fN
# SHAPES: (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v558__00fN = (v557__00fL)
v558__00fN = (v558__00fN*_00fM_coeff).reshape((1, 40000, 3))

# op _00g5 expand_array_eval
# LANG: _00g4 --> _00g6
# SHAPES: (1, 40000) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v568__00g6 = np.einsum('ab,c->abc', v567__00g4.reshape((1, 40000)) ,np.ones((3,))).reshape((1, 40000, 3))

# op _00gT_power_combination_eval
# LANG: _00gM, _00gS --> _00gU
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v593__00gU = (v589__00gM)*(v592__00gS)
v593__00gU = v593__00gU.reshape((1, 40000))

# op _00gb_power_combination_eval
# LANG: _00ga --> _00gc
# SHAPES: (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v571__00gc = (v570__00ga)
v571__00gc = (v571__00gc*_00gb_coeff).reshape((1, 40000, 3))

# op _00gv expand_array_eval
# LANG: _00gu --> _00gw
# SHAPES: (1, 40000) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v581__00gw = np.einsum('ab,c->abc', v580__00gu.reshape((1, 40000)) ,np.ones((3,))).reshape((1, 40000, 3))

# op _00gz cross_product_eval
# LANG: _00fD, _00fj --> _00gA
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v583__00gA = np.cross(v543__00fj, v553__00fD, axisa = 2, axisb = 2, axisc = 2)

# op _00ha_power_combination_eval
# LANG: _00h9 --> _00hb
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v602__00hb = (v601__00h9**-1)
v602__00hb = v602__00hb.reshape((1, 40000))

# op _00hg_linear_combination_eval
# LANG: _00hd, _00hf --> _00hh
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v605__00hh = v603__00hd+v604__00hf

# op _007V_linear_combination_eval
# LANG: _007U, eel_coll_pts_coords --> _007W
# SHAPES: (1, 50, 4, 3), (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp
v299__007W = v511_eel_coll_pts_coords+-1*v298__007U

# op _007X expand_array_eval
# LANG: ang_vel --> _007Y
# SHAPES: (1, 3) --> (1, 50, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp
v300__007Y = np.einsum('ad,bc->abcd', v295_ang_vel.reshape((1, 3)) ,np.ones((50, 4))).reshape((1, 50, 4, 3))

# op _008r_single_tensor_sum_with_axis_eval
# LANG: _008q --> _008s
# SHAPES: (1, 50, 4, 3) --> (1, 50, 4)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal
v318__008s = np.sum(v317__008q, axis = (3,)).reshape((1, 50, 4))

# op _00b7_power_combination_eval
# LANG: _00b6, _00af --> _00b8
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v407__00b8 = (v406__00b6)*(v379__00af)
v407__00b8 = v407__00b8.reshape((1, 55200, 3))

# op _00c4_power_combination_eval
# LANG: _00c3, _00bc --> _00c5
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v437__00c5 = (v436__00c3)*(v409__00bc)
v437__00c5 = v437__00c5.reshape((1, 55200, 3))

# op _00c8_power_combination_eval
# LANG: _00c7 --> _00c9
# SHAPES: (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v439__00c9 = (v438__00c7)
v439__00c9 = (v439__00c9*_00c8_coeff).reshape((1, 55200, 3))

# op _00c_ expand_array_eval
# LANG: _00cZ --> _00d0
# SHAPES: (1, 55200) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v466__00d0 = np.einsum('ab,c->abc', v465__00cZ.reshape((1, 55200)) ,np.ones((3,))).reshape((1, 55200, 3))

# op _00d3 cross_product_eval
# LANG: _00a5, _0098 --> _00d4
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v468__00d4 = np.cross(v374__00a5, v344__0098, axisa = 2, axisb = 2, axisc = 2)

# op _00dV_power_combination_eval
# LANG: _00dA, _00dU --> _00dW
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v495__00dW = (v484__00dA)*(v494__00dU**-1)
v495__00dW = v495__00dW.reshape((1, 55200))

# op _00g7_power_combination_eval
# LANG: _00g6, _00fN --> _00g8
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v569__00g8 = (v568__00g6)*(v558__00fN)
v569__00g8 = v569__00g8.reshape((1, 40000, 3))

# op _00gB_power_combination_eval
# LANG: _00gA --> _00gC
# SHAPES: (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v584__00gC = (v583__00gA)
v584__00gC = (v584__00gC*_00gB_coeff).reshape((1, 40000, 3))

# op _00gV expand_array_eval
# LANG: _00gU --> _00gW
# SHAPES: (1, 40000) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v594__00gW = np.einsum('ab,c->abc', v593__00gU.reshape((1, 40000)) ,np.ones((3,))).reshape((1, 40000, 3))

# op _00gZ cross_product_eval
# LANG: _00fD, _00eG --> _00g_
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v596__00g_ = np.cross(v553__00fD, v523__00eG, axisa = 2, axisb = 2, axisc = 2)

# op _00gx_power_combination_eval
# LANG: _00gw, _00gc --> _00gy
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v582__00gy = (v581__00gw)*(v571__00gc)
v582__00gy = v582__00gy.reshape((1, 40000, 3))

# op _00hi_power_combination_eval
# LANG: _00hb, _00hh --> _00hj
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v606__00hj = (v602__00hb)*(v605__00hh)
v606__00hj = v606__00hj.reshape((1, 40000))

# op _007Z cross_product_eval
# LANG: _007Y, _007W --> _007_
# SHAPES: (1, 50, 4, 3), (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp
v301__007_ = np.cross(v300__007Y, v299__007W, axisa = 3, axisb = 3, axisc = 3)

# op _008t_power_combination_eval
# LANG: _008s --> _008u
# SHAPES: (1, 50, 4) --> (1, 50, 4)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal
v319__008u = (v318__008s**0.5)
v319__008u = v319__008u.reshape((1, 50, 4))

# op _00d1_power_combination_eval
# LANG: _00d0, _00c9 --> _00d2
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v467__00d2 = (v466__00d0)*(v439__00c9)
v467__00d2 = v467__00d2.reshape((1, 55200, 3))

# op _00d5_power_combination_eval
# LANG: _00d4 --> _00d6
# SHAPES: (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v469__00d6 = (v468__00d4)
v469__00d6 = (v469__00d6*_00d5_coeff).reshape((1, 55200, 3))

# op _00dX expand_array_eval
# LANG: _00dW --> _00dY
# SHAPES: (1, 55200) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v496__00dY = np.einsum('ab,c->abc', v495__00dW.reshape((1, 55200)) ,np.ones((3,))).reshape((1, 55200, 3))

# op _00e0_linear_combination_eval
# LANG: _00b8, _00c5 --> _00e1
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v498__00e1 = v407__00b8+v437__00c5

# op _00gX_power_combination_eval
# LANG: _00gW, _00gC --> _00gY
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v595__00gY = (v594__00gW)*(v584__00gC)
v595__00gY = v595__00gY.reshape((1, 40000, 3))

# op _00h0_power_combination_eval
# LANG: _00g_ --> _00h1
# SHAPES: (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v597__00h1 = (v596__00g_)
v597__00h1 = (v597__00h1*_00h0_coeff).reshape((1, 40000, 3))

# op _00hk expand_array_eval
# LANG: _00hj --> _00hl
# SHAPES: (1, 40000) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v607__00hl = np.einsum('ab,c->abc', v606__00hj.reshape((1, 40000)) ,np.ones((3,))).reshape((1, 40000, 3))

# op _00ho_linear_combination_eval
# LANG: _00g8, _00gy --> _00hp
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v609__00hp = v569__00g8+v582__00gy

# op _0080 reshape_eval
# LANG: _007_ --> _0081
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp
v302__0081 = v301__007_.reshape((1, 200, 3))

# op _0082 expand_array_eval
# LANG: frame_vel --> _0083
# SHAPES: (1, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp
v303__0083 = np.einsum('ac,b->abc', v621_frame_vel.reshape((1, 3)) ,np.ones((200,))).reshape((1, 200, 3))

# op _008v expand_array_eval
# LANG: _008u --> _008w
# SHAPES: (1, 50, 4) --> (1, 50, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal
v320__008w = np.einsum('abc,d->abcd', v319__008u.reshape((1, 50, 4)) ,np.ones((3,))).reshape((1, 50, 4, 3))

# op _00dZ_power_combination_eval
# LANG: _00dY, _00d6 --> _00d_
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v497__00d_ = (v496__00dY)*(v469__00d6)
v497__00d_ = v497__00d_.reshape((1, 55200, 3))

# op _00e2_linear_combination_eval
# LANG: _00e1, _00d2 --> _00e3
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v499__00e3 = v498__00e1+v467__00d2

# op _00hm_power_combination_eval
# LANG: _00hl, _00h1 --> _00hn
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v608__00hn = (v607__00hl)*(v597__00h1)
v608__00hn = v608__00hn.reshape((1, 40000, 3))

# op _00hq_linear_combination_eval
# LANG: _00hp, _00gY --> _00hr
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v610__00hr = v609__00hp+v595__00gY

# op _0085_linear_combination_eval
# LANG: _0081, _0083 --> _0086
# SHAPES: (1, 200, 3), (1, 200, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp
v305__0086 = v302__0081+v303__0083

# op _0087 reshape_eval
# LANG: eel_coll_vel --> _0088
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp
v306__0088 = v304_eel_coll_vel.reshape((1, 200, 3))

# op _008x_power_combination_eval
# LANG: _008o, _008w --> eel_bd_vtx_normals
# SHAPES: (1, 50, 4, 3), (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal
v614_eel_bd_vtx_normals = (v316__008o)*(v320__008w**-1)
v614_eel_bd_vtx_normals = v614_eel_bd_vtx_normals.reshape((1, 50, 4, 3))

# op _00e4_linear_combination_eval
# LANG: _00e3, _00d_ --> aic_M00
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v500_aic_M00 = v499__00e3+v497__00d_

# op _00hs_linear_combination_eval
# LANG: _00hr, _00hn --> aic_bd00
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v611_aic_bd00 = v610__00hr+v608__00hn

# op _0089_linear_combination_eval
# LANG: _0086, _0088 --> _008a
# SHAPES: (1, 200, 3), (1, 200, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp
v307__008a = v305__0086+v306__0088

# op _008M reshape_eval
# LANG: aic_M00 --> _008N
# SHAPES: (1, 55200, 3) --> (1, 200, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic
v331__008N = v500_aic_M00.reshape((1, 200, 276, 3))

# op _00e9 reshape_eval
# LANG: eel_bd_vtx_normals --> _00ea
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_aic
v504__00ea = v614_eel_bd_vtx_normals.reshape((1, 200, 3))

# op _00ej reshape_eval
# LANG: aic_bd00 --> _00ek
# SHAPES: (1, 40000, 3) --> (1, 200, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd
v510__00ek = v611_aic_bd00.reshape((1, 200, 200, 3))

# op _00hx reshape_eval
# LANG: eel_bd_vtx_normals --> _00hy
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_aic_bd
v615__00hy = v614_eel_bd_vtx_normals.reshape((1, 200, 3))

# op _008C reshape_eval
# LANG: eel_bd_vtx_normals --> _008D
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_k_vel
v325__008D = v614_eel_bd_vtx_normals.reshape((1, 200, 3))

# op _008O_indexed_passthrough_eval
# LANG: _008N --> aic_M
# SHAPES: (1, 200, 276, 3) --> (1, 200, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic
v502_aic_M__temp[i_v331__008N__008O_indexed_passthrough_eval] = v331__008N.flatten()
v502_aic_M = v502_aic_M__temp.copy()

# op _008b_linear_combination_eval
# LANG: _008a --> eel_kinematic_vel
# SHAPES: (1, 200, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp
v323_eel_kinematic_vel = -1*v307__008a

# op _00eb_indexed_passthrough_eval
# LANG: _00ea --> normal_concatenated_M_mat
# SHAPES: (1, 200, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_aic
v501_normal_concatenated_M_mat__temp[i_v504__00ea__00eb_indexed_passthrough_eval] = v504__00ea.flatten()
v501_normal_concatenated_M_mat = v501_normal_concatenated_M_mat__temp.copy()

# op _00el_indexed_passthrough_eval
# LANG: _00ek --> aic_bd
# SHAPES: (1, 200, 200, 3) --> (1, 200, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd
v613_aic_bd__temp[i_v510__00ek__00el_indexed_passthrough_eval] = v510__00ek.flatten()
v613_aic_bd = v613_aic_bd__temp.copy()

# op _00hz_indexed_passthrough_eval
# LANG: _00hy --> normal_concatenated_aic_bd_proj
# SHAPES: (1, 200, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_aic_bd
v612_normal_concatenated_aic_bd_proj__temp[i_v615__00hy__00hz_indexed_passthrough_eval] = v615__00hy.flatten()
v612_normal_concatenated_aic_bd_proj = v612_normal_concatenated_aic_bd_proj__temp.copy()

# op _008E_custom_explicit_eval
# LANG: _008D, eel_kinematic_vel --> b
# SHAPES: (1, 200, 3), (1, 200, 3) --> (1, 200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_k_vel
temp = _008E_custom_explicit_func_b.solve(v323_eel_kinematic_vel, v325__008D)
v326_b = temp[0].copy()

# op _00ec_custom_explicit_eval
# LANG: normal_concatenated_M_mat, aic_M --> M_mat
# SHAPES: (1, 200, 3), (1, 200, 276, 3) --> (1, 200, 276)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_aic
temp = _00ec_custom_explicit_func_M_mat.solve(v502_aic_M, v501_normal_concatenated_M_mat)
v505_M_mat = temp[0].copy()

# op _00hA_custom_explicit_eval
# LANG: normal_concatenated_aic_bd_proj, aic_bd --> aic_bd_proj
# SHAPES: (1, 200, 3), (1, 200, 200, 3) --> (1, 200, 200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_aic_bd
temp = _00hA_custom_explicit_func_aic_bd_proj.solve(v613_aic_bd, v612_normal_concatenated_aic_bd_proj)
v616_aic_bd_proj = temp[0].copy()

# op _0075_indexed_passthrough_eval
# LANG: eel_gamma_w --> gamma_w
# SHAPES: (1, 69, 4) --> (1, 69, 4)
# full namespace: combine_gamma_w
v279_gamma_w__temp[i_v267_eel_gamma_w__0075_indexed_passthrough_eval] = v267_eel_gamma_w.flatten()
v279_gamma_w = v279_gamma_w__temp.copy()

# op _007r_newton_implict_eval
# LANG: gamma_w, b, aic_bd_proj, M_mat --> gamma_b
# SHAPES: (1, 69, 4), (1, 200), (1, 200, 200), (1, 200, 276) --> (1, 200)
# full namespace: solve_gamma_b_group
_007r_newton.set_guess(initial_guess_v617_gamma_b)
_007r_newton_out = _007r_newton.solve(v616_aic_bd_proj, v505_M_mat, v279_gamma_w, v326_b)
v617_gamma_b = _007r_newton_out[0]

# op _00hK_linear_combination_eval
# LANG: frame_vel --> _00hL
# SHAPES: (1, 3) --> (1, 3)
# full namespace: ComputeWakeTotalVel.ComputeWakeKinematicVel
v622__00hL = -1*v621_frame_vel

# op _00hM expand_array_eval
# LANG: _00hL --> eel_wake_kinematic_vel
# SHAPES: (1, 3) --> (1, 69, 5, 3)
# full namespace: ComputeWakeTotalVel.ComputeWakeKinematicVel
v623_eel_wake_kinematic_vel = np.einsum('ad,bc->abcd', v622__00hL.reshape((1, 3)) ,np.ones((69, 5))).reshape((1, 69, 5, 3))

# op _00hH_linear_combination_eval
# LANG: eel_wake_kinematic_vel --> eel_wake_total_vel
# SHAPES: (1, 69, 5, 3) --> (1, 69, 5, 3)
# full namespace: ComputeWakeTotalVel
v620_eel_wake_total_vel = v623_eel_wake_kinematic_vel

# op _003g_decompose_eval
# LANG: eel_wake_total_vel --> _003Z, _003h
# SHAPES: (1, 69, 5, 3) --> (1, 68, 5, 3), (1, 1, 5, 3)
# full namespace: 
v129__003h = ((v620_eel_wake_total_vel.flatten())[src_indices__003h__003g]).reshape((1, 1, 5, 3))
v152__003Z = ((v620_eel_wake_total_vel.flatten())[src_indices__003Z__003g]).reshape((1, 68, 5, 3))

# op _003H_power_combination_eval
# LANG: _003h --> _003I
# SHAPES: (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: 
v142__003I = (v129__003h)
v142__003I = (v142__003I*_003H_coeff).reshape((1, 1, 5, 3))

# op _003J_power_combination_eval
# LANG: _003I --> _003K
# SHAPES: (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: 
v143__003K = (v142__003I)
v143__003K = (v143__003K*_003J_coeff).reshape((1, 1, 5, 3))

# op _003e_decompose_eval
# LANG: eel_bd_vtx_coords --> _003f
# SHAPES: (1, 51, 5, 3) --> (1, 1, 5, 3)
# full namespace: 
v128__003f = ((v512_eel_bd_vtx_coords.flatten())[src_indices__003f__003e]).reshape((1, 1, 5, 3))

# op _003L_linear_combination_eval
# LANG: _003f, _003K --> _003M
# SHAPES: (1, 1, 5, 3), (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: 
v144__003M = v128__003f+v143__003K

# op _003o_decompose_eval
# LANG: eel_wake_coords --> _003W, _003p, _003T
# SHAPES: (1, 69, 5, 3) --> (1, 68, 5, 3), (1, 1, 5, 3), (1, 68, 5, 3)
# full namespace: 
v133__003p = ((v285_eel_wake_coords.flatten())[src_indices__003p__003o]).reshape((1, 1, 5, 3))
v148__003T = ((v285_eel_wake_coords.flatten())[src_indices__003T__003o]).reshape((1, 68, 5, 3))
v150__003W = ((v285_eel_wake_coords.flatten())[src_indices__003W__003o]).reshape((1, 68, 5, 3))

# op _005x_linear_combination_eval
# LANG: _004R, _004U --> _005y
# SHAPES: (1, 50, 5, 3), (1, 50, 5, 3) --> (1, 50, 5, 3)
# full namespace: MeshPreprocessing_comp
v212__005y = v186__004R+-1*v188__004U

# op _003N_linear_combination_eval
# LANG: _003M, _003p --> _003O
# SHAPES: (1, 1, 5, 3), (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: 
v145__003O = v144__003M+-1*v133__003p

# op _004N_linear_combination_eval
# LANG: eel --> _004O
# SHAPES: (1, 51, 5, 3) --> (1, 51, 5, 3)
# full namespace: MeshPreprocessing_comp
v184__004O = v309_eel

# op _004f_power_combination_eval
# LANG: u --> _004g
# SHAPES: (1, 1) --> (1, 1)
# full namespace: adapter_comp
v166__004g = (v156_u**2)
v166__004g = v166__004g.reshape((1, 1))

# op _004h_power_combination_eval
# LANG: v --> _004i
# SHAPES: (1, 1) --> (1, 1)
# full namespace: adapter_comp
v167__004i = (v157_v**2)
v167__004i = v167__004i.reshape((1, 1))

# op _005z pnorm_axis_eval
# LANG: _005y --> _005A
# SHAPES: (1, 50, 5, 3) --> (1, 50, 5)
# full namespace: MeshPreprocessing_comp
v213__005A = np.sum(v212__005y**2,axis=(3,))**(1 / 2)

# op _003P reshape_eval
# LANG: _003O --> _003Q
# SHAPES: (1, 1, 5, 3) --> (1, 5, 3)
# full namespace: 
v146__003Q = v145__003O.reshape((1, 5, 3))

# op _004j_linear_combination_eval
# LANG: _004g, _004i --> _004k
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: adapter_comp
v168__004k = v166__004g+v167__004i

# op _004l_power_combination_eval
# LANG: w --> _004m
# SHAPES: (1, 1) --> (1, 1)
# full namespace: adapter_comp
v169__004m = (v192_w**2)
v169__004m = v169__004m.reshape((1, 1))

# op _005B_decompose_eval
# LANG: _005A --> _005D, _005C
# SHAPES: (1, 50, 5) --> (1, 50, 4), (1, 50, 4)
# full namespace: MeshPreprocessing_comp
v214__005C = ((v213__005A.flatten())[src_indices__005C__005B]).reshape((1, 50, 4))
v215__005D = ((v213__005A.flatten())[src_indices__005D__005B]).reshape((1, 50, 4))

# op _005V_decompose_eval
# LANG: _004O --> _0060, _005W, _005X, _005_
# SHAPES: (1, 51, 5, 3) --> (1, 50, 4, 3), (1, 50, 4, 3), (1, 50, 4, 3), (1, 50, 4, 3)
# full namespace: MeshPreprocessing_comp
v226__005W = ((v184__004O.flatten())[src_indices__005W__005V]).reshape((1, 50, 4, 3))
v227__005X = ((v184__004O.flatten())[src_indices__005X__005V]).reshape((1, 50, 4, 3))
v229__005_ = ((v184__004O.flatten())[src_indices__005___005V]).reshape((1, 50, 4, 3))
v230__0060 = ((v184__004O.flatten())[src_indices__0060__005V]).reshape((1, 50, 4, 3))

# op _006f_power_combination_eval
# LANG: _006e --> _006g
# SHAPES: (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: MeshPreprocessing_comp
v239__006g = (v238__006e)
v239__006g = (v239__006g*_006f_coeff).reshape((1, 50, 4, 3))

# op _006i_power_combination_eval
# LANG: _006h --> _006j
# SHAPES: (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: MeshPreprocessing_comp
v241__006j = (v240__006h)
v241__006j = (v241__006j*_006i_coeff).reshape((1, 50, 4, 3))

# op _003R expand_array_eval
# LANG: _003Q --> _003S
# SHAPES: (1, 5, 3) --> (1, 68, 5, 3)
# full namespace: 
v147__003S = np.einsum('acd,b->abcd', v146__003Q.reshape((1, 5, 3)) ,np.ones((68,))).reshape((1, 68, 5, 3))

# op _003i_power_combination_eval
# LANG: _003h --> _003j
# SHAPES: (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: 
v130__003j = (v129__003h)
v130__003j = (v130__003j*_003i_coeff).reshape((1, 1, 5, 3))

# op _004n_linear_combination_eval
# LANG: _004k, _004m --> v_inf_sq
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: adapter_comp
v258_v_inf_sq = v168__004k+v169__004m

# op _005E_linear_combination_eval
# LANG: _005C, _005D --> _005F
# SHAPES: (1, 50, 4), (1, 50, 4) --> (1, 50, 4)
# full namespace: MeshPreprocessing_comp
v216__005F = v214__005C+v215__005D

# op _005Y_linear_combination_eval
# LANG: _005W, _005X --> _005Z
# SHAPES: (1, 50, 4, 3), (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: MeshPreprocessing_comp
v228__005Z = v226__005W+-1*v227__005X

# op _0061_linear_combination_eval
# LANG: _005_, _0060 --> _0062
# SHAPES: (1, 50, 4, 3), (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: MeshPreprocessing_comp
v231__0062 = v229__005_+-1*v230__0060

# op _006k_linear_combination_eval
# LANG: _006g, _006j --> _006l
# SHAPES: (1, 50, 4, 3), (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: MeshPreprocessing_comp
v242__006l = v239__006g+v241__006j

# op _006n_power_combination_eval
# LANG: _006m --> _006o
# SHAPES: (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: MeshPreprocessing_comp
v244__006o = (v243__006m)
v244__006o = (v244__006o*_006n_coeff).reshape((1, 50, 4, 3))

# op _00hD_decompose_eval
# LANG: gamma_b --> eel_gamma_b
# SHAPES: (1, 200) --> (1, 200)
# full namespace: seperate_gamma_b
v618_eel_gamma_b = ((v617_gamma_b.flatten())[src_indices_eel_gamma_b__00hD]).reshape((1, 200))

# op _002S_decompose_eval
# LANG: eel_gamma_b --> _002T
# SHAPES: (1, 200) --> (1, 4)
# full namespace: 
v114__002T = ((v618_eel_gamma_b.flatten())[src_indices__002T__002S]).reshape((1, 4))

# op _003U_linear_combination_eval
# LANG: _003S, _003T --> _003V
# SHAPES: (1, 68, 5, 3), (1, 68, 5, 3) --> (1, 68, 5, 3)
# full namespace: 
v149__003V = v147__003S+v148__003T

# op _003k_power_combination_eval
# LANG: _003j --> _003l
# SHAPES: (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: 
v131__003l = (v130__003j)
v131__003l = (v131__003l*_003k_coeff).reshape((1, 1, 5, 3))

# op _005G_power_combination_eval
# LANG: _005F --> eel_chord_length
# SHAPES: (1, 50, 4) --> (1, 50, 4)
# full namespace: MeshPreprocessing_comp
v217_eel_chord_length = (v216__005F)
v217_eel_chord_length = (v217_eel_chord_length*_005G_coeff).reshape((1, 50, 4))

# op _005K_linear_combination_eval
# LANG: _005I, _005J --> _005L
# SHAPES: (1, 51, 4, 3), (1, 51, 4, 3) --> (1, 51, 4, 3)
# full namespace: MeshPreprocessing_comp
v220__005L = v218__005I+-1*v219__005J

# op _0063 cross_product_eval
# LANG: _005Z, _0062 --> _0064
# SHAPES: (1, 50, 4, 3), (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: MeshPreprocessing_comp
v232__0064 = np.cross(v228__005Z, v231__0062, axisa = 3, axisb = 3, axisc = 3)

# op _006U_power_combination_eval
# LANG: v_inf_sq --> _006V
# SHAPES: (1, 1) --> (1, 1)
# full namespace: MeshPreprocessing_comp
v261__006V = (v258_v_inf_sq**0.5)
v261__006V = v261__006V.reshape((1, 1))

# op _006p_linear_combination_eval
# LANG: _006l, _006o --> _006q
# SHAPES: (1, 50, 4, 3), (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: MeshPreprocessing_comp
v245__006q = v242__006l+v244__006o

# op _006r_power_combination_eval
# LANG: _005q --> _006s
# SHAPES: (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: MeshPreprocessing_comp
v246__006s = (v208__005q)
v246__006s = (v246__006s*_006r_coeff).reshape((1, 50, 4, 3))

# op _002U reshape_eval
# LANG: _002T --> _002V
# SHAPES: (1, 4) --> (1, 1, 4)
# full namespace: 
v115__002V = v114__002T.reshape((1, 1, 4))

# op _002W_decompose_eval
# LANG: eel_gamma_w --> _0033, _002X, _0032
# SHAPES: (1, 69, 4) --> (1, 68, 4), (1, 1, 4), (1, 68, 4)
# full namespace: 
v116__002X = ((v267_eel_gamma_w.flatten())[src_indices__002X__002W]).reshape((1, 1, 4))
v119__0032 = ((v267_eel_gamma_w.flatten())[src_indices__0032__002W]).reshape((1, 68, 4))
v120__0033 = ((v267_eel_gamma_w.flatten())[src_indices__0033__002W]).reshape((1, 68, 4))

# op _003X_linear_combination_eval
# LANG: _003V, _003W --> _003Y
# SHAPES: (1, 68, 5, 3), (1, 68, 5, 3) --> (1, 68, 5, 3)
# full namespace: 
v151__003Y = v149__003V+-1*v150__003W

# op _003__power_combination_eval
# LANG: _003Z --> _0040
# SHAPES: (1, 68, 5, 3) --> (1, 68, 5, 3)
# full namespace: 
v153__0040 = (v152__003Z)
v153__0040 = (v153__0040*_003__coeff).reshape((1, 68, 5, 3))

# op _003m_linear_combination_eval
# LANG: _003f, _003l --> _003n
# SHAPES: (1, 1, 5, 3), (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: 
v132__003n = v128__003f+v131__003l

# op _005M pnorm_axis_eval
# LANG: _005L --> _005N
# SHAPES: (1, 51, 4, 3) --> (1, 51, 4)
# full namespace: MeshPreprocessing_comp
v221__005N = np.sum(v220__005L**2,axis=(3,))**(1 / 2)

# op _0065_power_combination_eval
# LANG: _0064 --> _0066
# SHAPES: (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: MeshPreprocessing_comp
v233__0066 = (v232__0064**2)
v233__0066 = v233__0066.reshape((1, 50, 4, 3))

# op _006A_power_combination_eval
# LANG: _006e --> _006B
# SHAPES: (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: MeshPreprocessing_comp
v250__006B = (v238__006e)
v250__006B = (v250__006B*_006A_coeff).reshape((1, 50, 4, 3))

# op _006C_power_combination_eval
# LANG: _006m --> _006D
# SHAPES: (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: MeshPreprocessing_comp
v251__006D = (v243__006m)
v251__006D = (v251__006D*_006C_coeff).reshape((1, 50, 4, 3))

# op _006Q_single_tensor_sum_with_axis_eval
# LANG: eel_chord_length --> _006R
# SHAPES: (1, 50, 4) --> (1, 4)
# full namespace: MeshPreprocessing_comp
v259__006R = np.sum(v217_eel_chord_length, axis = (1,)).reshape((1, 4))

# op _006W_power_combination_eval
# LANG: density, _006V --> _006X
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: MeshPreprocessing_comp
v262__006X = (v257_density)*(v261__006V)
v262__006X = v262__006X.reshape((1, 1))

# op _006t_linear_combination_eval
# LANG: _006q, _006s --> _006u
# SHAPES: (1, 50, 4, 3), (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: MeshPreprocessing_comp
v247__006u = v245__006q+v246__006s

# op _002Y_linear_combination_eval
# LANG: _002V, _002X --> _002Z
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: 
v117__002Z = v115__002V+-1*v116__002X

# op _0034_linear_combination_eval
# LANG: _0032, _0033 --> _0035
# SHAPES: (1, 68, 4), (1, 68, 4) --> (1, 68, 4)
# full namespace: 
v121__0035 = v119__0032+-1*v120__0033

# op _003q_linear_combination_eval
# LANG: _003n, _003p --> _003r
# SHAPES: (1, 1, 5, 3), (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: 
v134__003r = v132__003n+-1*v133__003p

# op _0041_linear_combination_eval
# LANG: _003Y, _0040 --> _0042
# SHAPES: (1, 68, 5, 3), (1, 68, 5, 3) --> (1, 68, 5, 3)
# full namespace: 
v154__0042 = v151__003Y+v153__0040

# op _005O_decompose_eval
# LANG: _005N --> _005Q, _005P
# SHAPES: (1, 51, 4) --> (1, 50, 4), (1, 50, 4)
# full namespace: MeshPreprocessing_comp
v222__005P = ((v221__005N.flatten())[src_indices__005P__005O]).reshape((1, 50, 4))
v223__005Q = ((v221__005N.flatten())[src_indices__005Q__005O]).reshape((1, 50, 4))

# op _0067_single_tensor_sum_with_axis_eval
# LANG: _0066 --> _0068
# SHAPES: (1, 50, 4, 3) --> (1, 50, 4)
# full namespace: MeshPreprocessing_comp
v234__0068 = np.sum(v233__0066, axis = (3,)).reshape((1, 50, 4))

# op _006E_linear_combination_eval
# LANG: _006B, _006D --> _006F
# SHAPES: (1, 50, 4, 3), (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: MeshPreprocessing_comp
v252__006F = v250__006B+v251__006D

# op _006G_power_combination_eval
# LANG: _006h --> _006H
# SHAPES: (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: MeshPreprocessing_comp
v253__006H = (v240__006h)
v253__006H = (v253__006H*_006G_coeff).reshape((1, 50, 4, 3))

# op _006S reshape_eval
# LANG: _006R --> _006T
# SHAPES: (1, 4) --> (1, 4, 1)
# full namespace: MeshPreprocessing_comp
v260__006T = v259__006R.reshape((1, 4, 1))

# op _006Y expand_array_eval
# LANG: _006X --> _006Z
# SHAPES: (1, 1) --> (1, 4, 1)
# full namespace: MeshPreprocessing_comp
v263__006Z = np.einsum('ac,b->abc', v262__006X.reshape((1, 1)) ,np.ones((4,))).reshape((1, 4, 1))

# op _006v reshape_eval
# LANG: _006u --> _006w
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: MeshPreprocessing_comp
v248__006w = v247__006u.reshape((1, 200, 3))

# op _002__power_combination_eval
# LANG: _002Z --> _0030
# SHAPES: (1, 1, 4) --> (1, 1, 4)
# full namespace: 
v118__0030 = (v117__002Z)
v118__0030 = (v118__0030*_002__coeff).reshape((1, 1, 4))

# op _0036_power_combination_eval
# LANG: _0035 --> _0037
# SHAPES: (1, 68, 4) --> (1, 68, 4)
# full namespace: 
v122__0037 = (v121__0035)
v122__0037 = (v122__0037*_0036_coeff).reshape((1, 68, 4))

# op _003s_power_combination_eval
# LANG: _003r --> _003t
# SHAPES: (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: 
v135__003t = (v134__003r)
v135__003t = (v135__003t*_003s_coeff).reshape((1, 1, 5, 3))

# op _0043_power_combination_eval
# LANG: _0042 --> _0044
# SHAPES: (1, 68, 5, 3) --> (1, 68, 5, 3)
# full namespace: 
v155__0044 = (v154__0042)
v155__0044 = (v155__0044*_0043_coeff).reshape((1, 68, 5, 3))

# op _005R_linear_combination_eval
# LANG: _005P, _005Q --> _005S
# SHAPES: (1, 50, 4), (1, 50, 4) --> (1, 50, 4)
# full namespace: MeshPreprocessing_comp
v224__005S = v222__005P+v223__005Q

# op _0069_power_combination_eval
# LANG: _0068 --> _006a
# SHAPES: (1, 50, 4) --> (1, 50, 4)
# full namespace: MeshPreprocessing_comp
v235__006a = (v234__0068**0.5)
v235__006a = v235__006a.reshape((1, 50, 4))

# op _006I_linear_combination_eval
# LANG: _006F, _006H --> _006J
# SHAPES: (1, 50, 4, 3), (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: MeshPreprocessing_comp
v254__006J = v252__006F+v253__006H

# op _006K_power_combination_eval
# LANG: _005q --> _006L
# SHAPES: (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: MeshPreprocessing_comp
v255__006L = (v208__005q)
v255__006L = (v255__006L*_006K_coeff).reshape((1, 50, 4, 3))

# op _006__power_combination_eval
# LANG: _006Z, _006T --> _0070
# SHAPES: (1, 4, 1), (1, 4, 1) --> (1, 4, 1)
# full namespace: MeshPreprocessing_comp
v264__0070 = (v263__006Z)*(v260__006T)
v264__0070 = v264__0070.reshape((1, 4, 1))

# op _006x_linear_combination_eval
# LANG: _006w --> _006y
# SHAPES: (1, 200, 3) --> (1, 200, 3)
# full namespace: MeshPreprocessing_comp
v249__006y = -1*v248__006w

# op _0031_indexed_passthrough_eval
# LANG: _0030, _0037 --> eel_dgammaw_dt
# SHAPES: (1, 1, 4), (1, 68, 4) --> (1, 69, 4)
# full namespace: 
v113_eel_dgammaw_dt__temp[i_v118__0030__0031_indexed_passthrough_eval] = v118__0030.flatten()
v113_eel_dgammaw_dt = v113_eel_dgammaw_dt__temp.copy()
v113_eel_dgammaw_dt__temp[i_v122__0037__0031_indexed_passthrough_eval] = v122__0037.flatten()
v113_eel_dgammaw_dt = v113_eel_dgammaw_dt__temp.copy()

# op _003u_indexed_passthrough_eval
# LANG: _003t, _0044 --> eel_dwake_coords_dt
# SHAPES: (1, 1, 5, 3), (1, 68, 5, 3) --> (1, 69, 5, 3)
# full namespace: 
v127_eel_dwake_coords_dt__temp[i_v135__003t__003u_indexed_passthrough_eval] = v135__003t.flatten()
v127_eel_dwake_coords_dt = v127_eel_dwake_coords_dt__temp.copy()
v127_eel_dwake_coords_dt__temp[i_v155__0044__003u_indexed_passthrough_eval] = v155__0044.flatten()
v127_eel_dwake_coords_dt = v127_eel_dwake_coords_dt__temp.copy()

# op _004B_linear_combination_eval
# LANG: theta, gamma --> alpha
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: adapter_comp
v177_alpha = v162_theta+-1*v164_gamma

# op _004D_linear_combination_eval
# LANG: psi, psiw --> beta
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: adapter_comp
v178_beta = v163_psi+v165_psiw

# op _005T_power_combination_eval
# LANG: _005S --> eel_span_length
# SHAPES: (1, 50, 4) --> (1, 50, 4)
# full namespace: MeshPreprocessing_comp
v225_eel_span_length = (v224__005S)
v225_eel_span_length = (v225_eel_span_length*_005T_coeff).reshape((1, 50, 4))

# op _006M_linear_combination_eval
# LANG: _006J, _006L --> eel_eval_pts_coords
# SHAPES: (1, 50, 4, 3), (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: MeshPreprocessing_comp
v256_eel_eval_pts_coords = v254__006J+v255__006L

# op _006b_power_combination_eval
# LANG: _006a --> eel_s_panel
# SHAPES: (1, 50, 4) --> (1, 50, 4)
# full namespace: MeshPreprocessing_comp
v236_eel_s_panel = (v235__006a)
v236_eel_s_panel = (v236_eel_s_panel*_006b_coeff).reshape((1, 50, 4))

# op _006z_indexed_passthrough_eval
# LANG: _006y --> bd_vec
# SHAPES: (1, 200, 3) --> (1, 200, 3)
# full namespace: MeshPreprocessing_comp
v237_bd_vec__temp[i_v249__006y__006z_indexed_passthrough_eval] = v249__006y.flatten()
v237_bd_vec = v237_bd_vec__temp.copy()

# op _0071_power_combination_eval
# LANG: _0070 --> eel_re_span
# SHAPES: (1, 4, 1) --> (1, 4, 1)
# full namespace: MeshPreprocessing_comp
v265_eel_re_span = (v264__0070)
v265_eel_re_span = (v265_eel_re_span*_0071_coeff).reshape((1, 4, 1))

# op _008G_indexed_passthrough_eval
# LANG: _008D --> normal_concatenated_b
# SHAPES: (1, 200, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_k_vel
v322_normal_concatenated_b__temp[i_v325__008D__008G_indexed_passthrough_eval] = v325__008D.flatten()
v322_normal_concatenated_b = v322_normal_concatenated_b__temp.copy()