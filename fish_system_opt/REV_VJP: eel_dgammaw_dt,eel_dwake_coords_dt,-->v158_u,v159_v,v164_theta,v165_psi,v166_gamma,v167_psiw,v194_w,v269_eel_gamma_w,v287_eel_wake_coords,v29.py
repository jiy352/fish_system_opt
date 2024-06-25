

# REV_VJP: eel_dgammaw_dt,eel_dwake_coords_dt,-->v158_u,v159_v,v164_theta,v165_psi,v166_gamma,v167_psiw,v194_w,v269_eel_gamma_w,v287_eel_wake_coords,v294_p,v295_q,v296_r,v306_eel_coll_vel,v311_eel,

# REV_VJP: eel_dgammaw_dt,eel_dwake_coords_dt,-->v158_u,v159_v,v164_theta,v165_psi,v166_gamma,v167_psiw,v194_w,v269_eel_gamma_w,v287_eel_wake_coords,v294_p,v295_q,v296_r,v306_eel_coll_vel,v311_eel,
path_to_v115_eel_dgammaw_dt = r_seed_v115_eel_dgammaw_dt
path_to_v129_eel_dwake_coords_dt = r_seed_v129_eel_dwake_coords_dt

# op _003y_indexed_passthrough_eval
# LANG: _003x, _0048 --> eel_dwake_coords_dt
# SHAPES: (1, 1, 5, 3), (1, 68, 5, 3) --> (1, 69, 5, 3)
# full namespace: 

# _003y_indexed_passthrough_eval_pv129_eel_dwake_coords_dt_pv157__0048
path_to_v137__003x = STD_MULT(path_to_v129_eel_dwake_coords_dt,pv129_eel_dwake_coords_dt_pv137__003x)
path_to_v157__0048 = STD_MULT(path_to_v129_eel_dwake_coords_dt,pv129_eel_dwake_coords_dt_pv157__0048)

# op _0035_indexed_passthrough_eval
# LANG: _0034, _003b --> eel_dgammaw_dt
# SHAPES: (1, 1, 4), (1, 68, 4) --> (1, 69, 4)
# full namespace: 

# _0035_indexed_passthrough_eval_pv115_eel_dgammaw_dt_pv124__003b
path_to_v120__0034 = STD_MULT(path_to_v115_eel_dgammaw_dt,pv115_eel_dgammaw_dt_pv120__0034)
path_to_v124__003b = STD_MULT(path_to_v115_eel_dgammaw_dt,pv115_eel_dgammaw_dt_pv124__003b)

# op _0047_power_combination_eval
# LANG: _0046 --> _0048
# SHAPES: (1, 68, 5, 3) --> (1, 68, 5, 3)
# full namespace: 

# _0047_power_combination_eval_pv157__0048_pv156__0046
temp_power = _0047_coeff_temp*1
pv157__0048_pv156__0046 = temp_power.flatten()
path_to_v156__0046 = DIAG_MULT(path_to_v157__0048,pv157__0048_pv156__0046)
del pv157__0048_pv156__0046
del path_to_v157__0048

# op _003w_power_combination_eval
# LANG: _003v --> _003x
# SHAPES: (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: 

# _003w_power_combination_eval_pv137__003x_pv136__003v
temp_power = _003w_coeff_temp*1
pv137__003x_pv136__003v = temp_power.flatten()
path_to_v136__003v = DIAG_MULT(path_to_v137__003x,pv137__003x_pv136__003v)
del path_to_v137__003x
del pv137__003x_pv136__003v

# op _003a_power_combination_eval
# LANG: _0039 --> _003b
# SHAPES: (1, 68, 4) --> (1, 68, 4)
# full namespace: 

# _003a_power_combination_eval_pv124__003b_pv123__0039
temp_power = _003a_coeff_temp*1
pv124__003b_pv123__0039 = temp_power.flatten()
path_to_v123__0039 = DIAG_MULT(path_to_v124__003b,pv124__003b_pv123__0039)
del pv124__003b_pv123__0039
del path_to_v124__003b

# op _0033_power_combination_eval
# LANG: _0032 --> _0034
# SHAPES: (1, 1, 4) --> (1, 1, 4)
# full namespace: 

# _0033_power_combination_eval_pv120__0034_pv119__0032
temp_power = _0033_coeff_temp*1
pv120__0034_pv119__0032 = temp_power.flatten()
path_to_v119__0032 = DIAG_MULT(path_to_v120__0034,pv120__0034_pv119__0032)
del pv120__0034_pv119__0032
del path_to_v120__0034

# op _0045_linear_combination_eval
# LANG: _0041, _0044 --> _0046
# SHAPES: (1, 68, 5, 3), (1, 68, 5, 3) --> (1, 68, 5, 3)
# full namespace: 

# _0045_linear_combination_eval_pv156__0046_pv155__0044
path_to_v153__0041 = DIAG_MULT(path_to_v156__0046,pv156__0046_pv153__0041)
path_to_v155__0044 = DIAG_MULT(path_to_v156__0046,pv156__0046_pv155__0044)
del path_to_v156__0046

# op _003u_linear_combination_eval
# LANG: _003r, _003t --> _003v
# SHAPES: (1, 1, 5, 3), (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: 

# _003u_linear_combination_eval_pv136__003v_pv135__003t
path_to_v134__003r = DIAG_MULT(path_to_v136__003v,pv136__003v_pv134__003r)
path_to_v135__003t = DIAG_MULT(path_to_v136__003v,pv136__003v_pv135__003t)
del path_to_v136__003v

# op _0038_linear_combination_eval
# LANG: _0036, _0037 --> _0039
# SHAPES: (1, 68, 4), (1, 68, 4) --> (1, 68, 4)
# full namespace: 

# _0038_linear_combination_eval_pv123__0039_pv122__0037
path_to_v121__0036 = DIAG_MULT(path_to_v123__0039,pv123__0039_pv121__0036)
path_to_v122__0037 = DIAG_MULT(path_to_v123__0039,pv123__0039_pv122__0037)
del path_to_v123__0039

# op _0031_linear_combination_eval
# LANG: _002Z, _0030 --> _0032
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: 

# _0031_linear_combination_eval_pv119__0032_pv118__0030
path_to_v117__002Z = DIAG_MULT(path_to_v119__0032,pv119__0032_pv117__002Z)
path_to_v118__0030 = DIAG_MULT(path_to_v119__0032,pv119__0032_pv118__0030)
del path_to_v119__0032

# op _0043_power_combination_eval
# LANG: _0042 --> _0044
# SHAPES: (1, 68, 5, 3) --> (1, 68, 5, 3)
# full namespace: 

# _0043_power_combination_eval_pv155__0044_pv154__0042
temp_power = _0043_coeff_temp*1
pv155__0044_pv154__0042 = temp_power.flatten()
path_to_v154__0042 = DIAG_MULT(path_to_v155__0044,pv155__0044_pv154__0042)
del pv155__0044_pv154__0042
del path_to_v155__0044

# op _0040_linear_combination_eval
# LANG: _003Z, _003_ --> _0041
# SHAPES: (1, 68, 5, 3), (1, 68, 5, 3) --> (1, 68, 5, 3)
# full namespace: 

# _0040_linear_combination_eval_pv153__0041_pv152__003_
path_to_v151__003Z = DIAG_MULT(path_to_v153__0041,pv153__0041_pv151__003Z)
path_to_v152__003_ = DIAG_MULT(path_to_v153__0041,pv153__0041_pv152__003_)
del path_to_v153__0041

# op _003q_linear_combination_eval
# LANG: _003j, _003p --> _003r
# SHAPES: (1, 1, 5, 3), (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: 

# _003q_linear_combination_eval_pv134__003r_pv133__003p
path_to_v130__003j = DIAG_MULT(path_to_v134__003r,pv134__003r_pv130__003j)
path_to_v133__003p = DIAG_MULT(path_to_v134__003r,pv134__003r_pv133__003p)
del path_to_v134__003r

# op _002__decompose_eval
# LANG: eel_gamma_w --> _0037, _0030, _0036
# SHAPES: (1, 69, 4) --> (1, 68, 4), (1, 1, 4), (1, 68, 4)
# full namespace: 

# _002__decompose_eval_pv121__0036_pv269_eel_gamma_w
path_to_v269_eel_gamma_w = STD_MULT(path_to_v122__0037,pv122__0037_pv269_eel_gamma_w)
path_to_v269_eel_gamma_w += STD_MULT(path_to_v118__0030,pv118__0030_pv269_eel_gamma_w)
path_to_v269_eel_gamma_w += STD_MULT(path_to_v121__0036,pv121__0036_pv269_eel_gamma_w)
del path_to_v121__0036
del path_to_v122__0037
del path_to_v118__0030

# op _002Y reshape_eval
# LANG: _002X --> _002Z
# SHAPES: (1, 4) --> (1, 1, 4)
# full namespace: 

# _002Y reshape_eval_pv117__002Z_pv116__002X
path_to_v116__002X = DIAG_MULT(path_to_v117__002Z,pv117__002Z_pv116__002X)
del path_to_v117__002Z

# op _003o_power_combination_eval
# LANG: _003n --> _003p
# SHAPES: (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: 

# _003o_power_combination_eval_pv133__003p_pv132__003n
temp_power = _003o_coeff_temp*1
pv133__003p_pv132__003n = temp_power.flatten()
path_to_v132__003n = DIAG_MULT(path_to_v133__003p,pv133__003p_pv132__003n)
del pv133__003p_pv132__003n
del path_to_v133__003p

# op _003Y_linear_combination_eval
# LANG: _003W, _003X --> _003Z
# SHAPES: (1, 68, 5, 3), (1, 68, 5, 3) --> (1, 68, 5, 3)
# full namespace: 

# _003Y_linear_combination_eval_pv151__003Z_pv150__003X
path_to_v149__003W = DIAG_MULT(path_to_v151__003Z,pv151__003Z_pv149__003W)
path_to_v150__003X = DIAG_MULT(path_to_v151__003Z,pv151__003Z_pv150__003X)
del path_to_v151__003Z

# op _002W_decompose_eval
# LANG: eel_gamma_b --> _002X
# SHAPES: (1, 200) --> (1, 4)
# full namespace: 

# _002W_decompose_eval_pv116__002X_pv620_eel_gamma_b
path_to_v620_eel_gamma_b = STD_MULT(path_to_v116__002X,pv116__002X_pv620_eel_gamma_b)
del path_to_v116__002X

# op _00hH_decompose_eval
# LANG: gamma_b --> eel_gamma_b
# SHAPES: (1, 200) --> (1, 200)
# full namespace: seperate_gamma_b

# _00hH_decompose_eval_pv620_eel_gamma_b_pv619_gamma_b
path_to_v619_gamma_b = STD_MULT(path_to_v620_eel_gamma_b,pv620_eel_gamma_b_pv619_gamma_b)
del path_to_v620_eel_gamma_b

# op _003m_power_combination_eval
# LANG: _003l --> _003n
# SHAPES: (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: 

# _003m_power_combination_eval_pv132__003n_pv131__003l
temp_power = _003m_coeff_temp*1
pv132__003n_pv131__003l = temp_power.flatten()
path_to_v131__003l = DIAG_MULT(path_to_v132__003n,pv132__003n_pv131__003l)
del path_to_v132__003n
del pv132__003n_pv131__003l

# op _003V expand_array_eval
# LANG: _003U --> _003W
# SHAPES: (1, 5, 3) --> (1, 68, 5, 3)
# full namespace: 

# _003V expand_array_eval_pv149__003W_pv148__003U
path_to_v148__003U = STD_MULT(path_to_v149__003W,pv149__003W_pv148__003U)
del path_to_v149__003W

# op _003T reshape_eval
# LANG: _003S --> _003U
# SHAPES: (1, 1, 5, 3) --> (1, 5, 3)
# full namespace: 

# _003T reshape_eval_pv148__003U_pv147__003S
path_to_v147__003S = DIAG_MULT(path_to_v148__003U,pv148__003U_pv147__003S)
del path_to_v148__003U

# op _003R_linear_combination_eval
# LANG: _003Q, _003t --> _003S
# SHAPES: (1, 1, 5, 3), (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: 

# _003R_linear_combination_eval_pv147__003S_pv135__003t
path_to_v146__003Q = DIAG_MULT(path_to_v147__003S,pv147__003S_pv146__003Q)
path_to_v135__003t += DIAG_MULT(path_to_v147__003S,pv147__003S_pv135__003t)
del path_to_v147__003S

# op _003s_decompose_eval
# LANG: eel_wake_coords --> _003_, _003t, _003X
# SHAPES: (1, 69, 5, 3) --> (1, 68, 5, 3), (1, 1, 5, 3), (1, 68, 5, 3)
# full namespace: 

# _003s_decompose_eval_pv150__003X_pv287_eel_wake_coords
path_to_v287_eel_wake_coords = STD_MULT(path_to_v152__003_,pv152__003__pv287_eel_wake_coords)
path_to_v287_eel_wake_coords += STD_MULT(path_to_v135__003t,pv135__003t_pv287_eel_wake_coords)
path_to_v287_eel_wake_coords += STD_MULT(path_to_v150__003X,pv150__003X_pv287_eel_wake_coords)
del path_to_v135__003t
del path_to_v150__003X
del path_to_v152__003_

# op _003P_linear_combination_eval
# LANG: _003j, _003O --> _003Q
# SHAPES: (1, 1, 5, 3), (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: 

# _003P_linear_combination_eval_pv146__003Q_pv145__003O
path_to_v130__003j += DIAG_MULT(path_to_v146__003Q,pv146__003Q_pv130__003j)
path_to_v145__003O = DIAG_MULT(path_to_v146__003Q,pv146__003Q_pv145__003O)
del path_to_v146__003Q

# op _003i_decompose_eval
# LANG: eel_bd_vtx_coords --> _003j
# SHAPES: (1, 51, 5, 3) --> (1, 1, 5, 3)
# full namespace: 

# _003i_decompose_eval_pv130__003j_pv514_eel_bd_vtx_coords
path_to_v514_eel_bd_vtx_coords = STD_MULT(path_to_v130__003j,pv130__003j_pv514_eel_bd_vtx_coords)
del path_to_v130__003j

# op _003N_power_combination_eval
# LANG: _003M --> _003O
# SHAPES: (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: 

# _003N_power_combination_eval_pv145__003O_pv144__003M
temp_power = _003N_coeff_temp*1
pv145__003O_pv144__003M = temp_power.flatten()
path_to_v144__003M = DIAG_MULT(path_to_v145__003O,pv145__003O_pv144__003M)
del pv145__003O_pv144__003M
del path_to_v145__003O

# op _003L_power_combination_eval
# LANG: _003l --> _003M
# SHAPES: (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: 

# _003L_power_combination_eval_pv144__003M_pv131__003l
temp_power = _003L_coeff_temp*1
pv144__003M_pv131__003l = temp_power.flatten()
path_to_v131__003l += DIAG_MULT(path_to_v144__003M,pv144__003M_pv131__003l)
del pv144__003M_pv131__003l
del path_to_v144__003M

# op _003k_decompose_eval
# LANG: eel_wake_total_vel --> _0042, _003l
# SHAPES: (1, 69, 5, 3) --> (1, 68, 5, 3), (1, 1, 5, 3)
# full namespace: 

# _003k_decompose_eval_pv131__003l_pv622_eel_wake_total_vel
path_to_v622_eel_wake_total_vel = STD_MULT(path_to_v154__0042,pv154__0042_pv622_eel_wake_total_vel)
path_to_v622_eel_wake_total_vel += STD_MULT(path_to_v131__003l,pv131__003l_pv622_eel_wake_total_vel)
del path_to_v154__0042
del path_to_v131__003l

# op _00hL_linear_combination_eval
# LANG: eel_wake_kinematic_vel --> eel_wake_total_vel
# SHAPES: (1, 69, 5, 3) --> (1, 69, 5, 3)
# full namespace: ComputeWakeTotalVel

# _00hL_linear_combination_eval_pv622_eel_wake_total_vel_pv625_eel_wake_kinematic_vel
path_to_v625_eel_wake_kinematic_vel = DIAG_MULT(path_to_v622_eel_wake_total_vel,pv622_eel_wake_total_vel_pv625_eel_wake_kinematic_vel)
del path_to_v622_eel_wake_total_vel

# op _00hQ expand_array_eval
# LANG: _00hP --> eel_wake_kinematic_vel
# SHAPES: (1, 3) --> (1, 69, 5, 3)
# full namespace: ComputeWakeTotalVel.ComputeWakeKinematicVel

# _00hQ expand_array_eval_pv625_eel_wake_kinematic_vel_pv624__00hP
path_to_v624__00hP = STD_MULT(path_to_v625_eel_wake_kinematic_vel,pv625_eel_wake_kinematic_vel_pv624__00hP)
del path_to_v625_eel_wake_kinematic_vel

# op _00hO_linear_combination_eval
# LANG: frame_vel --> _00hP
# SHAPES: (1, 3) --> (1, 3)
# full namespace: ComputeWakeTotalVel.ComputeWakeKinematicVel

# _00hO_linear_combination_eval_pv624__00hP_pv623_frame_vel
path_to_v623_frame_vel = DIAG_MULT(path_to_v624__00hP,pv624__00hP_pv623_frame_vel)
del path_to_v624__00hP

# _007v_newton_implict_eval__007v
_007v_newton_path_in = _007v_newton.accumulate_rev(path_to_v619_gamma_b)
_007v_v618_aic_bd_proj = _007v_newton_path_in[0]
_007v_v507_M_mat = _007v_newton_path_in[1]
_007v_v281_gamma_w = _007v_newton_path_in[2]
_007v_v328_b = _007v_newton_path_in[3]
path_to_v328_b = _007v_v328_b
path_to_v618_aic_bd_proj = _007v_v618_aic_bd_proj
path_to_v507_M_mat = _007v_v507_M_mat
path_to_v281_gamma_w = _007v_v281_gamma_w
del path_to_v619_gamma_b

# op _0079_indexed_passthrough_eval
# LANG: eel_gamma_w --> gamma_w
# SHAPES: (1, 69, 4) --> (1, 69, 4)
# full namespace: combine_gamma_w

# _0079_indexed_passthrough_eval_pv281_gamma_w_pv269_eel_gamma_w
path_to_v269_eel_gamma_w += STD_MULT(path_to_v281_gamma_w,pv281_gamma_w_pv269_eel_gamma_w)
del path_to_v281_gamma_w

# op _00hE_custom_explicit_eval
# LANG: normal_concatenated_aic_bd_proj, aic_bd --> aic_bd_proj
# SHAPES: (1, 200, 3), (1, 200, 200, 3) --> (1, 200, 200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_aic_bd

# _00hE_custom_explicit_eval_pv618_aic_bd_proj_pv615_aic_bd
pv618_aic_bd_proj_pv614_normal_concatenated_aic_bd_proj = _00hE_custom_explicit_func_aic_bd_proj.get_custom_explicit_partials('aic_bd_proj', 'normal_concatenated_aic_bd_proj')
pv618_aic_bd_proj_pv615_aic_bd = _00hE_custom_explicit_func_aic_bd_proj.get_custom_explicit_partials('aic_bd_proj', 'aic_bd')
path_to_v614_normal_concatenated_aic_bd_proj = STD_MULT(path_to_v618_aic_bd_proj,pv618_aic_bd_proj_pv614_normal_concatenated_aic_bd_proj)
path_to_v615_aic_bd = STD_MULT(path_to_v618_aic_bd_proj,pv618_aic_bd_proj_pv615_aic_bd)
del pv618_aic_bd_proj_pv615_aic_bd
del pv618_aic_bd_proj_pv614_normal_concatenated_aic_bd_proj
del path_to_v618_aic_bd_proj

# op _00eg_custom_explicit_eval
# LANG: normal_concatenated_M_mat, aic_M --> M_mat
# SHAPES: (1, 200, 3), (1, 200, 276, 3) --> (1, 200, 276)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_aic

# _00eg_custom_explicit_eval_pv507_M_mat_pv504_aic_M
pv507_M_mat_pv503_normal_concatenated_M_mat = _00eg_custom_explicit_func_M_mat.get_custom_explicit_partials('M_mat', 'normal_concatenated_M_mat')
pv507_M_mat_pv504_aic_M = _00eg_custom_explicit_func_M_mat.get_custom_explicit_partials('M_mat', 'aic_M')
path_to_v503_normal_concatenated_M_mat = STD_MULT(path_to_v507_M_mat,pv507_M_mat_pv503_normal_concatenated_M_mat)
path_to_v504_aic_M = STD_MULT(path_to_v507_M_mat,pv507_M_mat_pv504_aic_M)
del pv507_M_mat_pv504_aic_M
del path_to_v507_M_mat
del pv507_M_mat_pv503_normal_concatenated_M_mat

# op _008I_custom_explicit_eval
# LANG: _008H, eel_kinematic_vel --> b
# SHAPES: (1, 200, 3), (1, 200, 3) --> (1, 200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_k_vel

# _008I_custom_explicit_eval_pv328_b_pv325_eel_kinematic_vel
pv328_b_pv327__008H = _008I_custom_explicit_func_b.get_custom_explicit_partials('b', '_008H')
pv328_b_pv325_eel_kinematic_vel = _008I_custom_explicit_func_b.get_custom_explicit_partials('b', 'eel_kinematic_vel')
path_to_v327__008H = STD_MULT(path_to_v328_b,pv328_b_pv327__008H)
path_to_v325_eel_kinematic_vel = STD_MULT(path_to_v328_b,pv328_b_pv325_eel_kinematic_vel)
del path_to_v328_b
del pv328_b_pv327__008H
del pv328_b_pv325_eel_kinematic_vel

# op _00hD_indexed_passthrough_eval
# LANG: _00hC --> normal_concatenated_aic_bd_proj
# SHAPES: (1, 200, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_aic_bd

# _00hD_indexed_passthrough_eval_pv614_normal_concatenated_aic_bd_proj_pv617__00hC
path_to_v617__00hC = STD_MULT(path_to_v614_normal_concatenated_aic_bd_proj,pv614_normal_concatenated_aic_bd_proj_pv617__00hC)
del path_to_v614_normal_concatenated_aic_bd_proj

# op _00ep_indexed_passthrough_eval
# LANG: _00eo --> aic_bd
# SHAPES: (1, 200, 200, 3) --> (1, 200, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd

# _00ep_indexed_passthrough_eval_pv615_aic_bd_pv512__00eo
path_to_v512__00eo = STD_MULT(path_to_v615_aic_bd,pv615_aic_bd_pv512__00eo)
del path_to_v615_aic_bd

# op _00ef_indexed_passthrough_eval
# LANG: _00ee --> normal_concatenated_M_mat
# SHAPES: (1, 200, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_aic

# _00ef_indexed_passthrough_eval_pv503_normal_concatenated_M_mat_pv506__00ee
path_to_v506__00ee = STD_MULT(path_to_v503_normal_concatenated_M_mat,pv503_normal_concatenated_M_mat_pv506__00ee)
del path_to_v503_normal_concatenated_M_mat

# op _008f_linear_combination_eval
# LANG: _008e --> eel_kinematic_vel
# SHAPES: (1, 200, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp

# _008f_linear_combination_eval_pv325_eel_kinematic_vel_pv309__008e
path_to_v309__008e = DIAG_MULT(path_to_v325_eel_kinematic_vel,pv325_eel_kinematic_vel_pv309__008e)
del path_to_v325_eel_kinematic_vel

# op _008S_indexed_passthrough_eval
# LANG: _008R --> aic_M
# SHAPES: (1, 200, 276, 3) --> (1, 200, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic

# _008S_indexed_passthrough_eval_pv504_aic_M_pv333__008R
path_to_v333__008R = STD_MULT(path_to_v504_aic_M,pv504_aic_M_pv333__008R)
del path_to_v504_aic_M

# op _008G reshape_eval
# LANG: eel_bd_vtx_normals --> _008H
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_k_vel

# _008G reshape_eval_pv327__008H_pv616_eel_bd_vtx_normals
path_to_v616_eel_bd_vtx_normals = DIAG_MULT(path_to_v327__008H,pv327__008H_pv616_eel_bd_vtx_normals)
del path_to_v327__008H

# op _00hB reshape_eval
# LANG: eel_bd_vtx_normals --> _00hC
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_aic_bd

# _00hB reshape_eval_pv617__00hC_pv616_eel_bd_vtx_normals
path_to_v616_eel_bd_vtx_normals += DIAG_MULT(path_to_v617__00hC,pv617__00hC_pv616_eel_bd_vtx_normals)
del path_to_v617__00hC

# op _00en reshape_eval
# LANG: aic_bd00 --> _00eo
# SHAPES: (1, 40000, 3) --> (1, 200, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd

# _00en reshape_eval_pv512__00eo_pv613_aic_bd00
path_to_v613_aic_bd00 = DIAG_MULT(path_to_v512__00eo,pv512__00eo_pv613_aic_bd00)
del path_to_v512__00eo

# op _00ed reshape_eval
# LANG: eel_bd_vtx_normals --> _00ee
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_aic

# _00ed reshape_eval_pv506__00ee_pv616_eel_bd_vtx_normals
path_to_v616_eel_bd_vtx_normals += DIAG_MULT(path_to_v506__00ee,pv506__00ee_pv616_eel_bd_vtx_normals)
del path_to_v506__00ee

# op _008d_linear_combination_eval
# LANG: _008a, _008c --> _008e
# SHAPES: (1, 200, 3), (1, 200, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp

# _008d_linear_combination_eval_pv309__008e_pv308__008c
path_to_v307__008a = DIAG_MULT(path_to_v309__008e,pv309__008e_pv307__008a)
path_to_v308__008c = DIAG_MULT(path_to_v309__008e,pv309__008e_pv308__008c)
del path_to_v309__008e

# op _008Q reshape_eval
# LANG: aic_M00 --> _008R
# SHAPES: (1, 55200, 3) --> (1, 200, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic

# _008Q reshape_eval_pv333__008R_pv502_aic_M00
path_to_v502_aic_M00 = DIAG_MULT(path_to_v333__008R,pv333__008R_pv502_aic_M00)
del path_to_v333__008R

# op _00hw_linear_combination_eval
# LANG: _00hv, _00hr --> aic_bd00
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00hw_linear_combination_eval_pv613_aic_bd00_pv610__00hr
path_to_v612__00hv = DIAG_MULT(path_to_v613_aic_bd00,pv613_aic_bd00_pv612__00hv)
path_to_v610__00hr = DIAG_MULT(path_to_v613_aic_bd00,pv613_aic_bd00_pv610__00hr)
del path_to_v613_aic_bd00

# op _00e8_linear_combination_eval
# LANG: _00e7, _00e3 --> aic_M00
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00e8_linear_combination_eval_pv502_aic_M00_pv499__00e3
path_to_v501__00e7 = DIAG_MULT(path_to_v502_aic_M00,pv502_aic_M00_pv501__00e7)
path_to_v499__00e3 = DIAG_MULT(path_to_v502_aic_M00,pv502_aic_M00_pv499__00e3)
del path_to_v502_aic_M00

# op _008b reshape_eval
# LANG: eel_coll_vel --> _008c
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp

# _008b reshape_eval_pv308__008c_pv306_eel_coll_vel
path_to_v306_eel_coll_vel = DIAG_MULT(path_to_v308__008c,pv308__008c_pv306_eel_coll_vel)
del path_to_v308__008c

# op _008B_power_combination_eval
# LANG: _008s, _008A --> eel_bd_vtx_normals
# SHAPES: (1, 50, 4, 3), (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal

# _008B_power_combination_eval_pv616_eel_bd_vtx_normals_pv322__008A
temp_power = _008B_coeff_temp*1*(v322__008A**-1)
pv616_eel_bd_vtx_normals_pv318__008s = temp_power.flatten()
temp_power = _008B_coeff_temp*(v318__008s)*-1*(v322__008A**-2.0)
pv616_eel_bd_vtx_normals_pv322__008A = temp_power.flatten()
path_to_v318__008s = DIAG_MULT(path_to_v616_eel_bd_vtx_normals,pv616_eel_bd_vtx_normals_pv318__008s)
path_to_v322__008A = DIAG_MULT(path_to_v616_eel_bd_vtx_normals,pv616_eel_bd_vtx_normals_pv322__008A)
del pv616_eel_bd_vtx_normals_pv318__008s
del pv616_eel_bd_vtx_normals_pv322__008A
del path_to_v616_eel_bd_vtx_normals

# op _0089_linear_combination_eval
# LANG: _0085, _0087 --> _008a
# SHAPES: (1, 200, 3), (1, 200, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp

# _0089_linear_combination_eval_pv307__008a_pv305__0087
path_to_v304__0085 = DIAG_MULT(path_to_v307__008a,pv307__008a_pv304__0085)
path_to_v305__0087 = DIAG_MULT(path_to_v307__008a,pv307__008a_pv305__0087)
del path_to_v307__008a

# op _00hu_linear_combination_eval
# LANG: _00ht, _00h1 --> _00hv
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00hu_linear_combination_eval_pv612__00hv_pv597__00h1
path_to_v611__00ht = DIAG_MULT(path_to_v612__00hv,pv612__00hv_pv611__00ht)
path_to_v597__00h1 = DIAG_MULT(path_to_v612__00hv,pv612__00hv_pv597__00h1)
del path_to_v612__00hv

# op _00hq_power_combination_eval
# LANG: _00hp, _00h5 --> _00hr
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00hq_power_combination_eval_pv610__00hr_pv599__00h5
temp_power = _00hq_coeff_temp*1*(v599__00h5)
pv610__00hr_pv609__00hp = temp_power.flatten()
temp_power = _00hq_coeff_temp*(v609__00hp)*1
pv610__00hr_pv599__00h5 = temp_power.flatten()
path_to_v609__00hp = DIAG_MULT(path_to_v610__00hr,pv610__00hr_pv609__00hp)
path_to_v599__00h5 = DIAG_MULT(path_to_v610__00hr,pv610__00hr_pv599__00h5)
del path_to_v610__00hr
del pv610__00hr_pv609__00hp
del pv610__00hr_pv599__00h5

# op _00e6_linear_combination_eval
# LANG: _00e5, _00d6 --> _00e7
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00e6_linear_combination_eval_pv501__00e7_pv469__00d6
path_to_v500__00e5 = DIAG_MULT(path_to_v501__00e7,pv501__00e7_pv500__00e5)
path_to_v469__00d6 = DIAG_MULT(path_to_v501__00e7,pv501__00e7_pv469__00d6)
del path_to_v501__00e7

# op _00e2_power_combination_eval
# LANG: _00e1, _00da --> _00e3
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00e2_power_combination_eval_pv499__00e3_pv471__00da
temp_power = _00e2_coeff_temp*1*(v471__00da)
pv499__00e3_pv498__00e1 = temp_power.flatten()
temp_power = _00e2_coeff_temp*(v498__00e1)*1
pv499__00e3_pv471__00da = temp_power.flatten()
path_to_v498__00e1 = DIAG_MULT(path_to_v499__00e3,pv499__00e3_pv498__00e1)
path_to_v471__00da = DIAG_MULT(path_to_v499__00e3,pv499__00e3_pv471__00da)
del pv499__00e3_pv498__00e1
del path_to_v499__00e3
del pv499__00e3_pv471__00da

# op _008z expand_array_eval
# LANG: _008y --> _008A
# SHAPES: (1, 50, 4) --> (1, 50, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal

# _008z expand_array_eval_pv322__008A_pv321__008y
path_to_v321__008y = STD_MULT(path_to_v322__008A,pv322__008A_pv321__008y)
del path_to_v322__008A

# op _0086 expand_array_eval
# LANG: frame_vel --> _0087
# SHAPES: (1, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp

# _0086 expand_array_eval_pv305__0087_pv623_frame_vel
path_to_v623_frame_vel += STD_MULT(path_to_v305__0087,pv305__0087_pv623_frame_vel)
del path_to_v305__0087

# op _0084 reshape_eval
# LANG: _0083 --> _0085
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp

# _0084 reshape_eval_pv304__0085_pv303__0083
path_to_v303__0083 = DIAG_MULT(path_to_v304__0085,pv304__0085_pv303__0083)
del path_to_v304__0085

# op _00hs_linear_combination_eval
# LANG: _00gc, _00gC --> _00ht
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00hs_linear_combination_eval_pv611__00ht_pv584__00gC
path_to_v571__00gc = DIAG_MULT(path_to_v611__00ht,pv611__00ht_pv571__00gc)
path_to_v584__00gC = DIAG_MULT(path_to_v611__00ht,pv611__00ht_pv584__00gC)
del path_to_v611__00ht

# op _00ho expand_array_eval
# LANG: _00hn --> _00hp
# SHAPES: (1, 40000) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00ho expand_array_eval_pv609__00hp_pv608__00hn
path_to_v608__00hn = STD_MULT(path_to_v609__00hp,pv609__00hp_pv608__00hn)
del path_to_v609__00hp

# op _00h4_power_combination_eval
# LANG: _00h3 --> _00h5
# SHAPES: (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00h4_power_combination_eval_pv599__00h5_pv598__00h3
temp_power = _00h4_coeff_temp*1
pv599__00h5_pv598__00h3 = temp_power.flatten()
path_to_v598__00h3 = DIAG_MULT(path_to_v599__00h5,pv599__00h5_pv598__00h3)
del pv599__00h5_pv598__00h3
del path_to_v599__00h5

# op _00h0_power_combination_eval
# LANG: _00g_, _00gG --> _00h1
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00h0_power_combination_eval_pv597__00h1_pv586__00gG
temp_power = _00h0_coeff_temp*1*(v586__00gG)
pv597__00h1_pv596__00g_ = temp_power.flatten()
temp_power = _00h0_coeff_temp*(v596__00g_)*1
pv597__00h1_pv586__00gG = temp_power.flatten()
path_to_v596__00g_ = DIAG_MULT(path_to_v597__00h1,pv597__00h1_pv596__00g_)
path_to_v586__00gG = DIAG_MULT(path_to_v597__00h1,pv597__00h1_pv586__00gG)
del path_to_v597__00h1
del pv597__00h1_pv586__00gG
del pv597__00h1_pv596__00g_

# op _00e4_linear_combination_eval
# LANG: _00bc, _00c9 --> _00e5
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00e4_linear_combination_eval_pv500__00e5_pv439__00c9
path_to_v409__00bc = DIAG_MULT(path_to_v500__00e5,pv500__00e5_pv409__00bc)
path_to_v439__00c9 = DIAG_MULT(path_to_v500__00e5,pv500__00e5_pv439__00c9)
del path_to_v500__00e5

# op _00e0 expand_array_eval
# LANG: _00d_ --> _00e1
# SHAPES: (1, 55200) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00e0 expand_array_eval_pv498__00e1_pv497__00d_
path_to_v497__00d_ = STD_MULT(path_to_v498__00e1,pv498__00e1_pv497__00d_)
del path_to_v498__00e1

# op _00d9_power_combination_eval
# LANG: _00d8 --> _00da
# SHAPES: (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00d9_power_combination_eval_pv471__00da_pv470__00d8
temp_power = _00d9_coeff_temp*1
pv471__00da_pv470__00d8 = temp_power.flatten()
path_to_v470__00d8 = DIAG_MULT(path_to_v471__00da,pv471__00da_pv470__00d8)
del pv471__00da_pv470__00d8
del path_to_v471__00da

# op _00d5_power_combination_eval
# LANG: _00d4, _00cd --> _00d6
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00d5_power_combination_eval_pv469__00d6_pv441__00cd
temp_power = _00d5_coeff_temp*1*(v441__00cd)
pv469__00d6_pv468__00d4 = temp_power.flatten()
temp_power = _00d5_coeff_temp*(v468__00d4)*1
pv469__00d6_pv441__00cd = temp_power.flatten()
path_to_v468__00d4 = DIAG_MULT(path_to_v469__00d6,pv469__00d6_pv468__00d4)
path_to_v441__00cd = DIAG_MULT(path_to_v469__00d6,pv469__00d6_pv441__00cd)
del path_to_v469__00d6
del pv469__00d6_pv441__00cd
del pv469__00d6_pv468__00d4

# op _008x_power_combination_eval
# LANG: _008w --> _008y
# SHAPES: (1, 50, 4) --> (1, 50, 4)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal

# _008x_power_combination_eval_pv321__008y_pv320__008w
temp_power = _008x_coeff_temp*0.5*(v320__008w**-0.5)
pv321__008y_pv320__008w = temp_power.flatten()
path_to_v320__008w = DIAG_MULT(path_to_v321__008y,pv321__008y_pv320__008w)
del path_to_v321__008y
del pv321__008y_pv320__008w

# _0082 cross_product_eval__0082
_0082_path_in = _0082_vjp(v302__0081,v301__007_,path_to_v303__0083)
_0082_v302__0081 = _0082_path_in[0]
_0082_v301__007_ = _0082_path_in[1]
path_to_v302__0081 = _0082_v302__0081
path_to_v301__007_ = _0082_v301__007_
del path_to_v303__0083

# op _00hm_power_combination_eval
# LANG: _00hf, _00hl --> _00hn
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00hm_power_combination_eval_pv608__00hn_pv607__00hl
temp_power = _00hm_coeff_temp*1*(v607__00hl)
pv608__00hn_pv604__00hf = temp_power.flatten()
temp_power = _00hm_coeff_temp*(v604__00hf)*1
pv608__00hn_pv607__00hl = temp_power.flatten()
path_to_v604__00hf = DIAG_MULT(path_to_v608__00hn,pv608__00hn_pv604__00hf)
path_to_v607__00hl = DIAG_MULT(path_to_v608__00hn,pv608__00hn_pv607__00hl)
del pv608__00hn_pv607__00hl
del path_to_v608__00hn
del pv608__00hn_pv604__00hf

# _00h2 cross_product_eval__00h2
_00h2_path_in = _00h2_vjp(v555__00fH,v525__00eK,path_to_v598__00h3)
_00h2_v555__00fH = _00h2_path_in[0]
_00h2_v525__00eK = _00h2_path_in[1]
path_to_v555__00fH = _00h2_v555__00fH
path_to_v525__00eK = _00h2_v525__00eK
del path_to_v598__00h3

# op _00gb_power_combination_eval
# LANG: _00ga, _00fR --> _00gc
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gb_power_combination_eval_pv571__00gc_pv560__00fR
temp_power = _00gb_coeff_temp*1*(v560__00fR)
pv571__00gc_pv570__00ga = temp_power.flatten()
temp_power = _00gb_coeff_temp*(v570__00ga)*1
pv571__00gc_pv560__00fR = temp_power.flatten()
path_to_v570__00ga = DIAG_MULT(path_to_v571__00gc,pv571__00gc_pv570__00ga)
path_to_v560__00fR = DIAG_MULT(path_to_v571__00gc,pv571__00gc_pv560__00fR)
del path_to_v571__00gc
del pv571__00gc_pv570__00ga
del pv571__00gc_pv560__00fR

# op _00gZ expand_array_eval
# LANG: _00gY --> _00g_
# SHAPES: (1, 40000) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gZ expand_array_eval_pv596__00g__pv595__00gY
path_to_v595__00gY = STD_MULT(path_to_v596__00g_,pv596__00g__pv595__00gY)
del path_to_v596__00g_

# op _00gF_power_combination_eval
# LANG: _00gE --> _00gG
# SHAPES: (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gF_power_combination_eval_pv586__00gG_pv585__00gE
temp_power = _00gF_coeff_temp*1
pv586__00gG_pv585__00gE = temp_power.flatten()
path_to_v585__00gE = DIAG_MULT(path_to_v586__00gG,pv586__00gG_pv585__00gE)
del pv586__00gG_pv585__00gE
del path_to_v586__00gG

# op _00gB_power_combination_eval
# LANG: _00gA, _00gg --> _00gC
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gB_power_combination_eval_pv584__00gC_pv573__00gg
temp_power = _00gB_coeff_temp*1*(v573__00gg)
pv584__00gC_pv583__00gA = temp_power.flatten()
temp_power = _00gB_coeff_temp*(v583__00gA)*1
pv584__00gC_pv573__00gg = temp_power.flatten()
path_to_v583__00gA = DIAG_MULT(path_to_v584__00gC,pv584__00gC_pv583__00gA)
path_to_v573__00gg = DIAG_MULT(path_to_v584__00gC,pv584__00gC_pv573__00gg)
del path_to_v584__00gC
del pv584__00gC_pv583__00gA
del pv584__00gC_pv573__00gg

# op _00dZ_power_combination_eval
# LANG: _00dE, _00dY --> _00d_
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dZ_power_combination_eval_pv497__00d__pv496__00dY
temp_power = _00dZ_coeff_temp*1*(v496__00dY**-1)
pv497__00d__pv486__00dE = temp_power.flatten()
temp_power = _00dZ_coeff_temp*(v486__00dE)*-1*(v496__00dY**-2.0)
pv497__00d__pv496__00dY = temp_power.flatten()
path_to_v486__00dE = DIAG_MULT(path_to_v497__00d_,pv497__00d__pv486__00dE)
path_to_v496__00dY = DIAG_MULT(path_to_v497__00d_,pv497__00d__pv496__00dY)
del pv497__00d__pv496__00dY
del pv497__00d__pv486__00dE
del path_to_v497__00d_

# _00d7 cross_product_eval__00d7
_00d7_path_in = _00d7_vjp(v376__00a9,v346__009c,path_to_v470__00d8)
_00d7_v376__00a9 = _00d7_path_in[0]
_00d7_v346__009c = _00d7_path_in[1]
path_to_v376__00a9 = _00d7_v376__00a9
path_to_v346__009c = _00d7_v346__009c
del path_to_v470__00d8

# op _00d3 expand_array_eval
# LANG: _00d2 --> _00d4
# SHAPES: (1, 55200) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00d3 expand_array_eval_pv468__00d4_pv467__00d2
path_to_v467__00d2 = STD_MULT(path_to_v468__00d4,pv468__00d4_pv467__00d2)
del path_to_v468__00d4

# op _00cc_power_combination_eval
# LANG: _00cb --> _00cd
# SHAPES: (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cc_power_combination_eval_pv441__00cd_pv440__00cb
temp_power = _00cc_coeff_temp*1
pv441__00cd_pv440__00cb = temp_power.flatten()
path_to_v440__00cb = DIAG_MULT(path_to_v441__00cd,pv441__00cd_pv440__00cb)
del path_to_v441__00cd
del pv441__00cd_pv440__00cb

# op _00c8_power_combination_eval
# LANG: _00c7, _00bg --> _00c9
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00c8_power_combination_eval_pv439__00c9_pv411__00bg
temp_power = _00c8_coeff_temp*1*(v411__00bg)
pv439__00c9_pv438__00c7 = temp_power.flatten()
temp_power = _00c8_coeff_temp*(v438__00c7)*1
pv439__00c9_pv411__00bg = temp_power.flatten()
path_to_v438__00c7 = DIAG_MULT(path_to_v439__00c9,pv439__00c9_pv438__00c7)
path_to_v411__00bg = DIAG_MULT(path_to_v439__00c9,pv439__00c9_pv411__00bg)
del pv439__00c9_pv411__00bg
del path_to_v439__00c9
del pv439__00c9_pv438__00c7

# op _00bb_power_combination_eval
# LANG: _00ba, _00aj --> _00bc
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bb_power_combination_eval_pv409__00bc_pv381__00aj
temp_power = _00bb_coeff_temp*1*(v381__00aj)
pv409__00bc_pv408__00ba = temp_power.flatten()
temp_power = _00bb_coeff_temp*(v408__00ba)*1
pv409__00bc_pv381__00aj = temp_power.flatten()
path_to_v408__00ba = DIAG_MULT(path_to_v409__00bc,pv409__00bc_pv408__00ba)
path_to_v381__00aj = DIAG_MULT(path_to_v409__00bc,pv409__00bc_pv381__00aj)
del pv409__00bc_pv381__00aj
del pv409__00bc_pv408__00ba
del path_to_v409__00bc

# op _008v_single_tensor_sum_with_axis_eval
# LANG: _008u --> _008w
# SHAPES: (1, 50, 4, 3) --> (1, 50, 4)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal

# _008v_single_tensor_sum_with_axis_eval_pv320__008w_pv319__008u
path_to_v319__008u = STD_MULT(path_to_v320__008w,pv320__008w_pv319__008u)
del path_to_v320__008w

# op _0080 expand_array_eval
# LANG: ang_vel --> _0081
# SHAPES: (1, 3) --> (1, 50, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp

# _0080 expand_array_eval_pv302__0081_pv297_ang_vel
path_to_v297_ang_vel = STD_MULT(path_to_v302__0081,pv302__0081_pv297_ang_vel)
del path_to_v302__0081

# op _007Z_linear_combination_eval
# LANG: _007Y, eel_coll_pts_coords --> _007_
# SHAPES: (1, 50, 4, 3), (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp

# _007Z_linear_combination_eval_pv301__007__pv513_eel_coll_pts_coords
path_to_v513_eel_coll_pts_coords = DIAG_MULT(path_to_v301__007_,pv301__007__pv513_eel_coll_pts_coords)
del path_to_v301__007_

# op _00hk_linear_combination_eval
# LANG: _00hh, _00hj --> _00hl
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00hk_linear_combination_eval_pv607__00hl_pv606__00hj
path_to_v605__00hh = DIAG_MULT(path_to_v607__00hl,pv607__00hl_pv605__00hh)
path_to_v606__00hj = DIAG_MULT(path_to_v607__00hl,pv607__00hl_pv606__00hj)
del path_to_v607__00hl

# op _00he_power_combination_eval
# LANG: _00hd --> _00hf
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00he_power_combination_eval_pv604__00hf_pv603__00hd
temp_power = _00he_coeff_temp*-1*(v603__00hd**-2.0)
pv604__00hf_pv603__00hd = temp_power.flatten()
path_to_v603__00hd = DIAG_MULT(path_to_v604__00hf,pv604__00hf_pv603__00hd)
del path_to_v604__00hf
del pv604__00hf_pv603__00hd

# op _00gz expand_array_eval
# LANG: _00gy --> _00gA
# SHAPES: (1, 40000) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gz expand_array_eval_pv583__00gA_pv582__00gy
path_to_v582__00gy = STD_MULT(path_to_v583__00gA,pv583__00gA_pv582__00gy)
del path_to_v583__00gA

# op _00gf_power_combination_eval
# LANG: _00ge --> _00gg
# SHAPES: (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gf_power_combination_eval_pv573__00gg_pv572__00ge
temp_power = _00gf_coeff_temp*1
pv573__00gg_pv572__00ge = temp_power.flatten()
path_to_v572__00ge = DIAG_MULT(path_to_v573__00gg,pv573__00gg_pv572__00ge)
del path_to_v573__00gg
del pv573__00gg_pv572__00ge

# op _00gX_power_combination_eval
# LANG: _00gQ, _00gW --> _00gY
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gX_power_combination_eval_pv595__00gY_pv594__00gW
temp_power = _00gX_coeff_temp*1*(v594__00gW)
pv595__00gY_pv591__00gQ = temp_power.flatten()
temp_power = _00gX_coeff_temp*(v591__00gQ)*1
pv595__00gY_pv594__00gW = temp_power.flatten()
path_to_v591__00gQ = DIAG_MULT(path_to_v595__00gY,pv595__00gY_pv591__00gQ)
path_to_v594__00gW = DIAG_MULT(path_to_v595__00gY,pv595__00gY_pv594__00gW)
del path_to_v595__00gY
del pv595__00gY_pv594__00gW
del pv595__00gY_pv591__00gQ

# _00gD cross_product_eval__00gD
_00gD_path_in = _00gD_vjp(v545__00fn,v555__00fH,path_to_v585__00gE)
_00gD_v545__00fn = _00gD_path_in[0]
_00gD_v555__00fH = _00gD_path_in[1]
path_to_v555__00fH += _00gD_v555__00fH
path_to_v545__00fn = _00gD_v545__00fn
del path_to_v585__00gE

# op _00g9 expand_array_eval
# LANG: _00g8 --> _00ga
# SHAPES: (1, 40000) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00g9 expand_array_eval_pv570__00ga_pv569__00g8
path_to_v569__00g8 = STD_MULT(path_to_v570__00ga,pv570__00ga_pv569__00g8)
del path_to_v570__00ga

# op _00fQ_power_combination_eval
# LANG: _00fP --> _00fR
# SHAPES: (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fQ_power_combination_eval_pv560__00fR_pv559__00fP
temp_power = _00fQ_coeff_temp*1
pv560__00fR_pv559__00fP = temp_power.flatten()
path_to_v559__00fP = DIAG_MULT(path_to_v560__00fR,pv560__00fR_pv559__00fP)
del path_to_v560__00fR
del pv560__00fR_pv559__00fP

# op _00dX_linear_combination_eval
# LANG: _00dW --> _00dY
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dX_linear_combination_eval_pv496__00dY_pv495__00dW
path_to_v495__00dW = DIAG_MULT(path_to_v496__00dY,pv496__00dY_pv495__00dW)
del path_to_v496__00dY

# op _00dD_linear_combination_eval
# LANG: _00ds, _00dC --> _00dE
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dD_linear_combination_eval_pv486__00dE_pv485__00dC
path_to_v480__00ds = DIAG_MULT(path_to_v486__00dE,pv486__00dE_pv480__00ds)
path_to_v485__00dC = DIAG_MULT(path_to_v486__00dE,pv486__00dE_pv485__00dC)
del path_to_v486__00dE

# op _00d1_power_combination_eval
# LANG: _00cH, _00d0 --> _00d2
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00d1_power_combination_eval_pv467__00d2_pv466__00d0
temp_power = _00d1_coeff_temp*1*(v466__00d0**-1)
pv467__00d2_pv456__00cH = temp_power.flatten()
temp_power = _00d1_coeff_temp*(v456__00cH)*-1*(v466__00d0**-2.0)
pv467__00d2_pv466__00d0 = temp_power.flatten()
path_to_v456__00cH = DIAG_MULT(path_to_v467__00d2,pv467__00d2_pv456__00cH)
path_to_v466__00d0 = DIAG_MULT(path_to_v467__00d2,pv467__00d2_pv466__00d0)
del pv467__00d2_pv456__00cH
del pv467__00d2_pv466__00d0
del path_to_v467__00d2

# _00ca cross_product_eval__00ca
_00ca_path_in = _00ca_vjp(v366__009Q,v376__00a9,path_to_v440__00cb)
_00ca_v366__009Q = _00ca_path_in[0]
_00ca_v376__00a9 = _00ca_path_in[1]
path_to_v376__00a9 += _00ca_v376__00a9
path_to_v366__009Q = _00ca_v366__009Q
del path_to_v440__00cb

# op _00c6 expand_array_eval
# LANG: _00c5 --> _00c7
# SHAPES: (1, 55200) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00c6 expand_array_eval_pv438__00c7_pv437__00c5
path_to_v437__00c5 = STD_MULT(path_to_v438__00c7,pv438__00c7_pv437__00c5)
del path_to_v438__00c7

# op _00bf_power_combination_eval
# LANG: _00be --> _00bg
# SHAPES: (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bf_power_combination_eval_pv411__00bg_pv410__00be
temp_power = _00bf_coeff_temp*1
pv411__00bg_pv410__00be = temp_power.flatten()
path_to_v410__00be = DIAG_MULT(path_to_v411__00bg,pv411__00bg_pv410__00be)
del pv411__00bg_pv410__00be
del path_to_v411__00bg

# op _00b9 expand_array_eval
# LANG: _00b8 --> _00ba
# SHAPES: (1, 55200) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00b9 expand_array_eval_pv408__00ba_pv407__00b8
path_to_v407__00b8 = STD_MULT(path_to_v408__00ba,pv408__00ba_pv407__00b8)
del path_to_v408__00ba

# op _00ai_power_combination_eval
# LANG: _00ah --> _00aj
# SHAPES: (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00ai_power_combination_eval_pv381__00aj_pv380__00ah
temp_power = _00ai_coeff_temp*1
pv381__00aj_pv380__00ah = temp_power.flatten()
path_to_v380__00ah = DIAG_MULT(path_to_v381__00aj,pv381__00aj_pv380__00ah)
del pv381__00aj_pv380__00ah
del path_to_v381__00aj

# op _008t_power_combination_eval
# LANG: _008s --> _008u
# SHAPES: (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal

# _008t_power_combination_eval_pv319__008u_pv318__008s
temp_power = _008t_coeff_temp*2*(v318__008s)
pv319__008u_pv318__008s = temp_power.flatten()
path_to_v318__008s += DIAG_MULT(path_to_v319__008u,pv319__008u_pv318__008s)
del path_to_v319__008u
del pv319__008u_pv318__008s

# op _007U_indexed_passthrough_eval
# LANG: p, q, r --> ang_vel
# SHAPES: (1, 1), (1, 1), (1, 1) --> (1, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp

# _007U_indexed_passthrough_eval_pv297_ang_vel_pv296_r
path_to_v294_p = STD_MULT(path_to_v297_ang_vel,pv297_ang_vel_pv294_p)
path_to_v295_q = STD_MULT(path_to_v297_ang_vel,pv297_ang_vel_pv295_q)
path_to_v296_r = STD_MULT(path_to_v297_ang_vel,pv297_ang_vel_pv296_r)
del path_to_v297_ang_vel

# op _00hi_power_combination_eval
# LANG: _00eQ --> _00hj
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00hi_power_combination_eval_pv606__00hj_pv528__00eQ
temp_power = _00hi_coeff_temp*-1*(v528__00eQ**-2.0)
pv606__00hj_pv528__00eQ = temp_power.flatten()
path_to_v528__00eQ = DIAG_MULT(path_to_v606__00hj,pv606__00hj_pv528__00eQ)
del pv606__00hj_pv528__00eQ
del path_to_v606__00hj

# op _00hg_power_combination_eval
# LANG: _00fN --> _00hh
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00hg_power_combination_eval_pv605__00hh_pv558__00fN
temp_power = _00hg_coeff_temp*-1*(v558__00fN**-2.0)
pv605__00hh_pv558__00fN = temp_power.flatten()
path_to_v558__00fN = DIAG_MULT(path_to_v605__00hh,pv605__00hh_pv558__00fN)
del path_to_v605__00hh
del pv605__00hh_pv558__00fN

# op _00hc_linear_combination_eval
# LANG: _00hb, _00h9 --> _00hd
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00hc_linear_combination_eval_pv603__00hd_pv601__00h9
path_to_v602__00hb = DIAG_MULT(path_to_v603__00hd,pv603__00hd_pv602__00hb)
path_to_v601__00h9 = DIAG_MULT(path_to_v603__00hd,pv603__00hd_pv601__00h9)
del path_to_v603__00hd

# op _00gx_power_combination_eval
# LANG: _00gq, _00gw --> _00gy
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gx_power_combination_eval_pv582__00gy_pv581__00gw
temp_power = _00gx_coeff_temp*1*(v581__00gw)
pv582__00gy_pv578__00gq = temp_power.flatten()
temp_power = _00gx_coeff_temp*(v578__00gq)*1
pv582__00gy_pv581__00gw = temp_power.flatten()
path_to_v578__00gq = DIAG_MULT(path_to_v582__00gy,pv582__00gy_pv578__00gq)
path_to_v581__00gw = DIAG_MULT(path_to_v582__00gy,pv582__00gy_pv581__00gw)
del path_to_v582__00gy
del pv582__00gy_pv578__00gq
del pv582__00gy_pv581__00gw

# _00gd cross_product_eval__00gd
_00gd_path_in = _00gd_vjp(v535__00f3,v545__00fn,path_to_v572__00ge)
_00gd_v535__00f3 = _00gd_path_in[0]
_00gd_v545__00fn = _00gd_path_in[1]
path_to_v545__00fn += _00gd_v545__00fn
path_to_v535__00f3 = _00gd_v535__00f3
del path_to_v572__00ge

# op _00gV_linear_combination_eval
# LANG: _00gS, _00gU --> _00gW
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gV_linear_combination_eval_pv594__00gW_pv593__00gU
path_to_v592__00gS = DIAG_MULT(path_to_v594__00gW,pv594__00gW_pv592__00gS)
path_to_v593__00gU = DIAG_MULT(path_to_v594__00gW,pv594__00gW_pv593__00gU)
del path_to_v594__00gW

# op _00gP_power_combination_eval
# LANG: _00gO --> _00gQ
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gP_power_combination_eval_pv591__00gQ_pv590__00gO
temp_power = _00gP_coeff_temp*-1*(v590__00gO**-2.0)
pv591__00gQ_pv590__00gO = temp_power.flatten()
path_to_v590__00gO = DIAG_MULT(path_to_v591__00gQ,pv591__00gQ_pv590__00gO)
del path_to_v591__00gQ
del pv591__00gQ_pv590__00gO

# op _00g7_power_combination_eval
# LANG: _00g0, _00g6 --> _00g8
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00g7_power_combination_eval_pv569__00g8_pv568__00g6
temp_power = _00g7_coeff_temp*1*(v568__00g6)
pv569__00g8_pv565__00g0 = temp_power.flatten()
temp_power = _00g7_coeff_temp*(v565__00g0)*1
pv569__00g8_pv568__00g6 = temp_power.flatten()
path_to_v565__00g0 = DIAG_MULT(path_to_v569__00g8,pv569__00g8_pv565__00g0)
path_to_v568__00g6 = DIAG_MULT(path_to_v569__00g8,pv569__00g8_pv568__00g6)
del pv569__00g8_pv565__00g0
del pv569__00g8_pv568__00g6
del path_to_v569__00g8

# _00fO cross_product_eval__00fO
_00fO_path_in = _00fO_vjp(v525__00eK,v535__00f3,path_to_v559__00fP)
_00fO_v525__00eK = _00fO_path_in[0]
_00fO_v535__00f3 = _00fO_path_in[1]
path_to_v525__00eK += _00fO_v525__00eK
path_to_v535__00f3 += _00fO_v535__00f3
del path_to_v559__00fP

# op _00dr_power_combination_eval
# LANG: _00dk, _00dq --> _00ds
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dr_power_combination_eval_pv480__00ds_pv479__00dq
temp_power = _00dr_coeff_temp*1*(v479__00dq**-1)
pv480__00ds_pv476__00dk = temp_power.flatten()
temp_power = _00dr_coeff_temp*(v476__00dk)*-1*(v479__00dq**-2.0)
pv480__00ds_pv479__00dq = temp_power.flatten()
path_to_v476__00dk = DIAG_MULT(path_to_v480__00ds,pv480__00ds_pv476__00dk)
path_to_v479__00dq = DIAG_MULT(path_to_v480__00ds,pv480__00ds_pv479__00dq)
del pv480__00ds_pv479__00dq
del path_to_v480__00ds
del pv480__00ds_pv476__00dk

# op _00dV_linear_combination_eval
# LANG: _00dK, _00dU --> _00dW
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dV_linear_combination_eval_pv495__00dW_pv494__00dU
path_to_v489__00dK = DIAG_MULT(path_to_v495__00dW,pv495__00dW_pv489__00dK)
path_to_v494__00dU = DIAG_MULT(path_to_v495__00dW,pv495__00dW_pv494__00dU)
del path_to_v495__00dW

# op _00dB_power_combination_eval
# LANG: _00du, _00dA --> _00dC
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dB_power_combination_eval_pv485__00dC_pv484__00dA
temp_power = _00dB_coeff_temp*1*(v484__00dA**-1)
pv485__00dC_pv481__00du = temp_power.flatten()
temp_power = _00dB_coeff_temp*(v481__00du)*-1*(v484__00dA**-2.0)
pv485__00dC_pv484__00dA = temp_power.flatten()
path_to_v481__00du = DIAG_MULT(path_to_v485__00dC,pv485__00dC_pv481__00du)
path_to_v484__00dA = DIAG_MULT(path_to_v485__00dC,pv485__00dC_pv484__00dA)
del pv485__00dC_pv481__00du
del pv485__00dC_pv484__00dA
del path_to_v485__00dC

# op _00c__linear_combination_eval
# LANG: _00cZ --> _00d0
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00c__linear_combination_eval_pv466__00d0_pv465__00cZ
path_to_v465__00cZ = DIAG_MULT(path_to_v466__00d0,pv466__00d0_pv465__00cZ)
del path_to_v466__00d0

# op _00cG_linear_combination_eval
# LANG: _00cv, _00cF --> _00cH
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cG_linear_combination_eval_pv456__00cH_pv455__00cF
path_to_v450__00cv = DIAG_MULT(path_to_v456__00cH,pv456__00cH_pv450__00cv)
path_to_v455__00cF = DIAG_MULT(path_to_v456__00cH,pv456__00cH_pv455__00cF)
del path_to_v456__00cH

# op _00c4_power_combination_eval
# LANG: _00bK, _00c3 --> _00c5
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00c4_power_combination_eval_pv437__00c5_pv436__00c3
temp_power = _00c4_coeff_temp*1*(v436__00c3**-1)
pv437__00c5_pv426__00bK = temp_power.flatten()
temp_power = _00c4_coeff_temp*(v426__00bK)*-1*(v436__00c3**-2.0)
pv437__00c5_pv436__00c3 = temp_power.flatten()
path_to_v426__00bK = DIAG_MULT(path_to_v437__00c5,pv437__00c5_pv426__00bK)
path_to_v436__00c3 = DIAG_MULT(path_to_v437__00c5,pv437__00c5_pv436__00c3)
del path_to_v437__00c5
del pv437__00c5_pv426__00bK
del pv437__00c5_pv436__00c3

# _00bd cross_product_eval__00bd
_00bd_path_in = _00bd_vjp(v356__009w,v366__009Q,path_to_v410__00be)
_00bd_v356__009w = _00bd_path_in[0]
_00bd_v366__009Q = _00bd_path_in[1]
path_to_v366__009Q += _00bd_v366__009Q
path_to_v356__009w = _00bd_v356__009w
del path_to_v410__00be

# op _00b7_power_combination_eval
# LANG: _00aN, _00b6 --> _00b8
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00b7_power_combination_eval_pv407__00b8_pv406__00b6
temp_power = _00b7_coeff_temp*1*(v406__00b6**-1)
pv407__00b8_pv396__00aN = temp_power.flatten()
temp_power = _00b7_coeff_temp*(v396__00aN)*-1*(v406__00b6**-2.0)
pv407__00b8_pv406__00b6 = temp_power.flatten()
path_to_v396__00aN = DIAG_MULT(path_to_v407__00b8,pv407__00b8_pv396__00aN)
path_to_v406__00b6 = DIAG_MULT(path_to_v407__00b8,pv407__00b8_pv406__00b6)
del path_to_v407__00b8
del pv407__00b8_pv406__00b6
del pv407__00b8_pv396__00aN

# _00ag cross_product_eval__00ag
_00ag_path_in = _00ag_vjp(v346__009c,v356__009w,path_to_v380__00ah)
_00ag_v346__009c = _00ag_path_in[0]
_00ag_v356__009w = _00ag_path_in[1]
path_to_v346__009c += _00ag_v346__009c
path_to_v356__009w += _00ag_v356__009w
del path_to_v380__00ah

# _008r cross_product_eval__008r
_008r_path_in = _008r_vjp(v314__008m,v317__008q,path_to_v318__008s)
_008r_v314__008m = _008r_path_in[0]
_008r_v317__008q = _008r_path_in[1]
path_to_v314__008m = _008r_v314__008m
path_to_v317__008q = _008r_v317__008q
del path_to_v318__008s

# op _00ha_power_combination_eval
# LANG: _00eQ, _00fN --> _00hb
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00ha_power_combination_eval_pv602__00hb_pv558__00fN
temp_power = _00ha_coeff_temp*(v558__00fN)*1
pv602__00hb_pv528__00eQ = temp_power.flatten()
temp_power = _00ha_coeff_temp*1*(v528__00eQ)
pv602__00hb_pv558__00fN = temp_power.flatten()
path_to_v528__00eQ += DIAG_MULT(path_to_v602__00hb,pv602__00hb_pv528__00eQ)
path_to_v558__00fN += DIAG_MULT(path_to_v602__00hb,pv602__00hb_pv558__00fN)
del pv602__00hb_pv558__00fN
del path_to_v602__00hb
del pv602__00hb_pv528__00eQ

# op _00h8_single_tensor_sum_with_axis_eval
# LANG: _00h7 --> _00h9
# SHAPES: (1, 40000, 3) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00h8_single_tensor_sum_with_axis_eval_pv601__00h9_pv600__00h7
path_to_v600__00h7 = STD_MULT(path_to_v601__00h9,pv601__00h9_pv600__00h7)
del path_to_v601__00h9

# op _00gv_linear_combination_eval
# LANG: _00gs, _00gu --> _00gw
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gv_linear_combination_eval_pv581__00gw_pv580__00gu
path_to_v579__00gs = DIAG_MULT(path_to_v581__00gw,pv581__00gw_pv579__00gs)
path_to_v580__00gu = DIAG_MULT(path_to_v581__00gw,pv581__00gw_pv580__00gu)
del path_to_v581__00gw

# op _00gp_power_combination_eval
# LANG: _00go --> _00gq
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gp_power_combination_eval_pv578__00gq_pv577__00go
temp_power = _00gp_coeff_temp*-1*(v577__00go**-2.0)
pv578__00gq_pv577__00go = temp_power.flatten()
path_to_v577__00go = DIAG_MULT(path_to_v578__00gq,pv578__00gq_pv577__00go)
del pv578__00gq_pv577__00go
del path_to_v578__00gq

# op _00gT_power_combination_eval
# LANG: _00fN --> _00gU
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gT_power_combination_eval_pv593__00gU_pv558__00fN
temp_power = _00gT_coeff_temp*-1*(v558__00fN**-2.0)
pv593__00gU_pv558__00fN = temp_power.flatten()
path_to_v558__00fN += DIAG_MULT(path_to_v593__00gU,pv593__00gU_pv558__00fN)
del path_to_v593__00gU
del pv593__00gU_pv558__00fN

# op _00gR_power_combination_eval
# LANG: _00ft --> _00gS
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gR_power_combination_eval_pv592__00gS_pv548__00ft
temp_power = _00gR_coeff_temp*-1*(v548__00ft**-2.0)
pv592__00gS_pv548__00ft = temp_power.flatten()
path_to_v548__00ft = DIAG_MULT(path_to_v592__00gS,pv592__00gS_pv548__00ft)
del pv592__00gS_pv548__00ft
del path_to_v592__00gS

# op _00gN_linear_combination_eval
# LANG: _00gM, _00gK --> _00gO
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gN_linear_combination_eval_pv590__00gO_pv588__00gK
path_to_v589__00gM = DIAG_MULT(path_to_v590__00gO,pv590__00gO_pv589__00gM)
path_to_v588__00gK = DIAG_MULT(path_to_v590__00gO,pv590__00gO_pv588__00gK)
del path_to_v590__00gO

# op _00g5_linear_combination_eval
# LANG: _00g2, _00g4 --> _00g6
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00g5_linear_combination_eval_pv568__00g6_pv567__00g4
path_to_v566__00g2 = DIAG_MULT(path_to_v568__00g6,pv568__00g6_pv566__00g2)
path_to_v567__00g4 = DIAG_MULT(path_to_v568__00g6,pv568__00g6_pv567__00g4)
del path_to_v568__00g6

# op _00f__power_combination_eval
# LANG: _00fZ --> _00g0
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00f__power_combination_eval_pv565__00g0_pv564__00fZ
temp_power = _00f__coeff_temp*-1*(v564__00fZ**-2.0)
pv565__00g0_pv564__00fZ = temp_power.flatten()
path_to_v564__00fZ = DIAG_MULT(path_to_v565__00g0,pv565__00g0_pv564__00fZ)
del path_to_v565__00g0
del pv565__00g0_pv564__00fZ

# op _00dz_power_combination_eval
# LANG: _00dy --> _00dA
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dz_power_combination_eval_pv484__00dA_pv483__00dy
temp_power = _00dz_coeff_temp*0.5*(v483__00dy**-0.5)
pv484__00dA_pv483__00dy = temp_power.flatten()
path_to_v483__00dy = DIAG_MULT(path_to_v484__00dA,pv484__00dA_pv483__00dy)
del pv484__00dA_pv483__00dy
del path_to_v484__00dA

# op _00dt_linear_combination_eval
# LANG: _00di, _00de --> _00du
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dt_linear_combination_eval_pv481__00du_pv473__00de
path_to_v475__00di = DIAG_MULT(path_to_v481__00du,pv481__00du_pv475__00di)
path_to_v473__00de = DIAG_MULT(path_to_v481__00du,pv481__00du_pv473__00de)
del path_to_v481__00du

# op _00dp_power_combination_eval
# LANG: _00do --> _00dq
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dp_power_combination_eval_pv479__00dq_pv478__00do
temp_power = _00dp_coeff_temp*0.5*(v478__00do**-0.5)
pv479__00dq_pv478__00do = temp_power.flatten()
path_to_v478__00do = DIAG_MULT(path_to_v479__00dq,pv479__00dq_pv478__00do)
del path_to_v479__00dq
del pv479__00dq_pv478__00do

# op _00dj_linear_combination_eval
# LANG: _00dg, _00de --> _00dk
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dj_linear_combination_eval_pv476__00dk_pv473__00de
path_to_v474__00dg = DIAG_MULT(path_to_v476__00dk,pv476__00dk_pv474__00dg)
path_to_v473__00de += DIAG_MULT(path_to_v476__00dk,pv476__00dk_pv473__00de)
del path_to_v476__00dk

# op _00dT_power_combination_eval
# LANG: _00dS --> _00dU
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dT_power_combination_eval_pv494__00dU_pv493__00dS
temp_power = _00dT_coeff_temp*1
pv494__00dU_pv493__00dS = temp_power.flatten()
path_to_v493__00dS = DIAG_MULT(path_to_v494__00dU,pv494__00dU_pv493__00dS)
del path_to_v494__00dU
del pv494__00dU_pv493__00dS

# op _00dJ_linear_combination_eval
# LANG: _00dG, _00dI --> _00dK
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dJ_linear_combination_eval_pv489__00dK_pv488__00dI
path_to_v487__00dG = DIAG_MULT(path_to_v489__00dK,pv489__00dK_pv487__00dG)
path_to_v488__00dI = DIAG_MULT(path_to_v489__00dK,pv489__00dK_pv488__00dI)
del path_to_v489__00dK

# op _00cu_power_combination_eval
# LANG: _00cn, _00ct --> _00cv
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cu_power_combination_eval_pv450__00cv_pv449__00ct
temp_power = _00cu_coeff_temp*1*(v449__00ct**-1)
pv450__00cv_pv446__00cn = temp_power.flatten()
temp_power = _00cu_coeff_temp*(v446__00cn)*-1*(v449__00ct**-2.0)
pv450__00cv_pv449__00ct = temp_power.flatten()
path_to_v446__00cn = DIAG_MULT(path_to_v450__00cv,pv450__00cv_pv446__00cn)
path_to_v449__00ct = DIAG_MULT(path_to_v450__00cv,pv450__00cv_pv449__00ct)
del path_to_v450__00cv
del pv450__00cv_pv449__00ct
del pv450__00cv_pv446__00cn

# op _00cY_linear_combination_eval
# LANG: _00cN, _00cX --> _00cZ
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cY_linear_combination_eval_pv465__00cZ_pv464__00cX
path_to_v459__00cN = DIAG_MULT(path_to_v465__00cZ,pv465__00cZ_pv459__00cN)
path_to_v464__00cX = DIAG_MULT(path_to_v465__00cZ,pv465__00cZ_pv464__00cX)
del path_to_v465__00cZ

# op _00cE_power_combination_eval
# LANG: _00cx, _00cD --> _00cF
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cE_power_combination_eval_pv455__00cF_pv454__00cD
temp_power = _00cE_coeff_temp*1*(v454__00cD**-1)
pv455__00cF_pv451__00cx = temp_power.flatten()
temp_power = _00cE_coeff_temp*(v451__00cx)*-1*(v454__00cD**-2.0)
pv455__00cF_pv454__00cD = temp_power.flatten()
path_to_v451__00cx = DIAG_MULT(path_to_v455__00cF,pv455__00cF_pv451__00cx)
path_to_v454__00cD = DIAG_MULT(path_to_v455__00cF,pv455__00cF_pv454__00cD)
del pv455__00cF_pv454__00cD
del path_to_v455__00cF
del pv455__00cF_pv451__00cx

# op _00c2_linear_combination_eval
# LANG: _00c1 --> _00c3
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00c2_linear_combination_eval_pv436__00c3_pv435__00c1
path_to_v435__00c1 = DIAG_MULT(path_to_v436__00c3,pv436__00c3_pv435__00c1)
del path_to_v436__00c3

# op _00bJ_linear_combination_eval
# LANG: _00by, _00bI --> _00bK
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bJ_linear_combination_eval_pv426__00bK_pv425__00bI
path_to_v420__00by = DIAG_MULT(path_to_v426__00bK,pv426__00bK_pv420__00by)
path_to_v425__00bI = DIAG_MULT(path_to_v426__00bK,pv426__00bK_pv425__00bI)
del path_to_v426__00bK

# op _00b5_linear_combination_eval
# LANG: _00b4 --> _00b6
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00b5_linear_combination_eval_pv406__00b6_pv405__00b4
path_to_v405__00b4 = DIAG_MULT(path_to_v406__00b6,pv406__00b6_pv405__00b4)
del path_to_v406__00b6

# op _00aM_linear_combination_eval
# LANG: _00aB, _00aL --> _00aN
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00aM_linear_combination_eval_pv396__00aN_pv395__00aL
path_to_v390__00aB = DIAG_MULT(path_to_v396__00aN,pv396__00aN_pv390__00aB)
path_to_v395__00aL = DIAG_MULT(path_to_v396__00aN,pv396__00aN_pv395__00aL)
del path_to_v396__00aN

# op _008p_linear_combination_eval
# LANG: _008n, _008o --> _008q
# SHAPES: (1, 50, 4, 3), (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal

# _008p_linear_combination_eval_pv317__008q_pv316__008o
path_to_v315__008n = DIAG_MULT(path_to_v317__008q,pv317__008q_pv315__008n)
path_to_v316__008o = DIAG_MULT(path_to_v317__008q,pv317__008q_pv316__008o)
del path_to_v317__008q

# op _008l_linear_combination_eval
# LANG: _008j, _008k --> _008m
# SHAPES: (1, 50, 4, 3), (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal

# _008l_linear_combination_eval_pv314__008m_pv313__008k
path_to_v312__008j = DIAG_MULT(path_to_v314__008m,pv314__008m_pv312__008j)
path_to_v313__008k = DIAG_MULT(path_to_v314__008m,pv314__008m_pv313__008k)
del path_to_v314__008m

# op _00h6_power_combination_eval
# LANG: _00fH, _00eK --> _00h7
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00h6_power_combination_eval_pv600__00h7_pv525__00eK
temp_power = _00h6_coeff_temp*1*(v525__00eK)
pv600__00h7_pv555__00fH = temp_power.flatten()
temp_power = _00h6_coeff_temp*(v555__00fH)*1
pv600__00h7_pv525__00eK = temp_power.flatten()
path_to_v555__00fH += DIAG_MULT(path_to_v600__00h7,pv600__00h7_pv555__00fH)
path_to_v525__00eK += DIAG_MULT(path_to_v600__00h7,pv600__00h7_pv525__00eK)
del pv600__00h7_pv555__00fH
del pv600__00h7_pv525__00eK
del path_to_v600__00h7

# op _00gt_power_combination_eval
# LANG: _00ft --> _00gu
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gt_power_combination_eval_pv580__00gu_pv548__00ft
temp_power = _00gt_coeff_temp*-1*(v548__00ft**-2.0)
pv580__00gu_pv548__00ft = temp_power.flatten()
path_to_v548__00ft += DIAG_MULT(path_to_v580__00gu,pv580__00gu_pv548__00ft)
del path_to_v580__00gu
del pv580__00gu_pv548__00ft

# op _00gr_power_combination_eval
# LANG: _00f9 --> _00gs
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gr_power_combination_eval_pv579__00gs_pv538__00f9
temp_power = _00gr_coeff_temp*-1*(v538__00f9**-2.0)
pv579__00gs_pv538__00f9 = temp_power.flatten()
path_to_v538__00f9 = DIAG_MULT(path_to_v579__00gs,pv579__00gs_pv538__00f9)
del path_to_v579__00gs
del pv579__00gs_pv538__00f9

# op _00gn_linear_combination_eval
# LANG: _00gm, _00gk --> _00go
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gn_linear_combination_eval_pv577__00go_pv575__00gk
path_to_v576__00gm = DIAG_MULT(path_to_v577__00go,pv577__00go_pv576__00gm)
path_to_v575__00gk = DIAG_MULT(path_to_v577__00go,pv577__00go_pv575__00gk)
del path_to_v577__00go

# op _00gL_power_combination_eval
# LANG: _00fN, _00ft --> _00gM
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gL_power_combination_eval_pv589__00gM_pv548__00ft
temp_power = _00gL_coeff_temp*(v548__00ft)*1
pv589__00gM_pv558__00fN = temp_power.flatten()
temp_power = _00gL_coeff_temp*1*(v558__00fN)
pv589__00gM_pv548__00ft = temp_power.flatten()
path_to_v558__00fN += DIAG_MULT(path_to_v589__00gM,pv589__00gM_pv558__00fN)
path_to_v548__00ft += DIAG_MULT(path_to_v589__00gM,pv589__00gM_pv548__00ft)
del pv589__00gM_pv548__00ft
del pv589__00gM_pv558__00fN
del path_to_v589__00gM

# op _00gJ_single_tensor_sum_with_axis_eval
# LANG: _00gI --> _00gK
# SHAPES: (1, 40000, 3) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gJ_single_tensor_sum_with_axis_eval_pv588__00gK_pv587__00gI
path_to_v587__00gI = STD_MULT(path_to_v588__00gK,pv588__00gK_pv587__00gI)
del path_to_v588__00gK

# op _00g3_power_combination_eval
# LANG: _00f9 --> _00g4
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00g3_power_combination_eval_pv567__00g4_pv538__00f9
temp_power = _00g3_coeff_temp*-1*(v538__00f9**-2.0)
pv567__00g4_pv538__00f9 = temp_power.flatten()
path_to_v538__00f9 += DIAG_MULT(path_to_v567__00g4,pv567__00g4_pv538__00f9)
del pv567__00g4_pv538__00f9
del path_to_v567__00g4

# op _00g1_power_combination_eval
# LANG: _00eQ --> _00g2
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00g1_power_combination_eval_pv566__00g2_pv528__00eQ
temp_power = _00g1_coeff_temp*-1*(v528__00eQ**-2.0)
pv566__00g2_pv528__00eQ = temp_power.flatten()
path_to_v528__00eQ += DIAG_MULT(path_to_v566__00g2,pv566__00g2_pv528__00eQ)
del path_to_v566__00g2
del pv566__00g2_pv528__00eQ

# op _00fY_linear_combination_eval
# LANG: _00fX, _00fV --> _00fZ
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fY_linear_combination_eval_pv564__00fZ_pv562__00fV
path_to_v563__00fX = DIAG_MULT(path_to_v564__00fZ,pv564__00fZ_pv563__00fX)
path_to_v562__00fV = DIAG_MULT(path_to_v564__00fZ,pv564__00fZ_pv562__00fV)
del path_to_v564__00fZ

# op _00dx_linear_combination_eval
# LANG: _00dw --> _00dy
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dx_linear_combination_eval_pv483__00dy_pv482__00dw
path_to_v482__00dw = DIAG_MULT(path_to_v483__00dy,pv483__00dy_pv482__00dw)
del path_to_v483__00dy

# op _00dn_linear_combination_eval
# LANG: _00dm --> _00do
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dn_linear_combination_eval_pv478__00do_pv477__00dm
path_to_v477__00dm = DIAG_MULT(path_to_v478__00do,pv478__00do_pv477__00dm)
del path_to_v478__00do

# op _00dR_linear_combination_eval
# LANG: _00dM, _00dQ --> _00dS
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dR_linear_combination_eval_pv493__00dS_pv492__00dQ
path_to_v490__00dM = DIAG_MULT(path_to_v493__00dS,pv493__00dS_pv490__00dM)
path_to_v492__00dQ = DIAG_MULT(path_to_v493__00dS,pv493__00dS_pv492__00dQ)
del path_to_v493__00dS

# op _00dH_power_combination_eval
# LANG: _00de --> _00dI
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dH_power_combination_eval_pv488__00dI_pv473__00de
temp_power = _00dH_coeff_temp*2*(v473__00de)
pv488__00dI_pv473__00de = temp_power.flatten()
path_to_v473__00de += DIAG_MULT(path_to_v488__00dI,pv488__00dI_pv473__00de)
del path_to_v488__00dI
del pv488__00dI_pv473__00de

# op _00dF_power_combination_eval
# LANG: _00dg, _00di --> _00dG
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dF_power_combination_eval_pv487__00dG_pv475__00di
temp_power = _00dF_coeff_temp*1*(v475__00di)
pv487__00dG_pv474__00dg = temp_power.flatten()
temp_power = _00dF_coeff_temp*(v474__00dg)*1
pv487__00dG_pv475__00di = temp_power.flatten()
path_to_v474__00dg += DIAG_MULT(path_to_v487__00dG,pv487__00dG_pv474__00dg)
path_to_v475__00di += DIAG_MULT(path_to_v487__00dG,pv487__00dG_pv475__00di)
del pv487__00dG_pv475__00di
del pv487__00dG_pv474__00dg
del path_to_v487__00dG

# op _00cw_linear_combination_eval
# LANG: _00cl, _00ch --> _00cx
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cw_linear_combination_eval_pv451__00cx_pv443__00ch
path_to_v445__00cl = DIAG_MULT(path_to_v451__00cx,pv451__00cx_pv445__00cl)
path_to_v443__00ch = DIAG_MULT(path_to_v451__00cx,pv451__00cx_pv443__00ch)
del path_to_v451__00cx

# op _00cs_power_combination_eval
# LANG: _00cr --> _00ct
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cs_power_combination_eval_pv449__00ct_pv448__00cr
temp_power = _00cs_coeff_temp*0.5*(v448__00cr**-0.5)
pv449__00ct_pv448__00cr = temp_power.flatten()
path_to_v448__00cr = DIAG_MULT(path_to_v449__00ct,pv449__00ct_pv448__00cr)
del path_to_v449__00ct
del pv449__00ct_pv448__00cr

# op _00cm_linear_combination_eval
# LANG: _00cj, _00ch --> _00cn
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cm_linear_combination_eval_pv446__00cn_pv443__00ch
path_to_v444__00cj = DIAG_MULT(path_to_v446__00cn,pv446__00cn_pv444__00cj)
path_to_v443__00ch += DIAG_MULT(path_to_v446__00cn,pv446__00cn_pv443__00ch)
del path_to_v446__00cn

# op _00cW_power_combination_eval
# LANG: _00cV --> _00cX
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cW_power_combination_eval_pv464__00cX_pv463__00cV
temp_power = _00cW_coeff_temp*1
pv464__00cX_pv463__00cV = temp_power.flatten()
path_to_v463__00cV = DIAG_MULT(path_to_v464__00cX,pv464__00cX_pv463__00cV)
del path_to_v464__00cX
del pv464__00cX_pv463__00cV

# op _00cM_linear_combination_eval
# LANG: _00cJ, _00cL --> _00cN
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cM_linear_combination_eval_pv459__00cN_pv458__00cL
path_to_v457__00cJ = DIAG_MULT(path_to_v459__00cN,pv459__00cN_pv457__00cJ)
path_to_v458__00cL = DIAG_MULT(path_to_v459__00cN,pv459__00cN_pv458__00cL)
del path_to_v459__00cN

# op _00cC_power_combination_eval
# LANG: _00cB --> _00cD
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cC_power_combination_eval_pv454__00cD_pv453__00cB
temp_power = _00cC_coeff_temp*0.5*(v453__00cB**-0.5)
pv454__00cD_pv453__00cB = temp_power.flatten()
path_to_v453__00cB = DIAG_MULT(path_to_v454__00cD,pv454__00cD_pv453__00cB)
del pv454__00cD_pv453__00cB
del path_to_v454__00cD

# op _00c0_linear_combination_eval
# LANG: _00bQ, _00b_ --> _00c1
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00c0_linear_combination_eval_pv435__00c1_pv434__00b_
path_to_v429__00bQ = DIAG_MULT(path_to_v435__00c1,pv435__00c1_pv429__00bQ)
path_to_v434__00b_ = DIAG_MULT(path_to_v435__00c1,pv435__00c1_pv434__00b_)
del path_to_v435__00c1

# op _00bx_power_combination_eval
# LANG: _00bq, _00bw --> _00by
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bx_power_combination_eval_pv420__00by_pv419__00bw
temp_power = _00bx_coeff_temp*1*(v419__00bw**-1)
pv420__00by_pv416__00bq = temp_power.flatten()
temp_power = _00bx_coeff_temp*(v416__00bq)*-1*(v419__00bw**-2.0)
pv420__00by_pv419__00bw = temp_power.flatten()
path_to_v416__00bq = DIAG_MULT(path_to_v420__00by,pv420__00by_pv416__00bq)
path_to_v419__00bw = DIAG_MULT(path_to_v420__00by,pv420__00by_pv419__00bw)
del pv420__00by_pv416__00bq
del path_to_v420__00by
del pv420__00by_pv419__00bw

# op _00bH_power_combination_eval
# LANG: _00bA, _00bG --> _00bI
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bH_power_combination_eval_pv425__00bI_pv424__00bG
temp_power = _00bH_coeff_temp*1*(v424__00bG**-1)
pv425__00bI_pv421__00bA = temp_power.flatten()
temp_power = _00bH_coeff_temp*(v421__00bA)*-1*(v424__00bG**-2.0)
pv425__00bI_pv424__00bG = temp_power.flatten()
path_to_v421__00bA = DIAG_MULT(path_to_v425__00bI,pv425__00bI_pv421__00bA)
path_to_v424__00bG = DIAG_MULT(path_to_v425__00bI,pv425__00bI_pv424__00bG)
del pv425__00bI_pv424__00bG
del path_to_v425__00bI
del pv425__00bI_pv421__00bA

# op _00b3_linear_combination_eval
# LANG: _00aT, _00b2 --> _00b4
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00b3_linear_combination_eval_pv405__00b4_pv404__00b2
path_to_v399__00aT = DIAG_MULT(path_to_v405__00b4,pv405__00b4_pv399__00aT)
path_to_v404__00b2 = DIAG_MULT(path_to_v405__00b4,pv405__00b4_pv404__00b2)
del path_to_v405__00b4

# op _00aK_power_combination_eval
# LANG: _00aD, _00aJ --> _00aL
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00aK_power_combination_eval_pv395__00aL_pv394__00aJ
temp_power = _00aK_coeff_temp*1*(v394__00aJ**-1)
pv395__00aL_pv391__00aD = temp_power.flatten()
temp_power = _00aK_coeff_temp*(v391__00aD)*-1*(v394__00aJ**-2.0)
pv395__00aL_pv394__00aJ = temp_power.flatten()
path_to_v391__00aD = DIAG_MULT(path_to_v395__00aL,pv395__00aL_pv391__00aD)
path_to_v394__00aJ = DIAG_MULT(path_to_v395__00aL,pv395__00aL_pv394__00aJ)
del path_to_v395__00aL
del pv395__00aL_pv391__00aD
del pv395__00aL_pv394__00aJ

# op _00aA_power_combination_eval
# LANG: _00at, _00az --> _00aB
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00aA_power_combination_eval_pv390__00aB_pv389__00az
temp_power = _00aA_coeff_temp*1*(v389__00az**-1)
pv390__00aB_pv386__00at = temp_power.flatten()
temp_power = _00aA_coeff_temp*(v386__00at)*-1*(v389__00az**-2.0)
pv390__00aB_pv389__00az = temp_power.flatten()
path_to_v386__00at = DIAG_MULT(path_to_v390__00aB,pv390__00aB_pv386__00at)
path_to_v389__00az = DIAG_MULT(path_to_v390__00aB,pv390__00aB_pv389__00az)
del pv390__00aB_pv389__00az
del pv390__00aB_pv386__00at
del path_to_v390__00aB

# op _008i_decompose_eval
# LANG: eel --> _008o, _008j, _008k, _008n
# SHAPES: (1, 51, 5, 3) --> (1, 50, 4, 3), (1, 50, 4, 3), (1, 50, 4, 3), (1, 50, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal

# _008i_decompose_eval_pv315__008n_pv311_eel
path_to_v311_eel = STD_MULT(path_to_v316__008o,pv316__008o_pv311_eel)
path_to_v311_eel += STD_MULT(path_to_v312__008j,pv312__008j_pv311_eel)
path_to_v311_eel += STD_MULT(path_to_v313__008k,pv313__008k_pv311_eel)
path_to_v311_eel += STD_MULT(path_to_v315__008n,pv315__008n_pv311_eel)
del path_to_v315__008n
del path_to_v316__008o
del path_to_v313__008k
del path_to_v312__008j

# op _00gl_power_combination_eval
# LANG: _00ft, _00f9 --> _00gm
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gl_power_combination_eval_pv576__00gm_pv538__00f9
temp_power = _00gl_coeff_temp*(v538__00f9)*1
pv576__00gm_pv548__00ft = temp_power.flatten()
temp_power = _00gl_coeff_temp*1*(v548__00ft)
pv576__00gm_pv538__00f9 = temp_power.flatten()
path_to_v548__00ft += DIAG_MULT(path_to_v576__00gm,pv576__00gm_pv548__00ft)
path_to_v538__00f9 += DIAG_MULT(path_to_v576__00gm,pv576__00gm_pv538__00f9)
del pv576__00gm_pv538__00f9
del pv576__00gm_pv548__00ft
del path_to_v576__00gm

# op _00gj_single_tensor_sum_with_axis_eval
# LANG: _00gi --> _00gk
# SHAPES: (1, 40000, 3) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gj_single_tensor_sum_with_axis_eval_pv575__00gk_pv574__00gi
path_to_v574__00gi = STD_MULT(path_to_v575__00gk,pv575__00gk_pv574__00gi)
del path_to_v575__00gk

# op _00gH_power_combination_eval
# LANG: _00fH, _00fn --> _00gI
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gH_power_combination_eval_pv587__00gI_pv545__00fn
temp_power = _00gH_coeff_temp*(v545__00fn)*1
pv587__00gI_pv555__00fH = temp_power.flatten()
temp_power = _00gH_coeff_temp*1*(v555__00fH)
pv587__00gI_pv545__00fn = temp_power.flatten()
path_to_v555__00fH += DIAG_MULT(path_to_v587__00gI,pv587__00gI_pv555__00fH)
path_to_v545__00fn += DIAG_MULT(path_to_v587__00gI,pv587__00gI_pv545__00fn)
del path_to_v587__00gI
del pv587__00gI_pv545__00fn
del pv587__00gI_pv555__00fH

# op _00fW_power_combination_eval
# LANG: _00eQ, _00f9 --> _00fX
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fW_power_combination_eval_pv563__00fX_pv538__00f9
temp_power = _00fW_coeff_temp*1*(v538__00f9)
pv563__00fX_pv528__00eQ = temp_power.flatten()
temp_power = _00fW_coeff_temp*(v528__00eQ)*1
pv563__00fX_pv538__00f9 = temp_power.flatten()
path_to_v528__00eQ += DIAG_MULT(path_to_v563__00fX,pv563__00fX_pv528__00eQ)
path_to_v538__00f9 += DIAG_MULT(path_to_v563__00fX,pv563__00fX_pv538__00f9)
del path_to_v563__00fX
del pv563__00fX_pv528__00eQ
del pv563__00fX_pv538__00f9

# op _00fU_single_tensor_sum_with_axis_eval
# LANG: _00fT --> _00fV
# SHAPES: (1, 40000, 3) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fU_single_tensor_sum_with_axis_eval_pv562__00fV_pv561__00fT
path_to_v561__00fT = STD_MULT(path_to_v562__00fV,pv562__00fV_pv561__00fT)
del path_to_v562__00fV

# op _00fM_power_combination_eval
# LANG: _00fL --> _00fN
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fM_power_combination_eval_pv558__00fN_pv557__00fL
temp_power = _00fM_coeff_temp*0.5*(v557__00fL**-0.5)
pv558__00fN_pv557__00fL = temp_power.flatten()
path_to_v557__00fL = DIAG_MULT(path_to_v558__00fN,pv558__00fN_pv557__00fL)
del path_to_v558__00fN
del pv558__00fN_pv557__00fL

# op _00dv_linear_combination_eval
# LANG: _00di --> _00dw
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dv_linear_combination_eval_pv482__00dw_pv475__00di
path_to_v475__00di += DIAG_MULT(path_to_v482__00dw,pv482__00dw_pv475__00di)
del path_to_v482__00dw

# op _00dl_linear_combination_eval
# LANG: _00dg --> _00dm
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dl_linear_combination_eval_pv477__00dm_pv474__00dg
path_to_v474__00dg += DIAG_MULT(path_to_v477__00dm,pv477__00dm_pv474__00dg)
del path_to_v477__00dm

# op _00dd_single_tensor_sum_with_axis_eval
# LANG: _00dc --> _00de
# SHAPES: (1, 55200, 3) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dd_single_tensor_sum_with_axis_eval_pv473__00de_pv472__00dc
path_to_v472__00dc = STD_MULT(path_to_v473__00de,pv473__00de_pv472__00dc)
del path_to_v473__00de

# op _00dP_power_combination_eval
# LANG: _00dO, _009i --> _00dQ
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dP_power_combination_eval_pv492__00dQ_pv349__009i
temp_power = _00dP_coeff_temp*1*(v349__009i)
pv492__00dQ_pv491__00dO = temp_power.flatten()
temp_power = _00dP_coeff_temp*(v491__00dO)*1
pv492__00dQ_pv349__009i = temp_power.flatten()
path_to_v491__00dO = DIAG_MULT(path_to_v492__00dQ,pv492__00dQ_pv491__00dO)
path_to_v349__009i = DIAG_MULT(path_to_v492__00dQ,pv492__00dQ_pv349__009i)
del path_to_v492__00dQ
del pv492__00dQ_pv349__009i
del pv492__00dQ_pv491__00dO

# op _00dL_linear_combination_eval
# LANG: _00dg, _00di --> _00dM
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dL_linear_combination_eval_pv490__00dM_pv475__00di
path_to_v474__00dg += DIAG_MULT(path_to_v490__00dM,pv490__00dM_pv474__00dg)
path_to_v475__00di += DIAG_MULT(path_to_v490__00dM,pv490__00dM_pv475__00di)
del path_to_v490__00dM

# op _00cq_linear_combination_eval
# LANG: _00cp --> _00cr
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cq_linear_combination_eval_pv448__00cr_pv447__00cp
path_to_v447__00cp = DIAG_MULT(path_to_v448__00cr,pv448__00cr_pv447__00cp)
del path_to_v448__00cr

# op _00cU_linear_combination_eval
# LANG: _00cP, _00cT --> _00cV
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cU_linear_combination_eval_pv463__00cV_pv462__00cT
path_to_v460__00cP = DIAG_MULT(path_to_v463__00cV,pv463__00cV_pv460__00cP)
path_to_v462__00cT = DIAG_MULT(path_to_v463__00cV,pv463__00cV_pv462__00cT)
del path_to_v463__00cV

# op _00cK_power_combination_eval
# LANG: _00ch --> _00cL
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cK_power_combination_eval_pv458__00cL_pv443__00ch
temp_power = _00cK_coeff_temp*2*(v443__00ch)
pv458__00cL_pv443__00ch = temp_power.flatten()
path_to_v443__00ch += DIAG_MULT(path_to_v458__00cL,pv458__00cL_pv443__00ch)
del pv458__00cL_pv443__00ch
del path_to_v458__00cL

# op _00cI_power_combination_eval
# LANG: _00cj, _00cl --> _00cJ
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cI_power_combination_eval_pv457__00cJ_pv445__00cl
temp_power = _00cI_coeff_temp*1*(v445__00cl)
pv457__00cJ_pv444__00cj = temp_power.flatten()
temp_power = _00cI_coeff_temp*(v444__00cj)*1
pv457__00cJ_pv445__00cl = temp_power.flatten()
path_to_v444__00cj += DIAG_MULT(path_to_v457__00cJ,pv457__00cJ_pv444__00cj)
path_to_v445__00cl += DIAG_MULT(path_to_v457__00cJ,pv457__00cJ_pv445__00cl)
del pv457__00cJ_pv444__00cj
del pv457__00cJ_pv445__00cl
del path_to_v457__00cJ

# op _00cA_linear_combination_eval
# LANG: _00cz --> _00cB
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cA_linear_combination_eval_pv453__00cB_pv452__00cz
path_to_v452__00cz = DIAG_MULT(path_to_v453__00cB,pv453__00cB_pv452__00cz)
del path_to_v453__00cB

# op _00bz_linear_combination_eval
# LANG: _00bo, _00bk --> _00bA
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bz_linear_combination_eval_pv421__00bA_pv413__00bk
path_to_v415__00bo = DIAG_MULT(path_to_v421__00bA,pv421__00bA_pv415__00bo)
path_to_v413__00bk = DIAG_MULT(path_to_v421__00bA,pv421__00bA_pv413__00bk)
del path_to_v421__00bA

# op _00bv_power_combination_eval
# LANG: _00bu --> _00bw
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bv_power_combination_eval_pv419__00bw_pv418__00bu
temp_power = _00bv_coeff_temp*0.5*(v418__00bu**-0.5)
pv419__00bw_pv418__00bu = temp_power.flatten()
path_to_v418__00bu = DIAG_MULT(path_to_v419__00bw,pv419__00bw_pv418__00bu)
del path_to_v419__00bw
del pv419__00bw_pv418__00bu

# op _00bp_linear_combination_eval
# LANG: _00bm, _00bk --> _00bq
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bp_linear_combination_eval_pv416__00bq_pv413__00bk
path_to_v414__00bm = DIAG_MULT(path_to_v416__00bq,pv416__00bq_pv414__00bm)
path_to_v413__00bk += DIAG_MULT(path_to_v416__00bq,pv416__00bq_pv413__00bk)
del path_to_v416__00bq

# op _00bZ_power_combination_eval
# LANG: _00bY --> _00b_
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bZ_power_combination_eval_pv434__00b__pv433__00bY
temp_power = _00bZ_coeff_temp*1
pv434__00b__pv433__00bY = temp_power.flatten()
path_to_v433__00bY = DIAG_MULT(path_to_v434__00b_,pv434__00b__pv433__00bY)
del path_to_v434__00b_
del pv434__00b__pv433__00bY

# op _00bP_linear_combination_eval
# LANG: _00bM, _00bO --> _00bQ
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bP_linear_combination_eval_pv429__00bQ_pv428__00bO
path_to_v427__00bM = DIAG_MULT(path_to_v429__00bQ,pv429__00bQ_pv427__00bM)
path_to_v428__00bO = DIAG_MULT(path_to_v429__00bQ,pv429__00bQ_pv428__00bO)
del path_to_v429__00bQ

# op _00bF_power_combination_eval
# LANG: _00bE --> _00bG
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bF_power_combination_eval_pv424__00bG_pv423__00bE
temp_power = _00bF_coeff_temp*0.5*(v423__00bE**-0.5)
pv424__00bG_pv423__00bE = temp_power.flatten()
path_to_v423__00bE = DIAG_MULT(path_to_v424__00bG,pv424__00bG_pv423__00bE)
del path_to_v424__00bG
del pv424__00bG_pv423__00bE

# op _00b1_power_combination_eval
# LANG: _00b0 --> _00b2
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00b1_power_combination_eval_pv404__00b2_pv403__00b0
temp_power = _00b1_coeff_temp*1
pv404__00b2_pv403__00b0 = temp_power.flatten()
path_to_v403__00b0 = DIAG_MULT(path_to_v404__00b2,pv404__00b2_pv403__00b0)
del pv404__00b2_pv403__00b0
del path_to_v404__00b2

# op _00ay_power_combination_eval
# LANG: _00ax --> _00az
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00ay_power_combination_eval_pv389__00az_pv388__00ax
temp_power = _00ay_coeff_temp*0.5*(v388__00ax**-0.5)
pv389__00az_pv388__00ax = temp_power.flatten()
path_to_v388__00ax = DIAG_MULT(path_to_v389__00az,pv389__00az_pv388__00ax)
del path_to_v389__00az
del pv389__00az_pv388__00ax

# op _00as_linear_combination_eval
# LANG: _00ap, _00an --> _00at
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00as_linear_combination_eval_pv386__00at_pv383__00an
path_to_v384__00ap = DIAG_MULT(path_to_v386__00at,pv386__00at_pv384__00ap)
path_to_v383__00an = DIAG_MULT(path_to_v386__00at,pv386__00at_pv383__00an)
del path_to_v386__00at

# op _00aS_linear_combination_eval
# LANG: _00aP, _00aR --> _00aT
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00aS_linear_combination_eval_pv399__00aT_pv398__00aR
path_to_v397__00aP = DIAG_MULT(path_to_v399__00aT,pv399__00aT_pv397__00aP)
path_to_v398__00aR = DIAG_MULT(path_to_v399__00aT,pv399__00aT_pv398__00aR)
del path_to_v399__00aT

# op _00aI_power_combination_eval
# LANG: _00aH --> _00aJ
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00aI_power_combination_eval_pv394__00aJ_pv393__00aH
temp_power = _00aI_coeff_temp*0.5*(v393__00aH**-0.5)
pv394__00aJ_pv393__00aH = temp_power.flatten()
path_to_v393__00aH = DIAG_MULT(path_to_v394__00aJ,pv394__00aJ_pv393__00aH)
del pv394__00aJ_pv393__00aH
del path_to_v394__00aJ

# op _00aC_linear_combination_eval
# LANG: _00ar, _00an --> _00aD
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00aC_linear_combination_eval_pv391__00aD_pv383__00an
path_to_v385__00ar = DIAG_MULT(path_to_v391__00aD,pv391__00aD_pv385__00ar)
path_to_v383__00an += DIAG_MULT(path_to_v391__00aD,pv391__00aD_pv383__00an)
del path_to_v391__00aD

# op _00gh_power_combination_eval
# LANG: _00fn, _00f3 --> _00gi
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gh_power_combination_eval_pv574__00gi_pv535__00f3
temp_power = _00gh_coeff_temp*(v535__00f3)*1
pv574__00gi_pv545__00fn = temp_power.flatten()
temp_power = _00gh_coeff_temp*1*(v545__00fn)
pv574__00gi_pv535__00f3 = temp_power.flatten()
path_to_v545__00fn += DIAG_MULT(path_to_v574__00gi,pv574__00gi_pv545__00fn)
path_to_v535__00f3 += DIAG_MULT(path_to_v574__00gi,pv574__00gi_pv535__00f3)
del pv574__00gi_pv545__00fn
del path_to_v574__00gi
del pv574__00gi_pv535__00f3

# op _00fs_power_combination_eval
# LANG: _00fr --> _00ft
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fs_power_combination_eval_pv548__00ft_pv547__00fr
temp_power = _00fs_coeff_temp*0.5*(v547__00fr**-0.5)
pv548__00ft_pv547__00fr = temp_power.flatten()
path_to_v547__00fr = DIAG_MULT(path_to_v548__00ft,pv548__00ft_pv547__00fr)
del path_to_v548__00ft
del pv548__00ft_pv547__00fr

# op _00fS_power_combination_eval
# LANG: _00eK, _00f3 --> _00fT
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fS_power_combination_eval_pv561__00fT_pv535__00f3
temp_power = _00fS_coeff_temp*1*(v535__00f3)
pv561__00fT_pv525__00eK = temp_power.flatten()
temp_power = _00fS_coeff_temp*(v525__00eK)*1
pv561__00fT_pv535__00f3 = temp_power.flatten()
path_to_v525__00eK += DIAG_MULT(path_to_v561__00fT,pv561__00fT_pv525__00eK)
path_to_v535__00f3 += DIAG_MULT(path_to_v561__00fT,pv561__00fT_pv535__00f3)
del path_to_v561__00fT
del pv561__00fT_pv535__00f3
del pv561__00fT_pv525__00eK

# op _00fK_single_tensor_sum_with_axis_eval
# LANG: _00fJ --> _00fL
# SHAPES: (1, 40000, 3) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fK_single_tensor_sum_with_axis_eval_pv557__00fL_pv556__00fJ
path_to_v556__00fJ = STD_MULT(path_to_v557__00fL,pv557__00fL_pv556__00fJ)
del path_to_v557__00fL

# op _00f8_power_combination_eval
# LANG: _00f7 --> _00f9
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00f8_power_combination_eval_pv538__00f9_pv537__00f7
temp_power = _00f8_coeff_temp*0.5*(v537__00f7**-0.5)
pv538__00f9_pv537__00f7 = temp_power.flatten()
path_to_v537__00f7 = DIAG_MULT(path_to_v538__00f9,pv538__00f9_pv537__00f7)
del pv538__00f9_pv537__00f7
del path_to_v538__00f9

# op _00eP_power_combination_eval
# LANG: _00eO --> _00eQ
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00eP_power_combination_eval_pv528__00eQ_pv527__00eO
temp_power = _00eP_coeff_temp*0.5*(v527__00eO**-0.5)
pv528__00eQ_pv527__00eO = temp_power.flatten()
path_to_v527__00eO = DIAG_MULT(path_to_v528__00eQ,pv528__00eQ_pv527__00eO)
del pv528__00eQ_pv527__00eO
del path_to_v528__00eQ

# op _00dh_power_combination_eval
# LANG: _009i --> _00di
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dh_power_combination_eval_pv475__00di_pv349__009i
temp_power = _00dh_coeff_temp*2*(v349__009i)
pv475__00di_pv349__009i = temp_power.flatten()
path_to_v349__009i += DIAG_MULT(path_to_v475__00di,pv475__00di_pv349__009i)
del path_to_v475__00di
del pv475__00di_pv349__009i

# op _00df_power_combination_eval
# LANG: _00af --> _00dg
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00df_power_combination_eval_pv474__00dg_pv379__00af
temp_power = _00df_coeff_temp*2*(v379__00af)
pv474__00dg_pv379__00af = temp_power.flatten()
path_to_v379__00af = DIAG_MULT(path_to_v474__00dg,pv474__00dg_pv379__00af)
del path_to_v474__00dg
del pv474__00dg_pv379__00af

# op _00db_power_combination_eval
# LANG: _00a9, _009c --> _00dc
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00db_power_combination_eval_pv472__00dc_pv346__009c
temp_power = _00db_coeff_temp*1*(v346__009c)
pv472__00dc_pv376__00a9 = temp_power.flatten()
temp_power = _00db_coeff_temp*(v376__00a9)*1
pv472__00dc_pv346__009c = temp_power.flatten()
path_to_v376__00a9 += DIAG_MULT(path_to_v472__00dc,pv472__00dc_pv376__00a9)
path_to_v346__009c += DIAG_MULT(path_to_v472__00dc,pv472__00dc_pv346__009c)
del pv472__00dc_pv346__009c
del pv472__00dc_pv376__00a9
del path_to_v472__00dc

# op _00dN_power_combination_eval
# LANG: _00af --> _00dO
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dN_power_combination_eval_pv491__00dO_pv379__00af
temp_power = _00dN_coeff_temp*1
pv491__00dO_pv379__00af = temp_power.flatten()
path_to_v379__00af += DIAG_MULT(path_to_v491__00dO,pv491__00dO_pv379__00af)
del pv491__00dO_pv379__00af
del path_to_v491__00dO

# op _00cy_linear_combination_eval
# LANG: _00cl --> _00cz
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cy_linear_combination_eval_pv452__00cz_pv445__00cl
path_to_v445__00cl += DIAG_MULT(path_to_v452__00cz,pv452__00cz_pv445__00cl)
del path_to_v452__00cz

# op _00co_linear_combination_eval
# LANG: _00cj --> _00cp
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00co_linear_combination_eval_pv447__00cp_pv444__00cj
path_to_v444__00cj += DIAG_MULT(path_to_v447__00cp,pv447__00cp_pv444__00cj)
del path_to_v447__00cp

# op _00cg_single_tensor_sum_with_axis_eval
# LANG: _00cf --> _00ch
# SHAPES: (1, 55200, 3) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cg_single_tensor_sum_with_axis_eval_pv443__00ch_pv442__00cf
path_to_v442__00cf = STD_MULT(path_to_v443__00ch,pv443__00ch_pv442__00cf)
del path_to_v443__00ch

# op _00cS_power_combination_eval
# LANG: _00af, _00cR --> _00cT
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cS_power_combination_eval_pv462__00cT_pv461__00cR
temp_power = _00cS_coeff_temp*(v461__00cR)*1
pv462__00cT_pv379__00af = temp_power.flatten()
temp_power = _00cS_coeff_temp*1*(v379__00af)
pv462__00cT_pv461__00cR = temp_power.flatten()
path_to_v379__00af += DIAG_MULT(path_to_v462__00cT,pv462__00cT_pv379__00af)
path_to_v461__00cR = DIAG_MULT(path_to_v462__00cT,pv462__00cT_pv461__00cR)
del pv462__00cT_pv379__00af
del pv462__00cT_pv461__00cR
del path_to_v462__00cT

# op _00cO_linear_combination_eval
# LANG: _00cj, _00cl --> _00cP
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cO_linear_combination_eval_pv460__00cP_pv445__00cl
path_to_v444__00cj += DIAG_MULT(path_to_v460__00cP,pv460__00cP_pv444__00cj)
path_to_v445__00cl += DIAG_MULT(path_to_v460__00cP,pv460__00cP_pv445__00cl)
del path_to_v460__00cP

# op _00bt_linear_combination_eval
# LANG: _00bs --> _00bu
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bt_linear_combination_eval_pv418__00bu_pv417__00bs
path_to_v417__00bs = DIAG_MULT(path_to_v418__00bu,pv418__00bu_pv417__00bs)
del path_to_v418__00bu

# op _00bX_linear_combination_eval
# LANG: _00bS, _00bW --> _00bY
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bX_linear_combination_eval_pv433__00bY_pv432__00bW
path_to_v430__00bS = DIAG_MULT(path_to_v433__00bY,pv433__00bY_pv430__00bS)
path_to_v432__00bW = DIAG_MULT(path_to_v433__00bY,pv433__00bY_pv432__00bW)
del path_to_v433__00bY

# op _00bN_power_combination_eval
# LANG: _00bk --> _00bO
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bN_power_combination_eval_pv428__00bO_pv413__00bk
temp_power = _00bN_coeff_temp*2*(v413__00bk)
pv428__00bO_pv413__00bk = temp_power.flatten()
path_to_v413__00bk += DIAG_MULT(path_to_v428__00bO,pv428__00bO_pv413__00bk)
del path_to_v428__00bO
del pv428__00bO_pv413__00bk

# op _00bL_power_combination_eval
# LANG: _00bm, _00bo --> _00bM
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bL_power_combination_eval_pv427__00bM_pv415__00bo
temp_power = _00bL_coeff_temp*1*(v415__00bo)
pv427__00bM_pv414__00bm = temp_power.flatten()
temp_power = _00bL_coeff_temp*(v414__00bm)*1
pv427__00bM_pv415__00bo = temp_power.flatten()
path_to_v414__00bm += DIAG_MULT(path_to_v427__00bM,pv427__00bM_pv414__00bm)
path_to_v415__00bo += DIAG_MULT(path_to_v427__00bM,pv427__00bM_pv415__00bo)
del path_to_v427__00bM
del pv427__00bM_pv414__00bm
del pv427__00bM_pv415__00bo

# op _00bD_linear_combination_eval
# LANG: _00bC --> _00bE
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bD_linear_combination_eval_pv423__00bE_pv422__00bC
path_to_v422__00bC = DIAG_MULT(path_to_v423__00bE,pv423__00bE_pv422__00bC)
del path_to_v423__00bE

# op _00aw_linear_combination_eval
# LANG: _00av --> _00ax
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00aw_linear_combination_eval_pv388__00ax_pv387__00av
path_to_v387__00av = DIAG_MULT(path_to_v388__00ax,pv388__00ax_pv387__00av)
del path_to_v388__00ax

# op _00a__linear_combination_eval
# LANG: _00aV, _00aZ --> _00b0
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00a__linear_combination_eval_pv403__00b0_pv402__00aZ
path_to_v400__00aV = DIAG_MULT(path_to_v403__00b0,pv403__00b0_pv400__00aV)
path_to_v402__00aZ = DIAG_MULT(path_to_v403__00b0,pv403__00b0_pv402__00aZ)
del path_to_v403__00b0

# op _00aQ_power_combination_eval
# LANG: _00an --> _00aR
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00aQ_power_combination_eval_pv398__00aR_pv383__00an
temp_power = _00aQ_coeff_temp*2*(v383__00an)
pv398__00aR_pv383__00an = temp_power.flatten()
path_to_v383__00an += DIAG_MULT(path_to_v398__00aR,pv398__00aR_pv383__00an)
del pv398__00aR_pv383__00an
del path_to_v398__00aR

# op _00aO_power_combination_eval
# LANG: _00ap, _00ar --> _00aP
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00aO_power_combination_eval_pv397__00aP_pv385__00ar
temp_power = _00aO_coeff_temp*1*(v385__00ar)
pv397__00aP_pv384__00ap = temp_power.flatten()
temp_power = _00aO_coeff_temp*(v384__00ap)*1
pv397__00aP_pv385__00ar = temp_power.flatten()
path_to_v384__00ap += DIAG_MULT(path_to_v397__00aP,pv397__00aP_pv384__00ap)
path_to_v385__00ar += DIAG_MULT(path_to_v397__00aP,pv397__00aP_pv385__00ar)
del path_to_v397__00aP
del pv397__00aP_pv384__00ap
del pv397__00aP_pv385__00ar

# op _00aG_linear_combination_eval
# LANG: _00aF --> _00aH
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00aG_linear_combination_eval_pv393__00aH_pv392__00aF
path_to_v392__00aF = DIAG_MULT(path_to_v393__00aH,pv393__00aH_pv392__00aF)
del path_to_v393__00aH

# op _00fq_single_tensor_sum_with_axis_eval
# LANG: _00fp --> _00fr
# SHAPES: (1, 40000, 3) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fq_single_tensor_sum_with_axis_eval_pv547__00fr_pv546__00fp
path_to_v546__00fp = STD_MULT(path_to_v547__00fr,pv547__00fr_pv546__00fp)
del path_to_v547__00fr

# op _00fI_power_combination_eval
# LANG: _00fH --> _00fJ
# SHAPES: (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fI_power_combination_eval_pv556__00fJ_pv555__00fH
temp_power = _00fI_coeff_temp*2*(v555__00fH)
pv556__00fJ_pv555__00fH = temp_power.flatten()
path_to_v555__00fH += DIAG_MULT(path_to_v556__00fJ,pv556__00fJ_pv555__00fH)
del path_to_v556__00fJ
del pv556__00fJ_pv555__00fH

# op _00f6_single_tensor_sum_with_axis_eval
# LANG: _00f5 --> _00f7
# SHAPES: (1, 40000, 3) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00f6_single_tensor_sum_with_axis_eval_pv537__00f7_pv536__00f5
path_to_v536__00f5 = STD_MULT(path_to_v537__00f7,pv537__00f7_pv536__00f5)
del path_to_v537__00f7

# op _00eN_single_tensor_sum_with_axis_eval
# LANG: _00eM --> _00eO
# SHAPES: (1, 40000, 3) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00eN_single_tensor_sum_with_axis_eval_pv527__00eO_pv526__00eM
path_to_v526__00eM = STD_MULT(path_to_v527__00eO,pv527__00eO_pv526__00eM)
del path_to_v527__00eO

# op _00ck_power_combination_eval
# LANG: _00af --> _00cl
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00ck_power_combination_eval_pv445__00cl_pv379__00af
temp_power = _00ck_coeff_temp*2*(v379__00af)
pv445__00cl_pv379__00af = temp_power.flatten()
path_to_v379__00af += DIAG_MULT(path_to_v445__00cl,pv445__00cl_pv379__00af)
del pv445__00cl_pv379__00af
del path_to_v445__00cl

# op _00ci_power_combination_eval
# LANG: _009W --> _00cj
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00ci_power_combination_eval_pv444__00cj_pv369__009W
temp_power = _00ci_coeff_temp*2*(v369__009W)
pv444__00cj_pv369__009W = temp_power.flatten()
path_to_v369__009W = DIAG_MULT(path_to_v444__00cj,pv444__00cj_pv369__009W)
del path_to_v444__00cj
del pv444__00cj_pv369__009W

# op _00ce_power_combination_eval
# LANG: _00a9, _009Q --> _00cf
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00ce_power_combination_eval_pv442__00cf_pv366__009Q
temp_power = _00ce_coeff_temp*(v366__009Q)*1
pv442__00cf_pv376__00a9 = temp_power.flatten()
temp_power = _00ce_coeff_temp*1*(v376__00a9)
pv442__00cf_pv366__009Q = temp_power.flatten()
path_to_v376__00a9 += DIAG_MULT(path_to_v442__00cf,pv442__00cf_pv376__00a9)
path_to_v366__009Q += DIAG_MULT(path_to_v442__00cf,pv442__00cf_pv366__009Q)
del path_to_v442__00cf
del pv442__00cf_pv376__00a9
del pv442__00cf_pv366__009Q

# op _00cQ_power_combination_eval
# LANG: _009W --> _00cR
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cQ_power_combination_eval_pv461__00cR_pv369__009W
temp_power = _00cQ_coeff_temp*1
pv461__00cR_pv369__009W = temp_power.flatten()
path_to_v369__009W += DIAG_MULT(path_to_v461__00cR,pv461__00cR_pv369__009W)
del pv461__00cR_pv369__009W
del path_to_v461__00cR

# op _00br_linear_combination_eval
# LANG: _00bm --> _00bs
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00br_linear_combination_eval_pv417__00bs_pv414__00bm
path_to_v414__00bm += DIAG_MULT(path_to_v417__00bs,pv417__00bs_pv414__00bm)
del path_to_v417__00bs

# op _00bj_single_tensor_sum_with_axis_eval
# LANG: _00bi --> _00bk
# SHAPES: (1, 55200, 3) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bj_single_tensor_sum_with_axis_eval_pv413__00bk_pv412__00bi
path_to_v412__00bi = STD_MULT(path_to_v413__00bk,pv413__00bk_pv412__00bi)
del path_to_v413__00bk

# op _00bV_power_combination_eval
# LANG: _009W, _00bU --> _00bW
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bV_power_combination_eval_pv432__00bW_pv431__00bU
temp_power = _00bV_coeff_temp*(v431__00bU)*1
pv432__00bW_pv369__009W = temp_power.flatten()
temp_power = _00bV_coeff_temp*1*(v369__009W)
pv432__00bW_pv431__00bU = temp_power.flatten()
path_to_v369__009W += DIAG_MULT(path_to_v432__00bW,pv432__00bW_pv369__009W)
path_to_v431__00bU = DIAG_MULT(path_to_v432__00bW,pv432__00bW_pv431__00bU)
del path_to_v432__00bW
del pv432__00bW_pv431__00bU
del pv432__00bW_pv369__009W

# op _00bR_linear_combination_eval
# LANG: _00bm, _00bo --> _00bS
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bR_linear_combination_eval_pv430__00bS_pv415__00bo
path_to_v414__00bm += DIAG_MULT(path_to_v430__00bS,pv430__00bS_pv414__00bm)
path_to_v415__00bo += DIAG_MULT(path_to_v430__00bS,pv430__00bS_pv415__00bo)
del path_to_v430__00bS

# op _00bB_linear_combination_eval
# LANG: _00bo --> _00bC
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bB_linear_combination_eval_pv422__00bC_pv415__00bo
path_to_v415__00bo += DIAG_MULT(path_to_v422__00bC,pv422__00bC_pv415__00bo)
del path_to_v422__00bC

# op _00au_linear_combination_eval
# LANG: _00ap --> _00av
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00au_linear_combination_eval_pv387__00av_pv384__00ap
path_to_v384__00ap += DIAG_MULT(path_to_v387__00av,pv387__00av_pv384__00ap)
del path_to_v387__00av

# op _00am_single_tensor_sum_with_axis_eval
# LANG: _00al --> _00an
# SHAPES: (1, 55200, 3) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00am_single_tensor_sum_with_axis_eval_pv383__00an_pv382__00al
path_to_v382__00al = STD_MULT(path_to_v383__00an,pv383__00an_pv382__00al)
del path_to_v383__00an

# op _00aY_power_combination_eval
# LANG: _009C, _00aX --> _00aZ
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00aY_power_combination_eval_pv402__00aZ_pv401__00aX
temp_power = _00aY_coeff_temp*(v401__00aX)*1
pv402__00aZ_pv359__009C = temp_power.flatten()
temp_power = _00aY_coeff_temp*1*(v359__009C)
pv402__00aZ_pv401__00aX = temp_power.flatten()
path_to_v359__009C = DIAG_MULT(path_to_v402__00aZ,pv402__00aZ_pv359__009C)
path_to_v401__00aX = DIAG_MULT(path_to_v402__00aZ,pv402__00aZ_pv401__00aX)
del pv402__00aZ_pv401__00aX
del path_to_v402__00aZ
del pv402__00aZ_pv359__009C

# op _00aU_linear_combination_eval
# LANG: _00ap, _00ar --> _00aV
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00aU_linear_combination_eval_pv400__00aV_pv385__00ar
path_to_v384__00ap += DIAG_MULT(path_to_v400__00aV,pv400__00aV_pv384__00ap)
path_to_v385__00ar += DIAG_MULT(path_to_v400__00aV,pv400__00aV_pv385__00ar)
del path_to_v400__00aV

# op _00aE_linear_combination_eval
# LANG: _00ar --> _00aF
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00aE_linear_combination_eval_pv392__00aF_pv385__00ar
path_to_v385__00ar += DIAG_MULT(path_to_v392__00aF,pv392__00aF_pv385__00ar)
del path_to_v392__00aF

# op _00fo_power_combination_eval
# LANG: _00fn --> _00fp
# SHAPES: (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fo_power_combination_eval_pv546__00fp_pv545__00fn
temp_power = _00fo_coeff_temp*2*(v545__00fn)
pv546__00fp_pv545__00fn = temp_power.flatten()
path_to_v545__00fn += DIAG_MULT(path_to_v546__00fp,pv546__00fp_pv545__00fn)
del pv546__00fp_pv545__00fn
del path_to_v546__00fp

# op _00fG_linear_combination_eval
# LANG: _00fz, _00fF --> _00fH
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fG_linear_combination_eval_pv555__00fH_pv554__00fF
path_to_v551__00fz = DIAG_MULT(path_to_v555__00fH,pv555__00fH_pv551__00fz)
path_to_v554__00fF = DIAG_MULT(path_to_v555__00fH,pv555__00fH_pv554__00fF)
del path_to_v555__00fH

# op _00f4_power_combination_eval
# LANG: _00f3 --> _00f5
# SHAPES: (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00f4_power_combination_eval_pv536__00f5_pv535__00f3
temp_power = _00f4_coeff_temp*2*(v535__00f3)
pv536__00f5_pv535__00f3 = temp_power.flatten()
path_to_v535__00f3 += DIAG_MULT(path_to_v536__00f5,pv536__00f5_pv535__00f3)
del path_to_v536__00f5
del pv536__00f5_pv535__00f3

# op _00eL_power_combination_eval
# LANG: _00eK --> _00eM
# SHAPES: (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00eL_power_combination_eval_pv526__00eM_pv525__00eK
temp_power = _00eL_coeff_temp*2*(v525__00eK)
pv526__00eM_pv525__00eK = temp_power.flatten()
path_to_v525__00eK += DIAG_MULT(path_to_v526__00eM,pv526__00eM_pv525__00eK)
del path_to_v526__00eM
del pv526__00eM_pv525__00eK

# op _00bn_power_combination_eval
# LANG: _009W --> _00bo
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bn_power_combination_eval_pv415__00bo_pv369__009W
temp_power = _00bn_coeff_temp*2*(v369__009W)
pv415__00bo_pv369__009W = temp_power.flatten()
path_to_v369__009W += DIAG_MULT(path_to_v415__00bo,pv415__00bo_pv369__009W)
del path_to_v415__00bo
del pv415__00bo_pv369__009W

# op _00bl_power_combination_eval
# LANG: _009C --> _00bm
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bl_power_combination_eval_pv414__00bm_pv359__009C
temp_power = _00bl_coeff_temp*2*(v359__009C)
pv414__00bm_pv359__009C = temp_power.flatten()
path_to_v359__009C += DIAG_MULT(path_to_v414__00bm,pv414__00bm_pv359__009C)
del path_to_v414__00bm
del pv414__00bm_pv359__009C

# op _00bh_power_combination_eval
# LANG: _009Q, _009w --> _00bi
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bh_power_combination_eval_pv412__00bi_pv356__009w
temp_power = _00bh_coeff_temp*(v356__009w)*1
pv412__00bi_pv366__009Q = temp_power.flatten()
temp_power = _00bh_coeff_temp*1*(v366__009Q)
pv412__00bi_pv356__009w = temp_power.flatten()
path_to_v366__009Q += DIAG_MULT(path_to_v412__00bi,pv412__00bi_pv366__009Q)
path_to_v356__009w += DIAG_MULT(path_to_v412__00bi,pv412__00bi_pv356__009w)
del path_to_v412__00bi
del pv412__00bi_pv356__009w
del pv412__00bi_pv366__009Q

# op _00bT_power_combination_eval
# LANG: _009C --> _00bU
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bT_power_combination_eval_pv431__00bU_pv359__009C
temp_power = _00bT_coeff_temp*1
pv431__00bU_pv359__009C = temp_power.flatten()
path_to_v359__009C += DIAG_MULT(path_to_v431__00bU,pv431__00bU_pv359__009C)
del path_to_v431__00bU
del pv431__00bU_pv359__009C

# op _00aq_power_combination_eval
# LANG: _009C --> _00ar
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00aq_power_combination_eval_pv385__00ar_pv359__009C
temp_power = _00aq_coeff_temp*2*(v359__009C)
pv385__00ar_pv359__009C = temp_power.flatten()
path_to_v359__009C += DIAG_MULT(path_to_v385__00ar,pv385__00ar_pv359__009C)
del path_to_v385__00ar
del pv385__00ar_pv359__009C

# op _00ao_power_combination_eval
# LANG: _009i --> _00ap
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00ao_power_combination_eval_pv384__00ap_pv349__009i
temp_power = _00ao_coeff_temp*2*(v349__009i)
pv384__00ap_pv349__009i = temp_power.flatten()
path_to_v349__009i += DIAG_MULT(path_to_v384__00ap,pv384__00ap_pv349__009i)
del pv384__00ap_pv349__009i
del path_to_v384__00ap

# op _00ak_power_combination_eval
# LANG: _009c, _009w --> _00al
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00ak_power_combination_eval_pv382__00al_pv356__009w
temp_power = _00ak_coeff_temp*1*(v356__009w)
pv382__00al_pv346__009c = temp_power.flatten()
temp_power = _00ak_coeff_temp*(v346__009c)*1
pv382__00al_pv356__009w = temp_power.flatten()
path_to_v346__009c += DIAG_MULT(path_to_v382__00al,pv382__00al_pv346__009c)
path_to_v356__009w += DIAG_MULT(path_to_v382__00al,pv382__00al_pv356__009w)
del pv382__00al_pv346__009c
del pv382__00al_pv356__009w
del path_to_v382__00al

# op _00ae_power_combination_eval
# LANG: _00ad --> _00af
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00ae_power_combination_eval_pv379__00af_pv378__00ad
temp_power = _00ae_coeff_temp*0.5*(v378__00ad**-0.5)
pv379__00af_pv378__00ad = temp_power.flatten()
path_to_v378__00ad = DIAG_MULT(path_to_v379__00af,pv379__00af_pv378__00ad)
del pv379__00af_pv378__00ad
del path_to_v379__00af

# op _00aW_power_combination_eval
# LANG: _009i --> _00aX
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00aW_power_combination_eval_pv401__00aX_pv349__009i
temp_power = _00aW_coeff_temp*1
pv401__00aX_pv349__009i = temp_power.flatten()
path_to_v349__009i += DIAG_MULT(path_to_v401__00aX,pv401__00aX_pv349__009i)
del path_to_v401__00aX
del pv401__00aX_pv349__009i

# op _00fy reshape_eval
# LANG: _00fx --> _00fz
# SHAPES: (1, 200, 200, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fy reshape_eval_pv551__00fz_pv550__00fx
path_to_v550__00fx = DIAG_MULT(path_to_v551__00fz,pv551__00fz_pv550__00fx)
del path_to_v551__00fz

# op _00fm_linear_combination_eval
# LANG: _00ff, _00fl --> _00fn
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fm_linear_combination_eval_pv545__00fn_pv544__00fl
path_to_v541__00ff = DIAG_MULT(path_to_v545__00fn,pv545__00fn_pv541__00ff)
path_to_v544__00fl = DIAG_MULT(path_to_v545__00fn,pv545__00fn_pv544__00fl)
del path_to_v545__00fn

# op _00fE reshape_eval
# LANG: _00fD --> _00fF
# SHAPES: (1, 200, 200, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fE reshape_eval_pv554__00fF_pv553__00fD
path_to_v553__00fD = DIAG_MULT(path_to_v554__00fF,pv554__00fF_pv553__00fD)
del path_to_v554__00fF

# op _00f2_linear_combination_eval
# LANG: _00eW, _00f1 --> _00f3
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00f2_linear_combination_eval_pv535__00f3_pv534__00f1
path_to_v531__00eW = DIAG_MULT(path_to_v535__00f3,pv535__00f3_pv531__00eW)
path_to_v534__00f1 = DIAG_MULT(path_to_v535__00f3,pv535__00f3_pv534__00f1)
del path_to_v535__00f3

# op _00eJ_linear_combination_eval
# LANG: _00eC, _00eI --> _00eK
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00eJ_linear_combination_eval_pv525__00eK_pv524__00eI
path_to_v521__00eC = DIAG_MULT(path_to_v525__00eK,pv525__00eK_pv521__00eC)
path_to_v524__00eI = DIAG_MULT(path_to_v525__00eK,pv525__00eK_pv524__00eI)
del path_to_v525__00eK

# op _00ac_single_tensor_sum_with_axis_eval
# LANG: _00ab --> _00ad
# SHAPES: (1, 55200, 3) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00ac_single_tensor_sum_with_axis_eval_pv378__00ad_pv377__00ab
path_to_v377__00ab = STD_MULT(path_to_v378__00ad,pv378__00ad_pv377__00ab)
del path_to_v378__00ad

# op _009h_power_combination_eval
# LANG: _009g --> _009i
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009h_power_combination_eval_pv349__009i_pv348__009g
temp_power = _009h_coeff_temp*0.5*(v348__009g**-0.5)
pv349__009i_pv348__009g = temp_power.flatten()
path_to_v348__009g = DIAG_MULT(path_to_v349__009i,pv349__009i_pv348__009g)
del pv349__009i_pv348__009g
del path_to_v349__009i

# op _009V_power_combination_eval
# LANG: _009U --> _009W
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009V_power_combination_eval_pv369__009W_pv368__009U
temp_power = _009V_coeff_temp*0.5*(v368__009U**-0.5)
pv369__009W_pv368__009U = temp_power.flatten()
path_to_v368__009U = DIAG_MULT(path_to_v369__009W,pv369__009W_pv368__009U)
del pv369__009W_pv368__009U
del path_to_v369__009W

# op _009B_power_combination_eval
# LANG: _009A --> _009C
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009B_power_combination_eval_pv359__009C_pv358__009A
temp_power = _009B_coeff_temp*0.5*(v358__009A**-0.5)
pv359__009C_pv358__009A = temp_power.flatten()
path_to_v358__009A = DIAG_MULT(path_to_v359__009C,pv359__009C_pv358__009A)
del pv359__009C_pv358__009A
del path_to_v359__009C

# op _00fw expand_array_eval
# LANG: _00fv --> _00fx
# SHAPES: (1, 200, 3) --> (1, 200, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fw expand_array_eval_pv550__00fx_pv549__00fv
path_to_v549__00fv = STD_MULT(path_to_v550__00fx,pv550__00fx_pv549__00fv)
del path_to_v550__00fx

# op _00fk reshape_eval
# LANG: _00fj --> _00fl
# SHAPES: (1, 200, 200, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fk reshape_eval_pv544__00fl_pv543__00fj
path_to_v543__00fj = DIAG_MULT(path_to_v544__00fl,pv544__00fl_pv543__00fj)
del path_to_v544__00fl

# op _00fe reshape_eval
# LANG: _00fd --> _00ff
# SHAPES: (1, 200, 200, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fe reshape_eval_pv541__00ff_pv540__00fd
path_to_v540__00fd = DIAG_MULT(path_to_v541__00ff,pv541__00ff_pv540__00fd)
del path_to_v541__00ff

# op _00fC expand_array_eval
# LANG: _00fB --> _00fD
# SHAPES: (1, 200, 3) --> (1, 200, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fC expand_array_eval_pv553__00fD_pv552__00fB
path_to_v552__00fB = STD_MULT(path_to_v553__00fD,pv553__00fD_pv552__00fB)
del path_to_v553__00fD

# op _00f0 reshape_eval
# LANG: _00e_ --> _00f1
# SHAPES: (1, 200, 200, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00f0 reshape_eval_pv534__00f1_pv533__00e_
path_to_v533__00e_ = DIAG_MULT(path_to_v534__00f1,pv534__00f1_pv533__00e_)
del path_to_v534__00f1

# op _00eV reshape_eval
# LANG: _00eU --> _00eW
# SHAPES: (1, 200, 200, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00eV reshape_eval_pv531__00eW_pv530__00eU
path_to_v530__00eU = DIAG_MULT(path_to_v531__00eW,pv531__00eW_pv530__00eU)
del path_to_v531__00eW

# op _00eH reshape_eval
# LANG: _00eG --> _00eI
# SHAPES: (1, 200, 200, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00eH reshape_eval_pv524__00eI_pv523__00eG
path_to_v523__00eG = DIAG_MULT(path_to_v524__00eI,pv524__00eI_pv523__00eG)
del path_to_v524__00eI

# op _00eB reshape_eval
# LANG: _00eA --> _00eC
# SHAPES: (1, 200, 200, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00eB reshape_eval_pv521__00eC_pv520__00eA
path_to_v520__00eA = DIAG_MULT(path_to_v521__00eC,pv521__00eC_pv520__00eA)
del path_to_v521__00eC

# op _00aa_power_combination_eval
# LANG: _00a9 --> _00ab
# SHAPES: (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00aa_power_combination_eval_pv377__00ab_pv376__00a9
temp_power = _00aa_coeff_temp*2*(v376__00a9)
pv377__00ab_pv376__00a9 = temp_power.flatten()
path_to_v376__00a9 += DIAG_MULT(path_to_v377__00ab,pv377__00ab_pv376__00a9)
del path_to_v377__00ab
del pv377__00ab_pv376__00a9

# op _009z_single_tensor_sum_with_axis_eval
# LANG: _009y --> _009A
# SHAPES: (1, 55200, 3) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009z_single_tensor_sum_with_axis_eval_pv358__009A_pv357__009y
path_to_v357__009y = STD_MULT(path_to_v358__009A,pv358__009A_pv357__009y)
del path_to_v358__009A

# op _009f_single_tensor_sum_with_axis_eval
# LANG: _009e --> _009g
# SHAPES: (1, 55200, 3) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009f_single_tensor_sum_with_axis_eval_pv348__009g_pv347__009e
path_to_v347__009e = STD_MULT(path_to_v348__009g,pv348__009g_pv347__009e)
del path_to_v348__009g

# op _009T_single_tensor_sum_with_axis_eval
# LANG: _009S --> _009U
# SHAPES: (1, 55200, 3) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009T_single_tensor_sum_with_axis_eval_pv368__009U_pv367__009S
path_to_v367__009S = STD_MULT(path_to_v368__009U,pv368__009U_pv367__009S)
del path_to_v368__009U

# op _00fu reshape_eval
# LANG: eel_coll_pts_coords --> _00fv
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fu reshape_eval_pv549__00fv_pv513_eel_coll_pts_coords
path_to_v513_eel_coll_pts_coords += DIAG_MULT(path_to_v549__00fv,pv549__00fv_pv513_eel_coll_pts_coords)
del path_to_v549__00fv

# op _00fi expand_array_eval
# LANG: _00fh --> _00fj
# SHAPES: (1, 200, 3) --> (1, 200, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fi expand_array_eval_pv543__00fj_pv542__00fh
path_to_v542__00fh = STD_MULT(path_to_v543__00fj,pv543__00fj_pv542__00fh)
del path_to_v543__00fj

# op _00fc expand_array_eval
# LANG: _00fb --> _00fd
# SHAPES: (1, 200, 3) --> (1, 200, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fc expand_array_eval_pv540__00fd_pv539__00fb
path_to_v539__00fb = STD_MULT(path_to_v540__00fd,pv540__00fd_pv539__00fb)
del path_to_v540__00fd

# op _00fA reshape_eval
# LANG: _00ew --> _00fB
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fA reshape_eval_pv552__00fB_pv518__00ew
path_to_v518__00ew = DIAG_MULT(path_to_v552__00fB,pv552__00fB_pv518__00ew)
del path_to_v552__00fB

# op _00ez expand_array_eval
# LANG: _00ey --> _00eA
# SHAPES: (1, 200, 3) --> (1, 200, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00ez expand_array_eval_pv520__00eA_pv519__00ey
path_to_v519__00ey = STD_MULT(path_to_v520__00eA,pv520__00eA_pv519__00ey)
del path_to_v520__00eA

# op _00eZ expand_array_eval
# LANG: _00eY --> _00e_
# SHAPES: (1, 200, 3) --> (1, 200, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00eZ expand_array_eval_pv533__00e__pv532__00eY
path_to_v532__00eY = STD_MULT(path_to_v533__00e_,pv533__00e__pv532__00eY)
del path_to_v533__00e_

# op _00eT expand_array_eval
# LANG: _00eS --> _00eU
# SHAPES: (1, 200, 3) --> (1, 200, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00eT expand_array_eval_pv530__00eU_pv529__00eS
path_to_v529__00eS = STD_MULT(path_to_v530__00eU,pv530__00eU_pv529__00eS)
del path_to_v530__00eU

# op _00eF expand_array_eval
# LANG: _00eE --> _00eG
# SHAPES: (1, 200, 3) --> (1, 200, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00eF expand_array_eval_pv523__00eG_pv522__00eE
path_to_v522__00eE = STD_MULT(path_to_v523__00eG,pv523__00eG_pv522__00eE)
del path_to_v523__00eG

# op _00a8_linear_combination_eval
# LANG: _00a1, _00a7 --> _00a9
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00a8_linear_combination_eval_pv376__00a9_pv375__00a7
path_to_v372__00a1 = DIAG_MULT(path_to_v376__00a9,pv376__00a9_pv372__00a1)
path_to_v375__00a7 = DIAG_MULT(path_to_v376__00a9,pv376__00a9_pv375__00a7)
del path_to_v376__00a9

# op _009x_power_combination_eval
# LANG: _009w --> _009y
# SHAPES: (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009x_power_combination_eval_pv357__009y_pv356__009w
temp_power = _009x_coeff_temp*2*(v356__009w)
pv357__009y_pv356__009w = temp_power.flatten()
path_to_v356__009w += DIAG_MULT(path_to_v357__009y,pv357__009y_pv356__009w)
del path_to_v357__009y
del pv357__009y_pv356__009w

# op _009d_power_combination_eval
# LANG: _009c --> _009e
# SHAPES: (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009d_power_combination_eval_pv347__009e_pv346__009c
temp_power = _009d_coeff_temp*2*(v346__009c)
pv347__009e_pv346__009c = temp_power.flatten()
path_to_v346__009c += DIAG_MULT(path_to_v347__009e,pv347__009e_pv346__009c)
del pv347__009e_pv346__009c
del path_to_v347__009e

# op _009R_power_combination_eval
# LANG: _009Q --> _009S
# SHAPES: (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009R_power_combination_eval_pv367__009S_pv366__009Q
temp_power = _009R_coeff_temp*2*(v366__009Q)
pv367__009S_pv366__009Q = temp_power.flatten()
path_to_v366__009Q += DIAG_MULT(path_to_v367__009S,pv367__009S_pv366__009Q)
del pv367__009S_pv366__009Q
del path_to_v367__009S

# op _00fg reshape_eval
# LANG: _00ev --> _00fh
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fg reshape_eval_pv542__00fh_pv517__00ev
path_to_v517__00ev = DIAG_MULT(path_to_v542__00fh,pv542__00fh_pv517__00ev)
del path_to_v542__00fh

# op _00fa reshape_eval
# LANG: eel_coll_pts_coords --> _00fb
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fa reshape_eval_pv539__00fb_pv513_eel_coll_pts_coords
path_to_v513_eel_coll_pts_coords += DIAG_MULT(path_to_v539__00fb,pv539__00fb_pv513_eel_coll_pts_coords)
del path_to_v539__00fb

# op _00ex reshape_eval
# LANG: eel_coll_pts_coords --> _00ey
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00ex reshape_eval_pv519__00ey_pv513_eel_coll_pts_coords
path_to_v513_eel_coll_pts_coords += DIAG_MULT(path_to_v519__00ey,pv519__00ey_pv513_eel_coll_pts_coords)
del path_to_v519__00ey

# op _00eX reshape_eval
# LANG: _00eu --> _00eY
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00eX reshape_eval_pv532__00eY_pv516__00eu
path_to_v516__00eu = DIAG_MULT(path_to_v532__00eY,pv532__00eY_pv516__00eu)
del path_to_v532__00eY

# op _00eR reshape_eval
# LANG: eel_coll_pts_coords --> _00eS
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00eR reshape_eval_pv529__00eS_pv513_eel_coll_pts_coords
path_to_v513_eel_coll_pts_coords += DIAG_MULT(path_to_v529__00eS,pv529__00eS_pv513_eel_coll_pts_coords)
del path_to_v529__00eS

# op _00eD reshape_eval
# LANG: _00et --> _00eE
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00eD reshape_eval_pv522__00eE_pv515__00et
path_to_v515__00et = DIAG_MULT(path_to_v522__00eE,pv522__00eE_pv515__00et)
del path_to_v522__00eE

# op _00a6 reshape_eval
# LANG: _00a5 --> _00a7
# SHAPES: (1, 200, 276, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00a6 reshape_eval_pv375__00a7_pv374__00a5
path_to_v374__00a5 = DIAG_MULT(path_to_v375__00a7,pv375__00a7_pv374__00a5)
del path_to_v375__00a7

# op _00a0 reshape_eval
# LANG: _009_ --> _00a1
# SHAPES: (1, 200, 276, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00a0 reshape_eval_pv372__00a1_pv371__009_
path_to_v371__009_ = DIAG_MULT(path_to_v372__00a1,pv372__00a1_pv371__009_)
del path_to_v372__00a1

# op _009v_linear_combination_eval
# LANG: _009o, _009u --> _009w
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009v_linear_combination_eval_pv356__009w_pv355__009u
path_to_v352__009o = DIAG_MULT(path_to_v356__009w,pv356__009w_pv352__009o)
path_to_v355__009u = DIAG_MULT(path_to_v356__009w,pv356__009w_pv355__009u)
del path_to_v356__009w

# op _009b_linear_combination_eval
# LANG: _0094, _009a --> _009c
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009b_linear_combination_eval_pv346__009c_pv345__009a
path_to_v342__0094 = DIAG_MULT(path_to_v346__009c,pv346__009c_pv342__0094)
path_to_v345__009a = DIAG_MULT(path_to_v346__009c,pv346__009c_pv345__009a)
del path_to_v346__009c

# op _009P_linear_combination_eval
# LANG: _009I, _009O --> _009Q
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009P_linear_combination_eval_pv366__009Q_pv365__009O
path_to_v362__009I = DIAG_MULT(path_to_v366__009Q,pv366__009Q_pv362__009I)
path_to_v365__009O = DIAG_MULT(path_to_v366__009Q,pv366__009Q_pv365__009O)
del path_to_v366__009Q

# op _00es_decompose_eval
# LANG: eel_bd_vtx_coords --> _00et, _00eu, _00ev, _00ew
# SHAPES: (1, 51, 5, 3) --> (1, 50, 4, 3), (1, 50, 4, 3), (1, 50, 4, 3), (1, 50, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00es_decompose_eval_pv518__00ew_pv514_eel_bd_vtx_coords
path_to_v514_eel_bd_vtx_coords += STD_MULT(path_to_v515__00et,pv515__00et_pv514_eel_bd_vtx_coords)
path_to_v514_eel_bd_vtx_coords += STD_MULT(path_to_v516__00eu,pv516__00eu_pv514_eel_bd_vtx_coords)
path_to_v514_eel_bd_vtx_coords += STD_MULT(path_to_v517__00ev,pv517__00ev_pv514_eel_bd_vtx_coords)
path_to_v514_eel_bd_vtx_coords += STD_MULT(path_to_v518__00ew,pv518__00ew_pv514_eel_bd_vtx_coords)
del path_to_v518__00ew
del path_to_v517__00ev
del path_to_v515__00et
del path_to_v516__00eu

# op _00a4 expand_array_eval
# LANG: _00a3 --> _00a5
# SHAPES: (1, 276, 3) --> (1, 200, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00a4 expand_array_eval_pv374__00a5_pv373__00a3
path_to_v373__00a3 = STD_MULT(path_to_v374__00a5,pv374__00a5_pv373__00a3)
del path_to_v374__00a5

# op _009t reshape_eval
# LANG: _009s --> _009u
# SHAPES: (1, 200, 276, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009t reshape_eval_pv355__009u_pv354__009s
path_to_v354__009s = DIAG_MULT(path_to_v355__009u,pv355__009u_pv354__009s)
del path_to_v355__009u

# op _009n reshape_eval
# LANG: _009m --> _009o
# SHAPES: (1, 200, 276, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009n reshape_eval_pv352__009o_pv351__009m
path_to_v351__009m = DIAG_MULT(path_to_v352__009o,pv352__009o_pv351__009m)
del path_to_v352__009o

# op _009Z expand_array_eval
# LANG: _009Y --> _009_
# SHAPES: (1, 200, 3) --> (1, 200, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009Z expand_array_eval_pv371__009__pv370__009Y
path_to_v370__009Y = STD_MULT(path_to_v371__009_,pv371__009__pv370__009Y)
del path_to_v371__009_

# op _009N reshape_eval
# LANG: _009M --> _009O
# SHAPES: (1, 200, 276, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009N reshape_eval_pv365__009O_pv364__009M
path_to_v364__009M = DIAG_MULT(path_to_v365__009O,pv365__009O_pv364__009M)
del path_to_v365__009O

# op _009H reshape_eval
# LANG: _009G --> _009I
# SHAPES: (1, 200, 276, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009H reshape_eval_pv362__009I_pv361__009G
path_to_v361__009G = DIAG_MULT(path_to_v362__009I,pv362__009I_pv361__009G)
del path_to_v362__009I

# op _0099 reshape_eval
# LANG: _0098 --> _009a
# SHAPES: (1, 200, 276, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _0099 reshape_eval_pv345__009a_pv344__0098
path_to_v344__0098 = DIAG_MULT(path_to_v345__009a,pv345__009a_pv344__0098)
del path_to_v345__009a

# op _0093 reshape_eval
# LANG: _0092 --> _0094
# SHAPES: (1, 200, 276, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _0093 reshape_eval_pv342__0094_pv341__0092
path_to_v341__0092 = DIAG_MULT(path_to_v342__0094,pv342__0094_pv341__0092)
del path_to_v342__0094

# op _00a2 reshape_eval
# LANG: _008Z --> _00a3
# SHAPES: (1, 69, 4, 3) --> (1, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00a2 reshape_eval_pv373__00a3_pv339__008Z
path_to_v339__008Z = DIAG_MULT(path_to_v373__00a3,pv373__00a3_pv339__008Z)
del path_to_v373__00a3

# op _009r expand_array_eval
# LANG: _009q --> _009s
# SHAPES: (1, 276, 3) --> (1, 200, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009r expand_array_eval_pv354__009s_pv353__009q
path_to_v353__009q = STD_MULT(path_to_v354__009s,pv354__009s_pv353__009q)
del path_to_v354__009s

# op _009l expand_array_eval
# LANG: _009k --> _009m
# SHAPES: (1, 200, 3) --> (1, 200, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009l expand_array_eval_pv351__009m_pv350__009k
path_to_v350__009k = STD_MULT(path_to_v351__009m,pv351__009m_pv350__009k)
del path_to_v351__009m

# op _009X reshape_eval
# LANG: eel_coll_pts_coords --> _009Y
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009X reshape_eval_pv370__009Y_pv513_eel_coll_pts_coords
path_to_v513_eel_coll_pts_coords += DIAG_MULT(path_to_v370__009Y,pv370__009Y_pv513_eel_coll_pts_coords)
del path_to_v370__009Y

# op _009L expand_array_eval
# LANG: _009K --> _009M
# SHAPES: (1, 276, 3) --> (1, 200, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009L expand_array_eval_pv364__009M_pv363__009K
path_to_v363__009K = STD_MULT(path_to_v364__009M,pv364__009M_pv363__009K)
del path_to_v364__009M

# op _009F expand_array_eval
# LANG: _009E --> _009G
# SHAPES: (1, 200, 3) --> (1, 200, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009F expand_array_eval_pv361__009G_pv360__009E
path_to_v360__009E = STD_MULT(path_to_v361__009G,pv361__009G_pv360__009E)
del path_to_v361__009G

# op _0097 expand_array_eval
# LANG: _0096 --> _0098
# SHAPES: (1, 276, 3) --> (1, 200, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _0097 expand_array_eval_pv344__0098_pv343__0096
path_to_v343__0096 = STD_MULT(path_to_v344__0098,pv344__0098_pv343__0096)
del path_to_v344__0098

# op _0091 expand_array_eval
# LANG: _0090 --> _0092
# SHAPES: (1, 200, 3) --> (1, 200, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _0091 expand_array_eval_pv341__0092_pv340__0090
path_to_v340__0090 = STD_MULT(path_to_v341__0092,pv341__0092_pv340__0090)
del path_to_v341__0092

# op _0052_indexed_passthrough_eval
# LANG: _0051, _005m --> eel_bd_vtx_coords
# SHAPES: (1, 50, 5, 3), (1, 1, 5, 3) --> (1, 51, 5, 3)
# full namespace: MeshPreprocessing_comp

# _0052_indexed_passthrough_eval_pv514_eel_bd_vtx_coords_pv204__005m
path_to_v192__0051 = STD_MULT(path_to_v514_eel_bd_vtx_coords,pv514_eel_bd_vtx_coords_pv192__0051)
path_to_v204__005m = STD_MULT(path_to_v514_eel_bd_vtx_coords,pv514_eel_bd_vtx_coords_pv204__005m)
del path_to_v514_eel_bd_vtx_coords

# op _009p reshape_eval
# LANG: _008X --> _009q
# SHAPES: (1, 69, 4, 3) --> (1, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009p reshape_eval_pv353__009q_pv337__008X
path_to_v337__008X = DIAG_MULT(path_to_v353__009q,pv353__009q_pv337__008X)
del path_to_v353__009q

# op _009j reshape_eval
# LANG: eel_coll_pts_coords --> _009k
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009j reshape_eval_pv350__009k_pv513_eel_coll_pts_coords
path_to_v513_eel_coll_pts_coords += DIAG_MULT(path_to_v350__009k,pv350__009k_pv513_eel_coll_pts_coords)
del path_to_v350__009k

# op _009J reshape_eval
# LANG: _008Y --> _009K
# SHAPES: (1, 69, 4, 3) --> (1, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009J reshape_eval_pv363__009K_pv338__008Y
path_to_v338__008Y = DIAG_MULT(path_to_v363__009K,pv363__009K_pv338__008Y)
del path_to_v363__009K

# op _009D reshape_eval
# LANG: eel_coll_pts_coords --> _009E
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009D reshape_eval_pv360__009E_pv513_eel_coll_pts_coords
path_to_v513_eel_coll_pts_coords += DIAG_MULT(path_to_v360__009E,pv360__009E_pv513_eel_coll_pts_coords)
del path_to_v360__009E

# op _0095 reshape_eval
# LANG: _008W --> _0096
# SHAPES: (1, 69, 4, 3) --> (1, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _0095 reshape_eval_pv343__0096_pv336__008W
path_to_v336__008W = DIAG_MULT(path_to_v343__0096,pv343__0096_pv336__008W)
del path_to_v343__0096

# op _008_ reshape_eval
# LANG: eel_coll_pts_coords --> _0090
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _008_ reshape_eval_pv340__0090_pv513_eel_coll_pts_coords
path_to_v513_eel_coll_pts_coords += DIAG_MULT(path_to_v340__0090,pv340__0090_pv513_eel_coll_pts_coords)
del path_to_v340__0090

# op _005l_linear_combination_eval
# LANG: _005k, _005j --> _005m
# SHAPES: (1, 1, 5, 3), (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: MeshPreprocessing_comp

# _005l_linear_combination_eval_pv204__005m_pv202__005j
path_to_v203__005k = DIAG_MULT(path_to_v204__005m,pv204__005m_pv203__005k)
path_to_v202__005j = DIAG_MULT(path_to_v204__005m,pv204__005m_pv202__005j)
del path_to_v204__005m

# op _0050_linear_combination_eval
# LANG: _004X, _004_ --> _0051
# SHAPES: (1, 50, 5, 3), (1, 50, 5, 3) --> (1, 50, 5, 3)
# full namespace: MeshPreprocessing_comp

# _0050_linear_combination_eval_pv192__0051_pv191__004_
path_to_v189__004X = DIAG_MULT(path_to_v192__0051,pv192__0051_pv189__004X)
path_to_v191__004_ = DIAG_MULT(path_to_v192__0051,pv192__0051_pv191__004_)
del path_to_v192__0051

# op _008V_decompose_eval
# LANG: eel_TE_wake_coords --> _008W, _008X, _008Y, _008Z
# SHAPES: (1, 70, 5, 3) --> (1, 69, 4, 3), (1, 69, 4, 3), (1, 69, 4, 3), (1, 69, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _008V_decompose_eval_pv339__008Z_pv335_eel_TE_wake_coords
path_to_v335_eel_TE_wake_coords = STD_MULT(path_to_v336__008W,pv336__008W_pv335_eel_TE_wake_coords)
path_to_v335_eel_TE_wake_coords += STD_MULT(path_to_v337__008X,pv337__008X_pv335_eel_TE_wake_coords)
path_to_v335_eel_TE_wake_coords += STD_MULT(path_to_v338__008Y,pv338__008Y_pv335_eel_TE_wake_coords)
path_to_v335_eel_TE_wake_coords += STD_MULT(path_to_v339__008Z,pv339__008Z_pv335_eel_TE_wake_coords)
del path_to_v337__008X
del path_to_v338__008Y
del path_to_v336__008W
del path_to_v339__008Z

# op _005z_linear_combination_eval
# LANG: _005s, _005y --> eel_coll_pts_coords
# SHAPES: (1, 50, 4, 3), (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: MeshPreprocessing_comp

# _005z_linear_combination_eval_pv513_eel_coll_pts_coords_pv212__005y
path_to_v208__005s = DIAG_MULT(path_to_v513_eel_coll_pts_coords,pv513_eel_coll_pts_coords_pv208__005s)
path_to_v212__005y = DIAG_MULT(path_to_v513_eel_coll_pts_coords,pv513_eel_coll_pts_coords_pv212__005y)
del path_to_v513_eel_coll_pts_coords

# op _005i expand_array_eval
# LANG: _005h --> _005j
# SHAPES: (1, 3) --> (1, 1, 5, 3)
# full namespace: MeshPreprocessing_comp

# _005i expand_array_eval_pv202__005j_pv201__005h
path_to_v201__005h = STD_MULT(path_to_v202__005j,pv202__005j_pv201__005h)
del path_to_v202__005j

# op _004Z_power_combination_eval
# LANG: _004Y --> _004_
# SHAPES: (1, 50, 5, 3) --> (1, 50, 5, 3)
# full namespace: MeshPreprocessing_comp

# _004Z_power_combination_eval_pv191__004__pv190__004Y
temp_power = _004Z_coeff_temp*1
pv191__004__pv190__004Y = temp_power.flatten()
path_to_v190__004Y = DIAG_MULT(path_to_v191__004_,pv191__004__pv190__004Y)
del pv191__004__pv190__004Y
del path_to_v191__004_

# op _004W_power_combination_eval
# LANG: _004V --> _004X
# SHAPES: (1, 50, 5, 3) --> (1, 50, 5, 3)
# full namespace: MeshPreprocessing_comp

# _004W_power_combination_eval_pv189__004X_pv188__004V
temp_power = _004W_coeff_temp*1
pv189__004X_pv188__004V = temp_power.flatten()
path_to_v188__004V = DIAG_MULT(path_to_v189__004X,pv189__004X_pv188__004V)
del pv189__004X_pv188__004V
del path_to_v189__004X

# op _007E_indexed_passthrough_eval
# LANG: _007I, eel_wake_coords --> eel_TE_wake_coords
# SHAPES: (1, 1, 5, 3), (1, 69, 5, 3) --> (1, 70, 5, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group

# _007E_indexed_passthrough_eval_pv335_eel_TE_wake_coords_pv287_eel_wake_coords
path_to_v290__007I = STD_MULT(path_to_v335_eel_TE_wake_coords,pv335_eel_TE_wake_coords_pv290__007I)
path_to_v287_eel_wake_coords += STD_MULT(path_to_v335_eel_TE_wake_coords,pv335_eel_TE_wake_coords_pv287_eel_wake_coords)
del path_to_v335_eel_TE_wake_coords

# op _005x_power_combination_eval
# LANG: _005w --> _005y
# SHAPES: (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: MeshPreprocessing_comp

# _005x_power_combination_eval_pv212__005y_pv211__005w
temp_power = _005x_coeff_temp*1
pv212__005y_pv211__005w = temp_power.flatten()
path_to_v211__005w = DIAG_MULT(path_to_v212__005y,pv212__005y_pv211__005w)
del path_to_v212__005y
del pv212__005y_pv211__005w

# op _005r_power_combination_eval
# LANG: _005q --> _005s
# SHAPES: (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: MeshPreprocessing_comp

# _005r_power_combination_eval_pv208__005s_pv207__005q
temp_power = _005r_coeff_temp*1
pv208__005s_pv207__005q = temp_power.flatten()
path_to_v207__005q = DIAG_MULT(path_to_v208__005s,pv208__005s_pv207__005q)
del pv208__005s_pv207__005q
del path_to_v208__005s

# op _005g_power_combination_eval
# LANG: _005f --> _005h
# SHAPES: (1, 3) --> (1, 3)
# full namespace: MeshPreprocessing_comp

# _005g_power_combination_eval_pv201__005h_pv200__005f
temp_power = _005g_coeff_temp*1
pv201__005h_pv200__005f = temp_power.flatten()
path_to_v200__005f = DIAG_MULT(path_to_v201__005h,pv201__005h_pv200__005f)
del path_to_v201__005h
del pv201__005h_pv200__005f

# op _007H_power_combination_eval
# LANG: _007G --> _007I
# SHAPES: (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group

# _007H_power_combination_eval_pv290__007I_pv289__007G
temp_power = _007H_coeff_temp*1
pv290__007I_pv289__007G = temp_power.flatten()
path_to_v289__007G = DIAG_MULT(path_to_v290__007I,pv290__007I_pv289__007G)
del path_to_v290__007I
del pv290__007I_pv289__007G

# op _005v_linear_combination_eval
# LANG: _005u, _005t --> _005w
# SHAPES: (1, 50, 4, 3), (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: MeshPreprocessing_comp

# _005v_linear_combination_eval_pv211__005w_pv209__005t
path_to_v210__005u = DIAG_MULT(path_to_v211__005w,pv211__005w_pv210__005u)
path_to_v209__005t = DIAG_MULT(path_to_v211__005w,pv211__005w_pv209__005t)
del path_to_v211__005w

# op _005p_linear_combination_eval
# LANG: _005n, _005o --> _005q
# SHAPES: (1, 50, 4, 3), (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: MeshPreprocessing_comp

# _005p_linear_combination_eval_pv207__005q_pv206__005o
path_to_v205__005n = DIAG_MULT(path_to_v207__005q,pv207__005q_pv205__005n)
path_to_v206__005o = DIAG_MULT(path_to_v207__005q,pv207__005q_pv206__005o)
del path_to_v207__005q

# op _005e_power_combination_eval
# LANG: fs --> _005f
# SHAPES: (1, 3) --> (1, 3)
# full namespace: MeshPreprocessing_comp

# _005e_power_combination_eval_pv200__005f_pv195_fs
temp_power = _005e_coeff_temp*1
pv200__005f_pv195_fs = temp_power.flatten()
path_to_v195_fs = DIAG_MULT(path_to_v200__005f,pv200__005f_pv195_fs)
del pv200__005f_pv195_fs
del path_to_v200__005f

# op _007F_decompose_eval
# LANG: eel_wake_coords --> _007G
# SHAPES: (1, 69, 5, 3) --> (1, 1, 5, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group

# _007F_decompose_eval_pv289__007G_pv287_eel_wake_coords
path_to_v287_eel_wake_coords += STD_MULT(path_to_v289__007G,pv289__007G_pv287_eel_wake_coords)
del path_to_v289__007G

# op _005a_indexed_passthrough_eval
# LANG: _0059, _005d, w --> fs
# SHAPES: (1, 1), (1, 1), (1, 1) --> (1, 3)
# full namespace: MeshPreprocessing_comp

# _005a_indexed_passthrough_eval_pv195_fs_pv194_w
path_to_v197__0059 = STD_MULT(path_to_v195_fs,pv195_fs_pv197__0059)
path_to_v199__005d = STD_MULT(path_to_v195_fs,pv195_fs_pv199__005d)
path_to_v194_w = STD_MULT(path_to_v195_fs,pv195_fs_pv194_w)
del path_to_v195_fs

# op _004U_decompose_eval
# LANG: eel --> _005u, _004V, _004Y, _005k, _005n, _005o, _005t, _005M, _005N, _006i, _006l, _006q
# SHAPES: (1, 51, 5, 3) --> (1, 50, 4, 3), (1, 50, 5, 3), (1, 50, 5, 3), (1, 1, 5, 3), (1, 50, 4, 3), (1, 50, 4, 3), (1, 50, 4, 3), (1, 51, 4, 3), (1, 51, 4, 3), (1, 50, 4, 3), (1, 50, 4, 3), (1, 50, 4, 3)
# full namespace: MeshPreprocessing_comp

# _004U_decompose_eval_pv245__006q_pv311_eel
path_to_v311_eel += STD_MULT(path_to_v210__005u,pv210__005u_pv311_eel)
path_to_v311_eel += STD_MULT(path_to_v188__004V,pv188__004V_pv311_eel)
path_to_v311_eel += STD_MULT(path_to_v190__004Y,pv190__004Y_pv311_eel)
path_to_v311_eel += STD_MULT(path_to_v203__005k,pv203__005k_pv311_eel)
path_to_v311_eel += STD_MULT(path_to_v205__005n,pv205__005n_pv311_eel)
path_to_v311_eel += STD_MULT(path_to_v206__005o,pv206__005o_pv311_eel)
path_to_v311_eel += STD_MULT(path_to_v209__005t,pv209__005t_pv311_eel)
del path_to_v210__005u
del path_to_v203__005k
del path_to_v209__005t
del path_to_v188__004V
del path_to_v206__005o
del path_to_v205__005n
del path_to_v190__004Y

# op _005c_linear_combination_eval
# LANG: _005b --> _005d
# SHAPES: (1, 1) --> (1, 1)
# full namespace: MeshPreprocessing_comp

# _005c_linear_combination_eval_pv199__005d_pv198__005b
path_to_v198__005b = DIAG_MULT(path_to_v199__005d,pv199__005d_pv198__005b)
del path_to_v199__005d

# op _0058_linear_combination_eval
# LANG: _0057 --> _0059
# SHAPES: (1, 1) --> (1, 1)
# full namespace: MeshPreprocessing_comp

# _0058_linear_combination_eval_pv197__0059_pv196__0057
path_to_v196__0057 = DIAG_MULT(path_to_v197__0059,pv197__0059_pv196__0057)
del path_to_v197__0059

# op _0056_decompose_eval
# LANG: frame_vel --> _005b, _0057
# SHAPES: (1, 3) --> (1, 1), (1, 1)
# full namespace: MeshPreprocessing_comp

# _0056_decompose_eval_pv196__0057_pv623_frame_vel
path_to_v623_frame_vel += STD_MULT(path_to_v198__005b,pv198__005b_pv623_frame_vel)
path_to_v623_frame_vel += STD_MULT(path_to_v196__0057,pv196__0057_pv623_frame_vel)
del path_to_v198__005b
del path_to_v196__0057

# op _004M_indexed_passthrough_eval
# LANG: _004L, _004O --> frame_vel
# SHAPES: (1, 1), (1, 1) --> (1, 3)
# full namespace: adapter_comp

# _004M_indexed_passthrough_eval_pv623_frame_vel_pv183__004O
path_to_v182__004L = STD_MULT(path_to_v623_frame_vel,pv623_frame_vel_pv182__004L)
path_to_v183__004O = STD_MULT(path_to_v623_frame_vel,pv623_frame_vel_pv183__004O)
del path_to_v623_frame_vel

# op _004N_linear_combination_eval
# LANG: w --> _004O
# SHAPES: (1, 1) --> (1, 1)
# full namespace: adapter_comp

# _004N_linear_combination_eval_pv183__004O_pv194_w
path_to_v194_w += DIAG_MULT(path_to_v183__004O,pv183__004O_pv194_w)
del path_to_v183__004O

# op _004K_linear_combination_eval
# LANG: u --> _004L
# SHAPES: (1, 1) --> (1, 1)
# full namespace: adapter_comp

# _004K_linear_combination_eval_pv182__004L_pv158_u
path_to_v158_u = DIAG_MULT(path_to_v182__004L,pv182__004L_pv158_u)
del path_to_v182__004L
path_to_v158_u = path_to_v158_u.copy()
# path_to_v159_v = zero
path_to_v159_v = np.zeros((1,1))
# path_to_v164_theta = zero
path_to_v164_theta = np.zeros((1,1))
# path_to_v165_psi = zero
path_to_v165_psi = np.zeros((1,1))
# path_to_v166_gamma = zero
path_to_v166_gamma = np.zeros((1,1))
# path_to_v167_psiw = zero
path_to_v167_psiw = np.zeros((1,1))
path_to_v194_w = path_to_v194_w.copy()
path_to_v269_eel_gamma_w = path_to_v269_eel_gamma_w.copy()
path_to_v287_eel_wake_coords = path_to_v287_eel_wake_coords.copy()
path_to_v294_p = path_to_v294_p.copy()
path_to_v295_q = path_to_v295_q.copy()
path_to_v296_r = path_to_v296_r.copy()
path_to_v306_eel_coll_vel = path_to_v306_eel_coll_vel.copy()
path_to_v311_eel = path_to_v311_eel.copy()