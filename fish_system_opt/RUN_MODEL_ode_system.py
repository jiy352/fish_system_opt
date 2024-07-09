

# RUN_MODEL_ode_system

# system evaluation block

# op _005l_linear_combination_eval
# LANG: u --> _005m
# SHAPES: (1, 1) --> (1, 1)
# full namespace: adapter_comp
v203__005m = -1*v179_u

# op _005o_linear_combination_eval
# LANG: w --> _005p
# SHAPES: (1, 1) --> (1, 1)
# full namespace: adapter_comp
v204__005p = -1*v215_w

# op _005n_indexed_passthrough_eval
# LANG: _005m, _005p --> frame_vel
# SHAPES: (1, 1), (1, 1) --> (1, 3)
# full namespace: adapter_comp
v644_frame_vel__temp[i_v203__005m__005n_indexed_passthrough_eval] = v203__005m.flatten()
v644_frame_vel = v644_frame_vel__temp.copy()
v644_frame_vel__temp[i_v204__005p__005n_indexed_passthrough_eval] = v204__005p.flatten()
v644_frame_vel = v644_frame_vel__temp.copy()

# op _005I_decompose_eval
# LANG: frame_vel --> _005N, _005J
# SHAPES: (1, 3) --> (1, 1), (1, 1)
# full namespace: MeshPreprocessing_comp
v217__005J = ((v644_frame_vel.flatten())[src_indices__005J__005I]).reshape((1, 1))
v219__005N = ((v644_frame_vel.flatten())[src_indices__005N__005I]).reshape((1, 1))

# op _005K_linear_combination_eval
# LANG: _005J --> _005L
# SHAPES: (1, 1) --> (1, 1)
# full namespace: MeshPreprocessing_comp
v218__005L = -1*v217__005J

# op _005O_linear_combination_eval
# LANG: _005N --> _005P
# SHAPES: (1, 1) --> (1, 1)
# full namespace: MeshPreprocessing_comp
v220__005P = -1*v219__005N

# op _005M_indexed_passthrough_eval
# LANG: _005L, _005P, w --> fs
# SHAPES: (1, 1), (1, 1), (1, 1) --> (1, 3)
# full namespace: MeshPreprocessing_comp
v216_fs__temp[i_v218__005L__005M_indexed_passthrough_eval] = v218__005L.flatten()
v216_fs = v216_fs__temp.copy()
v216_fs__temp[i_v220__005P__005M_indexed_passthrough_eval] = v220__005P.flatten()
v216_fs = v216_fs__temp.copy()
v216_fs__temp[i_v215_w__005M_indexed_passthrough_eval] = v215_w.flatten()
v216_fs = v216_fs__temp.copy()

# op _005v_decompose_eval
# LANG: eel --> _0065, _005w, _005z, _005W, _005Z, _005_, _0064, _006n, _006o, _006U, _006X, _0071
# SHAPES: (1, 41, 5, 3) --> (1, 40, 4, 3), (1, 40, 5, 3), (1, 40, 5, 3), (1, 1, 5, 3), (1, 40, 4, 3), (1, 40, 4, 3), (1, 40, 4, 3), (1, 41, 4, 3), (1, 41, 4, 3), (1, 40, 4, 3), (1, 40, 4, 3), (1, 40, 4, 3)
# full namespace: MeshPreprocessing_comp
v209__005w = ((v332_eel.flatten())[src_indices__005w__005v]).reshape((1, 40, 5, 3))
v211__005z = ((v332_eel.flatten())[src_indices__005z__005v]).reshape((1, 40, 5, 3))
v224__005W = ((v332_eel.flatten())[src_indices__005W__005v]).reshape((1, 1, 5, 3))
v226__005Z = ((v332_eel.flatten())[src_indices__005Z__005v]).reshape((1, 40, 4, 3))
v227__005_ = ((v332_eel.flatten())[src_indices__005___005v]).reshape((1, 40, 4, 3))
v230__0064 = ((v332_eel.flatten())[src_indices__0064__005v]).reshape((1, 40, 4, 3))
v231__0065 = ((v332_eel.flatten())[src_indices__0065__005v]).reshape((1, 40, 4, 3))
v241__006n = ((v332_eel.flatten())[src_indices__006n__005v]).reshape((1, 41, 4, 3))
v242__006o = ((v332_eel.flatten())[src_indices__006o__005v]).reshape((1, 41, 4, 3))
v261__006U = ((v332_eel.flatten())[src_indices__006U__005v]).reshape((1, 40, 4, 3))
v263__006X = ((v332_eel.flatten())[src_indices__006X__005v]).reshape((1, 40, 4, 3))
v266__0071 = ((v332_eel.flatten())[src_indices__0071__005v]).reshape((1, 40, 4, 3))

# op _008g_decompose_eval
# LANG: eel_wake_coords --> _008h
# SHAPES: (1, 59, 5, 3) --> (1, 1, 5, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group
v310__008h = ((v308_eel_wake_coords.flatten())[src_indices__008h__008g]).reshape((1, 1, 5, 3))

# op _005Q_power_combination_eval
# LANG: fs --> _005R
# SHAPES: (1, 3) --> (1, 3)
# full namespace: MeshPreprocessing_comp
v221__005R = (v216_fs)
v221__005R = (v221__005R*_005Q_coeff).reshape((1, 3))

# op _0060_linear_combination_eval
# LANG: _005Z, _005_ --> _0061
# SHAPES: (1, 40, 4, 3), (1, 40, 4, 3) --> (1, 40, 4, 3)
# full namespace: MeshPreprocessing_comp
v228__0061 = v226__005Z+v227__005_

# op _0066_linear_combination_eval
# LANG: _0065, _0064 --> _0067
# SHAPES: (1, 40, 4, 3), (1, 40, 4, 3) --> (1, 40, 4, 3)
# full namespace: MeshPreprocessing_comp
v232__0067 = v230__0064+v231__0065

# op _008i_power_combination_eval
# LANG: _008h --> _008j
# SHAPES: (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group
v311__008j = (v310__008h)
v311__008j = v311__008j.reshape((1, 1, 5, 3))

# op _005S_power_combination_eval
# LANG: _005R --> _005T
# SHAPES: (1, 3) --> (1, 3)
# full namespace: MeshPreprocessing_comp
v222__005T = (v221__005R)
v222__005T = (v222__005T*_005S_coeff).reshape((1, 3))

# op _0062_power_combination_eval
# LANG: _0061 --> _0063
# SHAPES: (1, 40, 4, 3) --> (1, 40, 4, 3)
# full namespace: MeshPreprocessing_comp
v229__0063 = (v228__0061)
v229__0063 = (v229__0063*_0062_coeff).reshape((1, 40, 4, 3))

# op _0068_power_combination_eval
# LANG: _0067 --> _0069
# SHAPES: (1, 40, 4, 3) --> (1, 40, 4, 3)
# full namespace: MeshPreprocessing_comp
v233__0069 = (v232__0067)
v233__0069 = (v233__0069*_0068_coeff).reshape((1, 40, 4, 3))

# op _008f_indexed_passthrough_eval
# LANG: _008j, eel_wake_coords --> eel_TE_wake_coords
# SHAPES: (1, 1, 5, 3), (1, 59, 5, 3) --> (1, 60, 5, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group
v356_eel_TE_wake_coords__temp[i_v308_eel_wake_coords__008f_indexed_passthrough_eval] = v308_eel_wake_coords.flatten()
v356_eel_TE_wake_coords = v356_eel_TE_wake_coords__temp.copy()
v356_eel_TE_wake_coords__temp[i_v311__008j__008f_indexed_passthrough_eval] = v311__008j.flatten()
v356_eel_TE_wake_coords = v356_eel_TE_wake_coords__temp.copy()

# op _005A_power_combination_eval
# LANG: _005z --> _005B
# SHAPES: (1, 40, 5, 3) --> (1, 40, 5, 3)
# full namespace: MeshPreprocessing_comp
v212__005B = (v211__005z)
v212__005B = (v212__005B*_005A_coeff).reshape((1, 40, 5, 3))

# op _005U expand_array_eval
# LANG: _005T --> _005V
# SHAPES: (1, 3) --> (1, 1, 5, 3)
# full namespace: MeshPreprocessing_comp
v223__005V = np.einsum('ad,bc->abcd', v222__005T.reshape((1, 3)) ,np.ones((1, 5))).reshape((1, 1, 5, 3))

# op _005x_power_combination_eval
# LANG: _005w --> _005y
# SHAPES: (1, 40, 5, 3) --> (1, 40, 5, 3)
# full namespace: MeshPreprocessing_comp
v210__005y = (v209__005w)
v210__005y = (v210__005y*_005x_coeff).reshape((1, 40, 5, 3))

# op _006a_linear_combination_eval
# LANG: _0063, _0069 --> eel_coll_pts_coords
# SHAPES: (1, 40, 4, 3), (1, 40, 4, 3) --> (1, 40, 4, 3)
# full namespace: MeshPreprocessing_comp
v534_eel_coll_pts_coords = v229__0063+v233__0069

# op _009w_decompose_eval
# LANG: eel_TE_wake_coords --> _009x, _009y, _009z, _009A
# SHAPES: (1, 60, 5, 3) --> (1, 59, 4, 3), (1, 59, 4, 3), (1, 59, 4, 3), (1, 59, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v357__009x = ((v356_eel_TE_wake_coords.flatten())[src_indices__009x__009w]).reshape((1, 59, 4, 3))
v358__009y = ((v356_eel_TE_wake_coords.flatten())[src_indices__009y__009w]).reshape((1, 59, 4, 3))
v359__009z = ((v356_eel_TE_wake_coords.flatten())[src_indices__009z__009w]).reshape((1, 59, 4, 3))
v360__009A = ((v356_eel_TE_wake_coords.flatten())[src_indices__009A__009w]).reshape((1, 59, 4, 3))

# op _005C_linear_combination_eval
# LANG: _005y, _005B --> _005D
# SHAPES: (1, 40, 5, 3), (1, 40, 5, 3) --> (1, 40, 5, 3)
# full namespace: MeshPreprocessing_comp
v213__005D = v210__005y+v212__005B

# op _005X_linear_combination_eval
# LANG: _005W, _005V --> _005Y
# SHAPES: (1, 1, 5, 3), (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: MeshPreprocessing_comp
v225__005Y = v224__005W+v223__005V

# op _009B reshape_eval
# LANG: eel_coll_pts_coords --> _009C
# SHAPES: (1, 40, 4, 3) --> (1, 160, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v361__009C = v534_eel_coll_pts_coords.reshape((1, 160, 3))

# op _009H reshape_eval
# LANG: _009x --> _009I
# SHAPES: (1, 59, 4, 3) --> (1, 236, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v364__009I = v357__009x.reshape((1, 236, 3))

# op _009V reshape_eval
# LANG: eel_coll_pts_coords --> _009W
# SHAPES: (1, 40, 4, 3) --> (1, 160, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v371__009W = v534_eel_coll_pts_coords.reshape((1, 160, 3))

# op _00a0 reshape_eval
# LANG: _009y --> _00a1
# SHAPES: (1, 59, 4, 3) --> (1, 236, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v374__00a1 = v358__009y.reshape((1, 236, 3))

# op _00ae reshape_eval
# LANG: eel_coll_pts_coords --> _00af
# SHAPES: (1, 40, 4, 3) --> (1, 160, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v381__00af = v534_eel_coll_pts_coords.reshape((1, 160, 3))

# op _00ak reshape_eval
# LANG: _009z --> _00al
# SHAPES: (1, 59, 4, 3) --> (1, 236, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v384__00al = v359__009z.reshape((1, 236, 3))

# op _005E_indexed_passthrough_eval
# LANG: _005D, _005Y --> eel_bd_vtx_coords
# SHAPES: (1, 40, 5, 3), (1, 1, 5, 3) --> (1, 41, 5, 3)
# full namespace: MeshPreprocessing_comp
v535_eel_bd_vtx_coords__temp[i_v213__005D__005E_indexed_passthrough_eval] = v213__005D.flatten()
v535_eel_bd_vtx_coords = v535_eel_bd_vtx_coords__temp.copy()
v535_eel_bd_vtx_coords__temp[i_v225__005Y__005E_indexed_passthrough_eval] = v225__005Y.flatten()
v535_eel_bd_vtx_coords = v535_eel_bd_vtx_coords__temp.copy()

# op _009D expand_array_eval
# LANG: _009C --> _009E
# SHAPES: (1, 160, 3) --> (1, 160, 236, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v362__009E = np.einsum('abd,c->abcd', v361__009C.reshape((1, 160, 3)) ,np.ones((236,))).reshape((1, 160, 236, 3))

# op _009J expand_array_eval
# LANG: _009I --> _009K
# SHAPES: (1, 236, 3) --> (1, 160, 236, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v365__009K = np.einsum('acd,b->abcd', v364__009I.reshape((1, 236, 3)) ,np.ones((160,))).reshape((1, 160, 236, 3))

# op _009X expand_array_eval
# LANG: _009W --> _009Y
# SHAPES: (1, 160, 3) --> (1, 160, 236, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v372__009Y = np.einsum('abd,c->abcd', v371__009W.reshape((1, 160, 3)) ,np.ones((236,))).reshape((1, 160, 236, 3))

# op _00a2 expand_array_eval
# LANG: _00a1 --> _00a3
# SHAPES: (1, 236, 3) --> (1, 160, 236, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v375__00a3 = np.einsum('acd,b->abcd', v374__00a1.reshape((1, 236, 3)) ,np.ones((160,))).reshape((1, 160, 236, 3))

# op _00aE reshape_eval
# LANG: _009A --> _00aF
# SHAPES: (1, 59, 4, 3) --> (1, 236, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v394__00aF = v360__009A.reshape((1, 236, 3))

# op _00ag expand_array_eval
# LANG: _00af --> _00ah
# SHAPES: (1, 160, 3) --> (1, 160, 236, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v382__00ah = np.einsum('abd,c->abcd', v381__00af.reshape((1, 160, 3)) ,np.ones((236,))).reshape((1, 160, 236, 3))

# op _00am expand_array_eval
# LANG: _00al --> _00an
# SHAPES: (1, 236, 3) --> (1, 160, 236, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v385__00an = np.einsum('acd,b->abcd', v384__00al.reshape((1, 236, 3)) ,np.ones((160,))).reshape((1, 160, 236, 3))

# op _00ay reshape_eval
# LANG: eel_coll_pts_coords --> _00az
# SHAPES: (1, 40, 4, 3) --> (1, 160, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v391__00az = v534_eel_coll_pts_coords.reshape((1, 160, 3))

# op _009F reshape_eval
# LANG: _009E --> _009G
# SHAPES: (1, 160, 236, 3) --> (1, 37760, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v363__009G = v362__009E.reshape((1, 37760, 3))

# op _009L reshape_eval
# LANG: _009K --> _009M
# SHAPES: (1, 160, 236, 3) --> (1, 37760, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v366__009M = v365__009K.reshape((1, 37760, 3))

# op _009Z reshape_eval
# LANG: _009Y --> _009_
# SHAPES: (1, 160, 236, 3) --> (1, 37760, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v373__009_ = v372__009Y.reshape((1, 37760, 3))

# op _00a4 reshape_eval
# LANG: _00a3 --> _00a5
# SHAPES: (1, 160, 236, 3) --> (1, 37760, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v376__00a5 = v375__00a3.reshape((1, 37760, 3))

# op _00aA expand_array_eval
# LANG: _00az --> _00aB
# SHAPES: (1, 160, 3) --> (1, 160, 236, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v392__00aB = np.einsum('abd,c->abcd', v391__00az.reshape((1, 160, 3)) ,np.ones((236,))).reshape((1, 160, 236, 3))

# op _00aG expand_array_eval
# LANG: _00aF --> _00aH
# SHAPES: (1, 236, 3) --> (1, 160, 236, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v395__00aH = np.einsum('acd,b->abcd', v394__00aF.reshape((1, 236, 3)) ,np.ones((160,))).reshape((1, 160, 236, 3))

# op _00ai reshape_eval
# LANG: _00ah --> _00aj
# SHAPES: (1, 160, 236, 3) --> (1, 37760, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v383__00aj = v382__00ah.reshape((1, 37760, 3))

# op _00ao reshape_eval
# LANG: _00an --> _00ap
# SHAPES: (1, 160, 236, 3) --> (1, 37760, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v386__00ap = v385__00an.reshape((1, 37760, 3))

# op _00f3_decompose_eval
# LANG: eel_bd_vtx_coords --> _00f4, _00f5, _00f6, _00f7
# SHAPES: (1, 41, 5, 3) --> (1, 40, 4, 3), (1, 40, 4, 3), (1, 40, 4, 3), (1, 40, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v536__00f4 = ((v535_eel_bd_vtx_coords.flatten())[src_indices__00f4__00f3]).reshape((1, 40, 4, 3))
v537__00f5 = ((v535_eel_bd_vtx_coords.flatten())[src_indices__00f5__00f3]).reshape((1, 40, 4, 3))
v538__00f6 = ((v535_eel_bd_vtx_coords.flatten())[src_indices__00f6__00f3]).reshape((1, 40, 4, 3))
v539__00f7 = ((v535_eel_bd_vtx_coords.flatten())[src_indices__00f7__00f3]).reshape((1, 40, 4, 3))

# op _009N_linear_combination_eval
# LANG: _009G, _009M --> _009O
# SHAPES: (1, 37760, 3), (1, 37760, 3) --> (1, 37760, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v367__009O = v363__009G+-1*v366__009M

# op _00a6_linear_combination_eval
# LANG: _009_, _00a5 --> _00a7
# SHAPES: (1, 37760, 3), (1, 37760, 3) --> (1, 37760, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v377__00a7 = v373__009_+-1*v376__00a5

# op _00aC reshape_eval
# LANG: _00aB --> _00aD
# SHAPES: (1, 160, 236, 3) --> (1, 37760, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v393__00aD = v392__00aB.reshape((1, 37760, 3))

# op _00aI reshape_eval
# LANG: _00aH --> _00aJ
# SHAPES: (1, 160, 236, 3) --> (1, 37760, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v396__00aJ = v395__00aH.reshape((1, 37760, 3))

# op _00aq_linear_combination_eval
# LANG: _00aj, _00ap --> _00ar
# SHAPES: (1, 37760, 3), (1, 37760, 3) --> (1, 37760, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v387__00ar = v383__00aj+-1*v386__00ap

# op _00f8 reshape_eval
# LANG: eel_coll_pts_coords --> _00f9
# SHAPES: (1, 40, 4, 3) --> (1, 160, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v540__00f9 = v534_eel_coll_pts_coords.reshape((1, 160, 3))

# op _00fM reshape_eval
# LANG: eel_coll_pts_coords --> _00fN
# SHAPES: (1, 40, 4, 3) --> (1, 160, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v560__00fN = v534_eel_coll_pts_coords.reshape((1, 160, 3))

# op _00fS reshape_eval
# LANG: _00f6 --> _00fT
# SHAPES: (1, 40, 4, 3) --> (1, 160, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v563__00fT = v538__00f6.reshape((1, 160, 3))

# op _00fe reshape_eval
# LANG: _00f4 --> _00ff
# SHAPES: (1, 40, 4, 3) --> (1, 160, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v543__00ff = v536__00f4.reshape((1, 160, 3))

# op _00fs reshape_eval
# LANG: eel_coll_pts_coords --> _00ft
# SHAPES: (1, 40, 4, 3) --> (1, 160, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v550__00ft = v534_eel_coll_pts_coords.reshape((1, 160, 3))

# op _00fy reshape_eval
# LANG: _00f5 --> _00fz
# SHAPES: (1, 40, 4, 3) --> (1, 160, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v553__00fz = v537__00f5.reshape((1, 160, 3))

# op _009P_power_combination_eval
# LANG: _009O --> _009Q
# SHAPES: (1, 37760, 3) --> (1, 37760, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v368__009Q = (v367__009O**2)
v368__009Q = v368__009Q.reshape((1, 37760, 3))

# op _00a8_power_combination_eval
# LANG: _00a7 --> _00a9
# SHAPES: (1, 37760, 3) --> (1, 37760, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v378__00a9 = (v377__00a7**2)
v378__00a9 = v378__00a9.reshape((1, 37760, 3))

# op _00aK_linear_combination_eval
# LANG: _00aD, _00aJ --> _00aL
# SHAPES: (1, 37760, 3), (1, 37760, 3) --> (1, 37760, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v397__00aL = v393__00aD+-1*v396__00aJ

# op _00as_power_combination_eval
# LANG: _00ar --> _00at
# SHAPES: (1, 37760, 3) --> (1, 37760, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v388__00at = (v387__00ar**2)
v388__00at = v388__00at.reshape((1, 37760, 3))

# op _00fA expand_array_eval
# LANG: _00fz --> _00fB
# SHAPES: (1, 160, 3) --> (1, 160, 160, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v554__00fB = np.einsum('acd,b->abcd', v553__00fz.reshape((1, 160, 3)) ,np.ones((160,))).reshape((1, 160, 160, 3))

# op _00fO expand_array_eval
# LANG: _00fN --> _00fP
# SHAPES: (1, 160, 3) --> (1, 160, 160, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v561__00fP = np.einsum('abd,c->abcd', v560__00fN.reshape((1, 160, 3)) ,np.ones((160,))).reshape((1, 160, 160, 3))

# op _00fU expand_array_eval
# LANG: _00fT --> _00fV
# SHAPES: (1, 160, 3) --> (1, 160, 160, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v564__00fV = np.einsum('acd,b->abcd', v563__00fT.reshape((1, 160, 3)) ,np.ones((160,))).reshape((1, 160, 160, 3))

# op _00fa expand_array_eval
# LANG: _00f9 --> _00fb
# SHAPES: (1, 160, 3) --> (1, 160, 160, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v541__00fb = np.einsum('abd,c->abcd', v540__00f9.reshape((1, 160, 3)) ,np.ones((160,))).reshape((1, 160, 160, 3))

# op _00fg expand_array_eval
# LANG: _00ff --> _00fh
# SHAPES: (1, 160, 3) --> (1, 160, 160, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v544__00fh = np.einsum('acd,b->abcd', v543__00ff.reshape((1, 160, 3)) ,np.ones((160,))).reshape((1, 160, 160, 3))

# op _00fu expand_array_eval
# LANG: _00ft --> _00fv
# SHAPES: (1, 160, 3) --> (1, 160, 160, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v551__00fv = np.einsum('abd,c->abcd', v550__00ft.reshape((1, 160, 3)) ,np.ones((160,))).reshape((1, 160, 160, 3))

# op _00g5 reshape_eval
# LANG: eel_coll_pts_coords --> _00g6
# SHAPES: (1, 40, 4, 3) --> (1, 160, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v570__00g6 = v534_eel_coll_pts_coords.reshape((1, 160, 3))

# op _00gb reshape_eval
# LANG: _00f7 --> _00gc
# SHAPES: (1, 40, 4, 3) --> (1, 160, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v573__00gc = v539__00f7.reshape((1, 160, 3))

# op _009R_single_tensor_sum_with_axis_eval
# LANG: _009Q --> _009S
# SHAPES: (1, 37760, 3) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v369__009S = np.sum(v368__009Q, axis = (2,)).reshape((1, 37760))

# op _00aM_power_combination_eval
# LANG: _00aL --> _00aN
# SHAPES: (1, 37760, 3) --> (1, 37760, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v398__00aN = (v397__00aL**2)
v398__00aN = v398__00aN.reshape((1, 37760, 3))

# op _00aa_single_tensor_sum_with_axis_eval
# LANG: _00a9 --> _00ab
# SHAPES: (1, 37760, 3) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v379__00ab = np.sum(v378__00a9, axis = (2,)).reshape((1, 37760))

# op _00au_single_tensor_sum_with_axis_eval
# LANG: _00at --> _00av
# SHAPES: (1, 37760, 3) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v389__00av = np.sum(v388__00at, axis = (2,)).reshape((1, 37760))

# op _00fC reshape_eval
# LANG: _00fB --> _00fD
# SHAPES: (1, 160, 160, 3) --> (1, 25600, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v555__00fD = v554__00fB.reshape((1, 25600, 3))

# op _00fQ reshape_eval
# LANG: _00fP --> _00fR
# SHAPES: (1, 160, 160, 3) --> (1, 25600, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v562__00fR = v561__00fP.reshape((1, 25600, 3))

# op _00fW reshape_eval
# LANG: _00fV --> _00fX
# SHAPES: (1, 160, 160, 3) --> (1, 25600, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v565__00fX = v564__00fV.reshape((1, 25600, 3))

# op _00fc reshape_eval
# LANG: _00fb --> _00fd
# SHAPES: (1, 160, 160, 3) --> (1, 25600, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v542__00fd = v541__00fb.reshape((1, 25600, 3))

# op _00fi reshape_eval
# LANG: _00fh --> _00fj
# SHAPES: (1, 160, 160, 3) --> (1, 25600, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v545__00fj = v544__00fh.reshape((1, 25600, 3))

# op _00fw reshape_eval
# LANG: _00fv --> _00fx
# SHAPES: (1, 160, 160, 3) --> (1, 25600, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v552__00fx = v551__00fv.reshape((1, 25600, 3))

# op _00g7 expand_array_eval
# LANG: _00g6 --> _00g8
# SHAPES: (1, 160, 3) --> (1, 160, 160, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v571__00g8 = np.einsum('abd,c->abcd', v570__00g6.reshape((1, 160, 3)) ,np.ones((160,))).reshape((1, 160, 160, 3))

# op _00gd expand_array_eval
# LANG: _00gc --> _00ge
# SHAPES: (1, 160, 3) --> (1, 160, 160, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v574__00ge = np.einsum('acd,b->abcd', v573__00gc.reshape((1, 160, 3)) ,np.ones((160,))).reshape((1, 160, 160, 3))

# op _009T_power_combination_eval
# LANG: _009S --> _009U
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v370__009U = (v369__009S**0.5)
v370__009U = v370__009U.reshape((1, 37760))

# op _00aO_single_tensor_sum_with_axis_eval
# LANG: _00aN --> _00aP
# SHAPES: (1, 37760, 3) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v399__00aP = np.sum(v398__00aN, axis = (2,)).reshape((1, 37760))

# op _00ac_power_combination_eval
# LANG: _00ab --> _00ad
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v380__00ad = (v379__00ab**0.5)
v380__00ad = v380__00ad.reshape((1, 37760))

# op _00aw_power_combination_eval
# LANG: _00av --> _00ax
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v390__00ax = (v389__00av**0.5)
v390__00ax = v390__00ax.reshape((1, 37760))

# op _00fE_linear_combination_eval
# LANG: _00fx, _00fD --> _00fF
# SHAPES: (1, 25600, 3), (1, 25600, 3) --> (1, 25600, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v556__00fF = v552__00fx+-1*v555__00fD

# op _00fY_linear_combination_eval
# LANG: _00fR, _00fX --> _00fZ
# SHAPES: (1, 25600, 3), (1, 25600, 3) --> (1, 25600, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v566__00fZ = v562__00fR+-1*v565__00fX

# op _00fk_linear_combination_eval
# LANG: _00fd, _00fj --> _00fl
# SHAPES: (1, 25600, 3), (1, 25600, 3) --> (1, 25600, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v546__00fl = v542__00fd+-1*v545__00fj

# op _00g9 reshape_eval
# LANG: _00g8 --> _00ga
# SHAPES: (1, 160, 160, 3) --> (1, 25600, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v572__00ga = v571__00g8.reshape((1, 25600, 3))

# op _00gf reshape_eval
# LANG: _00ge --> _00gg
# SHAPES: (1, 160, 160, 3) --> (1, 25600, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v575__00gg = v574__00ge.reshape((1, 25600, 3))

# op _00aQ_power_combination_eval
# LANG: _00aP --> _00aR
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v400__00aR = (v399__00aP**0.5)
v400__00aR = v400__00aR.reshape((1, 37760))

# op _00aW_power_combination_eval
# LANG: _009O, _00a7 --> _00aX
# SHAPES: (1, 37760, 3), (1, 37760, 3) --> (1, 37760, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v403__00aX = (v367__009O)*(v377__00a7)
v403__00aX = v403__00aX.reshape((1, 37760, 3))

# op _00a__power_combination_eval
# LANG: _009U --> _00b0
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v405__00b0 = (v370__009U**2)
v405__00b0 = v405__00b0.reshape((1, 37760))

# op _00b1_power_combination_eval
# LANG: _00ad --> _00b2
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v406__00b2 = (v380__00ad**2)
v406__00b2 = v406__00b2.reshape((1, 37760))

# op _00bT_power_combination_eval
# LANG: _00ar, _00a7 --> _00bU
# SHAPES: (1, 37760, 3), (1, 37760, 3) --> (1, 37760, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v433__00bU = (v377__00a7)*(v387__00ar)
v433__00bU = v433__00bU.reshape((1, 37760, 3))

# op _00bX_power_combination_eval
# LANG: _00ad --> _00bY
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v435__00bY = (v380__00ad**2)
v435__00bY = v435__00bY.reshape((1, 37760))

# op _00bZ_power_combination_eval
# LANG: _00ax --> _00b_
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v436__00b_ = (v390__00ax**2)
v436__00b_ = v436__00b_.reshape((1, 37760))

# op _00bx_power_combination_eval
# LANG: _009U --> _00by
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v422__00by = (v370__009U)
v422__00by = (v422__00by*_00bx_coeff).reshape((1, 37760))

# op _00cu_power_combination_eval
# LANG: _00ad --> _00cv
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v452__00cv = (v380__00ad)
v452__00cv = (v452__00cv*_00cu_coeff).reshape((1, 37760))

# op _00fG_power_combination_eval
# LANG: _00fF --> _00fH
# SHAPES: (1, 25600, 3) --> (1, 25600, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v557__00fH = (v556__00fF**2)
v557__00fH = v557__00fH.reshape((1, 25600, 3))

# op _00f__power_combination_eval
# LANG: _00fZ --> _00g0
# SHAPES: (1, 25600, 3) --> (1, 25600, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v567__00g0 = (v566__00fZ**2)
v567__00g0 = v567__00g0.reshape((1, 25600, 3))

# op _00fm_power_combination_eval
# LANG: _00fl --> _00fn
# SHAPES: (1, 25600, 3) --> (1, 25600, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v547__00fn = (v546__00fl**2)
v547__00fn = v547__00fn.reshape((1, 25600, 3))

# op _00gh_linear_combination_eval
# LANG: _00ga, _00gg --> _00gi
# SHAPES: (1, 25600, 3), (1, 25600, 3) --> (1, 25600, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v576__00gi = v572__00ga+-1*v575__00gg

# op _00aY_single_tensor_sum_with_axis_eval
# LANG: _00aX --> _00aZ
# SHAPES: (1, 37760, 3) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v404__00aZ = np.sum(v403__00aX, axis = (2,)).reshape((1, 37760))

# op _00b5_linear_combination_eval
# LANG: _00b0 --> _00b6
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v408__00b6 = _00b5_constant+v405__00b0

# op _00bV_single_tensor_sum_with_axis_eval
# LANG: _00bU --> _00bW
# SHAPES: (1, 37760, 3) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v434__00bW = np.sum(v433__00bU, axis = (2,)).reshape((1, 37760))

# op _00bf_linear_combination_eval
# LANG: _00b2 --> _00bg
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v413__00bg = _00bf_constant+v406__00b2

# op _00bv_linear_combination_eval
# LANG: _00b0, _00b2 --> _00bw
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v421__00bw = v405__00b0+v406__00b2

# op _00bz_power_combination_eval
# LANG: _00ad, _00by --> _00bA
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v423__00bA = (v422__00by)*(v380__00ad)
v423__00bA = v423__00bA.reshape((1, 37760))

# op _00c2_linear_combination_eval
# LANG: _00bY --> _00c3
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v438__00c3 = _00c2_constant+v435__00bY

# op _00cQ_power_combination_eval
# LANG: _00aL, _00ar --> _00cR
# SHAPES: (1, 37760, 3), (1, 37760, 3) --> (1, 37760, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v463__00cR = (v387__00ar)*(v397__00aL)
v463__00cR = v463__00cR.reshape((1, 37760, 3))

# op _00cU_power_combination_eval
# LANG: _00ax --> _00cV
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v465__00cV = (v390__00ax**2)
v465__00cV = v465__00cV.reshape((1, 37760))

# op _00cW_power_combination_eval
# LANG: _00aR --> _00cX
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v466__00cX = (v400__00aR**2)
v466__00cX = v466__00cX.reshape((1, 37760))

# op _00cc_linear_combination_eval
# LANG: _00b_ --> _00cd
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v443__00cd = _00cc_constant+v436__00b_

# op _00cs_linear_combination_eval
# LANG: _00bY, _00b_ --> _00ct
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v451__00ct = v435__00bY+v436__00b_

# op _00cw_power_combination_eval
# LANG: _00ax, _00cv --> _00cx
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v453__00cx = (v452__00cv)*(v390__00ax)
v453__00cx = v453__00cx.reshape((1, 37760))

# op _00dr_power_combination_eval
# LANG: _00ax --> _00ds
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v482__00ds = (v390__00ax)
v482__00ds = (v482__00ds*_00dr_coeff).reshape((1, 37760))

# op _00fI_single_tensor_sum_with_axis_eval
# LANG: _00fH --> _00fJ
# SHAPES: (1, 25600, 3) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v558__00fJ = np.sum(v557__00fH, axis = (2,)).reshape((1, 25600))

# op _00fo_single_tensor_sum_with_axis_eval
# LANG: _00fn --> _00fp
# SHAPES: (1, 25600, 3) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v548__00fp = np.sum(v547__00fn, axis = (2,)).reshape((1, 25600))

# op _00g1_single_tensor_sum_with_axis_eval
# LANG: _00g0 --> _00g2
# SHAPES: (1, 25600, 3) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v568__00g2 = np.sum(v567__00g0, axis = (2,)).reshape((1, 25600))

# op _00gj_power_combination_eval
# LANG: _00gi --> _00gk
# SHAPES: (1, 25600, 3) --> (1, 25600, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v577__00gk = (v576__00gi**2)
v577__00gk = v577__00gk.reshape((1, 25600, 3))

# op _00b7_linear_combination_eval
# LANG: _00b6 --> _00b8
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v409__00b8 = _00b7_constant+v408__00b6

# op _00bB_linear_combination_eval
# LANG: _00bw, _00bA --> _00bC
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v424__00bC = v421__00bw+-1*v423__00bA

# op _00bh_linear_combination_eval
# LANG: _00bg --> _00bi
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v414__00bi = _00bh_constant+v413__00bg

# op _00bp_power_combination_eval
# LANG: _00b0, _00b2 --> _00bq
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v418__00bq = (v405__00b0)*(v406__00b2)
v418__00bq = v418__00bq.reshape((1, 37760))

# op _00br_power_combination_eval
# LANG: _00aZ --> _00bs
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v419__00bs = (v404__00aZ**2)
v419__00bs = v419__00bs.reshape((1, 37760))

# op _00c4_linear_combination_eval
# LANG: _00c3 --> _00c5
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v439__00c5 = _00c4_constant+v438__00c3

# op _00cS_single_tensor_sum_with_axis_eval
# LANG: _00cR --> _00cT
# SHAPES: (1, 37760, 3) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v464__00cT = np.sum(v463__00cR, axis = (2,)).reshape((1, 37760))

# op _00c__linear_combination_eval
# LANG: _00cV --> _00d0
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v468__00d0 = _00c__constant+v465__00cV

# op _00ce_linear_combination_eval
# LANG: _00cd --> _00cf
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v444__00cf = _00ce_constant+v443__00cd

# op _00cm_power_combination_eval
# LANG: _00bY, _00b_ --> _00cn
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v448__00cn = (v435__00bY)*(v436__00b_)
v448__00cn = v448__00cn.reshape((1, 37760))

# op _00co_power_combination_eval
# LANG: _00bW --> _00cp
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v449__00cp = (v434__00bW**2)
v449__00cp = v449__00cp.reshape((1, 37760))

# op _00cy_linear_combination_eval
# LANG: _00ct, _00cx --> _00cz
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v454__00cz = v451__00ct+-1*v453__00cx

# op _00d9_linear_combination_eval
# LANG: _00cX --> _00da
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v473__00da = _00d9_constant+v466__00cX

# op _00dN_power_combination_eval
# LANG: _00aL, _009O --> _00dO
# SHAPES: (1, 37760, 3), (1, 37760, 3) --> (1, 37760, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v493__00dO = (v397__00aL)*(v367__009O)
v493__00dO = v493__00dO.reshape((1, 37760, 3))

# op _00dR_power_combination_eval
# LANG: _00aR --> _00dS
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v495__00dS = (v400__00aR**2)
v495__00dS = v495__00dS.reshape((1, 37760))

# op _00dT_power_combination_eval
# LANG: _009U --> _00dU
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v496__00dU = (v370__009U**2)
v496__00dU = v496__00dU.reshape((1, 37760))

# op _00dp_linear_combination_eval
# LANG: _00cV, _00cX --> _00dq
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v481__00dq = v465__00cV+v466__00cX

# op _00dt_power_combination_eval
# LANG: _00aR, _00ds --> _00du
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v483__00du = (v482__00ds)*(v400__00aR)
v483__00du = v483__00du.reshape((1, 37760))

# op _00eo_power_combination_eval
# LANG: _00aR --> _00ep
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v512__00ep = (v400__00aR)
v512__00ep = (v512__00ep*_00eo_coeff).reshape((1, 37760))

# op _00fK_power_combination_eval
# LANG: _00fJ --> _00fL
# SHAPES: (1, 25600) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v559__00fL = (v558__00fJ**0.5)
v559__00fL = v559__00fL.reshape((1, 25600))

# op _00fq_power_combination_eval
# LANG: _00fp --> _00fr
# SHAPES: (1, 25600) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v549__00fr = (v548__00fp**0.5)
v549__00fr = v549__00fr.reshape((1, 25600))

# op _00g3_power_combination_eval
# LANG: _00g2 --> _00g4
# SHAPES: (1, 25600) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v569__00g4 = (v568__00g2**0.5)
v569__00g4 = v569__00g4.reshape((1, 25600))

# op _00gT_power_combination_eval
# LANG: _00fZ, _00fF --> _00gU
# SHAPES: (1, 25600, 3), (1, 25600, 3) --> (1, 25600, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v595__00gU = (v556__00fF)*(v566__00fZ)
v595__00gU = v595__00gU.reshape((1, 25600, 3))

# op _00gl_single_tensor_sum_with_axis_eval
# LANG: _00gk --> _00gm
# SHAPES: (1, 25600, 3) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v578__00gm = np.sum(v577__00gk, axis = (2,)).reshape((1, 25600))

# op _00gt_power_combination_eval
# LANG: _00fl, _00fF --> _00gu
# SHAPES: (1, 25600, 3), (1, 25600, 3) --> (1, 25600, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v582__00gu = (v546__00fl)*(v556__00fF)
v582__00gu = v582__00gu.reshape((1, 25600, 3))

# op _00b3_linear_combination_eval
# LANG: _00b0, _00aZ --> _00b4
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v407__00b4 = v405__00b0+-1*v404__00aZ

# op _00b9_power_combination_eval
# LANG: _00b8 --> _00ba
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v410__00ba = (v409__00b8**0.5)
v410__00ba = v410__00ba.reshape((1, 37760))

# op _00bD_power_combination_eval
# LANG: _00bC --> _00bE
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v425__00bE = (v424__00bC)
v425__00bE = (v425__00bE*_00bD_coeff).reshape((1, 37760))

# op _00bd_linear_combination_eval
# LANG: _00b2, _00aZ --> _00be
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v412__00be = v406__00b2+-1*v404__00aZ

# op _00bj_power_combination_eval
# LANG: _00bi --> _00bk
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v415__00bk = (v414__00bi**0.5)
v415__00bk = v415__00bk.reshape((1, 37760))

# op _00bt_linear_combination_eval
# LANG: _00bq, _00bs --> _00bu
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v420__00bu = v418__00bq+-1*v419__00bs

# op _00c0_linear_combination_eval
# LANG: _00bY, _00bW --> _00c1
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v437__00c1 = v435__00bY+-1*v434__00bW

# op _00c6_power_combination_eval
# LANG: _00c5 --> _00c7
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v440__00c7 = (v439__00c5**0.5)
v440__00c7 = v440__00c7.reshape((1, 37760))

# op _00cA_power_combination_eval
# LANG: _00cz --> _00cB
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v455__00cB = (v454__00cz)
v455__00cB = (v455__00cB*_00cA_coeff).reshape((1, 37760))

# op _00ca_linear_combination_eval
# LANG: _00b_, _00bW --> _00cb
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v442__00cb = v436__00b_+-1*v434__00bW

# op _00cg_power_combination_eval
# LANG: _00cf --> _00ch
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v445__00ch = (v444__00cf**0.5)
v445__00ch = v445__00ch.reshape((1, 37760))

# op _00cq_linear_combination_eval
# LANG: _00cn, _00cp --> _00cr
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v450__00cr = v448__00cn+-1*v449__00cp

# op _00d1_linear_combination_eval
# LANG: _00d0 --> _00d2
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v469__00d2 = _00d1_constant+v468__00d0

# op _00dP_single_tensor_sum_with_axis_eval
# LANG: _00dO --> _00dQ
# SHAPES: (1, 37760, 3) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v494__00dQ = np.sum(v493__00dO, axis = (2,)).reshape((1, 37760))

# op _00dX_linear_combination_eval
# LANG: _00dS --> _00dY
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v498__00dY = _00dX_constant+v495__00dS

# op _00db_linear_combination_eval
# LANG: _00da --> _00dc
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v474__00dc = _00db_constant+v473__00da

# op _00dj_power_combination_eval
# LANG: _00cV, _00cX --> _00dk
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v478__00dk = (v465__00cV)*(v466__00cX)
v478__00dk = v478__00dk.reshape((1, 37760))

# op _00dl_power_combination_eval
# LANG: _00cT --> _00dm
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v479__00dm = (v464__00cT**2)
v479__00dm = v479__00dm.reshape((1, 37760))

# op _00dv_linear_combination_eval
# LANG: _00dq, _00du --> _00dw
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v484__00dw = v481__00dq+-1*v483__00du

# op _00e6_linear_combination_eval
# LANG: _00dU --> _00e7
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v503__00e7 = _00e6_constant+v496__00dU

# op _00em_linear_combination_eval
# LANG: _00dS, _00dU --> _00en
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v511__00en = v495__00dS+v496__00dU

# op _00eq_power_combination_eval
# LANG: _00ep, _009U --> _00er
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v513__00er = (v512__00ep)*(v370__009U)
v513__00er = v513__00er.reshape((1, 37760))

# op _00gV_single_tensor_sum_with_axis_eval
# LANG: _00gU --> _00gW
# SHAPES: (1, 25600, 3) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v596__00gW = np.sum(v595__00gU, axis = (2,)).reshape((1, 25600))

# op _00gX_power_combination_eval
# LANG: _00g4, _00fL --> _00gY
# SHAPES: (1, 25600), (1, 25600) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v597__00gY = (v559__00fL)*(v569__00g4)
v597__00gY = v597__00gY.reshape((1, 25600))

# op _00gn_power_combination_eval
# LANG: _00gm --> _00go
# SHAPES: (1, 25600) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v579__00go = (v578__00gm**0.5)
v579__00go = v579__00go.reshape((1, 25600))

# op _00gv_single_tensor_sum_with_axis_eval
# LANG: _00gu --> _00gw
# SHAPES: (1, 25600, 3) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v583__00gw = np.sum(v582__00gu, axis = (2,)).reshape((1, 25600))

# op _00gx_power_combination_eval
# LANG: _00fr, _00fL --> _00gy
# SHAPES: (1, 25600), (1, 25600) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v584__00gy = (v549__00fr)*(v559__00fL)
v584__00gy = v584__00gy.reshape((1, 25600))

# op _00hi_power_combination_eval
# LANG: _00gi, _00fZ --> _00hj
# SHAPES: (1, 25600, 3), (1, 25600, 3) --> (1, 25600, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v608__00hj = (v566__00fZ)*(v576__00gi)
v608__00hj = v608__00hj.reshape((1, 25600, 3))

# op _008U_decompose_eval
# LANG: eel --> _008_, _008V, _008W, _008Z
# SHAPES: (1, 41, 5, 3) --> (1, 40, 4, 3), (1, 40, 4, 3), (1, 40, 4, 3), (1, 40, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal
v333__008V = ((v332_eel.flatten())[src_indices__008V__008U]).reshape((1, 40, 4, 3))
v334__008W = ((v332_eel.flatten())[src_indices__008W__008U]).reshape((1, 40, 4, 3))
v336__008Z = ((v332_eel.flatten())[src_indices__008Z__008U]).reshape((1, 40, 4, 3))
v337__008_ = ((v332_eel.flatten())[src_indices__008___008U]).reshape((1, 40, 4, 3))

# op _00bF_linear_combination_eval
# LANG: _00bu, _00bE --> _00bG
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v426__00bG = v420__00bu+v425__00bE

# op _00bb_power_combination_eval
# LANG: _00b4, _00ba --> _00bc
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v411__00bc = (v407__00b4)*(v410__00ba**-1)
v411__00bc = v411__00bc.reshape((1, 37760))

# op _00bl_power_combination_eval
# LANG: _00be, _00bk --> _00bm
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v416__00bm = (v412__00be)*(v415__00bk**-1)
v416__00bm = v416__00bm.reshape((1, 37760))

# op _00c8_power_combination_eval
# LANG: _00c1, _00c7 --> _00c9
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v441__00c9 = (v437__00c1)*(v440__00c7**-1)
v441__00c9 = v441__00c9.reshape((1, 37760))

# op _00cC_linear_combination_eval
# LANG: _00cr, _00cB --> _00cD
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v456__00cD = v450__00cr+v455__00cB

# op _00cY_linear_combination_eval
# LANG: _00cV, _00cT --> _00cZ
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v467__00cZ = v465__00cV+-1*v464__00cT

# op _00ci_power_combination_eval
# LANG: _00cb, _00ch --> _00cj
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v446__00cj = (v442__00cb)*(v445__00ch**-1)
v446__00cj = v446__00cj.reshape((1, 37760))

# op _00d3_power_combination_eval
# LANG: _00d2 --> _00d4
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v470__00d4 = (v469__00d2**0.5)
v470__00d4 = v470__00d4.reshape((1, 37760))

# op _00d7_linear_combination_eval
# LANG: _00cX, _00cT --> _00d8
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v472__00d8 = v466__00cX+-1*v464__00cT

# op _00dZ_linear_combination_eval
# LANG: _00dY --> _00d_
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v499__00d_ = _00dZ_constant+v498__00dY

# op _00dd_power_combination_eval
# LANG: _00dc --> _00de
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v475__00de = (v474__00dc**0.5)
v475__00de = v475__00de.reshape((1, 37760))

# op _00dn_linear_combination_eval
# LANG: _00dk, _00dm --> _00do
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v480__00do = v478__00dk+-1*v479__00dm

# op _00dx_power_combination_eval
# LANG: _00dw --> _00dy
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v485__00dy = (v484__00dw)
v485__00dy = (v485__00dy*_00dx_coeff).reshape((1, 37760))

# op _00e8_linear_combination_eval
# LANG: _00e7 --> _00e9
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v504__00e9 = _00e8_constant+v503__00e7

# op _00eg_power_combination_eval
# LANG: _00dS, _00dU --> _00eh
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v508__00eh = (v495__00dS)*(v496__00dU)
v508__00eh = v508__00eh.reshape((1, 37760))

# op _00ei_power_combination_eval
# LANG: _00dQ --> _00ej
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v509__00ej = (v494__00dQ**2)
v509__00ej = v509__00ej.reshape((1, 37760))

# op _00es_linear_combination_eval
# LANG: _00en, _00er --> _00et
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v514__00et = v511__00en+-1*v513__00er

# op _00gD_power_combination_eval
# LANG: _00fr --> _00gE
# SHAPES: (1, 25600) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v587__00gE = (v549__00fr**-1)
v587__00gE = v587__00gE.reshape((1, 25600))

# op _00gF_power_combination_eval
# LANG: _00fL --> _00gG
# SHAPES: (1, 25600) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v588__00gG = (v559__00fL**-1)
v588__00gG = v588__00gG.reshape((1, 25600))

# op _00gZ_linear_combination_eval
# LANG: _00gY, _00gW --> _00g_
# SHAPES: (1, 25600), (1, 25600) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v598__00g_ = v597__00gY+v596__00gW

# op _00gz_linear_combination_eval
# LANG: _00gy, _00gw --> _00gA
# SHAPES: (1, 25600), (1, 25600) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v585__00gA = v584__00gy+v583__00gw

# op _00h2_power_combination_eval
# LANG: _00fL --> _00h3
# SHAPES: (1, 25600) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v600__00h3 = (v559__00fL**-1)
v600__00h3 = v600__00h3.reshape((1, 25600))

# op _00h4_power_combination_eval
# LANG: _00g4 --> _00h5
# SHAPES: (1, 25600) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v601__00h5 = (v569__00g4**-1)
v601__00h5 = v601__00h5.reshape((1, 25600))

# op _00hI_power_combination_eval
# LANG: _00gi, _00fl --> _00hJ
# SHAPES: (1, 25600, 3), (1, 25600, 3) --> (1, 25600, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v621__00hJ = (v576__00gi)*(v546__00fl)
v621__00hJ = v621__00hJ.reshape((1, 25600, 3))

# op _00hk_single_tensor_sum_with_axis_eval
# LANG: _00hj --> _00hl
# SHAPES: (1, 25600, 3) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v609__00hl = np.sum(v608__00hj, axis = (2,)).reshape((1, 25600))

# op _00hm_power_combination_eval
# LANG: _00go, _00g4 --> _00hn
# SHAPES: (1, 25600), (1, 25600) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v610__00hn = (v569__00g4)*(v579__00go)
v610__00hn = v610__00hn.reshape((1, 25600))

# op _008X_linear_combination_eval
# LANG: _008V, _008W --> _008Y
# SHAPES: (1, 40, 4, 3), (1, 40, 4, 3) --> (1, 40, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal
v335__008Y = v333__008V+-1*v334__008W

# op _0090_linear_combination_eval
# LANG: _008Z, _008_ --> _0091
# SHAPES: (1, 40, 4, 3), (1, 40, 4, 3) --> (1, 40, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal
v338__0091 = v336__008Z+-1*v337__008_

# op _00bH_linear_combination_eval
# LANG: _00bG --> _00bI
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v427__00bI = _00bH_constant+v426__00bG

# op _00bn_linear_combination_eval
# LANG: _00bc, _00bm --> _00bo
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v417__00bo = v411__00bc+v416__00bm

# op _00cE_linear_combination_eval
# LANG: _00cD --> _00cF
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v457__00cF = _00cE_constant+v456__00cD

# op _00ck_linear_combination_eval
# LANG: _00c9, _00cj --> _00cl
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v447__00cl = v441__00c9+v446__00cj

# op _00d5_power_combination_eval
# LANG: _00cZ, _00d4 --> _00d6
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v471__00d6 = (v467__00cZ)*(v470__00d4**-1)
v471__00d6 = v471__00d6.reshape((1, 37760))

# op _00dV_linear_combination_eval
# LANG: _00dS, _00dQ --> _00dW
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v497__00dW = v495__00dS+-1*v494__00dQ

# op _00df_power_combination_eval
# LANG: _00d8, _00de --> _00dg
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v476__00dg = (v472__00d8)*(v475__00de**-1)
v476__00dg = v476__00dg.reshape((1, 37760))

# op _00dz_linear_combination_eval
# LANG: _00do, _00dy --> _00dA
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v486__00dA = v480__00do+v485__00dy

# op _00e0_power_combination_eval
# LANG: _00d_ --> _00e1
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v500__00e1 = (v499__00d_**0.5)
v500__00e1 = v500__00e1.reshape((1, 37760))

# op _00e4_linear_combination_eval
# LANG: _00dU, _00dQ --> _00e5
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v502__00e5 = v496__00dU+-1*v494__00dQ

# op _00ea_power_combination_eval
# LANG: _00e9 --> _00eb
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v505__00eb = (v504__00e9**0.5)
v505__00eb = v505__00eb.reshape((1, 37760))

# op _00ek_linear_combination_eval
# LANG: _00eh, _00ej --> _00el
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v510__00el = v508__00eh+-1*v509__00ej

# op _00eu_power_combination_eval
# LANG: _00et --> _00ev
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v515__00ev = (v514__00et)
v515__00ev = (v515__00ev*_00eu_coeff).reshape((1, 37760))

# op _00gB_power_combination_eval
# LANG: _00gA --> _00gC
# SHAPES: (1, 25600) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v586__00gC = (v585__00gA**-1)
v586__00gC = v586__00gC.reshape((1, 25600))

# op _00gH_linear_combination_eval
# LANG: _00gE, _00gG --> _00gI
# SHAPES: (1, 25600), (1, 25600) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v589__00gI = v587__00gE+v588__00gG

# op _00h0_power_combination_eval
# LANG: _00g_ --> _00h1
# SHAPES: (1, 25600) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v599__00h1 = (v598__00g_**-1)
v599__00h1 = v599__00h1.reshape((1, 25600))

# op _00h6_linear_combination_eval
# LANG: _00h3, _00h5 --> _00h7
# SHAPES: (1, 25600), (1, 25600) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v602__00h7 = v600__00h3+v601__00h5

# op _00hK_single_tensor_sum_with_axis_eval
# LANG: _00hJ --> _00hL
# SHAPES: (1, 25600, 3) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v622__00hL = np.sum(v621__00hJ, axis = (2,)).reshape((1, 25600))

# op _00hM_power_combination_eval
# LANG: _00fr, _00go --> _00hN
# SHAPES: (1, 25600), (1, 25600) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v623__00hN = (v579__00go)*(v549__00fr)
v623__00hN = v623__00hN.reshape((1, 25600))

# op _00ho_linear_combination_eval
# LANG: _00hn, _00hl --> _00hp
# SHAPES: (1, 25600), (1, 25600) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v611__00hp = v610__00hn+v609__00hl

# op _00hs_power_combination_eval
# LANG: _00g4 --> _00ht
# SHAPES: (1, 25600) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v613__00ht = (v569__00g4**-1)
v613__00ht = v613__00ht.reshape((1, 25600))

# op _00hu_power_combination_eval
# LANG: _00go --> _00hv
# SHAPES: (1, 25600) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v614__00hv = (v579__00go**-1)
v614__00hv = v614__00hv.reshape((1, 25600))

# op _0092 cross_product_eval
# LANG: _008Y, _0091 --> _0093
# SHAPES: (1, 40, 4, 3), (1, 40, 4, 3) --> (1, 40, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal
v339__0093 = np.cross(v335__008Y, v338__0091, axisa = 3, axisb = 3, axisc = 3)

# op _00aS cross_product_eval
# LANG: _009O, _00a7 --> _00aT
# SHAPES: (1, 37760, 3), (1, 37760, 3) --> (1, 37760, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v401__00aT = np.cross(v367__009O, v377__00a7, axisa = 2, axisb = 2, axisc = 2)

# op _00bJ_power_combination_eval
# LANG: _00bo, _00bI --> _00bK
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v428__00bK = (v417__00bo)*(v427__00bI**-1)
v428__00bK = v428__00bK.reshape((1, 37760))

# op _00bP cross_product_eval
# LANG: _00ar, _00a7 --> _00bQ
# SHAPES: (1, 37760, 3), (1, 37760, 3) --> (1, 37760, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v431__00bQ = np.cross(v377__00a7, v387__00ar, axisa = 2, axisb = 2, axisc = 2)

# op _00cG_power_combination_eval
# LANG: _00cl, _00cF --> _00cH
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v458__00cH = (v447__00cl)*(v457__00cF**-1)
v458__00cH = v458__00cH.reshape((1, 37760))

# op _00dB_linear_combination_eval
# LANG: _00dA --> _00dC
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v487__00dC = _00dB_constant+v486__00dA

# op _00dh_linear_combination_eval
# LANG: _00d6, _00dg --> _00di
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v477__00di = v471__00d6+v476__00dg

# op _00e2_power_combination_eval
# LANG: _00dW, _00e1 --> _00e3
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v501__00e3 = (v497__00dW)*(v500__00e1**-1)
v501__00e3 = v501__00e3.reshape((1, 37760))

# op _00ec_power_combination_eval
# LANG: _00e5, _00eb --> _00ed
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v506__00ed = (v502__00e5)*(v505__00eb**-1)
v506__00ed = v506__00ed.reshape((1, 37760))

# op _00ew_linear_combination_eval
# LANG: _00el, _00ev --> _00ex
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v516__00ex = v510__00el+v515__00ev

# op _00gJ_power_combination_eval
# LANG: _00gC, _00gI --> _00gK
# SHAPES: (1, 25600), (1, 25600) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v590__00gK = (v586__00gC)*(v589__00gI)
v590__00gK = v590__00gK.reshape((1, 25600))

# op _00gP cross_product_eval
# LANG: _00fZ, _00fF --> _00gQ
# SHAPES: (1, 25600, 3), (1, 25600, 3) --> (1, 25600, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v593__00gQ = np.cross(v556__00fF, v566__00fZ, axisa = 2, axisb = 2, axisc = 2)

# op _00gp cross_product_eval
# LANG: _00fl, _00fF --> _00gq
# SHAPES: (1, 25600, 3), (1, 25600, 3) --> (1, 25600, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v580__00gq = np.cross(v546__00fl, v556__00fF, axisa = 2, axisb = 2, axisc = 2)

# op _00h8_power_combination_eval
# LANG: _00h1, _00h7 --> _00h9
# SHAPES: (1, 25600), (1, 25600) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v603__00h9 = (v599__00h1)*(v602__00h7)
v603__00h9 = v603__00h9.reshape((1, 25600))

# op _00hO_linear_combination_eval
# LANG: _00hN, _00hL --> _00hP
# SHAPES: (1, 25600), (1, 25600) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v624__00hP = v623__00hN+v622__00hL

# op _00hS_power_combination_eval
# LANG: _00go --> _00hT
# SHAPES: (1, 25600) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v626__00hT = (v579__00go**-1)
v626__00hT = v626__00hT.reshape((1, 25600))

# op _00hU_power_combination_eval
# LANG: _00fr --> _00hV
# SHAPES: (1, 25600) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v627__00hV = (v549__00fr**-1)
v627__00hV = v627__00hV.reshape((1, 25600))

# op _00hq_power_combination_eval
# LANG: _00hp --> _00hr
# SHAPES: (1, 25600) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v612__00hr = (v611__00hp**-1)
v612__00hr = v612__00hr.reshape((1, 25600))

# op _00hw_linear_combination_eval
# LANG: _00ht, _00hv --> _00hx
# SHAPES: (1, 25600), (1, 25600) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v615__00hx = v613__00ht+v614__00hv

# op _008v_indexed_passthrough_eval
# LANG: p, q, r --> ang_vel
# SHAPES: (1, 1), (1, 1), (1, 1) --> (1, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp
v318_ang_vel__temp[i_v315_p__008v_indexed_passthrough_eval] = v315_p.flatten()
v318_ang_vel = v318_ang_vel__temp.copy()
v318_ang_vel__temp[i_v316_q__008v_indexed_passthrough_eval] = v316_q.flatten()
v318_ang_vel = v318_ang_vel__temp.copy()
v318_ang_vel__temp[i_v317_r__008v_indexed_passthrough_eval] = v317_r.flatten()
v318_ang_vel = v318_ang_vel__temp.copy()

# op _008y expand_array_eval
# LANG: eel_rot_ref --> _008z
# SHAPES: (1, 3) --> (1, 40, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp
v321__008z = np.einsum('ad,bc->abcd', v320_eel_rot_ref.reshape((1, 3)) ,np.ones((40, 4))).reshape((1, 40, 4, 3))

# op _0094_power_combination_eval
# LANG: _0093 --> _0095
# SHAPES: (1, 40, 4, 3) --> (1, 40, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal
v340__0095 = (v339__0093**2)
v340__0095 = v340__0095.reshape((1, 40, 4, 3))

# op _00aU_power_combination_eval
# LANG: _00aT --> _00aV
# SHAPES: (1, 37760, 3) --> (1, 37760, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v402__00aV = (v401__00aT)
v402__00aV = (v402__00aV*_00aU_coeff).reshape((1, 37760, 3))

# op _00bL expand_array_eval
# LANG: _00bK --> _00bM
# SHAPES: (1, 37760) --> (1, 37760, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v429__00bM = np.einsum('ab,c->abc', v428__00bK.reshape((1, 37760)) ,np.ones((3,))).reshape((1, 37760, 3))

# op _00bR_power_combination_eval
# LANG: _00bQ --> _00bS
# SHAPES: (1, 37760, 3) --> (1, 37760, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v432__00bS = (v431__00bQ)
v432__00bS = (v432__00bS*_00bR_coeff).reshape((1, 37760, 3))

# op _00cI expand_array_eval
# LANG: _00cH --> _00cJ
# SHAPES: (1, 37760) --> (1, 37760, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v459__00cJ = np.einsum('ab,c->abc', v458__00cH.reshape((1, 37760)) ,np.ones((3,))).reshape((1, 37760, 3))

# op _00cM cross_product_eval
# LANG: _00aL, _00ar --> _00cN
# SHAPES: (1, 37760, 3), (1, 37760, 3) --> (1, 37760, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v461__00cN = np.cross(v387__00ar, v397__00aL, axisa = 2, axisb = 2, axisc = 2)

# op _00dD_power_combination_eval
# LANG: _00di, _00dC --> _00dE
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v488__00dE = (v477__00di)*(v487__00dC**-1)
v488__00dE = v488__00dE.reshape((1, 37760))

# op _00ee_linear_combination_eval
# LANG: _00e3, _00ed --> _00ef
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v507__00ef = v501__00e3+v506__00ed

# op _00ey_linear_combination_eval
# LANG: _00ex --> _00ez
# SHAPES: (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v517__00ez = _00ey_constant+v516__00ex

# op _00gL expand_array_eval
# LANG: _00gK --> _00gM
# SHAPES: (1, 25600) --> (1, 25600, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v591__00gM = np.einsum('ab,c->abc', v590__00gK.reshape((1, 25600)) ,np.ones((3,))).reshape((1, 25600, 3))

# op _00gR_power_combination_eval
# LANG: _00gQ --> _00gS
# SHAPES: (1, 25600, 3) --> (1, 25600, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v594__00gS = (v593__00gQ)
v594__00gS = (v594__00gS*_00gR_coeff).reshape((1, 25600, 3))

# op _00gr_power_combination_eval
# LANG: _00gq --> _00gs
# SHAPES: (1, 25600, 3) --> (1, 25600, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v581__00gs = (v580__00gq)
v581__00gs = (v581__00gs*_00gr_coeff).reshape((1, 25600, 3))

# op _00hQ_power_combination_eval
# LANG: _00hP --> _00hR
# SHAPES: (1, 25600) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v625__00hR = (v624__00hP**-1)
v625__00hR = v625__00hR.reshape((1, 25600))

# op _00hW_linear_combination_eval
# LANG: _00hT, _00hV --> _00hX
# SHAPES: (1, 25600), (1, 25600) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v628__00hX = v626__00hT+v627__00hV

# op _00ha expand_array_eval
# LANG: _00h9 --> _00hb
# SHAPES: (1, 25600) --> (1, 25600, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v604__00hb = np.einsum('ab,c->abc', v603__00h9.reshape((1, 25600)) ,np.ones((3,))).reshape((1, 25600, 3))

# op _00he cross_product_eval
# LANG: _00gi, _00fZ --> _00hf
# SHAPES: (1, 25600, 3), (1, 25600, 3) --> (1, 25600, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v606__00hf = np.cross(v566__00fZ, v576__00gi, axisa = 2, axisb = 2, axisc = 2)

# op _00hy_power_combination_eval
# LANG: _00hr, _00hx --> _00hz
# SHAPES: (1, 25600), (1, 25600) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v616__00hz = (v612__00hr)*(v615__00hx)
v616__00hz = v616__00hz.reshape((1, 25600))

# op _008A_linear_combination_eval
# LANG: _008z, eel_coll_pts_coords --> _008B
# SHAPES: (1, 40, 4, 3), (1, 40, 4, 3) --> (1, 40, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp
v322__008B = v534_eel_coll_pts_coords+-1*v321__008z

# op _008C expand_array_eval
# LANG: ang_vel --> _008D
# SHAPES: (1, 3) --> (1, 40, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp
v323__008D = np.einsum('ad,bc->abcd', v318_ang_vel.reshape((1, 3)) ,np.ones((40, 4))).reshape((1, 40, 4, 3))

# op _0096_single_tensor_sum_with_axis_eval
# LANG: _0095 --> _0097
# SHAPES: (1, 40, 4, 3) --> (1, 40, 4)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal
v341__0097 = np.sum(v340__0095, axis = (3,)).reshape((1, 40, 4))

# op _00bN_power_combination_eval
# LANG: _00bM, _00aV --> _00bO
# SHAPES: (1, 37760, 3), (1, 37760, 3) --> (1, 37760, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v430__00bO = (v429__00bM)*(v402__00aV)
v430__00bO = v430__00bO.reshape((1, 37760, 3))

# op _00cK_power_combination_eval
# LANG: _00cJ, _00bS --> _00cL
# SHAPES: (1, 37760, 3), (1, 37760, 3) --> (1, 37760, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v460__00cL = (v459__00cJ)*(v432__00bS)
v460__00cL = v460__00cL.reshape((1, 37760, 3))

# op _00cO_power_combination_eval
# LANG: _00cN --> _00cP
# SHAPES: (1, 37760, 3) --> (1, 37760, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v462__00cP = (v461__00cN)
v462__00cP = (v462__00cP*_00cO_coeff).reshape((1, 37760, 3))

# op _00dF expand_array_eval
# LANG: _00dE --> _00dG
# SHAPES: (1, 37760) --> (1, 37760, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v489__00dG = np.einsum('ab,c->abc', v488__00dE.reshape((1, 37760)) ,np.ones((3,))).reshape((1, 37760, 3))

# op _00dJ cross_product_eval
# LANG: _00aL, _009O --> _00dK
# SHAPES: (1, 37760, 3), (1, 37760, 3) --> (1, 37760, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v491__00dK = np.cross(v397__00aL, v367__009O, axisa = 2, axisb = 2, axisc = 2)

# op _00eA_power_combination_eval
# LANG: _00ef, _00ez --> _00eB
# SHAPES: (1, 37760), (1, 37760) --> (1, 37760)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v518__00eB = (v507__00ef)*(v517__00ez**-1)
v518__00eB = v518__00eB.reshape((1, 37760))

# op _00gN_power_combination_eval
# LANG: _00gM, _00gs --> _00gO
# SHAPES: (1, 25600, 3), (1, 25600, 3) --> (1, 25600, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v592__00gO = (v591__00gM)*(v581__00gs)
v592__00gO = v592__00gO.reshape((1, 25600, 3))

# op _00hA expand_array_eval
# LANG: _00hz --> _00hB
# SHAPES: (1, 25600) --> (1, 25600, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v617__00hB = np.einsum('ab,c->abc', v616__00hz.reshape((1, 25600)) ,np.ones((3,))).reshape((1, 25600, 3))

# op _00hE cross_product_eval
# LANG: _00gi, _00fl --> _00hF
# SHAPES: (1, 25600, 3), (1, 25600, 3) --> (1, 25600, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v619__00hF = np.cross(v576__00gi, v546__00fl, axisa = 2, axisb = 2, axisc = 2)

# op _00hY_power_combination_eval
# LANG: _00hR, _00hX --> _00hZ
# SHAPES: (1, 25600), (1, 25600) --> (1, 25600)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v629__00hZ = (v625__00hR)*(v628__00hX)
v629__00hZ = v629__00hZ.reshape((1, 25600))

# op _00hc_power_combination_eval
# LANG: _00hb, _00gS --> _00hd
# SHAPES: (1, 25600, 3), (1, 25600, 3) --> (1, 25600, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v605__00hd = (v604__00hb)*(v594__00gS)
v605__00hd = v605__00hd.reshape((1, 25600, 3))

# op _00hg_power_combination_eval
# LANG: _00hf --> _00hh
# SHAPES: (1, 25600, 3) --> (1, 25600, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v607__00hh = (v606__00hf)
v607__00hh = (v607__00hh*_00hg_coeff).reshape((1, 25600, 3))

# op _008E cross_product_eval
# LANG: _008D, _008B --> _008F
# SHAPES: (1, 40, 4, 3), (1, 40, 4, 3) --> (1, 40, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp
v324__008F = np.cross(v323__008D, v322__008B, axisa = 3, axisb = 3, axisc = 3)

# op _0098_power_combination_eval
# LANG: _0097 --> _0099
# SHAPES: (1, 40, 4) --> (1, 40, 4)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal
v342__0099 = (v341__0097**0.5)
v342__0099 = v342__0099.reshape((1, 40, 4))

# op _00dH_power_combination_eval
# LANG: _00dG, _00cP --> _00dI
# SHAPES: (1, 37760, 3), (1, 37760, 3) --> (1, 37760, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v490__00dI = (v489__00dG)*(v462__00cP)
v490__00dI = v490__00dI.reshape((1, 37760, 3))

# op _00dL_power_combination_eval
# LANG: _00dK --> _00dM
# SHAPES: (1, 37760, 3) --> (1, 37760, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v492__00dM = (v491__00dK)
v492__00dM = (v492__00dM*_00dL_coeff).reshape((1, 37760, 3))

# op _00eC expand_array_eval
# LANG: _00eB --> _00eD
# SHAPES: (1, 37760) --> (1, 37760, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v519__00eD = np.einsum('ab,c->abc', v518__00eB.reshape((1, 37760)) ,np.ones((3,))).reshape((1, 37760, 3))

# op _00eG_linear_combination_eval
# LANG: _00bO, _00cL --> _00eH
# SHAPES: (1, 37760, 3), (1, 37760, 3) --> (1, 37760, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v521__00eH = v430__00bO+v460__00cL

# op _00hC_power_combination_eval
# LANG: _00hB, _00hh --> _00hD
# SHAPES: (1, 25600, 3), (1, 25600, 3) --> (1, 25600, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v618__00hD = (v617__00hB)*(v607__00hh)
v618__00hD = v618__00hD.reshape((1, 25600, 3))

# op _00hG_power_combination_eval
# LANG: _00hF --> _00hH
# SHAPES: (1, 25600, 3) --> (1, 25600, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v620__00hH = (v619__00hF)
v620__00hH = (v620__00hH*_00hG_coeff).reshape((1, 25600, 3))

# op _00h_ expand_array_eval
# LANG: _00hZ --> _00i0
# SHAPES: (1, 25600) --> (1, 25600, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v630__00i0 = np.einsum('ab,c->abc', v629__00hZ.reshape((1, 25600)) ,np.ones((3,))).reshape((1, 25600, 3))

# op _00i3_linear_combination_eval
# LANG: _00gO, _00hd --> _00i4
# SHAPES: (1, 25600, 3), (1, 25600, 3) --> (1, 25600, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v632__00i4 = v592__00gO+v605__00hd

# op _008G reshape_eval
# LANG: _008F --> _008H
# SHAPES: (1, 40, 4, 3) --> (1, 160, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp
v325__008H = v324__008F.reshape((1, 160, 3))

# op _008I expand_array_eval
# LANG: frame_vel --> _008J
# SHAPES: (1, 3) --> (1, 160, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp
v326__008J = np.einsum('ac,b->abc', v644_frame_vel.reshape((1, 3)) ,np.ones((160,))).reshape((1, 160, 3))

# op _009a expand_array_eval
# LANG: _0099 --> _009b
# SHAPES: (1, 40, 4) --> (1, 40, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal
v343__009b = np.einsum('abc,d->abcd', v342__0099.reshape((1, 40, 4)) ,np.ones((3,))).reshape((1, 40, 4, 3))

# op _00eE_power_combination_eval
# LANG: _00eD, _00dM --> _00eF
# SHAPES: (1, 37760, 3), (1, 37760, 3) --> (1, 37760, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v520__00eF = (v519__00eD)*(v492__00dM)
v520__00eF = v520__00eF.reshape((1, 37760, 3))

# op _00eI_linear_combination_eval
# LANG: _00eH, _00dI --> _00eJ
# SHAPES: (1, 37760, 3), (1, 37760, 3) --> (1, 37760, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v522__00eJ = v521__00eH+v490__00dI

# op _00i1_power_combination_eval
# LANG: _00i0, _00hH --> _00i2
# SHAPES: (1, 25600, 3), (1, 25600, 3) --> (1, 25600, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v631__00i2 = (v630__00i0)*(v620__00hH)
v631__00i2 = v631__00i2.reshape((1, 25600, 3))

# op _00i5_linear_combination_eval
# LANG: _00i4, _00hD --> _00i6
# SHAPES: (1, 25600, 3), (1, 25600, 3) --> (1, 25600, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v633__00i6 = v632__00i4+v618__00hD

# op _008L_linear_combination_eval
# LANG: _008H, _008J --> _008M
# SHAPES: (1, 160, 3), (1, 160, 3) --> (1, 160, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp
v328__008M = v325__008H+v326__008J

# op _008N reshape_eval
# LANG: eel_coll_vel --> _008O
# SHAPES: (1, 40, 4, 3) --> (1, 160, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp
v329__008O = v327_eel_coll_vel.reshape((1, 160, 3))

# op _009c_power_combination_eval
# LANG: _0093, _009b --> eel_bd_vtx_normals
# SHAPES: (1, 40, 4, 3), (1, 40, 4, 3) --> (1, 40, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal
v637_eel_bd_vtx_normals = (v339__0093)*(v343__009b**-1)
v637_eel_bd_vtx_normals = v637_eel_bd_vtx_normals.reshape((1, 40, 4, 3))

# op _00eK_linear_combination_eval
# LANG: _00eJ, _00eF --> aic_M00
# SHAPES: (1, 37760, 3), (1, 37760, 3) --> (1, 37760, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v523_aic_M00 = v522__00eJ+v520__00eF

# op _00i7_linear_combination_eval
# LANG: _00i6, _00i2 --> aic_bd00
# SHAPES: (1, 25600, 3), (1, 25600, 3) --> (1, 25600, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v634_aic_bd00 = v633__00i6+v631__00i2

# op _008P_linear_combination_eval
# LANG: _008M, _008O --> _008Q
# SHAPES: (1, 160, 3), (1, 160, 3) --> (1, 160, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp
v330__008Q = v328__008M+v329__008O

# op _009r reshape_eval
# LANG: aic_M00 --> _009s
# SHAPES: (1, 37760, 3) --> (1, 160, 236, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic
v354__009s = v523_aic_M00.reshape((1, 160, 236, 3))

# op _00eP reshape_eval
# LANG: eel_bd_vtx_normals --> _00eQ
# SHAPES: (1, 40, 4, 3) --> (1, 160, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_aic
v527__00eQ = v637_eel_bd_vtx_normals.reshape((1, 160, 3))

# op _00eZ reshape_eval
# LANG: aic_bd00 --> _00e_
# SHAPES: (1, 25600, 3) --> (1, 160, 160, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd
v533__00e_ = v634_aic_bd00.reshape((1, 160, 160, 3))

# op _00ic reshape_eval
# LANG: eel_bd_vtx_normals --> _00id
# SHAPES: (1, 40, 4, 3) --> (1, 160, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_aic_bd
v638__00id = v637_eel_bd_vtx_normals.reshape((1, 160, 3))

# op _008R_linear_combination_eval
# LANG: _008Q --> eel_kinematic_vel
# SHAPES: (1, 160, 3) --> (1, 160, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp
v346_eel_kinematic_vel = -1*v330__008Q

# op _009h reshape_eval
# LANG: eel_bd_vtx_normals --> _009i
# SHAPES: (1, 40, 4, 3) --> (1, 160, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_k_vel
v348__009i = v637_eel_bd_vtx_normals.reshape((1, 160, 3))

# op _009t_indexed_passthrough_eval
# LANG: _009s --> aic_M
# SHAPES: (1, 160, 236, 3) --> (1, 160, 236, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic
v525_aic_M__temp[i_v354__009s__009t_indexed_passthrough_eval] = v354__009s.flatten()
v525_aic_M = v525_aic_M__temp.copy()

# op _00eR_indexed_passthrough_eval
# LANG: _00eQ --> normal_concatenated_M_mat
# SHAPES: (1, 160, 3) --> (1, 160, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_aic
v524_normal_concatenated_M_mat__temp[i_v527__00eQ__00eR_indexed_passthrough_eval] = v527__00eQ.flatten()
v524_normal_concatenated_M_mat = v524_normal_concatenated_M_mat__temp.copy()

# op _00f0_indexed_passthrough_eval
# LANG: _00e_ --> aic_bd
# SHAPES: (1, 160, 160, 3) --> (1, 160, 160, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd
v636_aic_bd__temp[i_v533__00e___00f0_indexed_passthrough_eval] = v533__00e_.flatten()
v636_aic_bd = v636_aic_bd__temp.copy()

# op _00ie_indexed_passthrough_eval
# LANG: _00id --> normal_concatenated_aic_bd_proj
# SHAPES: (1, 160, 3) --> (1, 160, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_aic_bd
v635_normal_concatenated_aic_bd_proj__temp[i_v638__00id__00ie_indexed_passthrough_eval] = v638__00id.flatten()
v635_normal_concatenated_aic_bd_proj = v635_normal_concatenated_aic_bd_proj__temp.copy()

# op _009j_custom_explicit_eval
# LANG: _009i, eel_kinematic_vel --> b
# SHAPES: (1, 160, 3), (1, 160, 3) --> (1, 160)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_k_vel
temp = _009j_custom_explicit_func_b.solve(v346_eel_kinematic_vel, v348__009i)
v349_b = temp[0].copy()

# op _00eS_custom_explicit_eval
# LANG: normal_concatenated_M_mat, aic_M --> M_mat
# SHAPES: (1, 160, 3), (1, 160, 236, 3) --> (1, 160, 236)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_aic
temp = _00eS_custom_explicit_func_M_mat.solve(v525_aic_M, v524_normal_concatenated_M_mat)
v528_M_mat = temp[0].copy()

# op _00if_custom_explicit_eval
# LANG: normal_concatenated_aic_bd_proj, aic_bd --> aic_bd_proj
# SHAPES: (1, 160, 3), (1, 160, 160, 3) --> (1, 160, 160)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_aic_bd
temp = _00if_custom_explicit_func_aic_bd_proj.solve(v636_aic_bd, v635_normal_concatenated_aic_bd_proj)
v639_aic_bd_proj = temp[0].copy()

# op _007L_indexed_passthrough_eval
# LANG: eel_gamma_w --> gamma_w
# SHAPES: (1, 59, 4) --> (1, 59, 4)
# full namespace: combine_gamma_w
v302_gamma_w__temp[i_v290_eel_gamma_w__007L_indexed_passthrough_eval] = v290_eel_gamma_w.flatten()
v302_gamma_w = v302_gamma_w__temp.copy()

# op _0086_newton_implict_eval
# LANG: M_mat, aic_bd_proj, b, gamma_w --> gamma_b
# SHAPES: (1, 160, 236), (1, 160, 160), (1, 160), (1, 59, 4) --> (1, 160)
# full namespace: solve_gamma_b_group
_0086_newton.set_guess(initial_guess_v640_gamma_b)
_0086_newton_out = _0086_newton.solve(v639_aic_bd_proj, v528_M_mat, v302_gamma_w, v349_b)
v640_gamma_b = _0086_newton_out[0]

# op _00ip_linear_combination_eval
# LANG: frame_vel --> _00iq
# SHAPES: (1, 3) --> (1, 3)
# full namespace: ComputeWakeTotalVel.ComputeWakeKinematicVel
v645__00iq = -1*v644_frame_vel

# op _00ir expand_array_eval
# LANG: _00iq --> eel_wake_kinematic_vel
# SHAPES: (1, 3) --> (1, 59, 5, 3)
# full namespace: ComputeWakeTotalVel.ComputeWakeKinematicVel
v646_eel_wake_kinematic_vel = np.einsum('ad,bc->abcd', v645__00iq.reshape((1, 3)) ,np.ones((59, 5))).reshape((1, 59, 5, 3))

# op _00im_linear_combination_eval
# LANG: eel_wake_kinematic_vel --> eel_wake_total_vel
# SHAPES: (1, 59, 5, 3) --> (1, 59, 5, 3)
# full namespace: ComputeWakeTotalVel
v643_eel_wake_total_vel = v646_eel_wake_kinematic_vel

# op _003W_decompose_eval
# LANG: eel_wake_total_vel --> _004E, _003X
# SHAPES: (1, 59, 5, 3) --> (1, 58, 5, 3), (1, 1, 5, 3)
# full namespace: 
v152__003X = ((v643_eel_wake_total_vel.flatten())[src_indices__003X__003W]).reshape((1, 1, 5, 3))
v175__004E = ((v643_eel_wake_total_vel.flatten())[src_indices__004E__003W]).reshape((1, 58, 5, 3))

# op _004m_power_combination_eval
# LANG: _003X --> _004n
# SHAPES: (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: 
v165__004n = (v152__003X)
v165__004n = (v165__004n*_004m_coeff).reshape((1, 1, 5, 3))

# op _003U_decompose_eval
# LANG: eel_bd_vtx_coords --> _003V
# SHAPES: (1, 41, 5, 3) --> (1, 1, 5, 3)
# full namespace: 
v151__003V = ((v535_eel_bd_vtx_coords.flatten())[src_indices__003V__003U]).reshape((1, 1, 5, 3))

# op _004o_power_combination_eval
# LANG: _004n --> _004p
# SHAPES: (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: 
v166__004p = (v165__004n)
v166__004p = (v166__004p*_004o_coeff).reshape((1, 1, 5, 3))

# op _0043_decompose_eval
# LANG: eel_wake_coords --> _004B, _0044, _004y
# SHAPES: (1, 59, 5, 3) --> (1, 58, 5, 3), (1, 1, 5, 3), (1, 58, 5, 3)
# full namespace: 
v156__0044 = ((v308_eel_wake_coords.flatten())[src_indices__0044__0043]).reshape((1, 1, 5, 3))
v171__004y = ((v308_eel_wake_coords.flatten())[src_indices__004y__0043]).reshape((1, 58, 5, 3))
v173__004B = ((v308_eel_wake_coords.flatten())[src_indices__004B__0043]).reshape((1, 58, 5, 3))

# op _004q_linear_combination_eval
# LANG: _003V, _004p --> _004r
# SHAPES: (1, 1, 5, 3), (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: 
v167__004r = v151__003V+v166__004p

# op _006c_linear_combination_eval
# LANG: _005w, _005z --> _006d
# SHAPES: (1, 40, 5, 3), (1, 40, 5, 3) --> (1, 40, 5, 3)
# full namespace: MeshPreprocessing_comp
v235__006d = v209__005w+-1*v211__005z

# op _004V_power_combination_eval
# LANG: u --> _004W
# SHAPES: (1, 1) --> (1, 1)
# full namespace: adapter_comp
v189__004W = (v179_u**2)
v189__004W = v189__004W.reshape((1, 1))

# op _004X_power_combination_eval
# LANG: v --> _004Y
# SHAPES: (1, 1) --> (1, 1)
# full namespace: adapter_comp
v190__004Y = (v180_v**2)
v190__004Y = v190__004Y.reshape((1, 1))

# op _004s_linear_combination_eval
# LANG: _004r, _0044 --> _004t
# SHAPES: (1, 1, 5, 3), (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: 
v168__004t = v167__004r+-1*v156__0044

# op _005s_linear_combination_eval
# LANG: eel --> _005t
# SHAPES: (1, 41, 5, 3) --> (1, 41, 5, 3)
# full namespace: MeshPreprocessing_comp
v207__005t = v332_eel

# op _006e pnorm_axis_eval
# LANG: _006d --> _006f
# SHAPES: (1, 40, 5, 3) --> (1, 40, 5)
# full namespace: MeshPreprocessing_comp
v236__006f = np.sum(v235__006d**2,axis=(3,))**(1 / 2)

# op _004Z_linear_combination_eval
# LANG: _004W, _004Y --> _004_
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: adapter_comp
v191__004_ = v189__004W+v190__004Y

# op _004u reshape_eval
# LANG: _004t --> _004v
# SHAPES: (1, 1, 5, 3) --> (1, 5, 3)
# full namespace: 
v169__004v = v168__004t.reshape((1, 5, 3))

# op _0050_power_combination_eval
# LANG: w --> _0051
# SHAPES: (1, 1) --> (1, 1)
# full namespace: adapter_comp
v192__0051 = (v215_w**2)
v192__0051 = v192__0051.reshape((1, 1))

# op _006A_decompose_eval
# LANG: _005t --> _006G, _006B, _006C, _006F
# SHAPES: (1, 41, 5, 3) --> (1, 40, 4, 3), (1, 40, 4, 3), (1, 40, 4, 3), (1, 40, 4, 3)
# full namespace: MeshPreprocessing_comp
v249__006B = ((v207__005t.flatten())[src_indices__006B__006A]).reshape((1, 40, 4, 3))
v250__006C = ((v207__005t.flatten())[src_indices__006C__006A]).reshape((1, 40, 4, 3))
v252__006F = ((v207__005t.flatten())[src_indices__006F__006A]).reshape((1, 40, 4, 3))
v253__006G = ((v207__005t.flatten())[src_indices__006G__006A]).reshape((1, 40, 4, 3))

# op _006V_power_combination_eval
# LANG: _006U --> _006W
# SHAPES: (1, 40, 4, 3) --> (1, 40, 4, 3)
# full namespace: MeshPreprocessing_comp
v262__006W = (v261__006U)
v262__006W = (v262__006W*_006V_coeff).reshape((1, 40, 4, 3))

# op _006Y_power_combination_eval
# LANG: _006X --> _006Z
# SHAPES: (1, 40, 4, 3) --> (1, 40, 4, 3)
# full namespace: MeshPreprocessing_comp
v264__006Z = (v263__006X)
v264__006Z = (v264__006Z*_006Y_coeff).reshape((1, 40, 4, 3))

# op _006g_decompose_eval
# LANG: _006f --> _006i, _006h
# SHAPES: (1, 40, 5) --> (1, 40, 4), (1, 40, 4)
# full namespace: MeshPreprocessing_comp
v237__006h = ((v236__006f.flatten())[src_indices__006h__006g]).reshape((1, 40, 4))
v238__006i = ((v236__006f.flatten())[src_indices__006i__006g]).reshape((1, 40, 4))

# op _003Y_power_combination_eval
# LANG: _003X --> _003Z
# SHAPES: (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: 
v153__003Z = (v152__003X)
v153__003Z = (v153__003Z*_003Y_coeff).reshape((1, 1, 5, 3))

# op _004w expand_array_eval
# LANG: _004v --> _004x
# SHAPES: (1, 5, 3) --> (1, 58, 5, 3)
# full namespace: 
v170__004x = np.einsum('acd,b->abcd', v169__004v.reshape((1, 5, 3)) ,np.ones((58,))).reshape((1, 58, 5, 3))

# op _0052_linear_combination_eval
# LANG: _004_, _0051 --> v_inf_sq
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: adapter_comp
v281_v_inf_sq = v191__004_+v192__0051

# op _006D_linear_combination_eval
# LANG: _006B, _006C --> _006E
# SHAPES: (1, 40, 4, 3), (1, 40, 4, 3) --> (1, 40, 4, 3)
# full namespace: MeshPreprocessing_comp
v251__006E = v249__006B+-1*v250__006C

# op _006H_linear_combination_eval
# LANG: _006F, _006G --> _006I
# SHAPES: (1, 40, 4, 3), (1, 40, 4, 3) --> (1, 40, 4, 3)
# full namespace: MeshPreprocessing_comp
v254__006I = v252__006F+-1*v253__006G

# op _006__linear_combination_eval
# LANG: _006W, _006Z --> _0070
# SHAPES: (1, 40, 4, 3), (1, 40, 4, 3) --> (1, 40, 4, 3)
# full namespace: MeshPreprocessing_comp
v265__0070 = v262__006W+v264__006Z

# op _006j_linear_combination_eval
# LANG: _006h, _006i --> _006k
# SHAPES: (1, 40, 4), (1, 40, 4) --> (1, 40, 4)
# full namespace: MeshPreprocessing_comp
v239__006k = v237__006h+v238__006i

# op _0072_power_combination_eval
# LANG: _0071 --> _0073
# SHAPES: (1, 40, 4, 3) --> (1, 40, 4, 3)
# full namespace: MeshPreprocessing_comp
v267__0073 = (v266__0071)
v267__0073 = (v267__0073*_0072_coeff).reshape((1, 40, 4, 3))

# op _00ii_decompose_eval
# LANG: gamma_b --> eel_gamma_b
# SHAPES: (1, 160) --> (1, 160)
# full namespace: seperate_gamma_b
v641_eel_gamma_b = ((v640_gamma_b.flatten())[src_indices_eel_gamma_b__00ii]).reshape((1, 160))

# op _003__power_combination_eval
# LANG: _003Z --> _0040
# SHAPES: (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: 
v154__0040 = (v153__003Z)
v154__0040 = (v154__0040*_003__coeff).reshape((1, 1, 5, 3))

# op _003x_decompose_eval
# LANG: eel_gamma_b --> _003y
# SHAPES: (1, 160) --> (1, 4)
# full namespace: 
v137__003y = ((v641_eel_gamma_b.flatten())[src_indices__003y__003x]).reshape((1, 4))

# op _004z_linear_combination_eval
# LANG: _004x, _004y --> _004A
# SHAPES: (1, 58, 5, 3), (1, 58, 5, 3) --> (1, 58, 5, 3)
# full namespace: 
v172__004A = v170__004x+v171__004y

# op _006J cross_product_eval
# LANG: _006E, _006I --> _006K
# SHAPES: (1, 40, 4, 3), (1, 40, 4, 3) --> (1, 40, 4, 3)
# full namespace: MeshPreprocessing_comp
v255__006K = np.cross(v251__006E, v254__006I, axisa = 3, axisb = 3, axisc = 3)

# op _006l_power_combination_eval
# LANG: _006k --> eel_chord_length
# SHAPES: (1, 40, 4) --> (1, 40, 4)
# full namespace: MeshPreprocessing_comp
v240_eel_chord_length = (v239__006k)
v240_eel_chord_length = (v240_eel_chord_length*_006l_coeff).reshape((1, 40, 4))

# op _006p_linear_combination_eval
# LANG: _006n, _006o --> _006q
# SHAPES: (1, 41, 4, 3), (1, 41, 4, 3) --> (1, 41, 4, 3)
# full namespace: MeshPreprocessing_comp
v243__006q = v241__006n+-1*v242__006o

# op _0074_linear_combination_eval
# LANG: _0070, _0073 --> _0075
# SHAPES: (1, 40, 4, 3), (1, 40, 4, 3) --> (1, 40, 4, 3)
# full namespace: MeshPreprocessing_comp
v268__0075 = v265__0070+v267__0073

# op _0076_power_combination_eval
# LANG: _0065 --> _0077
# SHAPES: (1, 40, 4, 3) --> (1, 40, 4, 3)
# full namespace: MeshPreprocessing_comp
v269__0077 = (v231__0065)
v269__0077 = (v269__0077*_0076_coeff).reshape((1, 40, 4, 3))

# op _007z_power_combination_eval
# LANG: v_inf_sq --> _007A
# SHAPES: (1, 1) --> (1, 1)
# full namespace: MeshPreprocessing_comp
v284__007A = (v281_v_inf_sq**0.5)
v284__007A = v284__007A.reshape((1, 1))

# op _003B_decompose_eval
# LANG: eel_gamma_w --> _003J, _003C, _003I
# SHAPES: (1, 59, 4) --> (1, 58, 4), (1, 1, 4), (1, 58, 4)
# full namespace: 
v139__003C = ((v290_eel_gamma_w.flatten())[src_indices__003C__003B]).reshape((1, 1, 4))
v142__003I = ((v290_eel_gamma_w.flatten())[src_indices__003I__003B]).reshape((1, 58, 4))
v143__003J = ((v290_eel_gamma_w.flatten())[src_indices__003J__003B]).reshape((1, 58, 4))

# op _003z reshape_eval
# LANG: _003y --> _003A
# SHAPES: (1, 4) --> (1, 1, 4)
# full namespace: 
v138__003A = v137__003y.reshape((1, 1, 4))

# op _0041_linear_combination_eval
# LANG: _003V, _0040 --> _0042
# SHAPES: (1, 1, 5, 3), (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: 
v155__0042 = v151__003V+v154__0040

# op _004C_linear_combination_eval
# LANG: _004A, _004B --> _004D
# SHAPES: (1, 58, 5, 3), (1, 58, 5, 3) --> (1, 58, 5, 3)
# full namespace: 
v174__004D = v172__004A+-1*v173__004B

# op _004F_power_combination_eval
# LANG: _004E --> _004G
# SHAPES: (1, 58, 5, 3) --> (1, 58, 5, 3)
# full namespace: 
v176__004G = (v175__004E)
v176__004G = (v176__004G*_004F_coeff).reshape((1, 58, 5, 3))

# op _006L_power_combination_eval
# LANG: _006K --> _006M
# SHAPES: (1, 40, 4, 3) --> (1, 40, 4, 3)
# full namespace: MeshPreprocessing_comp
v256__006M = (v255__006K**2)
v256__006M = v256__006M.reshape((1, 40, 4, 3))

# op _006r pnorm_axis_eval
# LANG: _006q --> _006s
# SHAPES: (1, 41, 4, 3) --> (1, 41, 4)
# full namespace: MeshPreprocessing_comp
v244__006s = np.sum(v243__006q**2,axis=(3,))**(1 / 2)

# op _0078_linear_combination_eval
# LANG: _0075, _0077 --> _0079
# SHAPES: (1, 40, 4, 3), (1, 40, 4, 3) --> (1, 40, 4, 3)
# full namespace: MeshPreprocessing_comp
v270__0079 = v268__0075+v269__0077

# op _007B_power_combination_eval
# LANG: density, _007A --> _007C
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: MeshPreprocessing_comp
v285__007C = (v280_density)*(v284__007A)
v285__007C = v285__007C.reshape((1, 1))

# op _007f_power_combination_eval
# LANG: _006U --> _007g
# SHAPES: (1, 40, 4, 3) --> (1, 40, 4, 3)
# full namespace: MeshPreprocessing_comp
v273__007g = (v261__006U)
v273__007g = (v273__007g*_007f_coeff).reshape((1, 40, 4, 3))

# op _007h_power_combination_eval
# LANG: _0071 --> _007i
# SHAPES: (1, 40, 4, 3) --> (1, 40, 4, 3)
# full namespace: MeshPreprocessing_comp
v274__007i = (v266__0071)
v274__007i = (v274__007i*_007h_coeff).reshape((1, 40, 4, 3))

# op _007v_single_tensor_sum_with_axis_eval
# LANG: eel_chord_length --> _007w
# SHAPES: (1, 40, 4) --> (1, 4)
# full namespace: MeshPreprocessing_comp
v282__007w = np.sum(v240_eel_chord_length, axis = (1,)).reshape((1, 4))

# op _003D_linear_combination_eval
# LANG: _003A, _003C --> _003E
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: 
v140__003E = v138__003A+-1*v139__003C

# op _003K_linear_combination_eval
# LANG: _003I, _003J --> _003L
# SHAPES: (1, 58, 4), (1, 58, 4) --> (1, 58, 4)
# full namespace: 
v144__003L = v142__003I+-1*v143__003J

# op _0045_linear_combination_eval
# LANG: _0042, _0044 --> _0046
# SHAPES: (1, 1, 5, 3), (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: 
v157__0046 = v155__0042+-1*v156__0044

# op _004H_linear_combination_eval
# LANG: _004D, _004G --> _004I
# SHAPES: (1, 58, 5, 3), (1, 58, 5, 3) --> (1, 58, 5, 3)
# full namespace: 
v177__004I = v174__004D+v176__004G

# op _006N_single_tensor_sum_with_axis_eval
# LANG: _006M --> _006O
# SHAPES: (1, 40, 4, 3) --> (1, 40, 4)
# full namespace: MeshPreprocessing_comp
v257__006O = np.sum(v256__006M, axis = (3,)).reshape((1, 40, 4))

# op _006t_decompose_eval
# LANG: _006s --> _006v, _006u
# SHAPES: (1, 41, 4) --> (1, 40, 4), (1, 40, 4)
# full namespace: MeshPreprocessing_comp
v245__006u = ((v244__006s.flatten())[src_indices__006u__006t]).reshape((1, 40, 4))
v246__006v = ((v244__006s.flatten())[src_indices__006v__006t]).reshape((1, 40, 4))

# op _007D expand_array_eval
# LANG: _007C --> _007E
# SHAPES: (1, 1) --> (1, 4, 1)
# full namespace: MeshPreprocessing_comp
v286__007E = np.einsum('ac,b->abc', v285__007C.reshape((1, 1)) ,np.ones((4,))).reshape((1, 4, 1))

# op _007a reshape_eval
# LANG: _0079 --> _007b
# SHAPES: (1, 40, 4, 3) --> (1, 160, 3)
# full namespace: MeshPreprocessing_comp
v271__007b = v270__0079.reshape((1, 160, 3))

# op _007j_linear_combination_eval
# LANG: _007g, _007i --> _007k
# SHAPES: (1, 40, 4, 3), (1, 40, 4, 3) --> (1, 40, 4, 3)
# full namespace: MeshPreprocessing_comp
v275__007k = v273__007g+v274__007i

# op _007l_power_combination_eval
# LANG: _006X --> _007m
# SHAPES: (1, 40, 4, 3) --> (1, 40, 4, 3)
# full namespace: MeshPreprocessing_comp
v276__007m = (v263__006X)
v276__007m = (v276__007m*_007l_coeff).reshape((1, 40, 4, 3))

# op _007x reshape_eval
# LANG: _007w --> _007y
# SHAPES: (1, 4) --> (1, 4, 1)
# full namespace: MeshPreprocessing_comp
v283__007y = v282__007w.reshape((1, 4, 1))

# op _003F_power_combination_eval
# LANG: _003E --> _003G
# SHAPES: (1, 1, 4) --> (1, 1, 4)
# full namespace: 
v141__003G = (v140__003E)
v141__003G = (v141__003G*_003F_coeff).reshape((1, 1, 4))

# op _003M_power_combination_eval
# LANG: _003L --> _003N
# SHAPES: (1, 58, 4) --> (1, 58, 4)
# full namespace: 
v145__003N = (v144__003L)
v145__003N = (v145__003N*_003M_coeff).reshape((1, 58, 4))

# op _0047_power_combination_eval
# LANG: _0046 --> _0048
# SHAPES: (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: 
v158__0048 = (v157__0046)
v158__0048 = (v158__0048*_0047_coeff).reshape((1, 1, 5, 3))

# op _004J_power_combination_eval
# LANG: _004I --> _004K
# SHAPES: (1, 58, 5, 3) --> (1, 58, 5, 3)
# full namespace: 
v178__004K = (v177__004I)
v178__004K = (v178__004K*_004J_coeff).reshape((1, 58, 5, 3))

# op _006P_power_combination_eval
# LANG: _006O --> _006Q
# SHAPES: (1, 40, 4) --> (1, 40, 4)
# full namespace: MeshPreprocessing_comp
v258__006Q = (v257__006O**0.5)
v258__006Q = v258__006Q.reshape((1, 40, 4))

# op _006w_linear_combination_eval
# LANG: _006u, _006v --> _006x
# SHAPES: (1, 40, 4), (1, 40, 4) --> (1, 40, 4)
# full namespace: MeshPreprocessing_comp
v247__006x = v245__006u+v246__006v

# op _007F_power_combination_eval
# LANG: _007E, _007y --> _007G
# SHAPES: (1, 4, 1), (1, 4, 1) --> (1, 4, 1)
# full namespace: MeshPreprocessing_comp
v287__007G = (v286__007E)*(v283__007y)
v287__007G = v287__007G.reshape((1, 4, 1))

# op _007c_linear_combination_eval
# LANG: _007b --> _007d
# SHAPES: (1, 160, 3) --> (1, 160, 3)
# full namespace: MeshPreprocessing_comp
v272__007d = -1*v271__007b

# op _007n_linear_combination_eval
# LANG: _007k, _007m --> _007o
# SHAPES: (1, 40, 4, 3), (1, 40, 4, 3) --> (1, 40, 4, 3)
# full namespace: MeshPreprocessing_comp
v277__007o = v275__007k+v276__007m

# op _007p_power_combination_eval
# LANG: _0065 --> _007q
# SHAPES: (1, 40, 4, 3) --> (1, 40, 4, 3)
# full namespace: MeshPreprocessing_comp
v278__007q = (v231__0065)
v278__007q = (v278__007q*_007p_coeff).reshape((1, 40, 4, 3))

# op _003H_indexed_passthrough_eval
# LANG: _003G, _003N --> eel_dgammaw_dt
# SHAPES: (1, 1, 4), (1, 58, 4) --> (1, 59, 4)
# full namespace: 
v136_eel_dgammaw_dt__temp[i_v141__003G__003H_indexed_passthrough_eval] = v141__003G.flatten()
v136_eel_dgammaw_dt = v136_eel_dgammaw_dt__temp.copy()
v136_eel_dgammaw_dt__temp[i_v145__003N__003H_indexed_passthrough_eval] = v145__003N.flatten()
v136_eel_dgammaw_dt = v136_eel_dgammaw_dt__temp.copy()

# op _0049_indexed_passthrough_eval
# LANG: _0048, _004K --> eel_dwake_coords_dt
# SHAPES: (1, 1, 5, 3), (1, 58, 5, 3) --> (1, 59, 5, 3)
# full namespace: 
v150_eel_dwake_coords_dt__temp[i_v158__0048__0049_indexed_passthrough_eval] = v158__0048.flatten()
v150_eel_dwake_coords_dt = v150_eel_dwake_coords_dt__temp.copy()
v150_eel_dwake_coords_dt__temp[i_v178__004K__0049_indexed_passthrough_eval] = v178__004K.flatten()
v150_eel_dwake_coords_dt = v150_eel_dwake_coords_dt__temp.copy()

# op _005g_linear_combination_eval
# LANG: theta, gamma --> alpha
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: adapter_comp
v200_alpha = v185_theta+-1*v187_gamma

# op _005i_linear_combination_eval
# LANG: psi, psiw --> beta
# SHAPES: (1, 1), (1, 1) --> (1, 1)
# full namespace: adapter_comp
v201_beta = v186_psi+v188_psiw

# op _006R_power_combination_eval
# LANG: _006Q --> eel_s_panel
# SHAPES: (1, 40, 4) --> (1, 40, 4)
# full namespace: MeshPreprocessing_comp
v259_eel_s_panel = (v258__006Q)
v259_eel_s_panel = (v259_eel_s_panel*_006R_coeff).reshape((1, 40, 4))

# op _006y_power_combination_eval
# LANG: _006x --> eel_span_length
# SHAPES: (1, 40, 4) --> (1, 40, 4)
# full namespace: MeshPreprocessing_comp
v248_eel_span_length = (v247__006x)
v248_eel_span_length = (v248_eel_span_length*_006y_coeff).reshape((1, 40, 4))

# op _007H_power_combination_eval
# LANG: _007G --> eel_re_span
# SHAPES: (1, 4, 1) --> (1, 4, 1)
# full namespace: MeshPreprocessing_comp
v288_eel_re_span = (v287__007G)
v288_eel_re_span = (v288_eel_re_span*_007H_coeff).reshape((1, 4, 1))

# op _007e_indexed_passthrough_eval
# LANG: _007d --> bd_vec
# SHAPES: (1, 160, 3) --> (1, 160, 3)
# full namespace: MeshPreprocessing_comp
v260_bd_vec__temp[i_v272__007d__007e_indexed_passthrough_eval] = v272__007d.flatten()
v260_bd_vec = v260_bd_vec__temp.copy()

# op _007r_linear_combination_eval
# LANG: _007o, _007q --> eel_eval_pts_coords
# SHAPES: (1, 40, 4, 3), (1, 40, 4, 3) --> (1, 40, 4, 3)
# full namespace: MeshPreprocessing_comp
v279_eel_eval_pts_coords = v277__007o+v278__007q

# op _009l_indexed_passthrough_eval
# LANG: _009i --> normal_concatenated_b
# SHAPES: (1, 160, 3) --> (1, 160, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_k_vel
v345_normal_concatenated_b__temp[i_v348__009i__009l_indexed_passthrough_eval] = v348__009i.flatten()
v345_normal_concatenated_b = v345_normal_concatenated_b__temp.copy()