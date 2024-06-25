

# REV_VJP: eel_dgammaw_dt,eel_dwake_coords_dt,-->v179_u,v180_v,v185_theta,v186_psi,v187_gamma,v188_psiw,v215_w,v290_eel_gamma_w,v308_eel_wake_coords,v315_p,v316_q,v317_r,v327_eel_coll_vel,v332_eel,

# REV_VJP: eel_dgammaw_dt,eel_dwake_coords_dt,-->v179_u,v180_v,v185_theta,v186_psi,v187_gamma,v188_psiw,v215_w,v290_eel_gamma_w,v308_eel_wake_coords,v315_p,v316_q,v317_r,v327_eel_coll_vel,v332_eel,
path_to_v136_eel_dgammaw_dt = r_seed_v136_eel_dgammaw_dt
path_to_v150_eel_dwake_coords_dt = r_seed_v150_eel_dwake_coords_dt

# op _0049_indexed_passthrough_eval
# LANG: _0048, _004K --> eel_dwake_coords_dt
# SHAPES: (1, 1, 5, 3), (1, 68, 5, 3) --> (1, 69, 5, 3)
# full namespace: 

# _0049_indexed_passthrough_eval_pv150_eel_dwake_coords_dt_pv178__004K
path_to_v158__0048 = STD_MULT(path_to_v150_eel_dwake_coords_dt,pv150_eel_dwake_coords_dt_pv158__0048)
path_to_v178__004K = STD_MULT(path_to_v150_eel_dwake_coords_dt,pv150_eel_dwake_coords_dt_pv178__004K)

# op _003H_indexed_passthrough_eval
# LANG: _003G, _003N --> eel_dgammaw_dt
# SHAPES: (1, 1, 4), (1, 68, 4) --> (1, 69, 4)
# full namespace: 

# _003H_indexed_passthrough_eval_pv136_eel_dgammaw_dt_pv145__003N
path_to_v141__003G = STD_MULT(path_to_v136_eel_dgammaw_dt,pv136_eel_dgammaw_dt_pv141__003G)
path_to_v145__003N = STD_MULT(path_to_v136_eel_dgammaw_dt,pv136_eel_dgammaw_dt_pv145__003N)

# op _004J_power_combination_eval
# LANG: _004I --> _004K
# SHAPES: (1, 68, 5, 3) --> (1, 68, 5, 3)
# full namespace: 

# _004J_power_combination_eval_pv178__004K_pv177__004I
temp_power = _004J_coeff_temp*1
pv178__004K_pv177__004I = temp_power.flatten()
path_to_v177__004I = DIAG_MULT(path_to_v178__004K,pv178__004K_pv177__004I)
del path_to_v178__004K
del pv178__004K_pv177__004I

# op _0047_power_combination_eval
# LANG: _0046 --> _0048
# SHAPES: (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: 

# _0047_power_combination_eval_pv158__0048_pv157__0046
temp_power = _0047_coeff_temp*1
pv158__0048_pv157__0046 = temp_power.flatten()
path_to_v157__0046 = DIAG_MULT(path_to_v158__0048,pv158__0048_pv157__0046)
del path_to_v158__0048
del pv158__0048_pv157__0046

# op _003M_power_combination_eval
# LANG: _003L --> _003N
# SHAPES: (1, 68, 4) --> (1, 68, 4)
# full namespace: 

# _003M_power_combination_eval_pv145__003N_pv144__003L
temp_power = _003M_coeff_temp*1
pv145__003N_pv144__003L = temp_power.flatten()
path_to_v144__003L = DIAG_MULT(path_to_v145__003N,pv145__003N_pv144__003L)
del path_to_v145__003N
del pv145__003N_pv144__003L

# op _003F_power_combination_eval
# LANG: _003E --> _003G
# SHAPES: (1, 1, 4) --> (1, 1, 4)
# full namespace: 

# _003F_power_combination_eval_pv141__003G_pv140__003E
temp_power = _003F_coeff_temp*1
pv141__003G_pv140__003E = temp_power.flatten()
path_to_v140__003E = DIAG_MULT(path_to_v141__003G,pv141__003G_pv140__003E)
del pv141__003G_pv140__003E
del path_to_v141__003G

# op _004H_linear_combination_eval
# LANG: _004D, _004G --> _004I
# SHAPES: (1, 68, 5, 3), (1, 68, 5, 3) --> (1, 68, 5, 3)
# full namespace: 

# _004H_linear_combination_eval_pv177__004I_pv176__004G
path_to_v174__004D = DIAG_MULT(path_to_v177__004I,pv177__004I_pv174__004D)
path_to_v176__004G = DIAG_MULT(path_to_v177__004I,pv177__004I_pv176__004G)
del path_to_v177__004I

# op _0045_linear_combination_eval
# LANG: _0042, _0044 --> _0046
# SHAPES: (1, 1, 5, 3), (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: 

# _0045_linear_combination_eval_pv157__0046_pv156__0044
path_to_v155__0042 = DIAG_MULT(path_to_v157__0046,pv157__0046_pv155__0042)
path_to_v156__0044 = DIAG_MULT(path_to_v157__0046,pv157__0046_pv156__0044)
del path_to_v157__0046

# op _003K_linear_combination_eval
# LANG: _003I, _003J --> _003L
# SHAPES: (1, 68, 4), (1, 68, 4) --> (1, 68, 4)
# full namespace: 

# _003K_linear_combination_eval_pv144__003L_pv143__003J
path_to_v142__003I = DIAG_MULT(path_to_v144__003L,pv144__003L_pv142__003I)
path_to_v143__003J = DIAG_MULT(path_to_v144__003L,pv144__003L_pv143__003J)
del path_to_v144__003L

# op _003D_linear_combination_eval
# LANG: _003A, _003C --> _003E
# SHAPES: (1, 1, 4), (1, 1, 4) --> (1, 1, 4)
# full namespace: 

# _003D_linear_combination_eval_pv140__003E_pv139__003C
path_to_v138__003A = DIAG_MULT(path_to_v140__003E,pv140__003E_pv138__003A)
path_to_v139__003C = DIAG_MULT(path_to_v140__003E,pv140__003E_pv139__003C)
del path_to_v140__003E

# op _004F_power_combination_eval
# LANG: _004E --> _004G
# SHAPES: (1, 68, 5, 3) --> (1, 68, 5, 3)
# full namespace: 

# _004F_power_combination_eval_pv176__004G_pv175__004E
temp_power = _004F_coeff_temp*1
pv176__004G_pv175__004E = temp_power.flatten()
path_to_v175__004E = DIAG_MULT(path_to_v176__004G,pv176__004G_pv175__004E)
del pv176__004G_pv175__004E
del path_to_v176__004G

# op _004C_linear_combination_eval
# LANG: _004A, _004B --> _004D
# SHAPES: (1, 68, 5, 3), (1, 68, 5, 3) --> (1, 68, 5, 3)
# full namespace: 

# _004C_linear_combination_eval_pv174__004D_pv173__004B
path_to_v172__004A = DIAG_MULT(path_to_v174__004D,pv174__004D_pv172__004A)
path_to_v173__004B = DIAG_MULT(path_to_v174__004D,pv174__004D_pv173__004B)
del path_to_v174__004D

# op _0041_linear_combination_eval
# LANG: _003V, _0040 --> _0042
# SHAPES: (1, 1, 5, 3), (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: 

# _0041_linear_combination_eval_pv155__0042_pv154__0040
path_to_v151__003V = DIAG_MULT(path_to_v155__0042,pv155__0042_pv151__003V)
path_to_v154__0040 = DIAG_MULT(path_to_v155__0042,pv155__0042_pv154__0040)
del path_to_v155__0042

# op _003z reshape_eval
# LANG: _003y --> _003A
# SHAPES: (1, 4) --> (1, 1, 4)
# full namespace: 

# _003z reshape_eval_pv138__003A_pv137__003y
path_to_v137__003y = DIAG_MULT(path_to_v138__003A,pv138__003A_pv137__003y)
del path_to_v138__003A

# op _003B_decompose_eval
# LANG: eel_gamma_w --> _003J, _003C, _003I
# SHAPES: (1, 69, 4) --> (1, 68, 4), (1, 1, 4), (1, 68, 4)
# full namespace: 

# _003B_decompose_eval_pv142__003I_pv290_eel_gamma_w
path_to_v290_eel_gamma_w = STD_MULT(path_to_v143__003J,pv143__003J_pv290_eel_gamma_w)
path_to_v290_eel_gamma_w += STD_MULT(path_to_v139__003C,pv139__003C_pv290_eel_gamma_w)
path_to_v290_eel_gamma_w += STD_MULT(path_to_v142__003I,pv142__003I_pv290_eel_gamma_w)
del path_to_v142__003I
del path_to_v143__003J
del path_to_v139__003C

# op _004z_linear_combination_eval
# LANG: _004x, _004y --> _004A
# SHAPES: (1, 68, 5, 3), (1, 68, 5, 3) --> (1, 68, 5, 3)
# full namespace: 

# _004z_linear_combination_eval_pv172__004A_pv171__004y
path_to_v170__004x = DIAG_MULT(path_to_v172__004A,pv172__004A_pv170__004x)
path_to_v171__004y = DIAG_MULT(path_to_v172__004A,pv172__004A_pv171__004y)
del path_to_v172__004A

# op _003x_decompose_eval
# LANG: eel_gamma_b --> _003y
# SHAPES: (1, 200) --> (1, 4)
# full namespace: 

# _003x_decompose_eval_pv137__003y_pv641_eel_gamma_b
path_to_v641_eel_gamma_b = STD_MULT(path_to_v137__003y,pv137__003y_pv641_eel_gamma_b)
del path_to_v137__003y

# op _003__power_combination_eval
# LANG: _003Z --> _0040
# SHAPES: (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: 

# _003__power_combination_eval_pv154__0040_pv153__003Z
temp_power = _003__coeff_temp*1
pv154__0040_pv153__003Z = temp_power.flatten()
path_to_v153__003Z = DIAG_MULT(path_to_v154__0040,pv154__0040_pv153__003Z)
del pv154__0040_pv153__003Z
del path_to_v154__0040

# op _00ii_decompose_eval
# LANG: gamma_b --> eel_gamma_b
# SHAPES: (1, 200) --> (1, 200)
# full namespace: seperate_gamma_b

# _00ii_decompose_eval_pv641_eel_gamma_b_pv640_gamma_b
path_to_v640_gamma_b = STD_MULT(path_to_v641_eel_gamma_b,pv641_eel_gamma_b_pv640_gamma_b)
del path_to_v641_eel_gamma_b

# op _004w expand_array_eval
# LANG: _004v --> _004x
# SHAPES: (1, 5, 3) --> (1, 68, 5, 3)
# full namespace: 

# _004w expand_array_eval_pv170__004x_pv169__004v
path_to_v169__004v = STD_MULT(path_to_v170__004x,pv170__004x_pv169__004v)
del path_to_v170__004x

# op _003Y_power_combination_eval
# LANG: _003X --> _003Z
# SHAPES: (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: 

# _003Y_power_combination_eval_pv153__003Z_pv152__003X
temp_power = _003Y_coeff_temp*1
pv153__003Z_pv152__003X = temp_power.flatten()
path_to_v152__003X = DIAG_MULT(path_to_v153__003Z,pv153__003Z_pv152__003X)
del pv153__003Z_pv152__003X
del path_to_v153__003Z

# op _004u reshape_eval
# LANG: _004t --> _004v
# SHAPES: (1, 1, 5, 3) --> (1, 5, 3)
# full namespace: 

# _004u reshape_eval_pv169__004v_pv168__004t
path_to_v168__004t = DIAG_MULT(path_to_v169__004v,pv169__004v_pv168__004t)
del path_to_v169__004v

# op _004s_linear_combination_eval
# LANG: _004r, _0044 --> _004t
# SHAPES: (1, 1, 5, 3), (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: 

# _004s_linear_combination_eval_pv168__004t_pv156__0044
path_to_v167__004r = DIAG_MULT(path_to_v168__004t,pv168__004t_pv167__004r)
path_to_v156__0044 += DIAG_MULT(path_to_v168__004t,pv168__004t_pv156__0044)
del path_to_v168__004t

# op _004q_linear_combination_eval
# LANG: _003V, _004p --> _004r
# SHAPES: (1, 1, 5, 3), (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: 

# _004q_linear_combination_eval_pv167__004r_pv166__004p
path_to_v151__003V += DIAG_MULT(path_to_v167__004r,pv167__004r_pv151__003V)
path_to_v166__004p = DIAG_MULT(path_to_v167__004r,pv167__004r_pv166__004p)
del path_to_v167__004r

# op _0043_decompose_eval
# LANG: eel_wake_coords --> _004B, _0044, _004y
# SHAPES: (1, 69, 5, 3) --> (1, 68, 5, 3), (1, 1, 5, 3), (1, 68, 5, 3)
# full namespace: 

# _0043_decompose_eval_pv171__004y_pv308_eel_wake_coords
path_to_v308_eel_wake_coords = STD_MULT(path_to_v173__004B,pv173__004B_pv308_eel_wake_coords)
path_to_v308_eel_wake_coords += STD_MULT(path_to_v156__0044,pv156__0044_pv308_eel_wake_coords)
path_to_v308_eel_wake_coords += STD_MULT(path_to_v171__004y,pv171__004y_pv308_eel_wake_coords)
del path_to_v156__0044
del path_to_v173__004B
del path_to_v171__004y

# op _004o_power_combination_eval
# LANG: _004n --> _004p
# SHAPES: (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: 

# _004o_power_combination_eval_pv166__004p_pv165__004n
temp_power = _004o_coeff_temp*1
pv166__004p_pv165__004n = temp_power.flatten()
path_to_v165__004n = DIAG_MULT(path_to_v166__004p,pv166__004p_pv165__004n)
del pv166__004p_pv165__004n
del path_to_v166__004p

# op _003U_decompose_eval
# LANG: eel_bd_vtx_coords --> _003V
# SHAPES: (1, 51, 5, 3) --> (1, 1, 5, 3)
# full namespace: 

# _003U_decompose_eval_pv151__003V_pv535_eel_bd_vtx_coords
path_to_v535_eel_bd_vtx_coords = STD_MULT(path_to_v151__003V,pv151__003V_pv535_eel_bd_vtx_coords)
del path_to_v151__003V

# op _004m_power_combination_eval
# LANG: _003X --> _004n
# SHAPES: (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: 

# _004m_power_combination_eval_pv165__004n_pv152__003X
temp_power = _004m_coeff_temp*1
pv165__004n_pv152__003X = temp_power.flatten()
path_to_v152__003X += DIAG_MULT(path_to_v165__004n,pv165__004n_pv152__003X)
del pv165__004n_pv152__003X
del path_to_v165__004n

# op _003W_decompose_eval
# LANG: eel_wake_total_vel --> _004E, _003X
# SHAPES: (1, 69, 5, 3) --> (1, 68, 5, 3), (1, 1, 5, 3)
# full namespace: 

# _003W_decompose_eval_pv152__003X_pv643_eel_wake_total_vel
path_to_v643_eel_wake_total_vel = STD_MULT(path_to_v175__004E,pv175__004E_pv643_eel_wake_total_vel)
path_to_v643_eel_wake_total_vel += STD_MULT(path_to_v152__003X,pv152__003X_pv643_eel_wake_total_vel)
del path_to_v175__004E
del path_to_v152__003X

# op _00im_linear_combination_eval
# LANG: eel_wake_kinematic_vel --> eel_wake_total_vel
# SHAPES: (1, 69, 5, 3) --> (1, 69, 5, 3)
# full namespace: ComputeWakeTotalVel

# _00im_linear_combination_eval_pv643_eel_wake_total_vel_pv646_eel_wake_kinematic_vel
path_to_v646_eel_wake_kinematic_vel = DIAG_MULT(path_to_v643_eel_wake_total_vel,pv643_eel_wake_total_vel_pv646_eel_wake_kinematic_vel)
del path_to_v643_eel_wake_total_vel

# op _00ir expand_array_eval
# LANG: _00iq --> eel_wake_kinematic_vel
# SHAPES: (1, 3) --> (1, 69, 5, 3)
# full namespace: ComputeWakeTotalVel.ComputeWakeKinematicVel

# _00ir expand_array_eval_pv646_eel_wake_kinematic_vel_pv645__00iq
path_to_v645__00iq = STD_MULT(path_to_v646_eel_wake_kinematic_vel,pv646_eel_wake_kinematic_vel_pv645__00iq)
del path_to_v646_eel_wake_kinematic_vel

# op _00ip_linear_combination_eval
# LANG: frame_vel --> _00iq
# SHAPES: (1, 3) --> (1, 3)
# full namespace: ComputeWakeTotalVel.ComputeWakeKinematicVel

# _00ip_linear_combination_eval_pv645__00iq_pv644_frame_vel
path_to_v644_frame_vel = DIAG_MULT(path_to_v645__00iq,pv645__00iq_pv644_frame_vel)
del path_to_v645__00iq

# _0086_newton_implict_eval__0086
_0086_newton_path_in = _0086_newton.accumulate_rev(path_to_v640_gamma_b)
_0086_v639_aic_bd_proj = _0086_newton_path_in[0]
_0086_v528_M_mat = _0086_newton_path_in[1]
_0086_v302_gamma_w = _0086_newton_path_in[2]
_0086_v349_b = _0086_newton_path_in[3]
path_to_v302_gamma_w = _0086_v302_gamma_w
path_to_v528_M_mat = _0086_v528_M_mat
path_to_v349_b = _0086_v349_b
path_to_v639_aic_bd_proj = _0086_v639_aic_bd_proj
del path_to_v640_gamma_b

# op _007L_indexed_passthrough_eval
# LANG: eel_gamma_w --> gamma_w
# SHAPES: (1, 69, 4) --> (1, 69, 4)
# full namespace: combine_gamma_w

# _007L_indexed_passthrough_eval_pv302_gamma_w_pv290_eel_gamma_w
path_to_v290_eel_gamma_w += STD_MULT(path_to_v302_gamma_w,pv302_gamma_w_pv290_eel_gamma_w)
del path_to_v302_gamma_w

# op _00if_custom_explicit_eval
# LANG: normal_concatenated_aic_bd_proj, aic_bd --> aic_bd_proj
# SHAPES: (1, 200, 3), (1, 200, 200, 3) --> (1, 200, 200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_aic_bd

# _00if_custom_explicit_eval_pv639_aic_bd_proj_pv636_aic_bd
pv639_aic_bd_proj_pv635_normal_concatenated_aic_bd_proj = _00if_custom_explicit_func_aic_bd_proj.get_custom_explicit_partials('aic_bd_proj', 'normal_concatenated_aic_bd_proj')
pv639_aic_bd_proj_pv636_aic_bd = _00if_custom_explicit_func_aic_bd_proj.get_custom_explicit_partials('aic_bd_proj', 'aic_bd')
path_to_v635_normal_concatenated_aic_bd_proj = STD_MULT(path_to_v639_aic_bd_proj,pv639_aic_bd_proj_pv635_normal_concatenated_aic_bd_proj)
path_to_v636_aic_bd = STD_MULT(path_to_v639_aic_bd_proj,pv639_aic_bd_proj_pv636_aic_bd)
del pv639_aic_bd_proj_pv636_aic_bd
del pv639_aic_bd_proj_pv635_normal_concatenated_aic_bd_proj
del path_to_v639_aic_bd_proj

# op _00eS_custom_explicit_eval
# LANG: normal_concatenated_M_mat, aic_M --> M_mat
# SHAPES: (1, 200, 3), (1, 200, 276, 3) --> (1, 200, 276)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_aic

# _00eS_custom_explicit_eval_pv528_M_mat_pv525_aic_M
pv528_M_mat_pv524_normal_concatenated_M_mat = _00eS_custom_explicit_func_M_mat.get_custom_explicit_partials('M_mat', 'normal_concatenated_M_mat')
pv528_M_mat_pv525_aic_M = _00eS_custom_explicit_func_M_mat.get_custom_explicit_partials('M_mat', 'aic_M')
path_to_v524_normal_concatenated_M_mat = STD_MULT(path_to_v528_M_mat,pv528_M_mat_pv524_normal_concatenated_M_mat)
path_to_v525_aic_M = STD_MULT(path_to_v528_M_mat,pv528_M_mat_pv525_aic_M)
del pv528_M_mat_pv524_normal_concatenated_M_mat
del pv528_M_mat_pv525_aic_M
del path_to_v528_M_mat

# op _009j_custom_explicit_eval
# LANG: _009i, eel_kinematic_vel --> b
# SHAPES: (1, 200, 3), (1, 200, 3) --> (1, 200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_k_vel

# _009j_custom_explicit_eval_pv349_b_pv346_eel_kinematic_vel
pv349_b_pv348__009i = _009j_custom_explicit_func_b.get_custom_explicit_partials('b', '_009i')
pv349_b_pv346_eel_kinematic_vel = _009j_custom_explicit_func_b.get_custom_explicit_partials('b', 'eel_kinematic_vel')
path_to_v348__009i = STD_MULT(path_to_v349_b,pv349_b_pv348__009i)
path_to_v346_eel_kinematic_vel = STD_MULT(path_to_v349_b,pv349_b_pv346_eel_kinematic_vel)
del path_to_v349_b
del pv349_b_pv348__009i
del pv349_b_pv346_eel_kinematic_vel

# op _00ie_indexed_passthrough_eval
# LANG: _00id --> normal_concatenated_aic_bd_proj
# SHAPES: (1, 200, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_aic_bd

# _00ie_indexed_passthrough_eval_pv635_normal_concatenated_aic_bd_proj_pv638__00id
path_to_v638__00id = STD_MULT(path_to_v635_normal_concatenated_aic_bd_proj,pv635_normal_concatenated_aic_bd_proj_pv638__00id)
del path_to_v635_normal_concatenated_aic_bd_proj

# op _00f0_indexed_passthrough_eval
# LANG: _00e_ --> aic_bd
# SHAPES: (1, 200, 200, 3) --> (1, 200, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd

# _00f0_indexed_passthrough_eval_pv636_aic_bd_pv533__00e_
path_to_v533__00e_ = STD_MULT(path_to_v636_aic_bd,pv636_aic_bd_pv533__00e_)
del path_to_v636_aic_bd

# op _00eR_indexed_passthrough_eval
# LANG: _00eQ --> normal_concatenated_M_mat
# SHAPES: (1, 200, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_aic

# _00eR_indexed_passthrough_eval_pv524_normal_concatenated_M_mat_pv527__00eQ
path_to_v527__00eQ = STD_MULT(path_to_v524_normal_concatenated_M_mat,pv524_normal_concatenated_M_mat_pv527__00eQ)
del path_to_v524_normal_concatenated_M_mat

# op _009t_indexed_passthrough_eval
# LANG: _009s --> aic_M
# SHAPES: (1, 200, 276, 3) --> (1, 200, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic

# _009t_indexed_passthrough_eval_pv525_aic_M_pv354__009s
path_to_v354__009s = STD_MULT(path_to_v525_aic_M,pv525_aic_M_pv354__009s)
del path_to_v525_aic_M

# op _009h reshape_eval
# LANG: eel_bd_vtx_normals --> _009i
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_k_vel

# _009h reshape_eval_pv348__009i_pv637_eel_bd_vtx_normals
path_to_v637_eel_bd_vtx_normals = DIAG_MULT(path_to_v348__009i,pv348__009i_pv637_eel_bd_vtx_normals)
del path_to_v348__009i

# op _008R_linear_combination_eval
# LANG: _008Q --> eel_kinematic_vel
# SHAPES: (1, 200, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp

# _008R_linear_combination_eval_pv346_eel_kinematic_vel_pv330__008Q
path_to_v330__008Q = DIAG_MULT(path_to_v346_eel_kinematic_vel,pv346_eel_kinematic_vel_pv330__008Q)
del path_to_v346_eel_kinematic_vel

# op _00ic reshape_eval
# LANG: eel_bd_vtx_normals --> _00id
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_aic_bd

# _00ic reshape_eval_pv638__00id_pv637_eel_bd_vtx_normals
path_to_v637_eel_bd_vtx_normals += DIAG_MULT(path_to_v638__00id,pv638__00id_pv637_eel_bd_vtx_normals)
del path_to_v638__00id

# op _00eZ reshape_eval
# LANG: aic_bd00 --> _00e_
# SHAPES: (1, 40000, 3) --> (1, 200, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd

# _00eZ reshape_eval_pv533__00e__pv634_aic_bd00
path_to_v634_aic_bd00 = DIAG_MULT(path_to_v533__00e_,pv533__00e__pv634_aic_bd00)
del path_to_v533__00e_

# op _00eP reshape_eval
# LANG: eel_bd_vtx_normals --> _00eQ
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_aic

# _00eP reshape_eval_pv527__00eQ_pv637_eel_bd_vtx_normals
path_to_v637_eel_bd_vtx_normals += DIAG_MULT(path_to_v527__00eQ,pv527__00eQ_pv637_eel_bd_vtx_normals)
del path_to_v527__00eQ

# op _009r reshape_eval
# LANG: aic_M00 --> _009s
# SHAPES: (1, 55200, 3) --> (1, 200, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic

# _009r reshape_eval_pv354__009s_pv523_aic_M00
path_to_v523_aic_M00 = DIAG_MULT(path_to_v354__009s,pv354__009s_pv523_aic_M00)
del path_to_v354__009s

# op _008P_linear_combination_eval
# LANG: _008M, _008O --> _008Q
# SHAPES: (1, 200, 3), (1, 200, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp

# _008P_linear_combination_eval_pv330__008Q_pv329__008O
path_to_v328__008M = DIAG_MULT(path_to_v330__008Q,pv330__008Q_pv328__008M)
path_to_v329__008O = DIAG_MULT(path_to_v330__008Q,pv330__008Q_pv329__008O)
del path_to_v330__008Q

# op _00i7_linear_combination_eval
# LANG: _00i6, _00i2 --> aic_bd00
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00i7_linear_combination_eval_pv634_aic_bd00_pv631__00i2
path_to_v633__00i6 = DIAG_MULT(path_to_v634_aic_bd00,pv634_aic_bd00_pv633__00i6)
path_to_v631__00i2 = DIAG_MULT(path_to_v634_aic_bd00,pv634_aic_bd00_pv631__00i2)
del path_to_v634_aic_bd00

# op _00eK_linear_combination_eval
# LANG: _00eJ, _00eF --> aic_M00
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00eK_linear_combination_eval_pv523_aic_M00_pv520__00eF
path_to_v522__00eJ = DIAG_MULT(path_to_v523_aic_M00,pv523_aic_M00_pv522__00eJ)
path_to_v520__00eF = DIAG_MULT(path_to_v523_aic_M00,pv523_aic_M00_pv520__00eF)
del path_to_v523_aic_M00

# op _009c_power_combination_eval
# LANG: _0093, _009b --> eel_bd_vtx_normals
# SHAPES: (1, 50, 4, 3), (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal

# _009c_power_combination_eval_pv637_eel_bd_vtx_normals_pv343__009b
temp_power = _009c_coeff_temp*1*(v343__009b**-1)
pv637_eel_bd_vtx_normals_pv339__0093 = temp_power.flatten()
temp_power = _009c_coeff_temp*(v339__0093)*-1*(v343__009b**-2.0)
pv637_eel_bd_vtx_normals_pv343__009b = temp_power.flatten()
path_to_v339__0093 = DIAG_MULT(path_to_v637_eel_bd_vtx_normals,pv637_eel_bd_vtx_normals_pv339__0093)
path_to_v343__009b = DIAG_MULT(path_to_v637_eel_bd_vtx_normals,pv637_eel_bd_vtx_normals_pv343__009b)
del pv637_eel_bd_vtx_normals_pv343__009b
del path_to_v637_eel_bd_vtx_normals
del pv637_eel_bd_vtx_normals_pv339__0093

# op _008N reshape_eval
# LANG: eel_coll_vel --> _008O
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp

# _008N reshape_eval_pv329__008O_pv327_eel_coll_vel
path_to_v327_eel_coll_vel = DIAG_MULT(path_to_v329__008O,pv329__008O_pv327_eel_coll_vel)
del path_to_v329__008O

# op _008L_linear_combination_eval
# LANG: _008H, _008J --> _008M
# SHAPES: (1, 200, 3), (1, 200, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp

# _008L_linear_combination_eval_pv328__008M_pv326__008J
path_to_v325__008H = DIAG_MULT(path_to_v328__008M,pv328__008M_pv325__008H)
path_to_v326__008J = DIAG_MULT(path_to_v328__008M,pv328__008M_pv326__008J)
del path_to_v328__008M

# op _00i5_linear_combination_eval
# LANG: _00i4, _00hD --> _00i6
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00i5_linear_combination_eval_pv633__00i6_pv618__00hD
path_to_v632__00i4 = DIAG_MULT(path_to_v633__00i6,pv633__00i6_pv632__00i4)
path_to_v618__00hD = DIAG_MULT(path_to_v633__00i6,pv633__00i6_pv618__00hD)
del path_to_v633__00i6

# op _00i1_power_combination_eval
# LANG: _00i0, _00hH --> _00i2
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00i1_power_combination_eval_pv631__00i2_pv620__00hH
temp_power = _00i1_coeff_temp*1*(v620__00hH)
pv631__00i2_pv630__00i0 = temp_power.flatten()
temp_power = _00i1_coeff_temp*(v630__00i0)*1
pv631__00i2_pv620__00hH = temp_power.flatten()
path_to_v630__00i0 = DIAG_MULT(path_to_v631__00i2,pv631__00i2_pv630__00i0)
path_to_v620__00hH = DIAG_MULT(path_to_v631__00i2,pv631__00i2_pv620__00hH)
del path_to_v631__00i2
del pv631__00i2_pv620__00hH
del pv631__00i2_pv630__00i0

# op _00eI_linear_combination_eval
# LANG: _00eH, _00dI --> _00eJ
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00eI_linear_combination_eval_pv522__00eJ_pv490__00dI
path_to_v521__00eH = DIAG_MULT(path_to_v522__00eJ,pv522__00eJ_pv521__00eH)
path_to_v490__00dI = DIAG_MULT(path_to_v522__00eJ,pv522__00eJ_pv490__00dI)
del path_to_v522__00eJ

# op _00eE_power_combination_eval
# LANG: _00eD, _00dM --> _00eF
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00eE_power_combination_eval_pv520__00eF_pv492__00dM
temp_power = _00eE_coeff_temp*1*(v492__00dM)
pv520__00eF_pv519__00eD = temp_power.flatten()
temp_power = _00eE_coeff_temp*(v519__00eD)*1
pv520__00eF_pv492__00dM = temp_power.flatten()
path_to_v519__00eD = DIAG_MULT(path_to_v520__00eF,pv520__00eF_pv519__00eD)
path_to_v492__00dM = DIAG_MULT(path_to_v520__00eF,pv520__00eF_pv492__00dM)
del pv520__00eF_pv492__00dM
del path_to_v520__00eF
del pv520__00eF_pv519__00eD

# op _009a expand_array_eval
# LANG: _0099 --> _009b
# SHAPES: (1, 50, 4) --> (1, 50, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal

# _009a expand_array_eval_pv343__009b_pv342__0099
path_to_v342__0099 = STD_MULT(path_to_v343__009b,pv343__009b_pv342__0099)
del path_to_v343__009b

# op _008I expand_array_eval
# LANG: frame_vel --> _008J
# SHAPES: (1, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp

# _008I expand_array_eval_pv326__008J_pv644_frame_vel
path_to_v644_frame_vel += STD_MULT(path_to_v326__008J,pv326__008J_pv644_frame_vel)
del path_to_v326__008J

# op _008G reshape_eval
# LANG: _008F --> _008H
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp

# _008G reshape_eval_pv325__008H_pv324__008F
path_to_v324__008F = DIAG_MULT(path_to_v325__008H,pv325__008H_pv324__008F)
del path_to_v325__008H

# op _00i3_linear_combination_eval
# LANG: _00gO, _00hd --> _00i4
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00i3_linear_combination_eval_pv632__00i4_pv605__00hd
path_to_v592__00gO = DIAG_MULT(path_to_v632__00i4,pv632__00i4_pv592__00gO)
path_to_v605__00hd = DIAG_MULT(path_to_v632__00i4,pv632__00i4_pv605__00hd)
del path_to_v632__00i4

# op _00h_ expand_array_eval
# LANG: _00hZ --> _00i0
# SHAPES: (1, 40000) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00h_ expand_array_eval_pv630__00i0_pv629__00hZ
path_to_v629__00hZ = STD_MULT(path_to_v630__00i0,pv630__00i0_pv629__00hZ)
del path_to_v630__00i0

# op _00hG_power_combination_eval
# LANG: _00hF --> _00hH
# SHAPES: (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00hG_power_combination_eval_pv620__00hH_pv619__00hF
temp_power = _00hG_coeff_temp*1
pv620__00hH_pv619__00hF = temp_power.flatten()
path_to_v619__00hF = DIAG_MULT(path_to_v620__00hH,pv620__00hH_pv619__00hF)
del path_to_v620__00hH
del pv620__00hH_pv619__00hF

# op _00hC_power_combination_eval
# LANG: _00hB, _00hh --> _00hD
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00hC_power_combination_eval_pv618__00hD_pv607__00hh
temp_power = _00hC_coeff_temp*1*(v607__00hh)
pv618__00hD_pv617__00hB = temp_power.flatten()
temp_power = _00hC_coeff_temp*(v617__00hB)*1
pv618__00hD_pv607__00hh = temp_power.flatten()
path_to_v617__00hB = DIAG_MULT(path_to_v618__00hD,pv618__00hD_pv617__00hB)
path_to_v607__00hh = DIAG_MULT(path_to_v618__00hD,pv618__00hD_pv607__00hh)
del path_to_v618__00hD
del pv618__00hD_pv617__00hB
del pv618__00hD_pv607__00hh

# op _00eG_linear_combination_eval
# LANG: _00bO, _00cL --> _00eH
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00eG_linear_combination_eval_pv521__00eH_pv460__00cL
path_to_v430__00bO = DIAG_MULT(path_to_v521__00eH,pv521__00eH_pv430__00bO)
path_to_v460__00cL = DIAG_MULT(path_to_v521__00eH,pv521__00eH_pv460__00cL)
del path_to_v521__00eH

# op _00eC expand_array_eval
# LANG: _00eB --> _00eD
# SHAPES: (1, 55200) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00eC expand_array_eval_pv519__00eD_pv518__00eB
path_to_v518__00eB = STD_MULT(path_to_v519__00eD,pv519__00eD_pv518__00eB)
del path_to_v519__00eD

# op _00dL_power_combination_eval
# LANG: _00dK --> _00dM
# SHAPES: (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dL_power_combination_eval_pv492__00dM_pv491__00dK
temp_power = _00dL_coeff_temp*1
pv492__00dM_pv491__00dK = temp_power.flatten()
path_to_v491__00dK = DIAG_MULT(path_to_v492__00dM,pv492__00dM_pv491__00dK)
del pv492__00dM_pv491__00dK
del path_to_v492__00dM

# op _00dH_power_combination_eval
# LANG: _00dG, _00cP --> _00dI
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dH_power_combination_eval_pv490__00dI_pv462__00cP
temp_power = _00dH_coeff_temp*1*(v462__00cP)
pv490__00dI_pv489__00dG = temp_power.flatten()
temp_power = _00dH_coeff_temp*(v489__00dG)*1
pv490__00dI_pv462__00cP = temp_power.flatten()
path_to_v489__00dG = DIAG_MULT(path_to_v490__00dI,pv490__00dI_pv489__00dG)
path_to_v462__00cP = DIAG_MULT(path_to_v490__00dI,pv490__00dI_pv462__00cP)
del pv490__00dI_pv489__00dG
del pv490__00dI_pv462__00cP
del path_to_v490__00dI

# op _0098_power_combination_eval
# LANG: _0097 --> _0099
# SHAPES: (1, 50, 4) --> (1, 50, 4)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal

# _0098_power_combination_eval_pv342__0099_pv341__0097
temp_power = _0098_coeff_temp*0.5*(v341__0097**-0.5)
pv342__0099_pv341__0097 = temp_power.flatten()
path_to_v341__0097 = DIAG_MULT(path_to_v342__0099,pv342__0099_pv341__0097)
del path_to_v342__0099
del pv342__0099_pv341__0097

# _008E cross_product_eval__008E
_008E_path_in = _008E_vjp(v323__008D,v322__008B,path_to_v324__008F)
_008E_v323__008D = _008E_path_in[0]
_008E_v322__008B = _008E_path_in[1]
path_to_v323__008D = _008E_v323__008D
path_to_v322__008B = _008E_v322__008B
del path_to_v324__008F

# op _00hg_power_combination_eval
# LANG: _00hf --> _00hh
# SHAPES: (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00hg_power_combination_eval_pv607__00hh_pv606__00hf
temp_power = _00hg_coeff_temp*1
pv607__00hh_pv606__00hf = temp_power.flatten()
path_to_v606__00hf = DIAG_MULT(path_to_v607__00hh,pv607__00hh_pv606__00hf)
del pv607__00hh_pv606__00hf
del path_to_v607__00hh

# op _00hc_power_combination_eval
# LANG: _00hb, _00gS --> _00hd
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00hc_power_combination_eval_pv605__00hd_pv594__00gS
temp_power = _00hc_coeff_temp*1*(v594__00gS)
pv605__00hd_pv604__00hb = temp_power.flatten()
temp_power = _00hc_coeff_temp*(v604__00hb)*1
pv605__00hd_pv594__00gS = temp_power.flatten()
path_to_v604__00hb = DIAG_MULT(path_to_v605__00hd,pv605__00hd_pv604__00hb)
path_to_v594__00gS = DIAG_MULT(path_to_v605__00hd,pv605__00hd_pv594__00gS)
del pv605__00hd_pv604__00hb
del path_to_v605__00hd
del pv605__00hd_pv594__00gS

# op _00hY_power_combination_eval
# LANG: _00hR, _00hX --> _00hZ
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00hY_power_combination_eval_pv629__00hZ_pv628__00hX
temp_power = _00hY_coeff_temp*1*(v628__00hX)
pv629__00hZ_pv625__00hR = temp_power.flatten()
temp_power = _00hY_coeff_temp*(v625__00hR)*1
pv629__00hZ_pv628__00hX = temp_power.flatten()
path_to_v625__00hR = DIAG_MULT(path_to_v629__00hZ,pv629__00hZ_pv625__00hR)
path_to_v628__00hX = DIAG_MULT(path_to_v629__00hZ,pv629__00hZ_pv628__00hX)
del pv629__00hZ_pv625__00hR
del pv629__00hZ_pv628__00hX
del path_to_v629__00hZ

# _00hE cross_product_eval__00hE
_00hE_path_in = _00hE_vjp(v576__00gi,v546__00fl,path_to_v619__00hF)
_00hE_v576__00gi = _00hE_path_in[0]
_00hE_v546__00fl = _00hE_path_in[1]
path_to_v576__00gi = _00hE_v576__00gi
path_to_v546__00fl = _00hE_v546__00fl
del path_to_v619__00hF

# op _00hA expand_array_eval
# LANG: _00hz --> _00hB
# SHAPES: (1, 40000) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00hA expand_array_eval_pv617__00hB_pv616__00hz
path_to_v616__00hz = STD_MULT(path_to_v617__00hB,pv617__00hB_pv616__00hz)
del path_to_v617__00hB

# op _00gN_power_combination_eval
# LANG: _00gM, _00gs --> _00gO
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gN_power_combination_eval_pv592__00gO_pv581__00gs
temp_power = _00gN_coeff_temp*1*(v581__00gs)
pv592__00gO_pv591__00gM = temp_power.flatten()
temp_power = _00gN_coeff_temp*(v591__00gM)*1
pv592__00gO_pv581__00gs = temp_power.flatten()
path_to_v591__00gM = DIAG_MULT(path_to_v592__00gO,pv592__00gO_pv591__00gM)
path_to_v581__00gs = DIAG_MULT(path_to_v592__00gO,pv592__00gO_pv581__00gs)
del pv592__00gO_pv581__00gs
del path_to_v592__00gO
del pv592__00gO_pv591__00gM

# op _00eA_power_combination_eval
# LANG: _00ef, _00ez --> _00eB
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00eA_power_combination_eval_pv518__00eB_pv517__00ez
temp_power = _00eA_coeff_temp*1*(v517__00ez**-1)
pv518__00eB_pv507__00ef = temp_power.flatten()
temp_power = _00eA_coeff_temp*(v507__00ef)*-1*(v517__00ez**-2.0)
pv518__00eB_pv517__00ez = temp_power.flatten()
path_to_v507__00ef = DIAG_MULT(path_to_v518__00eB,pv518__00eB_pv507__00ef)
path_to_v517__00ez = DIAG_MULT(path_to_v518__00eB,pv518__00eB_pv517__00ez)
del path_to_v518__00eB
del pv518__00eB_pv507__00ef
del pv518__00eB_pv517__00ez

# _00dJ cross_product_eval__00dJ
_00dJ_path_in = _00dJ_vjp(v397__00aL,v367__009O,path_to_v491__00dK)
_00dJ_v397__00aL = _00dJ_path_in[0]
_00dJ_v367__009O = _00dJ_path_in[1]
path_to_v397__00aL = _00dJ_v397__00aL
path_to_v367__009O = _00dJ_v367__009O
del path_to_v491__00dK

# op _00dF expand_array_eval
# LANG: _00dE --> _00dG
# SHAPES: (1, 55200) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dF expand_array_eval_pv489__00dG_pv488__00dE
path_to_v488__00dE = STD_MULT(path_to_v489__00dG,pv489__00dG_pv488__00dE)
del path_to_v489__00dG

# op _00cO_power_combination_eval
# LANG: _00cN --> _00cP
# SHAPES: (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cO_power_combination_eval_pv462__00cP_pv461__00cN
temp_power = _00cO_coeff_temp*1
pv462__00cP_pv461__00cN = temp_power.flatten()
path_to_v461__00cN = DIAG_MULT(path_to_v462__00cP,pv462__00cP_pv461__00cN)
del pv462__00cP_pv461__00cN
del path_to_v462__00cP

# op _00cK_power_combination_eval
# LANG: _00cJ, _00bS --> _00cL
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cK_power_combination_eval_pv460__00cL_pv432__00bS
temp_power = _00cK_coeff_temp*1*(v432__00bS)
pv460__00cL_pv459__00cJ = temp_power.flatten()
temp_power = _00cK_coeff_temp*(v459__00cJ)*1
pv460__00cL_pv432__00bS = temp_power.flatten()
path_to_v459__00cJ = DIAG_MULT(path_to_v460__00cL,pv460__00cL_pv459__00cJ)
path_to_v432__00bS = DIAG_MULT(path_to_v460__00cL,pv460__00cL_pv432__00bS)
del pv460__00cL_pv459__00cJ
del path_to_v460__00cL
del pv460__00cL_pv432__00bS

# op _00bN_power_combination_eval
# LANG: _00bM, _00aV --> _00bO
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bN_power_combination_eval_pv430__00bO_pv402__00aV
temp_power = _00bN_coeff_temp*1*(v402__00aV)
pv430__00bO_pv429__00bM = temp_power.flatten()
temp_power = _00bN_coeff_temp*(v429__00bM)*1
pv430__00bO_pv402__00aV = temp_power.flatten()
path_to_v429__00bM = DIAG_MULT(path_to_v430__00bO,pv430__00bO_pv429__00bM)
path_to_v402__00aV = DIAG_MULT(path_to_v430__00bO,pv430__00bO_pv402__00aV)
del pv430__00bO_pv402__00aV
del path_to_v430__00bO
del pv430__00bO_pv429__00bM

# op _0096_single_tensor_sum_with_axis_eval
# LANG: _0095 --> _0097
# SHAPES: (1, 50, 4, 3) --> (1, 50, 4)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal

# _0096_single_tensor_sum_with_axis_eval_pv341__0097_pv340__0095
path_to_v340__0095 = STD_MULT(path_to_v341__0097,pv341__0097_pv340__0095)
del path_to_v341__0097

# op _008C expand_array_eval
# LANG: ang_vel --> _008D
# SHAPES: (1, 3) --> (1, 50, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp

# _008C expand_array_eval_pv323__008D_pv318_ang_vel
path_to_v318_ang_vel = STD_MULT(path_to_v323__008D,pv323__008D_pv318_ang_vel)
del path_to_v323__008D

# op _008A_linear_combination_eval
# LANG: _008z, eel_coll_pts_coords --> _008B
# SHAPES: (1, 50, 4, 3), (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp

# _008A_linear_combination_eval_pv322__008B_pv534_eel_coll_pts_coords
path_to_v534_eel_coll_pts_coords = DIAG_MULT(path_to_v322__008B,pv322__008B_pv534_eel_coll_pts_coords)
del path_to_v322__008B

# op _00hy_power_combination_eval
# LANG: _00hr, _00hx --> _00hz
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00hy_power_combination_eval_pv616__00hz_pv615__00hx
temp_power = _00hy_coeff_temp*1*(v615__00hx)
pv616__00hz_pv612__00hr = temp_power.flatten()
temp_power = _00hy_coeff_temp*(v612__00hr)*1
pv616__00hz_pv615__00hx = temp_power.flatten()
path_to_v612__00hr = DIAG_MULT(path_to_v616__00hz,pv616__00hz_pv612__00hr)
path_to_v615__00hx = DIAG_MULT(path_to_v616__00hz,pv616__00hz_pv615__00hx)
del pv616__00hz_pv615__00hx
del pv616__00hz_pv612__00hr
del path_to_v616__00hz

# _00he cross_product_eval__00he
_00he_path_in = _00he_vjp(v566__00fZ,v576__00gi,path_to_v606__00hf)
_00he_v566__00fZ = _00he_path_in[0]
_00he_v576__00gi = _00he_path_in[1]
path_to_v576__00gi += _00he_v576__00gi
path_to_v566__00fZ = _00he_v566__00fZ
del path_to_v606__00hf

# op _00ha expand_array_eval
# LANG: _00h9 --> _00hb
# SHAPES: (1, 40000) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00ha expand_array_eval_pv604__00hb_pv603__00h9
path_to_v603__00h9 = STD_MULT(path_to_v604__00hb,pv604__00hb_pv603__00h9)
del path_to_v604__00hb

# op _00hW_linear_combination_eval
# LANG: _00hT, _00hV --> _00hX
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00hW_linear_combination_eval_pv628__00hX_pv627__00hV
path_to_v626__00hT = DIAG_MULT(path_to_v628__00hX,pv628__00hX_pv626__00hT)
path_to_v627__00hV = DIAG_MULT(path_to_v628__00hX,pv628__00hX_pv627__00hV)
del path_to_v628__00hX

# op _00hQ_power_combination_eval
# LANG: _00hP --> _00hR
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00hQ_power_combination_eval_pv625__00hR_pv624__00hP
temp_power = _00hQ_coeff_temp*-1*(v624__00hP**-2.0)
pv625__00hR_pv624__00hP = temp_power.flatten()
path_to_v624__00hP = DIAG_MULT(path_to_v625__00hR,pv625__00hR_pv624__00hP)
del pv625__00hR_pv624__00hP
del path_to_v625__00hR

# op _00gr_power_combination_eval
# LANG: _00gq --> _00gs
# SHAPES: (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gr_power_combination_eval_pv581__00gs_pv580__00gq
temp_power = _00gr_coeff_temp*1
pv581__00gs_pv580__00gq = temp_power.flatten()
path_to_v580__00gq = DIAG_MULT(path_to_v581__00gs,pv581__00gs_pv580__00gq)
del pv581__00gs_pv580__00gq
del path_to_v581__00gs

# op _00gR_power_combination_eval
# LANG: _00gQ --> _00gS
# SHAPES: (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gR_power_combination_eval_pv594__00gS_pv593__00gQ
temp_power = _00gR_coeff_temp*1
pv594__00gS_pv593__00gQ = temp_power.flatten()
path_to_v593__00gQ = DIAG_MULT(path_to_v594__00gS,pv594__00gS_pv593__00gQ)
del pv594__00gS_pv593__00gQ
del path_to_v594__00gS

# op _00gL expand_array_eval
# LANG: _00gK --> _00gM
# SHAPES: (1, 40000) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gL expand_array_eval_pv591__00gM_pv590__00gK
path_to_v590__00gK = STD_MULT(path_to_v591__00gM,pv591__00gM_pv590__00gK)
del path_to_v591__00gM

# op _00ey_linear_combination_eval
# LANG: _00ex --> _00ez
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00ey_linear_combination_eval_pv517__00ez_pv516__00ex
path_to_v516__00ex = DIAG_MULT(path_to_v517__00ez,pv517__00ez_pv516__00ex)
del path_to_v517__00ez

# op _00ee_linear_combination_eval
# LANG: _00e3, _00ed --> _00ef
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00ee_linear_combination_eval_pv507__00ef_pv506__00ed
path_to_v501__00e3 = DIAG_MULT(path_to_v507__00ef,pv507__00ef_pv501__00e3)
path_to_v506__00ed = DIAG_MULT(path_to_v507__00ef,pv507__00ef_pv506__00ed)
del path_to_v507__00ef

# op _00dD_power_combination_eval
# LANG: _00di, _00dC --> _00dE
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dD_power_combination_eval_pv488__00dE_pv487__00dC
temp_power = _00dD_coeff_temp*1*(v487__00dC**-1)
pv488__00dE_pv477__00di = temp_power.flatten()
temp_power = _00dD_coeff_temp*(v477__00di)*-1*(v487__00dC**-2.0)
pv488__00dE_pv487__00dC = temp_power.flatten()
path_to_v477__00di = DIAG_MULT(path_to_v488__00dE,pv488__00dE_pv477__00di)
path_to_v487__00dC = DIAG_MULT(path_to_v488__00dE,pv488__00dE_pv487__00dC)
del pv488__00dE_pv477__00di
del pv488__00dE_pv487__00dC
del path_to_v488__00dE

# _00cM cross_product_eval__00cM
_00cM_path_in = _00cM_vjp(v387__00ar,v397__00aL,path_to_v461__00cN)
_00cM_v387__00ar = _00cM_path_in[0]
_00cM_v397__00aL = _00cM_path_in[1]
path_to_v397__00aL += _00cM_v397__00aL
path_to_v387__00ar = _00cM_v387__00ar
del path_to_v461__00cN

# op _00cI expand_array_eval
# LANG: _00cH --> _00cJ
# SHAPES: (1, 55200) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cI expand_array_eval_pv459__00cJ_pv458__00cH
path_to_v458__00cH = STD_MULT(path_to_v459__00cJ,pv459__00cJ_pv458__00cH)
del path_to_v459__00cJ

# op _00bR_power_combination_eval
# LANG: _00bQ --> _00bS
# SHAPES: (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bR_power_combination_eval_pv432__00bS_pv431__00bQ
temp_power = _00bR_coeff_temp*1
pv432__00bS_pv431__00bQ = temp_power.flatten()
path_to_v431__00bQ = DIAG_MULT(path_to_v432__00bS,pv432__00bS_pv431__00bQ)
del path_to_v432__00bS
del pv432__00bS_pv431__00bQ

# op _00bL expand_array_eval
# LANG: _00bK --> _00bM
# SHAPES: (1, 55200) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bL expand_array_eval_pv429__00bM_pv428__00bK
path_to_v428__00bK = STD_MULT(path_to_v429__00bM,pv429__00bM_pv428__00bK)
del path_to_v429__00bM

# op _00aU_power_combination_eval
# LANG: _00aT --> _00aV
# SHAPES: (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00aU_power_combination_eval_pv402__00aV_pv401__00aT
temp_power = _00aU_coeff_temp*1
pv402__00aV_pv401__00aT = temp_power.flatten()
path_to_v401__00aT = DIAG_MULT(path_to_v402__00aV,pv402__00aV_pv401__00aT)
del path_to_v402__00aV
del pv402__00aV_pv401__00aT

# op _0094_power_combination_eval
# LANG: _0093 --> _0095
# SHAPES: (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal

# _0094_power_combination_eval_pv340__0095_pv339__0093
temp_power = _0094_coeff_temp*2*(v339__0093)
pv340__0095_pv339__0093 = temp_power.flatten()
path_to_v339__0093 += DIAG_MULT(path_to_v340__0095,pv340__0095_pv339__0093)
del pv340__0095_pv339__0093
del path_to_v340__0095

# op _008v_indexed_passthrough_eval
# LANG: p, q, r --> ang_vel
# SHAPES: (1, 1), (1, 1), (1, 1) --> (1, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp

# _008v_indexed_passthrough_eval_pv318_ang_vel_pv317_r
path_to_v315_p = STD_MULT(path_to_v318_ang_vel,pv318_ang_vel_pv315_p)
path_to_v316_q = STD_MULT(path_to_v318_ang_vel,pv318_ang_vel_pv316_q)
path_to_v317_r = STD_MULT(path_to_v318_ang_vel,pv318_ang_vel_pv317_r)
del path_to_v318_ang_vel

# op _00hw_linear_combination_eval
# LANG: _00ht, _00hv --> _00hx
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00hw_linear_combination_eval_pv615__00hx_pv614__00hv
path_to_v613__00ht = DIAG_MULT(path_to_v615__00hx,pv615__00hx_pv613__00ht)
path_to_v614__00hv = DIAG_MULT(path_to_v615__00hx,pv615__00hx_pv614__00hv)
del path_to_v615__00hx

# op _00hq_power_combination_eval
# LANG: _00hp --> _00hr
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00hq_power_combination_eval_pv612__00hr_pv611__00hp
temp_power = _00hq_coeff_temp*-1*(v611__00hp**-2.0)
pv612__00hr_pv611__00hp = temp_power.flatten()
path_to_v611__00hp = DIAG_MULT(path_to_v612__00hr,pv612__00hr_pv611__00hp)
del pv612__00hr_pv611__00hp
del path_to_v612__00hr

# op _00hU_power_combination_eval
# LANG: _00fr --> _00hV
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00hU_power_combination_eval_pv627__00hV_pv549__00fr
temp_power = _00hU_coeff_temp*-1*(v549__00fr**-2.0)
pv627__00hV_pv549__00fr = temp_power.flatten()
path_to_v549__00fr = DIAG_MULT(path_to_v627__00hV,pv627__00hV_pv549__00fr)
del pv627__00hV_pv549__00fr
del path_to_v627__00hV

# op _00hS_power_combination_eval
# LANG: _00go --> _00hT
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00hS_power_combination_eval_pv626__00hT_pv579__00go
temp_power = _00hS_coeff_temp*-1*(v579__00go**-2.0)
pv626__00hT_pv579__00go = temp_power.flatten()
path_to_v579__00go = DIAG_MULT(path_to_v626__00hT,pv626__00hT_pv579__00go)
del pv626__00hT_pv579__00go
del path_to_v626__00hT

# op _00hO_linear_combination_eval
# LANG: _00hN, _00hL --> _00hP
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00hO_linear_combination_eval_pv624__00hP_pv622__00hL
path_to_v623__00hN = DIAG_MULT(path_to_v624__00hP,pv624__00hP_pv623__00hN)
path_to_v622__00hL = DIAG_MULT(path_to_v624__00hP,pv624__00hP_pv622__00hL)
del path_to_v624__00hP

# op _00h8_power_combination_eval
# LANG: _00h1, _00h7 --> _00h9
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00h8_power_combination_eval_pv603__00h9_pv602__00h7
temp_power = _00h8_coeff_temp*1*(v602__00h7)
pv603__00h9_pv599__00h1 = temp_power.flatten()
temp_power = _00h8_coeff_temp*(v599__00h1)*1
pv603__00h9_pv602__00h7 = temp_power.flatten()
path_to_v599__00h1 = DIAG_MULT(path_to_v603__00h9,pv603__00h9_pv599__00h1)
path_to_v602__00h7 = DIAG_MULT(path_to_v603__00h9,pv603__00h9_pv602__00h7)
del path_to_v603__00h9
del pv603__00h9_pv602__00h7
del pv603__00h9_pv599__00h1

# _00gp cross_product_eval__00gp
_00gp_path_in = _00gp_vjp(v546__00fl,v556__00fF,path_to_v580__00gq)
_00gp_v546__00fl = _00gp_path_in[0]
_00gp_v556__00fF = _00gp_path_in[1]
path_to_v546__00fl += _00gp_v546__00fl
path_to_v556__00fF = _00gp_v556__00fF
del path_to_v580__00gq

# _00gP cross_product_eval__00gP
_00gP_path_in = _00gP_vjp(v556__00fF,v566__00fZ,path_to_v593__00gQ)
_00gP_v556__00fF = _00gP_path_in[0]
_00gP_v566__00fZ = _00gP_path_in[1]
path_to_v566__00fZ += _00gP_v566__00fZ
path_to_v556__00fF += _00gP_v556__00fF
del path_to_v593__00gQ

# op _00gJ_power_combination_eval
# LANG: _00gC, _00gI --> _00gK
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gJ_power_combination_eval_pv590__00gK_pv589__00gI
temp_power = _00gJ_coeff_temp*1*(v589__00gI)
pv590__00gK_pv586__00gC = temp_power.flatten()
temp_power = _00gJ_coeff_temp*(v586__00gC)*1
pv590__00gK_pv589__00gI = temp_power.flatten()
path_to_v586__00gC = DIAG_MULT(path_to_v590__00gK,pv590__00gK_pv586__00gC)
path_to_v589__00gI = DIAG_MULT(path_to_v590__00gK,pv590__00gK_pv589__00gI)
del pv590__00gK_pv589__00gI
del path_to_v590__00gK
del pv590__00gK_pv586__00gC

# op _00ew_linear_combination_eval
# LANG: _00el, _00ev --> _00ex
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00ew_linear_combination_eval_pv516__00ex_pv515__00ev
path_to_v510__00el = DIAG_MULT(path_to_v516__00ex,pv516__00ex_pv510__00el)
path_to_v515__00ev = DIAG_MULT(path_to_v516__00ex,pv516__00ex_pv515__00ev)
del path_to_v516__00ex

# op _00ec_power_combination_eval
# LANG: _00e5, _00eb --> _00ed
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00ec_power_combination_eval_pv506__00ed_pv505__00eb
temp_power = _00ec_coeff_temp*1*(v505__00eb**-1)
pv506__00ed_pv502__00e5 = temp_power.flatten()
temp_power = _00ec_coeff_temp*(v502__00e5)*-1*(v505__00eb**-2.0)
pv506__00ed_pv505__00eb = temp_power.flatten()
path_to_v502__00e5 = DIAG_MULT(path_to_v506__00ed,pv506__00ed_pv502__00e5)
path_to_v505__00eb = DIAG_MULT(path_to_v506__00ed,pv506__00ed_pv505__00eb)
del pv506__00ed_pv502__00e5
del path_to_v506__00ed
del pv506__00ed_pv505__00eb

# op _00e2_power_combination_eval
# LANG: _00dW, _00e1 --> _00e3
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00e2_power_combination_eval_pv501__00e3_pv500__00e1
temp_power = _00e2_coeff_temp*1*(v500__00e1**-1)
pv501__00e3_pv497__00dW = temp_power.flatten()
temp_power = _00e2_coeff_temp*(v497__00dW)*-1*(v500__00e1**-2.0)
pv501__00e3_pv500__00e1 = temp_power.flatten()
path_to_v497__00dW = DIAG_MULT(path_to_v501__00e3,pv501__00e3_pv497__00dW)
path_to_v500__00e1 = DIAG_MULT(path_to_v501__00e3,pv501__00e3_pv500__00e1)
del pv501__00e3_pv497__00dW
del path_to_v501__00e3
del pv501__00e3_pv500__00e1

# op _00dh_linear_combination_eval
# LANG: _00d6, _00dg --> _00di
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dh_linear_combination_eval_pv477__00di_pv476__00dg
path_to_v471__00d6 = DIAG_MULT(path_to_v477__00di,pv477__00di_pv471__00d6)
path_to_v476__00dg = DIAG_MULT(path_to_v477__00di,pv477__00di_pv476__00dg)
del path_to_v477__00di

# op _00dB_linear_combination_eval
# LANG: _00dA --> _00dC
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dB_linear_combination_eval_pv487__00dC_pv486__00dA
path_to_v486__00dA = DIAG_MULT(path_to_v487__00dC,pv487__00dC_pv486__00dA)
del path_to_v487__00dC

# op _00cG_power_combination_eval
# LANG: _00cl, _00cF --> _00cH
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cG_power_combination_eval_pv458__00cH_pv457__00cF
temp_power = _00cG_coeff_temp*1*(v457__00cF**-1)
pv458__00cH_pv447__00cl = temp_power.flatten()
temp_power = _00cG_coeff_temp*(v447__00cl)*-1*(v457__00cF**-2.0)
pv458__00cH_pv457__00cF = temp_power.flatten()
path_to_v447__00cl = DIAG_MULT(path_to_v458__00cH,pv458__00cH_pv447__00cl)
path_to_v457__00cF = DIAG_MULT(path_to_v458__00cH,pv458__00cH_pv457__00cF)
del path_to_v458__00cH
del pv458__00cH_pv447__00cl
del pv458__00cH_pv457__00cF

# _00bP cross_product_eval__00bP
_00bP_path_in = _00bP_vjp(v377__00a7,v387__00ar,path_to_v431__00bQ)
_00bP_v377__00a7 = _00bP_path_in[0]
_00bP_v387__00ar = _00bP_path_in[1]
path_to_v387__00ar += _00bP_v387__00ar
path_to_v377__00a7 = _00bP_v377__00a7
del path_to_v431__00bQ

# op _00bJ_power_combination_eval
# LANG: _00bo, _00bI --> _00bK
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bJ_power_combination_eval_pv428__00bK_pv427__00bI
temp_power = _00bJ_coeff_temp*1*(v427__00bI**-1)
pv428__00bK_pv417__00bo = temp_power.flatten()
temp_power = _00bJ_coeff_temp*(v417__00bo)*-1*(v427__00bI**-2.0)
pv428__00bK_pv427__00bI = temp_power.flatten()
path_to_v417__00bo = DIAG_MULT(path_to_v428__00bK,pv428__00bK_pv417__00bo)
path_to_v427__00bI = DIAG_MULT(path_to_v428__00bK,pv428__00bK_pv427__00bI)
del path_to_v428__00bK
del pv428__00bK_pv417__00bo
del pv428__00bK_pv427__00bI

# _00aS cross_product_eval__00aS
_00aS_path_in = _00aS_vjp(v367__009O,v377__00a7,path_to_v401__00aT)
_00aS_v367__009O = _00aS_path_in[0]
_00aS_v377__00a7 = _00aS_path_in[1]
path_to_v367__009O += _00aS_v367__009O
path_to_v377__00a7 += _00aS_v377__00a7
del path_to_v401__00aT

# _0092 cross_product_eval__0092
_0092_path_in = _0092_vjp(v335__008Y,v338__0091,path_to_v339__0093)
_0092_v335__008Y = _0092_path_in[0]
_0092_v338__0091 = _0092_path_in[1]
path_to_v335__008Y = _0092_v335__008Y
path_to_v338__0091 = _0092_v338__0091
del path_to_v339__0093

# op _00hu_power_combination_eval
# LANG: _00go --> _00hv
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00hu_power_combination_eval_pv614__00hv_pv579__00go
temp_power = _00hu_coeff_temp*-1*(v579__00go**-2.0)
pv614__00hv_pv579__00go = temp_power.flatten()
path_to_v579__00go += DIAG_MULT(path_to_v614__00hv,pv614__00hv_pv579__00go)
del pv614__00hv_pv579__00go
del path_to_v614__00hv

# op _00hs_power_combination_eval
# LANG: _00g4 --> _00ht
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00hs_power_combination_eval_pv613__00ht_pv569__00g4
temp_power = _00hs_coeff_temp*-1*(v569__00g4**-2.0)
pv613__00ht_pv569__00g4 = temp_power.flatten()
path_to_v569__00g4 = DIAG_MULT(path_to_v613__00ht,pv613__00ht_pv569__00g4)
del pv613__00ht_pv569__00g4
del path_to_v613__00ht

# op _00ho_linear_combination_eval
# LANG: _00hn, _00hl --> _00hp
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00ho_linear_combination_eval_pv611__00hp_pv609__00hl
path_to_v610__00hn = DIAG_MULT(path_to_v611__00hp,pv611__00hp_pv610__00hn)
path_to_v609__00hl = DIAG_MULT(path_to_v611__00hp,pv611__00hp_pv609__00hl)
del path_to_v611__00hp

# op _00hM_power_combination_eval
# LANG: _00fr, _00go --> _00hN
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00hM_power_combination_eval_pv623__00hN_pv579__00go
temp_power = _00hM_coeff_temp*(v579__00go)*1
pv623__00hN_pv549__00fr = temp_power.flatten()
temp_power = _00hM_coeff_temp*1*(v549__00fr)
pv623__00hN_pv579__00go = temp_power.flatten()
path_to_v549__00fr += DIAG_MULT(path_to_v623__00hN,pv623__00hN_pv549__00fr)
path_to_v579__00go += DIAG_MULT(path_to_v623__00hN,pv623__00hN_pv579__00go)
del path_to_v623__00hN
del pv623__00hN_pv549__00fr
del pv623__00hN_pv579__00go

# op _00hK_single_tensor_sum_with_axis_eval
# LANG: _00hJ --> _00hL
# SHAPES: (1, 40000, 3) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00hK_single_tensor_sum_with_axis_eval_pv622__00hL_pv621__00hJ
path_to_v621__00hJ = STD_MULT(path_to_v622__00hL,pv622__00hL_pv621__00hJ)
del path_to_v622__00hL

# op _00h6_linear_combination_eval
# LANG: _00h3, _00h5 --> _00h7
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00h6_linear_combination_eval_pv602__00h7_pv601__00h5
path_to_v600__00h3 = DIAG_MULT(path_to_v602__00h7,pv602__00h7_pv600__00h3)
path_to_v601__00h5 = DIAG_MULT(path_to_v602__00h7,pv602__00h7_pv601__00h5)
del path_to_v602__00h7

# op _00h0_power_combination_eval
# LANG: _00g_ --> _00h1
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00h0_power_combination_eval_pv599__00h1_pv598__00g_
temp_power = _00h0_coeff_temp*-1*(v598__00g_**-2.0)
pv599__00h1_pv598__00g_ = temp_power.flatten()
path_to_v598__00g_ = DIAG_MULT(path_to_v599__00h1,pv599__00h1_pv598__00g_)
del pv599__00h1_pv598__00g_
del path_to_v599__00h1

# op _00gH_linear_combination_eval
# LANG: _00gE, _00gG --> _00gI
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gH_linear_combination_eval_pv589__00gI_pv588__00gG
path_to_v587__00gE = DIAG_MULT(path_to_v589__00gI,pv589__00gI_pv587__00gE)
path_to_v588__00gG = DIAG_MULT(path_to_v589__00gI,pv589__00gI_pv588__00gG)
del path_to_v589__00gI

# op _00gB_power_combination_eval
# LANG: _00gA --> _00gC
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gB_power_combination_eval_pv586__00gC_pv585__00gA
temp_power = _00gB_coeff_temp*-1*(v585__00gA**-2.0)
pv586__00gC_pv585__00gA = temp_power.flatten()
path_to_v585__00gA = DIAG_MULT(path_to_v586__00gC,pv586__00gC_pv585__00gA)
del path_to_v586__00gC
del pv586__00gC_pv585__00gA

# op _00eu_power_combination_eval
# LANG: _00et --> _00ev
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00eu_power_combination_eval_pv515__00ev_pv514__00et
temp_power = _00eu_coeff_temp*1
pv515__00ev_pv514__00et = temp_power.flatten()
path_to_v514__00et = DIAG_MULT(path_to_v515__00ev,pv515__00ev_pv514__00et)
del path_to_v515__00ev
del pv515__00ev_pv514__00et

# op _00ek_linear_combination_eval
# LANG: _00eh, _00ej --> _00el
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00ek_linear_combination_eval_pv510__00el_pv509__00ej
path_to_v508__00eh = DIAG_MULT(path_to_v510__00el,pv510__00el_pv508__00eh)
path_to_v509__00ej = DIAG_MULT(path_to_v510__00el,pv510__00el_pv509__00ej)
del path_to_v510__00el

# op _00ea_power_combination_eval
# LANG: _00e9 --> _00eb
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00ea_power_combination_eval_pv505__00eb_pv504__00e9
temp_power = _00ea_coeff_temp*0.5*(v504__00e9**-0.5)
pv505__00eb_pv504__00e9 = temp_power.flatten()
path_to_v504__00e9 = DIAG_MULT(path_to_v505__00eb,pv505__00eb_pv504__00e9)
del path_to_v505__00eb
del pv505__00eb_pv504__00e9

# op _00e4_linear_combination_eval
# LANG: _00dU, _00dQ --> _00e5
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00e4_linear_combination_eval_pv502__00e5_pv494__00dQ
path_to_v496__00dU = DIAG_MULT(path_to_v502__00e5,pv502__00e5_pv496__00dU)
path_to_v494__00dQ = DIAG_MULT(path_to_v502__00e5,pv502__00e5_pv494__00dQ)
del path_to_v502__00e5

# op _00e0_power_combination_eval
# LANG: _00d_ --> _00e1
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00e0_power_combination_eval_pv500__00e1_pv499__00d_
temp_power = _00e0_coeff_temp*0.5*(v499__00d_**-0.5)
pv500__00e1_pv499__00d_ = temp_power.flatten()
path_to_v499__00d_ = DIAG_MULT(path_to_v500__00e1,pv500__00e1_pv499__00d_)
del path_to_v500__00e1
del pv500__00e1_pv499__00d_

# op _00dz_linear_combination_eval
# LANG: _00do, _00dy --> _00dA
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dz_linear_combination_eval_pv486__00dA_pv485__00dy
path_to_v480__00do = DIAG_MULT(path_to_v486__00dA,pv486__00dA_pv480__00do)
path_to_v485__00dy = DIAG_MULT(path_to_v486__00dA,pv486__00dA_pv485__00dy)
del path_to_v486__00dA

# op _00df_power_combination_eval
# LANG: _00d8, _00de --> _00dg
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00df_power_combination_eval_pv476__00dg_pv475__00de
temp_power = _00df_coeff_temp*1*(v475__00de**-1)
pv476__00dg_pv472__00d8 = temp_power.flatten()
temp_power = _00df_coeff_temp*(v472__00d8)*-1*(v475__00de**-2.0)
pv476__00dg_pv475__00de = temp_power.flatten()
path_to_v472__00d8 = DIAG_MULT(path_to_v476__00dg,pv476__00dg_pv472__00d8)
path_to_v475__00de = DIAG_MULT(path_to_v476__00dg,pv476__00dg_pv475__00de)
del pv476__00dg_pv475__00de
del pv476__00dg_pv472__00d8
del path_to_v476__00dg

# op _00dV_linear_combination_eval
# LANG: _00dS, _00dQ --> _00dW
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dV_linear_combination_eval_pv497__00dW_pv494__00dQ
path_to_v495__00dS = DIAG_MULT(path_to_v497__00dW,pv497__00dW_pv495__00dS)
path_to_v494__00dQ += DIAG_MULT(path_to_v497__00dW,pv497__00dW_pv494__00dQ)
del path_to_v497__00dW

# op _00d5_power_combination_eval
# LANG: _00cZ, _00d4 --> _00d6
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00d5_power_combination_eval_pv471__00d6_pv470__00d4
temp_power = _00d5_coeff_temp*1*(v470__00d4**-1)
pv471__00d6_pv467__00cZ = temp_power.flatten()
temp_power = _00d5_coeff_temp*(v467__00cZ)*-1*(v470__00d4**-2.0)
pv471__00d6_pv470__00d4 = temp_power.flatten()
path_to_v467__00cZ = DIAG_MULT(path_to_v471__00d6,pv471__00d6_pv467__00cZ)
path_to_v470__00d4 = DIAG_MULT(path_to_v471__00d6,pv471__00d6_pv470__00d4)
del pv471__00d6_pv467__00cZ
del path_to_v471__00d6
del pv471__00d6_pv470__00d4

# op _00ck_linear_combination_eval
# LANG: _00c9, _00cj --> _00cl
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00ck_linear_combination_eval_pv447__00cl_pv446__00cj
path_to_v441__00c9 = DIAG_MULT(path_to_v447__00cl,pv447__00cl_pv441__00c9)
path_to_v446__00cj = DIAG_MULT(path_to_v447__00cl,pv447__00cl_pv446__00cj)
del path_to_v447__00cl

# op _00cE_linear_combination_eval
# LANG: _00cD --> _00cF
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cE_linear_combination_eval_pv457__00cF_pv456__00cD
path_to_v456__00cD = DIAG_MULT(path_to_v457__00cF,pv457__00cF_pv456__00cD)
del path_to_v457__00cF

# op _00bn_linear_combination_eval
# LANG: _00bc, _00bm --> _00bo
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bn_linear_combination_eval_pv417__00bo_pv416__00bm
path_to_v411__00bc = DIAG_MULT(path_to_v417__00bo,pv417__00bo_pv411__00bc)
path_to_v416__00bm = DIAG_MULT(path_to_v417__00bo,pv417__00bo_pv416__00bm)
del path_to_v417__00bo

# op _00bH_linear_combination_eval
# LANG: _00bG --> _00bI
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bH_linear_combination_eval_pv427__00bI_pv426__00bG
path_to_v426__00bG = DIAG_MULT(path_to_v427__00bI,pv427__00bI_pv426__00bG)
del path_to_v427__00bI

# op _0090_linear_combination_eval
# LANG: _008Z, _008_ --> _0091
# SHAPES: (1, 50, 4, 3), (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal

# _0090_linear_combination_eval_pv338__0091_pv337__008_
path_to_v336__008Z = DIAG_MULT(path_to_v338__0091,pv338__0091_pv336__008Z)
path_to_v337__008_ = DIAG_MULT(path_to_v338__0091,pv338__0091_pv337__008_)
del path_to_v338__0091

# op _008X_linear_combination_eval
# LANG: _008V, _008W --> _008Y
# SHAPES: (1, 50, 4, 3), (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal

# _008X_linear_combination_eval_pv335__008Y_pv334__008W
path_to_v333__008V = DIAG_MULT(path_to_v335__008Y,pv335__008Y_pv333__008V)
path_to_v334__008W = DIAG_MULT(path_to_v335__008Y,pv335__008Y_pv334__008W)
del path_to_v335__008Y

# op _00hm_power_combination_eval
# LANG: _00go, _00g4 --> _00hn
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00hm_power_combination_eval_pv610__00hn_pv569__00g4
temp_power = _00hm_coeff_temp*(v569__00g4)*1
pv610__00hn_pv579__00go = temp_power.flatten()
temp_power = _00hm_coeff_temp*1*(v579__00go)
pv610__00hn_pv569__00g4 = temp_power.flatten()
path_to_v579__00go += DIAG_MULT(path_to_v610__00hn,pv610__00hn_pv579__00go)
path_to_v569__00g4 += DIAG_MULT(path_to_v610__00hn,pv610__00hn_pv569__00g4)
del pv610__00hn_pv579__00go
del path_to_v610__00hn
del pv610__00hn_pv569__00g4

# op _00hk_single_tensor_sum_with_axis_eval
# LANG: _00hj --> _00hl
# SHAPES: (1, 40000, 3) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00hk_single_tensor_sum_with_axis_eval_pv609__00hl_pv608__00hj
path_to_v608__00hj = STD_MULT(path_to_v609__00hl,pv609__00hl_pv608__00hj)
del path_to_v609__00hl

# op _00hI_power_combination_eval
# LANG: _00gi, _00fl --> _00hJ
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00hI_power_combination_eval_pv621__00hJ_pv546__00fl
temp_power = _00hI_coeff_temp*1*(v546__00fl)
pv621__00hJ_pv576__00gi = temp_power.flatten()
temp_power = _00hI_coeff_temp*(v576__00gi)*1
pv621__00hJ_pv546__00fl = temp_power.flatten()
path_to_v576__00gi += DIAG_MULT(path_to_v621__00hJ,pv621__00hJ_pv576__00gi)
path_to_v546__00fl += DIAG_MULT(path_to_v621__00hJ,pv621__00hJ_pv546__00fl)
del pv621__00hJ_pv546__00fl
del pv621__00hJ_pv576__00gi
del path_to_v621__00hJ

# op _00h4_power_combination_eval
# LANG: _00g4 --> _00h5
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00h4_power_combination_eval_pv601__00h5_pv569__00g4
temp_power = _00h4_coeff_temp*-1*(v569__00g4**-2.0)
pv601__00h5_pv569__00g4 = temp_power.flatten()
path_to_v569__00g4 += DIAG_MULT(path_to_v601__00h5,pv601__00h5_pv569__00g4)
del pv601__00h5_pv569__00g4
del path_to_v601__00h5

# op _00h2_power_combination_eval
# LANG: _00fL --> _00h3
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00h2_power_combination_eval_pv600__00h3_pv559__00fL
temp_power = _00h2_coeff_temp*-1*(v559__00fL**-2.0)
pv600__00h3_pv559__00fL = temp_power.flatten()
path_to_v559__00fL = DIAG_MULT(path_to_v600__00h3,pv600__00h3_pv559__00fL)
del path_to_v600__00h3
del pv600__00h3_pv559__00fL

# op _00gz_linear_combination_eval
# LANG: _00gy, _00gw --> _00gA
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gz_linear_combination_eval_pv585__00gA_pv583__00gw
path_to_v584__00gy = DIAG_MULT(path_to_v585__00gA,pv585__00gA_pv584__00gy)
path_to_v583__00gw = DIAG_MULT(path_to_v585__00gA,pv585__00gA_pv583__00gw)
del path_to_v585__00gA

# op _00gZ_linear_combination_eval
# LANG: _00gY, _00gW --> _00g_
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gZ_linear_combination_eval_pv598__00g__pv596__00gW
path_to_v597__00gY = DIAG_MULT(path_to_v598__00g_,pv598__00g__pv597__00gY)
path_to_v596__00gW = DIAG_MULT(path_to_v598__00g_,pv598__00g__pv596__00gW)
del path_to_v598__00g_

# op _00gF_power_combination_eval
# LANG: _00fL --> _00gG
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gF_power_combination_eval_pv588__00gG_pv559__00fL
temp_power = _00gF_coeff_temp*-1*(v559__00fL**-2.0)
pv588__00gG_pv559__00fL = temp_power.flatten()
path_to_v559__00fL += DIAG_MULT(path_to_v588__00gG,pv588__00gG_pv559__00fL)
del pv588__00gG_pv559__00fL
del path_to_v588__00gG

# op _00gD_power_combination_eval
# LANG: _00fr --> _00gE
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gD_power_combination_eval_pv587__00gE_pv549__00fr
temp_power = _00gD_coeff_temp*-1*(v549__00fr**-2.0)
pv587__00gE_pv549__00fr = temp_power.flatten()
path_to_v549__00fr += DIAG_MULT(path_to_v587__00gE,pv587__00gE_pv549__00fr)
del path_to_v587__00gE
del pv587__00gE_pv549__00fr

# op _00es_linear_combination_eval
# LANG: _00en, _00er --> _00et
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00es_linear_combination_eval_pv514__00et_pv513__00er
path_to_v511__00en = DIAG_MULT(path_to_v514__00et,pv514__00et_pv511__00en)
path_to_v513__00er = DIAG_MULT(path_to_v514__00et,pv514__00et_pv513__00er)
del path_to_v514__00et

# op _00ei_power_combination_eval
# LANG: _00dQ --> _00ej
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00ei_power_combination_eval_pv509__00ej_pv494__00dQ
temp_power = _00ei_coeff_temp*2*(v494__00dQ)
pv509__00ej_pv494__00dQ = temp_power.flatten()
path_to_v494__00dQ += DIAG_MULT(path_to_v509__00ej,pv509__00ej_pv494__00dQ)
del pv509__00ej_pv494__00dQ
del path_to_v509__00ej

# op _00eg_power_combination_eval
# LANG: _00dS, _00dU --> _00eh
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00eg_power_combination_eval_pv508__00eh_pv496__00dU
temp_power = _00eg_coeff_temp*1*(v496__00dU)
pv508__00eh_pv495__00dS = temp_power.flatten()
temp_power = _00eg_coeff_temp*(v495__00dS)*1
pv508__00eh_pv496__00dU = temp_power.flatten()
path_to_v495__00dS += DIAG_MULT(path_to_v508__00eh,pv508__00eh_pv495__00dS)
path_to_v496__00dU += DIAG_MULT(path_to_v508__00eh,pv508__00eh_pv496__00dU)
del path_to_v508__00eh
del pv508__00eh_pv496__00dU
del pv508__00eh_pv495__00dS

# op _00e8_linear_combination_eval
# LANG: _00e7 --> _00e9
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00e8_linear_combination_eval_pv504__00e9_pv503__00e7
path_to_v503__00e7 = DIAG_MULT(path_to_v504__00e9,pv504__00e9_pv503__00e7)
del path_to_v504__00e9

# op _00dx_power_combination_eval
# LANG: _00dw --> _00dy
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dx_power_combination_eval_pv485__00dy_pv484__00dw
temp_power = _00dx_coeff_temp*1
pv485__00dy_pv484__00dw = temp_power.flatten()
path_to_v484__00dw = DIAG_MULT(path_to_v485__00dy,pv485__00dy_pv484__00dw)
del pv485__00dy_pv484__00dw
del path_to_v485__00dy

# op _00dn_linear_combination_eval
# LANG: _00dk, _00dm --> _00do
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dn_linear_combination_eval_pv480__00do_pv479__00dm
path_to_v478__00dk = DIAG_MULT(path_to_v480__00do,pv480__00do_pv478__00dk)
path_to_v479__00dm = DIAG_MULT(path_to_v480__00do,pv480__00do_pv479__00dm)
del path_to_v480__00do

# op _00dd_power_combination_eval
# LANG: _00dc --> _00de
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dd_power_combination_eval_pv475__00de_pv474__00dc
temp_power = _00dd_coeff_temp*0.5*(v474__00dc**-0.5)
pv475__00de_pv474__00dc = temp_power.flatten()
path_to_v474__00dc = DIAG_MULT(path_to_v475__00de,pv475__00de_pv474__00dc)
del path_to_v475__00de
del pv475__00de_pv474__00dc

# op _00dZ_linear_combination_eval
# LANG: _00dY --> _00d_
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dZ_linear_combination_eval_pv499__00d__pv498__00dY
path_to_v498__00dY = DIAG_MULT(path_to_v499__00d_,pv499__00d__pv498__00dY)
del path_to_v499__00d_

# op _00d7_linear_combination_eval
# LANG: _00cX, _00cT --> _00d8
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00d7_linear_combination_eval_pv472__00d8_pv464__00cT
path_to_v466__00cX = DIAG_MULT(path_to_v472__00d8,pv472__00d8_pv466__00cX)
path_to_v464__00cT = DIAG_MULT(path_to_v472__00d8,pv472__00d8_pv464__00cT)
del path_to_v472__00d8

# op _00d3_power_combination_eval
# LANG: _00d2 --> _00d4
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00d3_power_combination_eval_pv470__00d4_pv469__00d2
temp_power = _00d3_coeff_temp*0.5*(v469__00d2**-0.5)
pv470__00d4_pv469__00d2 = temp_power.flatten()
path_to_v469__00d2 = DIAG_MULT(path_to_v470__00d4,pv470__00d4_pv469__00d2)
del pv470__00d4_pv469__00d2
del path_to_v470__00d4

# op _00ci_power_combination_eval
# LANG: _00cb, _00ch --> _00cj
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00ci_power_combination_eval_pv446__00cj_pv445__00ch
temp_power = _00ci_coeff_temp*1*(v445__00ch**-1)
pv446__00cj_pv442__00cb = temp_power.flatten()
temp_power = _00ci_coeff_temp*(v442__00cb)*-1*(v445__00ch**-2.0)
pv446__00cj_pv445__00ch = temp_power.flatten()
path_to_v442__00cb = DIAG_MULT(path_to_v446__00cj,pv446__00cj_pv442__00cb)
path_to_v445__00ch = DIAG_MULT(path_to_v446__00cj,pv446__00cj_pv445__00ch)
del pv446__00cj_pv442__00cb
del pv446__00cj_pv445__00ch
del path_to_v446__00cj

# op _00cY_linear_combination_eval
# LANG: _00cV, _00cT --> _00cZ
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cY_linear_combination_eval_pv467__00cZ_pv464__00cT
path_to_v465__00cV = DIAG_MULT(path_to_v467__00cZ,pv467__00cZ_pv465__00cV)
path_to_v464__00cT += DIAG_MULT(path_to_v467__00cZ,pv467__00cZ_pv464__00cT)
del path_to_v467__00cZ

# op _00cC_linear_combination_eval
# LANG: _00cr, _00cB --> _00cD
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cC_linear_combination_eval_pv456__00cD_pv455__00cB
path_to_v450__00cr = DIAG_MULT(path_to_v456__00cD,pv456__00cD_pv450__00cr)
path_to_v455__00cB = DIAG_MULT(path_to_v456__00cD,pv456__00cD_pv455__00cB)
del path_to_v456__00cD

# op _00c8_power_combination_eval
# LANG: _00c1, _00c7 --> _00c9
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00c8_power_combination_eval_pv441__00c9_pv440__00c7
temp_power = _00c8_coeff_temp*1*(v440__00c7**-1)
pv441__00c9_pv437__00c1 = temp_power.flatten()
temp_power = _00c8_coeff_temp*(v437__00c1)*-1*(v440__00c7**-2.0)
pv441__00c9_pv440__00c7 = temp_power.flatten()
path_to_v437__00c1 = DIAG_MULT(path_to_v441__00c9,pv441__00c9_pv437__00c1)
path_to_v440__00c7 = DIAG_MULT(path_to_v441__00c9,pv441__00c9_pv440__00c7)
del path_to_v441__00c9
del pv441__00c9_pv437__00c1
del pv441__00c9_pv440__00c7

# op _00bl_power_combination_eval
# LANG: _00be, _00bk --> _00bm
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bl_power_combination_eval_pv416__00bm_pv415__00bk
temp_power = _00bl_coeff_temp*1*(v415__00bk**-1)
pv416__00bm_pv412__00be = temp_power.flatten()
temp_power = _00bl_coeff_temp*(v412__00be)*-1*(v415__00bk**-2.0)
pv416__00bm_pv415__00bk = temp_power.flatten()
path_to_v412__00be = DIAG_MULT(path_to_v416__00bm,pv416__00bm_pv412__00be)
path_to_v415__00bk = DIAG_MULT(path_to_v416__00bm,pv416__00bm_pv415__00bk)
del path_to_v416__00bm
del pv416__00bm_pv412__00be
del pv416__00bm_pv415__00bk

# op _00bb_power_combination_eval
# LANG: _00b4, _00ba --> _00bc
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bb_power_combination_eval_pv411__00bc_pv410__00ba
temp_power = _00bb_coeff_temp*1*(v410__00ba**-1)
pv411__00bc_pv407__00b4 = temp_power.flatten()
temp_power = _00bb_coeff_temp*(v407__00b4)*-1*(v410__00ba**-2.0)
pv411__00bc_pv410__00ba = temp_power.flatten()
path_to_v407__00b4 = DIAG_MULT(path_to_v411__00bc,pv411__00bc_pv407__00b4)
path_to_v410__00ba = DIAG_MULT(path_to_v411__00bc,pv411__00bc_pv410__00ba)
del path_to_v411__00bc
del pv411__00bc_pv410__00ba
del pv411__00bc_pv407__00b4

# op _00bF_linear_combination_eval
# LANG: _00bu, _00bE --> _00bG
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bF_linear_combination_eval_pv426__00bG_pv425__00bE
path_to_v420__00bu = DIAG_MULT(path_to_v426__00bG,pv426__00bG_pv420__00bu)
path_to_v425__00bE = DIAG_MULT(path_to_v426__00bG,pv426__00bG_pv425__00bE)
del path_to_v426__00bG

# op _008U_decompose_eval
# LANG: eel --> _008_, _008V, _008W, _008Z
# SHAPES: (1, 51, 5, 3) --> (1, 50, 4, 3), (1, 50, 4, 3), (1, 50, 4, 3), (1, 50, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal

# _008U_decompose_eval_pv336__008Z_pv332_eel
path_to_v332_eel = STD_MULT(path_to_v337__008_,pv337__008__pv332_eel)
path_to_v332_eel += STD_MULT(path_to_v333__008V,pv333__008V_pv332_eel)
path_to_v332_eel += STD_MULT(path_to_v334__008W,pv334__008W_pv332_eel)
path_to_v332_eel += STD_MULT(path_to_v336__008Z,pv336__008Z_pv332_eel)
del path_to_v336__008Z
del path_to_v334__008W
del path_to_v333__008V
del path_to_v337__008_

# op _00hi_power_combination_eval
# LANG: _00gi, _00fZ --> _00hj
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00hi_power_combination_eval_pv608__00hj_pv566__00fZ
temp_power = _00hi_coeff_temp*(v566__00fZ)*1
pv608__00hj_pv576__00gi = temp_power.flatten()
temp_power = _00hi_coeff_temp*1*(v576__00gi)
pv608__00hj_pv566__00fZ = temp_power.flatten()
path_to_v576__00gi += DIAG_MULT(path_to_v608__00hj,pv608__00hj_pv576__00gi)
path_to_v566__00fZ += DIAG_MULT(path_to_v608__00hj,pv608__00hj_pv566__00fZ)
del pv608__00hj_pv566__00fZ
del path_to_v608__00hj
del pv608__00hj_pv576__00gi

# op _00gx_power_combination_eval
# LANG: _00fr, _00fL --> _00gy
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gx_power_combination_eval_pv584__00gy_pv559__00fL
temp_power = _00gx_coeff_temp*1*(v559__00fL)
pv584__00gy_pv549__00fr = temp_power.flatten()
temp_power = _00gx_coeff_temp*(v549__00fr)*1
pv584__00gy_pv559__00fL = temp_power.flatten()
path_to_v549__00fr += DIAG_MULT(path_to_v584__00gy,pv584__00gy_pv549__00fr)
path_to_v559__00fL += DIAG_MULT(path_to_v584__00gy,pv584__00gy_pv559__00fL)
del path_to_v584__00gy
del pv584__00gy_pv549__00fr
del pv584__00gy_pv559__00fL

# op _00gv_single_tensor_sum_with_axis_eval
# LANG: _00gu --> _00gw
# SHAPES: (1, 40000, 3) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gv_single_tensor_sum_with_axis_eval_pv583__00gw_pv582__00gu
path_to_v582__00gu = STD_MULT(path_to_v583__00gw,pv583__00gw_pv582__00gu)
del path_to_v583__00gw

# op _00gn_power_combination_eval
# LANG: _00gm --> _00go
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gn_power_combination_eval_pv579__00go_pv578__00gm
temp_power = _00gn_coeff_temp*0.5*(v578__00gm**-0.5)
pv579__00go_pv578__00gm = temp_power.flatten()
path_to_v578__00gm = DIAG_MULT(path_to_v579__00go,pv579__00go_pv578__00gm)
del path_to_v579__00go
del pv579__00go_pv578__00gm

# op _00gX_power_combination_eval
# LANG: _00g4, _00fL --> _00gY
# SHAPES: (1, 40000), (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gX_power_combination_eval_pv597__00gY_pv559__00fL
temp_power = _00gX_coeff_temp*(v559__00fL)*1
pv597__00gY_pv569__00g4 = temp_power.flatten()
temp_power = _00gX_coeff_temp*1*(v569__00g4)
pv597__00gY_pv559__00fL = temp_power.flatten()
path_to_v569__00g4 += DIAG_MULT(path_to_v597__00gY,pv597__00gY_pv569__00g4)
path_to_v559__00fL += DIAG_MULT(path_to_v597__00gY,pv597__00gY_pv559__00fL)
del pv597__00gY_pv569__00g4
del pv597__00gY_pv559__00fL
del path_to_v597__00gY

# op _00gV_single_tensor_sum_with_axis_eval
# LANG: _00gU --> _00gW
# SHAPES: (1, 40000, 3) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gV_single_tensor_sum_with_axis_eval_pv596__00gW_pv595__00gU
path_to_v595__00gU = STD_MULT(path_to_v596__00gW,pv596__00gW_pv595__00gU)
del path_to_v596__00gW

# op _00eq_power_combination_eval
# LANG: _00ep, _009U --> _00er
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00eq_power_combination_eval_pv513__00er_pv370__009U
temp_power = _00eq_coeff_temp*1*(v370__009U)
pv513__00er_pv512__00ep = temp_power.flatten()
temp_power = _00eq_coeff_temp*(v512__00ep)*1
pv513__00er_pv370__009U = temp_power.flatten()
path_to_v512__00ep = DIAG_MULT(path_to_v513__00er,pv513__00er_pv512__00ep)
path_to_v370__009U = DIAG_MULT(path_to_v513__00er,pv513__00er_pv370__009U)
del pv513__00er_pv512__00ep
del path_to_v513__00er
del pv513__00er_pv370__009U

# op _00em_linear_combination_eval
# LANG: _00dS, _00dU --> _00en
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00em_linear_combination_eval_pv511__00en_pv496__00dU
path_to_v495__00dS += DIAG_MULT(path_to_v511__00en,pv511__00en_pv495__00dS)
path_to_v496__00dU += DIAG_MULT(path_to_v511__00en,pv511__00en_pv496__00dU)
del path_to_v511__00en

# op _00e6_linear_combination_eval
# LANG: _00dU --> _00e7
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00e6_linear_combination_eval_pv503__00e7_pv496__00dU
path_to_v496__00dU += DIAG_MULT(path_to_v503__00e7,pv503__00e7_pv496__00dU)
del path_to_v503__00e7

# op _00dv_linear_combination_eval
# LANG: _00dq, _00du --> _00dw
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dv_linear_combination_eval_pv484__00dw_pv483__00du
path_to_v481__00dq = DIAG_MULT(path_to_v484__00dw,pv484__00dw_pv481__00dq)
path_to_v483__00du = DIAG_MULT(path_to_v484__00dw,pv484__00dw_pv483__00du)
del path_to_v484__00dw

# op _00dl_power_combination_eval
# LANG: _00cT --> _00dm
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dl_power_combination_eval_pv479__00dm_pv464__00cT
temp_power = _00dl_coeff_temp*2*(v464__00cT)
pv479__00dm_pv464__00cT = temp_power.flatten()
path_to_v464__00cT += DIAG_MULT(path_to_v479__00dm,pv479__00dm_pv464__00cT)
del path_to_v479__00dm
del pv479__00dm_pv464__00cT

# op _00dj_power_combination_eval
# LANG: _00cV, _00cX --> _00dk
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dj_power_combination_eval_pv478__00dk_pv466__00cX
temp_power = _00dj_coeff_temp*1*(v466__00cX)
pv478__00dk_pv465__00cV = temp_power.flatten()
temp_power = _00dj_coeff_temp*(v465__00cV)*1
pv478__00dk_pv466__00cX = temp_power.flatten()
path_to_v465__00cV += DIAG_MULT(path_to_v478__00dk,pv478__00dk_pv465__00cV)
path_to_v466__00cX += DIAG_MULT(path_to_v478__00dk,pv478__00dk_pv466__00cX)
del pv478__00dk_pv465__00cV
del pv478__00dk_pv466__00cX
del path_to_v478__00dk

# op _00db_linear_combination_eval
# LANG: _00da --> _00dc
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00db_linear_combination_eval_pv474__00dc_pv473__00da
path_to_v473__00da = DIAG_MULT(path_to_v474__00dc,pv474__00dc_pv473__00da)
del path_to_v474__00dc

# op _00dX_linear_combination_eval
# LANG: _00dS --> _00dY
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dX_linear_combination_eval_pv498__00dY_pv495__00dS
path_to_v495__00dS += DIAG_MULT(path_to_v498__00dY,pv498__00dY_pv495__00dS)
del path_to_v498__00dY

# op _00dP_single_tensor_sum_with_axis_eval
# LANG: _00dO --> _00dQ
# SHAPES: (1, 55200, 3) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dP_single_tensor_sum_with_axis_eval_pv494__00dQ_pv493__00dO
path_to_v493__00dO = STD_MULT(path_to_v494__00dQ,pv494__00dQ_pv493__00dO)
del path_to_v494__00dQ

# op _00d1_linear_combination_eval
# LANG: _00d0 --> _00d2
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00d1_linear_combination_eval_pv469__00d2_pv468__00d0
path_to_v468__00d0 = DIAG_MULT(path_to_v469__00d2,pv469__00d2_pv468__00d0)
del path_to_v469__00d2

# op _00cq_linear_combination_eval
# LANG: _00cn, _00cp --> _00cr
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cq_linear_combination_eval_pv450__00cr_pv449__00cp
path_to_v448__00cn = DIAG_MULT(path_to_v450__00cr,pv450__00cr_pv448__00cn)
path_to_v449__00cp = DIAG_MULT(path_to_v450__00cr,pv450__00cr_pv449__00cp)
del path_to_v450__00cr

# op _00cg_power_combination_eval
# LANG: _00cf --> _00ch
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cg_power_combination_eval_pv445__00ch_pv444__00cf
temp_power = _00cg_coeff_temp*0.5*(v444__00cf**-0.5)
pv445__00ch_pv444__00cf = temp_power.flatten()
path_to_v444__00cf = DIAG_MULT(path_to_v445__00ch,pv445__00ch_pv444__00cf)
del pv445__00ch_pv444__00cf
del path_to_v445__00ch

# op _00ca_linear_combination_eval
# LANG: _00b_, _00bW --> _00cb
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00ca_linear_combination_eval_pv442__00cb_pv434__00bW
path_to_v436__00b_ = DIAG_MULT(path_to_v442__00cb,pv442__00cb_pv436__00b_)
path_to_v434__00bW = DIAG_MULT(path_to_v442__00cb,pv442__00cb_pv434__00bW)
del path_to_v442__00cb

# op _00cA_power_combination_eval
# LANG: _00cz --> _00cB
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cA_power_combination_eval_pv455__00cB_pv454__00cz
temp_power = _00cA_coeff_temp*1
pv455__00cB_pv454__00cz = temp_power.flatten()
path_to_v454__00cz = DIAG_MULT(path_to_v455__00cB,pv455__00cB_pv454__00cz)
del pv455__00cB_pv454__00cz
del path_to_v455__00cB

# op _00c6_power_combination_eval
# LANG: _00c5 --> _00c7
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00c6_power_combination_eval_pv440__00c7_pv439__00c5
temp_power = _00c6_coeff_temp*0.5*(v439__00c5**-0.5)
pv440__00c7_pv439__00c5 = temp_power.flatten()
path_to_v439__00c5 = DIAG_MULT(path_to_v440__00c7,pv440__00c7_pv439__00c5)
del pv440__00c7_pv439__00c5
del path_to_v440__00c7

# op _00c0_linear_combination_eval
# LANG: _00bY, _00bW --> _00c1
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00c0_linear_combination_eval_pv437__00c1_pv434__00bW
path_to_v435__00bY = DIAG_MULT(path_to_v437__00c1,pv437__00c1_pv435__00bY)
path_to_v434__00bW += DIAG_MULT(path_to_v437__00c1,pv437__00c1_pv434__00bW)
del path_to_v437__00c1

# op _00bt_linear_combination_eval
# LANG: _00bq, _00bs --> _00bu
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bt_linear_combination_eval_pv420__00bu_pv419__00bs
path_to_v418__00bq = DIAG_MULT(path_to_v420__00bu,pv420__00bu_pv418__00bq)
path_to_v419__00bs = DIAG_MULT(path_to_v420__00bu,pv420__00bu_pv419__00bs)
del path_to_v420__00bu

# op _00bj_power_combination_eval
# LANG: _00bi --> _00bk
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bj_power_combination_eval_pv415__00bk_pv414__00bi
temp_power = _00bj_coeff_temp*0.5*(v414__00bi**-0.5)
pv415__00bk_pv414__00bi = temp_power.flatten()
path_to_v414__00bi = DIAG_MULT(path_to_v415__00bk,pv415__00bk_pv414__00bi)
del pv415__00bk_pv414__00bi
del path_to_v415__00bk

# op _00bd_linear_combination_eval
# LANG: _00b2, _00aZ --> _00be
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bd_linear_combination_eval_pv412__00be_pv404__00aZ
path_to_v406__00b2 = DIAG_MULT(path_to_v412__00be,pv412__00be_pv406__00b2)
path_to_v404__00aZ = DIAG_MULT(path_to_v412__00be,pv412__00be_pv404__00aZ)
del path_to_v412__00be

# op _00bD_power_combination_eval
# LANG: _00bC --> _00bE
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bD_power_combination_eval_pv425__00bE_pv424__00bC
temp_power = _00bD_coeff_temp*1
pv425__00bE_pv424__00bC = temp_power.flatten()
path_to_v424__00bC = DIAG_MULT(path_to_v425__00bE,pv425__00bE_pv424__00bC)
del path_to_v425__00bE
del pv425__00bE_pv424__00bC

# op _00b9_power_combination_eval
# LANG: _00b8 --> _00ba
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00b9_power_combination_eval_pv410__00ba_pv409__00b8
temp_power = _00b9_coeff_temp*0.5*(v409__00b8**-0.5)
pv410__00ba_pv409__00b8 = temp_power.flatten()
path_to_v409__00b8 = DIAG_MULT(path_to_v410__00ba,pv410__00ba_pv409__00b8)
del pv410__00ba_pv409__00b8
del path_to_v410__00ba

# op _00b3_linear_combination_eval
# LANG: _00b0, _00aZ --> _00b4
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00b3_linear_combination_eval_pv407__00b4_pv404__00aZ
path_to_v405__00b0 = DIAG_MULT(path_to_v407__00b4,pv407__00b4_pv405__00b0)
path_to_v404__00aZ += DIAG_MULT(path_to_v407__00b4,pv407__00b4_pv404__00aZ)
del path_to_v407__00b4

# op _00gt_power_combination_eval
# LANG: _00fl, _00fF --> _00gu
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gt_power_combination_eval_pv582__00gu_pv556__00fF
temp_power = _00gt_coeff_temp*1*(v556__00fF)
pv582__00gu_pv546__00fl = temp_power.flatten()
temp_power = _00gt_coeff_temp*(v546__00fl)*1
pv582__00gu_pv556__00fF = temp_power.flatten()
path_to_v546__00fl += DIAG_MULT(path_to_v582__00gu,pv582__00gu_pv546__00fl)
path_to_v556__00fF += DIAG_MULT(path_to_v582__00gu,pv582__00gu_pv556__00fF)
del pv582__00gu_pv546__00fl
del path_to_v582__00gu
del pv582__00gu_pv556__00fF

# op _00gl_single_tensor_sum_with_axis_eval
# LANG: _00gk --> _00gm
# SHAPES: (1, 40000, 3) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gl_single_tensor_sum_with_axis_eval_pv578__00gm_pv577__00gk
path_to_v577__00gk = STD_MULT(path_to_v578__00gm,pv578__00gm_pv577__00gk)
del path_to_v578__00gm

# op _00gT_power_combination_eval
# LANG: _00fZ, _00fF --> _00gU
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gT_power_combination_eval_pv595__00gU_pv556__00fF
temp_power = _00gT_coeff_temp*(v556__00fF)*1
pv595__00gU_pv566__00fZ = temp_power.flatten()
temp_power = _00gT_coeff_temp*1*(v566__00fZ)
pv595__00gU_pv556__00fF = temp_power.flatten()
path_to_v566__00fZ += DIAG_MULT(path_to_v595__00gU,pv595__00gU_pv566__00fZ)
path_to_v556__00fF += DIAG_MULT(path_to_v595__00gU,pv595__00gU_pv556__00fF)
del path_to_v595__00gU
del pv595__00gU_pv566__00fZ
del pv595__00gU_pv556__00fF

# op _00g3_power_combination_eval
# LANG: _00g2 --> _00g4
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00g3_power_combination_eval_pv569__00g4_pv568__00g2
temp_power = _00g3_coeff_temp*0.5*(v568__00g2**-0.5)
pv569__00g4_pv568__00g2 = temp_power.flatten()
path_to_v568__00g2 = DIAG_MULT(path_to_v569__00g4,pv569__00g4_pv568__00g2)
del path_to_v569__00g4
del pv569__00g4_pv568__00g2

# op _00fq_power_combination_eval
# LANG: _00fp --> _00fr
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fq_power_combination_eval_pv549__00fr_pv548__00fp
temp_power = _00fq_coeff_temp*0.5*(v548__00fp**-0.5)
pv549__00fr_pv548__00fp = temp_power.flatten()
path_to_v548__00fp = DIAG_MULT(path_to_v549__00fr,pv549__00fr_pv548__00fp)
del pv549__00fr_pv548__00fp
del path_to_v549__00fr

# op _00fK_power_combination_eval
# LANG: _00fJ --> _00fL
# SHAPES: (1, 40000) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fK_power_combination_eval_pv559__00fL_pv558__00fJ
temp_power = _00fK_coeff_temp*0.5*(v558__00fJ**-0.5)
pv559__00fL_pv558__00fJ = temp_power.flatten()
path_to_v558__00fJ = DIAG_MULT(path_to_v559__00fL,pv559__00fL_pv558__00fJ)
del path_to_v559__00fL
del pv559__00fL_pv558__00fJ

# op _00eo_power_combination_eval
# LANG: _00aR --> _00ep
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00eo_power_combination_eval_pv512__00ep_pv400__00aR
temp_power = _00eo_coeff_temp*1
pv512__00ep_pv400__00aR = temp_power.flatten()
path_to_v400__00aR = DIAG_MULT(path_to_v512__00ep,pv512__00ep_pv400__00aR)
del pv512__00ep_pv400__00aR
del path_to_v512__00ep

# op _00dt_power_combination_eval
# LANG: _00aR, _00ds --> _00du
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dt_power_combination_eval_pv483__00du_pv482__00ds
temp_power = _00dt_coeff_temp*(v482__00ds)*1
pv483__00du_pv400__00aR = temp_power.flatten()
temp_power = _00dt_coeff_temp*1*(v400__00aR)
pv483__00du_pv482__00ds = temp_power.flatten()
path_to_v400__00aR += DIAG_MULT(path_to_v483__00du,pv483__00du_pv400__00aR)
path_to_v482__00ds = DIAG_MULT(path_to_v483__00du,pv483__00du_pv482__00ds)
del pv483__00du_pv482__00ds
del path_to_v483__00du
del pv483__00du_pv400__00aR

# op _00dp_linear_combination_eval
# LANG: _00cV, _00cX --> _00dq
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dp_linear_combination_eval_pv481__00dq_pv466__00cX
path_to_v465__00cV += DIAG_MULT(path_to_v481__00dq,pv481__00dq_pv465__00cV)
path_to_v466__00cX += DIAG_MULT(path_to_v481__00dq,pv481__00dq_pv466__00cX)
del path_to_v481__00dq

# op _00dT_power_combination_eval
# LANG: _009U --> _00dU
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dT_power_combination_eval_pv496__00dU_pv370__009U
temp_power = _00dT_coeff_temp*2*(v370__009U)
pv496__00dU_pv370__009U = temp_power.flatten()
path_to_v370__009U += DIAG_MULT(path_to_v496__00dU,pv496__00dU_pv370__009U)
del path_to_v496__00dU
del pv496__00dU_pv370__009U

# op _00dR_power_combination_eval
# LANG: _00aR --> _00dS
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dR_power_combination_eval_pv495__00dS_pv400__00aR
temp_power = _00dR_coeff_temp*2*(v400__00aR)
pv495__00dS_pv400__00aR = temp_power.flatten()
path_to_v400__00aR += DIAG_MULT(path_to_v495__00dS,pv495__00dS_pv400__00aR)
del pv495__00dS_pv400__00aR
del path_to_v495__00dS

# op _00dN_power_combination_eval
# LANG: _00aL, _009O --> _00dO
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dN_power_combination_eval_pv493__00dO_pv367__009O
temp_power = _00dN_coeff_temp*1*(v367__009O)
pv493__00dO_pv397__00aL = temp_power.flatten()
temp_power = _00dN_coeff_temp*(v397__00aL)*1
pv493__00dO_pv367__009O = temp_power.flatten()
path_to_v397__00aL += DIAG_MULT(path_to_v493__00dO,pv493__00dO_pv397__00aL)
path_to_v367__009O += DIAG_MULT(path_to_v493__00dO,pv493__00dO_pv367__009O)
del path_to_v493__00dO
del pv493__00dO_pv367__009O
del pv493__00dO_pv397__00aL

# op _00d9_linear_combination_eval
# LANG: _00cX --> _00da
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00d9_linear_combination_eval_pv473__00da_pv466__00cX
path_to_v466__00cX += DIAG_MULT(path_to_v473__00da,pv473__00da_pv466__00cX)
del path_to_v473__00da

# op _00cy_linear_combination_eval
# LANG: _00ct, _00cx --> _00cz
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cy_linear_combination_eval_pv454__00cz_pv453__00cx
path_to_v451__00ct = DIAG_MULT(path_to_v454__00cz,pv454__00cz_pv451__00ct)
path_to_v453__00cx = DIAG_MULT(path_to_v454__00cz,pv454__00cz_pv453__00cx)
del path_to_v454__00cz

# op _00co_power_combination_eval
# LANG: _00bW --> _00cp
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00co_power_combination_eval_pv449__00cp_pv434__00bW
temp_power = _00co_coeff_temp*2*(v434__00bW)
pv449__00cp_pv434__00bW = temp_power.flatten()
path_to_v434__00bW += DIAG_MULT(path_to_v449__00cp,pv449__00cp_pv434__00bW)
del pv449__00cp_pv434__00bW
del path_to_v449__00cp

# op _00cm_power_combination_eval
# LANG: _00bY, _00b_ --> _00cn
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cm_power_combination_eval_pv448__00cn_pv436__00b_
temp_power = _00cm_coeff_temp*1*(v436__00b_)
pv448__00cn_pv435__00bY = temp_power.flatten()
temp_power = _00cm_coeff_temp*(v435__00bY)*1
pv448__00cn_pv436__00b_ = temp_power.flatten()
path_to_v435__00bY += DIAG_MULT(path_to_v448__00cn,pv448__00cn_pv435__00bY)
path_to_v436__00b_ += DIAG_MULT(path_to_v448__00cn,pv448__00cn_pv436__00b_)
del path_to_v448__00cn
del pv448__00cn_pv435__00bY
del pv448__00cn_pv436__00b_

# op _00ce_linear_combination_eval
# LANG: _00cd --> _00cf
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00ce_linear_combination_eval_pv444__00cf_pv443__00cd
path_to_v443__00cd = DIAG_MULT(path_to_v444__00cf,pv444__00cf_pv443__00cd)
del path_to_v444__00cf

# op _00c__linear_combination_eval
# LANG: _00cV --> _00d0
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00c__linear_combination_eval_pv468__00d0_pv465__00cV
path_to_v465__00cV += DIAG_MULT(path_to_v468__00d0,pv468__00d0_pv465__00cV)
del path_to_v468__00d0

# op _00cS_single_tensor_sum_with_axis_eval
# LANG: _00cR --> _00cT
# SHAPES: (1, 55200, 3) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cS_single_tensor_sum_with_axis_eval_pv464__00cT_pv463__00cR
path_to_v463__00cR = STD_MULT(path_to_v464__00cT,pv464__00cT_pv463__00cR)
del path_to_v464__00cT

# op _00c4_linear_combination_eval
# LANG: _00c3 --> _00c5
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00c4_linear_combination_eval_pv439__00c5_pv438__00c3
path_to_v438__00c3 = DIAG_MULT(path_to_v439__00c5,pv439__00c5_pv438__00c3)
del path_to_v439__00c5

# op _00br_power_combination_eval
# LANG: _00aZ --> _00bs
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00br_power_combination_eval_pv419__00bs_pv404__00aZ
temp_power = _00br_coeff_temp*2*(v404__00aZ)
pv419__00bs_pv404__00aZ = temp_power.flatten()
path_to_v404__00aZ += DIAG_MULT(path_to_v419__00bs,pv419__00bs_pv404__00aZ)
del path_to_v419__00bs
del pv419__00bs_pv404__00aZ

# op _00bp_power_combination_eval
# LANG: _00b0, _00b2 --> _00bq
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bp_power_combination_eval_pv418__00bq_pv406__00b2
temp_power = _00bp_coeff_temp*1*(v406__00b2)
pv418__00bq_pv405__00b0 = temp_power.flatten()
temp_power = _00bp_coeff_temp*(v405__00b0)*1
pv418__00bq_pv406__00b2 = temp_power.flatten()
path_to_v405__00b0 += DIAG_MULT(path_to_v418__00bq,pv418__00bq_pv405__00b0)
path_to_v406__00b2 += DIAG_MULT(path_to_v418__00bq,pv418__00bq_pv406__00b2)
del pv418__00bq_pv406__00b2
del pv418__00bq_pv405__00b0
del path_to_v418__00bq

# op _00bh_linear_combination_eval
# LANG: _00bg --> _00bi
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bh_linear_combination_eval_pv414__00bi_pv413__00bg
path_to_v413__00bg = DIAG_MULT(path_to_v414__00bi,pv414__00bi_pv413__00bg)
del path_to_v414__00bi

# op _00bB_linear_combination_eval
# LANG: _00bw, _00bA --> _00bC
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bB_linear_combination_eval_pv424__00bC_pv423__00bA
path_to_v421__00bw = DIAG_MULT(path_to_v424__00bC,pv424__00bC_pv421__00bw)
path_to_v423__00bA = DIAG_MULT(path_to_v424__00bC,pv424__00bC_pv423__00bA)
del path_to_v424__00bC

# op _00b7_linear_combination_eval
# LANG: _00b6 --> _00b8
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00b7_linear_combination_eval_pv409__00b8_pv408__00b6
path_to_v408__00b6 = DIAG_MULT(path_to_v409__00b8,pv409__00b8_pv408__00b6)
del path_to_v409__00b8

# op _00gj_power_combination_eval
# LANG: _00gi --> _00gk
# SHAPES: (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gj_power_combination_eval_pv577__00gk_pv576__00gi
temp_power = _00gj_coeff_temp*2*(v576__00gi)
pv577__00gk_pv576__00gi = temp_power.flatten()
path_to_v576__00gi += DIAG_MULT(path_to_v577__00gk,pv577__00gk_pv576__00gi)
del pv577__00gk_pv576__00gi
del path_to_v577__00gk

# op _00g1_single_tensor_sum_with_axis_eval
# LANG: _00g0 --> _00g2
# SHAPES: (1, 40000, 3) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00g1_single_tensor_sum_with_axis_eval_pv568__00g2_pv567__00g0
path_to_v567__00g0 = STD_MULT(path_to_v568__00g2,pv568__00g2_pv567__00g0)
del path_to_v568__00g2

# op _00fo_single_tensor_sum_with_axis_eval
# LANG: _00fn --> _00fp
# SHAPES: (1, 40000, 3) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fo_single_tensor_sum_with_axis_eval_pv548__00fp_pv547__00fn
path_to_v547__00fn = STD_MULT(path_to_v548__00fp,pv548__00fp_pv547__00fn)
del path_to_v548__00fp

# op _00fI_single_tensor_sum_with_axis_eval
# LANG: _00fH --> _00fJ
# SHAPES: (1, 40000, 3) --> (1, 40000)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fI_single_tensor_sum_with_axis_eval_pv558__00fJ_pv557__00fH
path_to_v557__00fH = STD_MULT(path_to_v558__00fJ,pv558__00fJ_pv557__00fH)
del path_to_v558__00fJ

# op _00dr_power_combination_eval
# LANG: _00ax --> _00ds
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00dr_power_combination_eval_pv482__00ds_pv390__00ax
temp_power = _00dr_coeff_temp*1
pv482__00ds_pv390__00ax = temp_power.flatten()
path_to_v390__00ax = DIAG_MULT(path_to_v482__00ds,pv482__00ds_pv390__00ax)
del pv482__00ds_pv390__00ax
del path_to_v482__00ds

# op _00cw_power_combination_eval
# LANG: _00ax, _00cv --> _00cx
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cw_power_combination_eval_pv453__00cx_pv452__00cv
temp_power = _00cw_coeff_temp*(v452__00cv)*1
pv453__00cx_pv390__00ax = temp_power.flatten()
temp_power = _00cw_coeff_temp*1*(v390__00ax)
pv453__00cx_pv452__00cv = temp_power.flatten()
path_to_v390__00ax += DIAG_MULT(path_to_v453__00cx,pv453__00cx_pv390__00ax)
path_to_v452__00cv = DIAG_MULT(path_to_v453__00cx,pv453__00cx_pv452__00cv)
del pv453__00cx_pv390__00ax
del path_to_v453__00cx
del pv453__00cx_pv452__00cv

# op _00cs_linear_combination_eval
# LANG: _00bY, _00b_ --> _00ct
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cs_linear_combination_eval_pv451__00ct_pv436__00b_
path_to_v435__00bY += DIAG_MULT(path_to_v451__00ct,pv451__00ct_pv435__00bY)
path_to_v436__00b_ += DIAG_MULT(path_to_v451__00ct,pv451__00ct_pv436__00b_)
del path_to_v451__00ct

# op _00cc_linear_combination_eval
# LANG: _00b_ --> _00cd
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cc_linear_combination_eval_pv443__00cd_pv436__00b_
path_to_v436__00b_ += DIAG_MULT(path_to_v443__00cd,pv443__00cd_pv436__00b_)
del path_to_v443__00cd

# op _00cW_power_combination_eval
# LANG: _00aR --> _00cX
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cW_power_combination_eval_pv466__00cX_pv400__00aR
temp_power = _00cW_coeff_temp*2*(v400__00aR)
pv466__00cX_pv400__00aR = temp_power.flatten()
path_to_v400__00aR += DIAG_MULT(path_to_v466__00cX,pv466__00cX_pv400__00aR)
del pv466__00cX_pv400__00aR
del path_to_v466__00cX

# op _00cU_power_combination_eval
# LANG: _00ax --> _00cV
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cU_power_combination_eval_pv465__00cV_pv390__00ax
temp_power = _00cU_coeff_temp*2*(v390__00ax)
pv465__00cV_pv390__00ax = temp_power.flatten()
path_to_v390__00ax += DIAG_MULT(path_to_v465__00cV,pv465__00cV_pv390__00ax)
del pv465__00cV_pv390__00ax
del path_to_v465__00cV

# op _00cQ_power_combination_eval
# LANG: _00aL, _00ar --> _00cR
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cQ_power_combination_eval_pv463__00cR_pv387__00ar
temp_power = _00cQ_coeff_temp*(v387__00ar)*1
pv463__00cR_pv397__00aL = temp_power.flatten()
temp_power = _00cQ_coeff_temp*1*(v397__00aL)
pv463__00cR_pv387__00ar = temp_power.flatten()
path_to_v397__00aL += DIAG_MULT(path_to_v463__00cR,pv463__00cR_pv397__00aL)
path_to_v387__00ar += DIAG_MULT(path_to_v463__00cR,pv463__00cR_pv387__00ar)
del pv463__00cR_pv387__00ar
del path_to_v463__00cR
del pv463__00cR_pv397__00aL

# op _00c2_linear_combination_eval
# LANG: _00bY --> _00c3
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00c2_linear_combination_eval_pv438__00c3_pv435__00bY
path_to_v435__00bY += DIAG_MULT(path_to_v438__00c3,pv438__00c3_pv435__00bY)
del path_to_v438__00c3

# op _00bz_power_combination_eval
# LANG: _00ad, _00by --> _00bA
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bz_power_combination_eval_pv423__00bA_pv422__00by
temp_power = _00bz_coeff_temp*(v422__00by)*1
pv423__00bA_pv380__00ad = temp_power.flatten()
temp_power = _00bz_coeff_temp*1*(v380__00ad)
pv423__00bA_pv422__00by = temp_power.flatten()
path_to_v380__00ad = DIAG_MULT(path_to_v423__00bA,pv423__00bA_pv380__00ad)
path_to_v422__00by = DIAG_MULT(path_to_v423__00bA,pv423__00bA_pv422__00by)
del pv423__00bA_pv422__00by
del pv423__00bA_pv380__00ad
del path_to_v423__00bA

# op _00bv_linear_combination_eval
# LANG: _00b0, _00b2 --> _00bw
# SHAPES: (1, 55200), (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bv_linear_combination_eval_pv421__00bw_pv406__00b2
path_to_v405__00b0 += DIAG_MULT(path_to_v421__00bw,pv421__00bw_pv405__00b0)
path_to_v406__00b2 += DIAG_MULT(path_to_v421__00bw,pv421__00bw_pv406__00b2)
del path_to_v421__00bw

# op _00bf_linear_combination_eval
# LANG: _00b2 --> _00bg
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bf_linear_combination_eval_pv413__00bg_pv406__00b2
path_to_v406__00b2 += DIAG_MULT(path_to_v413__00bg,pv413__00bg_pv406__00b2)
del path_to_v413__00bg

# op _00bV_single_tensor_sum_with_axis_eval
# LANG: _00bU --> _00bW
# SHAPES: (1, 55200, 3) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bV_single_tensor_sum_with_axis_eval_pv434__00bW_pv433__00bU
path_to_v433__00bU = STD_MULT(path_to_v434__00bW,pv434__00bW_pv433__00bU)
del path_to_v434__00bW

# op _00b5_linear_combination_eval
# LANG: _00b0 --> _00b6
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00b5_linear_combination_eval_pv408__00b6_pv405__00b0
path_to_v405__00b0 += DIAG_MULT(path_to_v408__00b6,pv408__00b6_pv405__00b0)
del path_to_v408__00b6

# op _00aY_single_tensor_sum_with_axis_eval
# LANG: _00aX --> _00aZ
# SHAPES: (1, 55200, 3) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00aY_single_tensor_sum_with_axis_eval_pv404__00aZ_pv403__00aX
path_to_v403__00aX = STD_MULT(path_to_v404__00aZ,pv404__00aZ_pv403__00aX)
del path_to_v404__00aZ

# op _00gh_linear_combination_eval
# LANG: _00ga, _00gg --> _00gi
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gh_linear_combination_eval_pv576__00gi_pv575__00gg
path_to_v572__00ga = DIAG_MULT(path_to_v576__00gi,pv576__00gi_pv572__00ga)
path_to_v575__00gg = DIAG_MULT(path_to_v576__00gi,pv576__00gi_pv575__00gg)
del path_to_v576__00gi

# op _00fm_power_combination_eval
# LANG: _00fl --> _00fn
# SHAPES: (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fm_power_combination_eval_pv547__00fn_pv546__00fl
temp_power = _00fm_coeff_temp*2*(v546__00fl)
pv547__00fn_pv546__00fl = temp_power.flatten()
path_to_v546__00fl += DIAG_MULT(path_to_v547__00fn,pv547__00fn_pv546__00fl)
del path_to_v547__00fn
del pv547__00fn_pv546__00fl

# op _00f__power_combination_eval
# LANG: _00fZ --> _00g0
# SHAPES: (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00f__power_combination_eval_pv567__00g0_pv566__00fZ
temp_power = _00f__coeff_temp*2*(v566__00fZ)
pv567__00g0_pv566__00fZ = temp_power.flatten()
path_to_v566__00fZ += DIAG_MULT(path_to_v567__00g0,pv567__00g0_pv566__00fZ)
del path_to_v567__00g0
del pv567__00g0_pv566__00fZ

# op _00fG_power_combination_eval
# LANG: _00fF --> _00fH
# SHAPES: (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fG_power_combination_eval_pv557__00fH_pv556__00fF
temp_power = _00fG_coeff_temp*2*(v556__00fF)
pv557__00fH_pv556__00fF = temp_power.flatten()
path_to_v556__00fF += DIAG_MULT(path_to_v557__00fH,pv557__00fH_pv556__00fF)
del pv557__00fH_pv556__00fF
del path_to_v557__00fH

# op _00cu_power_combination_eval
# LANG: _00ad --> _00cv
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00cu_power_combination_eval_pv452__00cv_pv380__00ad
temp_power = _00cu_coeff_temp*1
pv452__00cv_pv380__00ad = temp_power.flatten()
path_to_v380__00ad += DIAG_MULT(path_to_v452__00cv,pv452__00cv_pv380__00ad)
del path_to_v452__00cv
del pv452__00cv_pv380__00ad

# op _00bx_power_combination_eval
# LANG: _009U --> _00by
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bx_power_combination_eval_pv422__00by_pv370__009U
temp_power = _00bx_coeff_temp*1
pv422__00by_pv370__009U = temp_power.flatten()
path_to_v370__009U += DIAG_MULT(path_to_v422__00by,pv422__00by_pv370__009U)
del path_to_v422__00by
del pv422__00by_pv370__009U

# op _00bZ_power_combination_eval
# LANG: _00ax --> _00b_
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bZ_power_combination_eval_pv436__00b__pv390__00ax
temp_power = _00bZ_coeff_temp*2*(v390__00ax)
pv436__00b__pv390__00ax = temp_power.flatten()
path_to_v390__00ax += DIAG_MULT(path_to_v436__00b_,pv436__00b__pv390__00ax)
del path_to_v436__00b_
del pv436__00b__pv390__00ax

# op _00bX_power_combination_eval
# LANG: _00ad --> _00bY
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bX_power_combination_eval_pv435__00bY_pv380__00ad
temp_power = _00bX_coeff_temp*2*(v380__00ad)
pv435__00bY_pv380__00ad = temp_power.flatten()
path_to_v380__00ad += DIAG_MULT(path_to_v435__00bY,pv435__00bY_pv380__00ad)
del path_to_v435__00bY
del pv435__00bY_pv380__00ad

# op _00bT_power_combination_eval
# LANG: _00ar, _00a7 --> _00bU
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00bT_power_combination_eval_pv433__00bU_pv377__00a7
temp_power = _00bT_coeff_temp*(v377__00a7)*1
pv433__00bU_pv387__00ar = temp_power.flatten()
temp_power = _00bT_coeff_temp*1*(v387__00ar)
pv433__00bU_pv377__00a7 = temp_power.flatten()
path_to_v387__00ar += DIAG_MULT(path_to_v433__00bU,pv433__00bU_pv387__00ar)
path_to_v377__00a7 += DIAG_MULT(path_to_v433__00bU,pv433__00bU_pv377__00a7)
del path_to_v433__00bU
del pv433__00bU_pv387__00ar
del pv433__00bU_pv377__00a7

# op _00b1_power_combination_eval
# LANG: _00ad --> _00b2
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00b1_power_combination_eval_pv406__00b2_pv380__00ad
temp_power = _00b1_coeff_temp*2*(v380__00ad)
pv406__00b2_pv380__00ad = temp_power.flatten()
path_to_v380__00ad += DIAG_MULT(path_to_v406__00b2,pv406__00b2_pv380__00ad)
del pv406__00b2_pv380__00ad
del path_to_v406__00b2

# op _00a__power_combination_eval
# LANG: _009U --> _00b0
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00a__power_combination_eval_pv405__00b0_pv370__009U
temp_power = _00a__coeff_temp*2*(v370__009U)
pv405__00b0_pv370__009U = temp_power.flatten()
path_to_v370__009U += DIAG_MULT(path_to_v405__00b0,pv405__00b0_pv370__009U)
del path_to_v405__00b0
del pv405__00b0_pv370__009U

# op _00aW_power_combination_eval
# LANG: _009O, _00a7 --> _00aX
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00aW_power_combination_eval_pv403__00aX_pv377__00a7
temp_power = _00aW_coeff_temp*1*(v377__00a7)
pv403__00aX_pv367__009O = temp_power.flatten()
temp_power = _00aW_coeff_temp*(v367__009O)*1
pv403__00aX_pv377__00a7 = temp_power.flatten()
path_to_v367__009O += DIAG_MULT(path_to_v403__00aX,pv403__00aX_pv367__009O)
path_to_v377__00a7 += DIAG_MULT(path_to_v403__00aX,pv403__00aX_pv377__00a7)
del path_to_v403__00aX
del pv403__00aX_pv367__009O
del pv403__00aX_pv377__00a7

# op _00aQ_power_combination_eval
# LANG: _00aP --> _00aR
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00aQ_power_combination_eval_pv400__00aR_pv399__00aP
temp_power = _00aQ_coeff_temp*0.5*(v399__00aP**-0.5)
pv400__00aR_pv399__00aP = temp_power.flatten()
path_to_v399__00aP = DIAG_MULT(path_to_v400__00aR,pv400__00aR_pv399__00aP)
del path_to_v400__00aR
del pv400__00aR_pv399__00aP

# op _00gf reshape_eval
# LANG: _00ge --> _00gg
# SHAPES: (1, 200, 200, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gf reshape_eval_pv575__00gg_pv574__00ge
path_to_v574__00ge = DIAG_MULT(path_to_v575__00gg,pv575__00gg_pv574__00ge)
del path_to_v575__00gg

# op _00g9 reshape_eval
# LANG: _00g8 --> _00ga
# SHAPES: (1, 200, 200, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00g9 reshape_eval_pv572__00ga_pv571__00g8
path_to_v571__00g8 = DIAG_MULT(path_to_v572__00ga,pv572__00ga_pv571__00g8)
del path_to_v572__00ga

# op _00fk_linear_combination_eval
# LANG: _00fd, _00fj --> _00fl
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fk_linear_combination_eval_pv546__00fl_pv545__00fj
path_to_v542__00fd = DIAG_MULT(path_to_v546__00fl,pv546__00fl_pv542__00fd)
path_to_v545__00fj = DIAG_MULT(path_to_v546__00fl,pv546__00fl_pv545__00fj)
del path_to_v546__00fl

# op _00fY_linear_combination_eval
# LANG: _00fR, _00fX --> _00fZ
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fY_linear_combination_eval_pv566__00fZ_pv565__00fX
path_to_v562__00fR = DIAG_MULT(path_to_v566__00fZ,pv566__00fZ_pv562__00fR)
path_to_v565__00fX = DIAG_MULT(path_to_v566__00fZ,pv566__00fZ_pv565__00fX)
del path_to_v566__00fZ

# op _00fE_linear_combination_eval
# LANG: _00fx, _00fD --> _00fF
# SHAPES: (1, 40000, 3), (1, 40000, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fE_linear_combination_eval_pv556__00fF_pv555__00fD
path_to_v552__00fx = DIAG_MULT(path_to_v556__00fF,pv556__00fF_pv552__00fx)
path_to_v555__00fD = DIAG_MULT(path_to_v556__00fF,pv556__00fF_pv555__00fD)
del path_to_v556__00fF

# op _00aw_power_combination_eval
# LANG: _00av --> _00ax
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00aw_power_combination_eval_pv390__00ax_pv389__00av
temp_power = _00aw_coeff_temp*0.5*(v389__00av**-0.5)
pv390__00ax_pv389__00av = temp_power.flatten()
path_to_v389__00av = DIAG_MULT(path_to_v390__00ax,pv390__00ax_pv389__00av)
del path_to_v390__00ax
del pv390__00ax_pv389__00av

# op _00ac_power_combination_eval
# LANG: _00ab --> _00ad
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00ac_power_combination_eval_pv380__00ad_pv379__00ab
temp_power = _00ac_coeff_temp*0.5*(v379__00ab**-0.5)
pv380__00ad_pv379__00ab = temp_power.flatten()
path_to_v379__00ab = DIAG_MULT(path_to_v380__00ad,pv380__00ad_pv379__00ab)
del path_to_v380__00ad
del pv380__00ad_pv379__00ab

# op _00aO_single_tensor_sum_with_axis_eval
# LANG: _00aN --> _00aP
# SHAPES: (1, 55200, 3) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00aO_single_tensor_sum_with_axis_eval_pv399__00aP_pv398__00aN
path_to_v398__00aN = STD_MULT(path_to_v399__00aP,pv399__00aP_pv398__00aN)
del path_to_v399__00aP

# op _009T_power_combination_eval
# LANG: _009S --> _009U
# SHAPES: (1, 55200) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009T_power_combination_eval_pv370__009U_pv369__009S
temp_power = _009T_coeff_temp*0.5*(v369__009S**-0.5)
pv370__009U_pv369__009S = temp_power.flatten()
path_to_v369__009S = DIAG_MULT(path_to_v370__009U,pv370__009U_pv369__009S)
del path_to_v370__009U
del pv370__009U_pv369__009S

# op _00gd expand_array_eval
# LANG: _00gc --> _00ge
# SHAPES: (1, 200, 3) --> (1, 200, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gd expand_array_eval_pv574__00ge_pv573__00gc
path_to_v573__00gc = STD_MULT(path_to_v574__00ge,pv574__00ge_pv573__00gc)
del path_to_v574__00ge

# op _00g7 expand_array_eval
# LANG: _00g6 --> _00g8
# SHAPES: (1, 200, 3) --> (1, 200, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00g7 expand_array_eval_pv571__00g8_pv570__00g6
path_to_v570__00g6 = STD_MULT(path_to_v571__00g8,pv571__00g8_pv570__00g6)
del path_to_v571__00g8

# op _00fw reshape_eval
# LANG: _00fv --> _00fx
# SHAPES: (1, 200, 200, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fw reshape_eval_pv552__00fx_pv551__00fv
path_to_v551__00fv = DIAG_MULT(path_to_v552__00fx,pv552__00fx_pv551__00fv)
del path_to_v552__00fx

# op _00fi reshape_eval
# LANG: _00fh --> _00fj
# SHAPES: (1, 200, 200, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fi reshape_eval_pv545__00fj_pv544__00fh
path_to_v544__00fh = DIAG_MULT(path_to_v545__00fj,pv545__00fj_pv544__00fh)
del path_to_v545__00fj

# op _00fc reshape_eval
# LANG: _00fb --> _00fd
# SHAPES: (1, 200, 200, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fc reshape_eval_pv542__00fd_pv541__00fb
path_to_v541__00fb = DIAG_MULT(path_to_v542__00fd,pv542__00fd_pv541__00fb)
del path_to_v542__00fd

# op _00fW reshape_eval
# LANG: _00fV --> _00fX
# SHAPES: (1, 200, 200, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fW reshape_eval_pv565__00fX_pv564__00fV
path_to_v564__00fV = DIAG_MULT(path_to_v565__00fX,pv565__00fX_pv564__00fV)
del path_to_v565__00fX

# op _00fQ reshape_eval
# LANG: _00fP --> _00fR
# SHAPES: (1, 200, 200, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fQ reshape_eval_pv562__00fR_pv561__00fP
path_to_v561__00fP = DIAG_MULT(path_to_v562__00fR,pv562__00fR_pv561__00fP)
del path_to_v562__00fR

# op _00fC reshape_eval
# LANG: _00fB --> _00fD
# SHAPES: (1, 200, 200, 3) --> (1, 40000, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fC reshape_eval_pv555__00fD_pv554__00fB
path_to_v554__00fB = DIAG_MULT(path_to_v555__00fD,pv555__00fD_pv554__00fB)
del path_to_v555__00fD

# op _00au_single_tensor_sum_with_axis_eval
# LANG: _00at --> _00av
# SHAPES: (1, 55200, 3) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00au_single_tensor_sum_with_axis_eval_pv389__00av_pv388__00at
path_to_v388__00at = STD_MULT(path_to_v389__00av,pv389__00av_pv388__00at)
del path_to_v389__00av

# op _00aa_single_tensor_sum_with_axis_eval
# LANG: _00a9 --> _00ab
# SHAPES: (1, 55200, 3) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00aa_single_tensor_sum_with_axis_eval_pv379__00ab_pv378__00a9
path_to_v378__00a9 = STD_MULT(path_to_v379__00ab,pv379__00ab_pv378__00a9)
del path_to_v379__00ab

# op _00aM_power_combination_eval
# LANG: _00aL --> _00aN
# SHAPES: (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00aM_power_combination_eval_pv398__00aN_pv397__00aL
temp_power = _00aM_coeff_temp*2*(v397__00aL)
pv398__00aN_pv397__00aL = temp_power.flatten()
path_to_v397__00aL += DIAG_MULT(path_to_v398__00aN,pv398__00aN_pv397__00aL)
del pv398__00aN_pv397__00aL
del path_to_v398__00aN

# op _009R_single_tensor_sum_with_axis_eval
# LANG: _009Q --> _009S
# SHAPES: (1, 55200, 3) --> (1, 55200)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009R_single_tensor_sum_with_axis_eval_pv369__009S_pv368__009Q
path_to_v368__009Q = STD_MULT(path_to_v369__009S,pv369__009S_pv368__009Q)
del path_to_v369__009S

# op _00gb reshape_eval
# LANG: _00f7 --> _00gc
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00gb reshape_eval_pv573__00gc_pv539__00f7
path_to_v539__00f7 = DIAG_MULT(path_to_v573__00gc,pv573__00gc_pv539__00f7)
del path_to_v573__00gc

# op _00g5 reshape_eval
# LANG: eel_coll_pts_coords --> _00g6
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00g5 reshape_eval_pv570__00g6_pv534_eel_coll_pts_coords
path_to_v534_eel_coll_pts_coords += DIAG_MULT(path_to_v570__00g6,pv570__00g6_pv534_eel_coll_pts_coords)
del path_to_v570__00g6

# op _00fu expand_array_eval
# LANG: _00ft --> _00fv
# SHAPES: (1, 200, 3) --> (1, 200, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fu expand_array_eval_pv551__00fv_pv550__00ft
path_to_v550__00ft = STD_MULT(path_to_v551__00fv,pv551__00fv_pv550__00ft)
del path_to_v551__00fv

# op _00fg expand_array_eval
# LANG: _00ff --> _00fh
# SHAPES: (1, 200, 3) --> (1, 200, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fg expand_array_eval_pv544__00fh_pv543__00ff
path_to_v543__00ff = STD_MULT(path_to_v544__00fh,pv544__00fh_pv543__00ff)
del path_to_v544__00fh

# op _00fa expand_array_eval
# LANG: _00f9 --> _00fb
# SHAPES: (1, 200, 3) --> (1, 200, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fa expand_array_eval_pv541__00fb_pv540__00f9
path_to_v540__00f9 = STD_MULT(path_to_v541__00fb,pv541__00fb_pv540__00f9)
del path_to_v541__00fb

# op _00fU expand_array_eval
# LANG: _00fT --> _00fV
# SHAPES: (1, 200, 3) --> (1, 200, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fU expand_array_eval_pv564__00fV_pv563__00fT
path_to_v563__00fT = STD_MULT(path_to_v564__00fV,pv564__00fV_pv563__00fT)
del path_to_v564__00fV

# op _00fO expand_array_eval
# LANG: _00fN --> _00fP
# SHAPES: (1, 200, 3) --> (1, 200, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fO expand_array_eval_pv561__00fP_pv560__00fN
path_to_v560__00fN = STD_MULT(path_to_v561__00fP,pv561__00fP_pv560__00fN)
del path_to_v561__00fP

# op _00fA expand_array_eval
# LANG: _00fz --> _00fB
# SHAPES: (1, 200, 3) --> (1, 200, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fA expand_array_eval_pv554__00fB_pv553__00fz
path_to_v553__00fz = STD_MULT(path_to_v554__00fB,pv554__00fB_pv553__00fz)
del path_to_v554__00fB

# op _00as_power_combination_eval
# LANG: _00ar --> _00at
# SHAPES: (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00as_power_combination_eval_pv388__00at_pv387__00ar
temp_power = _00as_coeff_temp*2*(v387__00ar)
pv388__00at_pv387__00ar = temp_power.flatten()
path_to_v387__00ar += DIAG_MULT(path_to_v388__00at,pv388__00at_pv387__00ar)
del pv388__00at_pv387__00ar
del path_to_v388__00at

# op _00aK_linear_combination_eval
# LANG: _00aD, _00aJ --> _00aL
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00aK_linear_combination_eval_pv397__00aL_pv396__00aJ
path_to_v393__00aD = DIAG_MULT(path_to_v397__00aL,pv397__00aL_pv393__00aD)
path_to_v396__00aJ = DIAG_MULT(path_to_v397__00aL,pv397__00aL_pv396__00aJ)
del path_to_v397__00aL

# op _00a8_power_combination_eval
# LANG: _00a7 --> _00a9
# SHAPES: (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00a8_power_combination_eval_pv378__00a9_pv377__00a7
temp_power = _00a8_coeff_temp*2*(v377__00a7)
pv378__00a9_pv377__00a7 = temp_power.flatten()
path_to_v377__00a7 += DIAG_MULT(path_to_v378__00a9,pv378__00a9_pv377__00a7)
del path_to_v378__00a9
del pv378__00a9_pv377__00a7

# op _009P_power_combination_eval
# LANG: _009O --> _009Q
# SHAPES: (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009P_power_combination_eval_pv368__009Q_pv367__009O
temp_power = _009P_coeff_temp*2*(v367__009O)
pv368__009Q_pv367__009O = temp_power.flatten()
path_to_v367__009O += DIAG_MULT(path_to_v368__009Q,pv368__009Q_pv367__009O)
del path_to_v368__009Q
del pv368__009Q_pv367__009O

# op _00fy reshape_eval
# LANG: _00f5 --> _00fz
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fy reshape_eval_pv553__00fz_pv537__00f5
path_to_v537__00f5 = DIAG_MULT(path_to_v553__00fz,pv553__00fz_pv537__00f5)
del path_to_v553__00fz

# op _00fs reshape_eval
# LANG: eel_coll_pts_coords --> _00ft
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fs reshape_eval_pv550__00ft_pv534_eel_coll_pts_coords
path_to_v534_eel_coll_pts_coords += DIAG_MULT(path_to_v550__00ft,pv550__00ft_pv534_eel_coll_pts_coords)
del path_to_v550__00ft

# op _00fe reshape_eval
# LANG: _00f4 --> _00ff
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fe reshape_eval_pv543__00ff_pv536__00f4
path_to_v536__00f4 = DIAG_MULT(path_to_v543__00ff,pv543__00ff_pv536__00f4)
del path_to_v543__00ff

# op _00fS reshape_eval
# LANG: _00f6 --> _00fT
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fS reshape_eval_pv563__00fT_pv538__00f6
path_to_v538__00f6 = DIAG_MULT(path_to_v563__00fT,pv563__00fT_pv538__00f6)
del path_to_v563__00fT

# op _00fM reshape_eval
# LANG: eel_coll_pts_coords --> _00fN
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00fM reshape_eval_pv560__00fN_pv534_eel_coll_pts_coords
path_to_v534_eel_coll_pts_coords += DIAG_MULT(path_to_v560__00fN,pv560__00fN_pv534_eel_coll_pts_coords)
del path_to_v560__00fN

# op _00f8 reshape_eval
# LANG: eel_coll_pts_coords --> _00f9
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00f8 reshape_eval_pv540__00f9_pv534_eel_coll_pts_coords
path_to_v534_eel_coll_pts_coords += DIAG_MULT(path_to_v540__00f9,pv540__00f9_pv534_eel_coll_pts_coords)
del path_to_v540__00f9

# op _00aq_linear_combination_eval
# LANG: _00aj, _00ap --> _00ar
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00aq_linear_combination_eval_pv387__00ar_pv386__00ap
path_to_v383__00aj = DIAG_MULT(path_to_v387__00ar,pv387__00ar_pv383__00aj)
path_to_v386__00ap = DIAG_MULT(path_to_v387__00ar,pv387__00ar_pv386__00ap)
del path_to_v387__00ar

# op _00aI reshape_eval
# LANG: _00aH --> _00aJ
# SHAPES: (1, 200, 276, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00aI reshape_eval_pv396__00aJ_pv395__00aH
path_to_v395__00aH = DIAG_MULT(path_to_v396__00aJ,pv396__00aJ_pv395__00aH)
del path_to_v396__00aJ

# op _00aC reshape_eval
# LANG: _00aB --> _00aD
# SHAPES: (1, 200, 276, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00aC reshape_eval_pv393__00aD_pv392__00aB
path_to_v392__00aB = DIAG_MULT(path_to_v393__00aD,pv393__00aD_pv392__00aB)
del path_to_v393__00aD

# op _00a6_linear_combination_eval
# LANG: _009_, _00a5 --> _00a7
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00a6_linear_combination_eval_pv377__00a7_pv376__00a5
path_to_v373__009_ = DIAG_MULT(path_to_v377__00a7,pv377__00a7_pv373__009_)
path_to_v376__00a5 = DIAG_MULT(path_to_v377__00a7,pv377__00a7_pv376__00a5)
del path_to_v377__00a7

# op _009N_linear_combination_eval
# LANG: _009G, _009M --> _009O
# SHAPES: (1, 55200, 3), (1, 55200, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009N_linear_combination_eval_pv367__009O_pv366__009M
path_to_v363__009G = DIAG_MULT(path_to_v367__009O,pv367__009O_pv363__009G)
path_to_v366__009M = DIAG_MULT(path_to_v367__009O,pv367__009O_pv366__009M)
del path_to_v367__009O

# op _00f3_decompose_eval
# LANG: eel_bd_vtx_coords --> _00f4, _00f5, _00f6, _00f7
# SHAPES: (1, 51, 5, 3) --> (1, 50, 4, 3), (1, 50, 4, 3), (1, 50, 4, 3), (1, 50, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate

# _00f3_decompose_eval_pv539__00f7_pv535_eel_bd_vtx_coords
path_to_v535_eel_bd_vtx_coords += STD_MULT(path_to_v536__00f4,pv536__00f4_pv535_eel_bd_vtx_coords)
path_to_v535_eel_bd_vtx_coords += STD_MULT(path_to_v537__00f5,pv537__00f5_pv535_eel_bd_vtx_coords)
path_to_v535_eel_bd_vtx_coords += STD_MULT(path_to_v538__00f6,pv538__00f6_pv535_eel_bd_vtx_coords)
path_to_v535_eel_bd_vtx_coords += STD_MULT(path_to_v539__00f7,pv539__00f7_pv535_eel_bd_vtx_coords)
del path_to_v539__00f7
del path_to_v537__00f5
del path_to_v538__00f6
del path_to_v536__00f4

# op _00ao reshape_eval
# LANG: _00an --> _00ap
# SHAPES: (1, 200, 276, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00ao reshape_eval_pv386__00ap_pv385__00an
path_to_v385__00an = DIAG_MULT(path_to_v386__00ap,pv386__00ap_pv385__00an)
del path_to_v386__00ap

# op _00ai reshape_eval
# LANG: _00ah --> _00aj
# SHAPES: (1, 200, 276, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00ai reshape_eval_pv383__00aj_pv382__00ah
path_to_v382__00ah = DIAG_MULT(path_to_v383__00aj,pv383__00aj_pv382__00ah)
del path_to_v383__00aj

# op _00aG expand_array_eval
# LANG: _00aF --> _00aH
# SHAPES: (1, 276, 3) --> (1, 200, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00aG expand_array_eval_pv395__00aH_pv394__00aF
path_to_v394__00aF = STD_MULT(path_to_v395__00aH,pv395__00aH_pv394__00aF)
del path_to_v395__00aH

# op _00aA expand_array_eval
# LANG: _00az --> _00aB
# SHAPES: (1, 200, 3) --> (1, 200, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00aA expand_array_eval_pv392__00aB_pv391__00az
path_to_v391__00az = STD_MULT(path_to_v392__00aB,pv392__00aB_pv391__00az)
del path_to_v392__00aB

# op _00a4 reshape_eval
# LANG: _00a3 --> _00a5
# SHAPES: (1, 200, 276, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00a4 reshape_eval_pv376__00a5_pv375__00a3
path_to_v375__00a3 = DIAG_MULT(path_to_v376__00a5,pv376__00a5_pv375__00a3)
del path_to_v376__00a5

# op _009Z reshape_eval
# LANG: _009Y --> _009_
# SHAPES: (1, 200, 276, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009Z reshape_eval_pv373__009__pv372__009Y
path_to_v372__009Y = DIAG_MULT(path_to_v373__009_,pv373__009__pv372__009Y)
del path_to_v373__009_

# op _009L reshape_eval
# LANG: _009K --> _009M
# SHAPES: (1, 200, 276, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009L reshape_eval_pv366__009M_pv365__009K
path_to_v365__009K = DIAG_MULT(path_to_v366__009M,pv366__009M_pv365__009K)
del path_to_v366__009M

# op _009F reshape_eval
# LANG: _009E --> _009G
# SHAPES: (1, 200, 276, 3) --> (1, 55200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009F reshape_eval_pv363__009G_pv362__009E
path_to_v362__009E = DIAG_MULT(path_to_v363__009G,pv363__009G_pv362__009E)
del path_to_v363__009G

# op _00ay reshape_eval
# LANG: eel_coll_pts_coords --> _00az
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00ay reshape_eval_pv391__00az_pv534_eel_coll_pts_coords
path_to_v534_eel_coll_pts_coords += DIAG_MULT(path_to_v391__00az,pv391__00az_pv534_eel_coll_pts_coords)
del path_to_v391__00az

# op _00am expand_array_eval
# LANG: _00al --> _00an
# SHAPES: (1, 276, 3) --> (1, 200, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00am expand_array_eval_pv385__00an_pv384__00al
path_to_v384__00al = STD_MULT(path_to_v385__00an,pv385__00an_pv384__00al)
del path_to_v385__00an

# op _00ag expand_array_eval
# LANG: _00af --> _00ah
# SHAPES: (1, 200, 3) --> (1, 200, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00ag expand_array_eval_pv382__00ah_pv381__00af
path_to_v381__00af = STD_MULT(path_to_v382__00ah,pv382__00ah_pv381__00af)
del path_to_v382__00ah

# op _00aE reshape_eval
# LANG: _009A --> _00aF
# SHAPES: (1, 69, 4, 3) --> (1, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00aE reshape_eval_pv394__00aF_pv360__009A
path_to_v360__009A = DIAG_MULT(path_to_v394__00aF,pv394__00aF_pv360__009A)
del path_to_v394__00aF

# op _00a2 expand_array_eval
# LANG: _00a1 --> _00a3
# SHAPES: (1, 276, 3) --> (1, 200, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00a2 expand_array_eval_pv375__00a3_pv374__00a1
path_to_v374__00a1 = STD_MULT(path_to_v375__00a3,pv375__00a3_pv374__00a1)
del path_to_v375__00a3

# op _009X expand_array_eval
# LANG: _009W --> _009Y
# SHAPES: (1, 200, 3) --> (1, 200, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009X expand_array_eval_pv372__009Y_pv371__009W
path_to_v371__009W = STD_MULT(path_to_v372__009Y,pv372__009Y_pv371__009W)
del path_to_v372__009Y

# op _009J expand_array_eval
# LANG: _009I --> _009K
# SHAPES: (1, 276, 3) --> (1, 200, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009J expand_array_eval_pv365__009K_pv364__009I
path_to_v364__009I = STD_MULT(path_to_v365__009K,pv365__009K_pv364__009I)
del path_to_v365__009K

# op _009D expand_array_eval
# LANG: _009C --> _009E
# SHAPES: (1, 200, 3) --> (1, 200, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009D expand_array_eval_pv362__009E_pv361__009C
path_to_v361__009C = STD_MULT(path_to_v362__009E,pv362__009E_pv361__009C)
del path_to_v362__009E

# op _005E_indexed_passthrough_eval
# LANG: _005D, _005Y --> eel_bd_vtx_coords
# SHAPES: (1, 50, 5, 3), (1, 1, 5, 3) --> (1, 51, 5, 3)
# full namespace: MeshPreprocessing_comp

# _005E_indexed_passthrough_eval_pv535_eel_bd_vtx_coords_pv225__005Y
path_to_v213__005D = STD_MULT(path_to_v535_eel_bd_vtx_coords,pv535_eel_bd_vtx_coords_pv213__005D)
path_to_v225__005Y = STD_MULT(path_to_v535_eel_bd_vtx_coords,pv535_eel_bd_vtx_coords_pv225__005Y)
del path_to_v535_eel_bd_vtx_coords

# op _00ak reshape_eval
# LANG: _009z --> _00al
# SHAPES: (1, 69, 4, 3) --> (1, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00ak reshape_eval_pv384__00al_pv359__009z
path_to_v359__009z = DIAG_MULT(path_to_v384__00al,pv384__00al_pv359__009z)
del path_to_v384__00al

# op _00ae reshape_eval
# LANG: eel_coll_pts_coords --> _00af
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00ae reshape_eval_pv381__00af_pv534_eel_coll_pts_coords
path_to_v534_eel_coll_pts_coords += DIAG_MULT(path_to_v381__00af,pv381__00af_pv534_eel_coll_pts_coords)
del path_to_v381__00af

# op _00a0 reshape_eval
# LANG: _009y --> _00a1
# SHAPES: (1, 69, 4, 3) --> (1, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _00a0 reshape_eval_pv374__00a1_pv358__009y
path_to_v358__009y = DIAG_MULT(path_to_v374__00a1,pv374__00a1_pv358__009y)
del path_to_v374__00a1

# op _009V reshape_eval
# LANG: eel_coll_pts_coords --> _009W
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009V reshape_eval_pv371__009W_pv534_eel_coll_pts_coords
path_to_v534_eel_coll_pts_coords += DIAG_MULT(path_to_v371__009W,pv371__009W_pv534_eel_coll_pts_coords)
del path_to_v371__009W

# op _009H reshape_eval
# LANG: _009x --> _009I
# SHAPES: (1, 69, 4, 3) --> (1, 276, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009H reshape_eval_pv364__009I_pv357__009x
path_to_v357__009x = DIAG_MULT(path_to_v364__009I,pv364__009I_pv357__009x)
del path_to_v364__009I

# op _009B reshape_eval
# LANG: eel_coll_pts_coords --> _009C
# SHAPES: (1, 50, 4, 3) --> (1, 200, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009B reshape_eval_pv361__009C_pv534_eel_coll_pts_coords
path_to_v534_eel_coll_pts_coords += DIAG_MULT(path_to_v361__009C,pv361__009C_pv534_eel_coll_pts_coords)
del path_to_v361__009C

# op _005X_linear_combination_eval
# LANG: _005W, _005V --> _005Y
# SHAPES: (1, 1, 5, 3), (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: MeshPreprocessing_comp

# _005X_linear_combination_eval_pv225__005Y_pv223__005V
path_to_v224__005W = DIAG_MULT(path_to_v225__005Y,pv225__005Y_pv224__005W)
path_to_v223__005V = DIAG_MULT(path_to_v225__005Y,pv225__005Y_pv223__005V)
del path_to_v225__005Y

# op _005C_linear_combination_eval
# LANG: _005y, _005B --> _005D
# SHAPES: (1, 50, 5, 3), (1, 50, 5, 3) --> (1, 50, 5, 3)
# full namespace: MeshPreprocessing_comp

# _005C_linear_combination_eval_pv213__005D_pv212__005B
path_to_v210__005y = DIAG_MULT(path_to_v213__005D,pv213__005D_pv210__005y)
path_to_v212__005B = DIAG_MULT(path_to_v213__005D,pv213__005D_pv212__005B)
del path_to_v213__005D

# op _009w_decompose_eval
# LANG: eel_TE_wake_coords --> _009x, _009y, _009z, _009A
# SHAPES: (1, 70, 5, 3) --> (1, 69, 4, 3), (1, 69, 4, 3), (1, 69, 4, 3), (1, 69, 4, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate

# _009w_decompose_eval_pv360__009A_pv356_eel_TE_wake_coords
path_to_v356_eel_TE_wake_coords = STD_MULT(path_to_v357__009x,pv357__009x_pv356_eel_TE_wake_coords)
path_to_v356_eel_TE_wake_coords += STD_MULT(path_to_v358__009y,pv358__009y_pv356_eel_TE_wake_coords)
path_to_v356_eel_TE_wake_coords += STD_MULT(path_to_v359__009z,pv359__009z_pv356_eel_TE_wake_coords)
path_to_v356_eel_TE_wake_coords += STD_MULT(path_to_v360__009A,pv360__009A_pv356_eel_TE_wake_coords)
del path_to_v357__009x
del path_to_v358__009y
del path_to_v360__009A
del path_to_v359__009z

# op _006a_linear_combination_eval
# LANG: _0063, _0069 --> eel_coll_pts_coords
# SHAPES: (1, 50, 4, 3), (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: MeshPreprocessing_comp

# _006a_linear_combination_eval_pv534_eel_coll_pts_coords_pv233__0069
path_to_v229__0063 = DIAG_MULT(path_to_v534_eel_coll_pts_coords,pv534_eel_coll_pts_coords_pv229__0063)
path_to_v233__0069 = DIAG_MULT(path_to_v534_eel_coll_pts_coords,pv534_eel_coll_pts_coords_pv233__0069)
del path_to_v534_eel_coll_pts_coords

# op _005x_power_combination_eval
# LANG: _005w --> _005y
# SHAPES: (1, 50, 5, 3) --> (1, 50, 5, 3)
# full namespace: MeshPreprocessing_comp

# _005x_power_combination_eval_pv210__005y_pv209__005w
temp_power = _005x_coeff_temp*1
pv210__005y_pv209__005w = temp_power.flatten()
path_to_v209__005w = DIAG_MULT(path_to_v210__005y,pv210__005y_pv209__005w)
del path_to_v210__005y
del pv210__005y_pv209__005w

# op _005U expand_array_eval
# LANG: _005T --> _005V
# SHAPES: (1, 3) --> (1, 1, 5, 3)
# full namespace: MeshPreprocessing_comp

# _005U expand_array_eval_pv223__005V_pv222__005T
path_to_v222__005T = STD_MULT(path_to_v223__005V,pv223__005V_pv222__005T)
del path_to_v223__005V

# op _005A_power_combination_eval
# LANG: _005z --> _005B
# SHAPES: (1, 50, 5, 3) --> (1, 50, 5, 3)
# full namespace: MeshPreprocessing_comp

# _005A_power_combination_eval_pv212__005B_pv211__005z
temp_power = _005A_coeff_temp*1
pv212__005B_pv211__005z = temp_power.flatten()
path_to_v211__005z = DIAG_MULT(path_to_v212__005B,pv212__005B_pv211__005z)
del pv212__005B_pv211__005z
del path_to_v212__005B

# op _008f_indexed_passthrough_eval
# LANG: _008j, eel_wake_coords --> eel_TE_wake_coords
# SHAPES: (1, 1, 5, 3), (1, 69, 5, 3) --> (1, 70, 5, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group

# _008f_indexed_passthrough_eval_pv356_eel_TE_wake_coords_pv308_eel_wake_coords
path_to_v311__008j = STD_MULT(path_to_v356_eel_TE_wake_coords,pv356_eel_TE_wake_coords_pv311__008j)
path_to_v308_eel_wake_coords += STD_MULT(path_to_v356_eel_TE_wake_coords,pv356_eel_TE_wake_coords_pv308_eel_wake_coords)
del path_to_v356_eel_TE_wake_coords

# op _0068_power_combination_eval
# LANG: _0067 --> _0069
# SHAPES: (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: MeshPreprocessing_comp

# _0068_power_combination_eval_pv233__0069_pv232__0067
temp_power = _0068_coeff_temp*1
pv233__0069_pv232__0067 = temp_power.flatten()
path_to_v232__0067 = DIAG_MULT(path_to_v233__0069,pv233__0069_pv232__0067)
del pv233__0069_pv232__0067
del path_to_v233__0069

# op _0062_power_combination_eval
# LANG: _0061 --> _0063
# SHAPES: (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: MeshPreprocessing_comp

# _0062_power_combination_eval_pv229__0063_pv228__0061
temp_power = _0062_coeff_temp*1
pv229__0063_pv228__0061 = temp_power.flatten()
path_to_v228__0061 = DIAG_MULT(path_to_v229__0063,pv229__0063_pv228__0061)
del path_to_v229__0063
del pv229__0063_pv228__0061

# op _005S_power_combination_eval
# LANG: _005R --> _005T
# SHAPES: (1, 3) --> (1, 3)
# full namespace: MeshPreprocessing_comp

# _005S_power_combination_eval_pv222__005T_pv221__005R
temp_power = _005S_coeff_temp*1
pv222__005T_pv221__005R = temp_power.flatten()
path_to_v221__005R = DIAG_MULT(path_to_v222__005T,pv222__005T_pv221__005R)
del pv222__005T_pv221__005R
del path_to_v222__005T

# op _008i_power_combination_eval
# LANG: _008h --> _008j
# SHAPES: (1, 1, 5, 3) --> (1, 1, 5, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group

# _008i_power_combination_eval_pv311__008j_pv310__008h
temp_power = _008i_coeff_temp*1
pv311__008j_pv310__008h = temp_power.flatten()
path_to_v310__008h = DIAG_MULT(path_to_v311__008j,pv311__008j_pv310__008h)
del path_to_v311__008j
del pv311__008j_pv310__008h

# op _0066_linear_combination_eval
# LANG: _0065, _0064 --> _0067
# SHAPES: (1, 50, 4, 3), (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: MeshPreprocessing_comp

# _0066_linear_combination_eval_pv232__0067_pv230__0064
path_to_v231__0065 = DIAG_MULT(path_to_v232__0067,pv232__0067_pv231__0065)
path_to_v230__0064 = DIAG_MULT(path_to_v232__0067,pv232__0067_pv230__0064)
del path_to_v232__0067

# op _0060_linear_combination_eval
# LANG: _005Z, _005_ --> _0061
# SHAPES: (1, 50, 4, 3), (1, 50, 4, 3) --> (1, 50, 4, 3)
# full namespace: MeshPreprocessing_comp

# _0060_linear_combination_eval_pv228__0061_pv227__005_
path_to_v226__005Z = DIAG_MULT(path_to_v228__0061,pv228__0061_pv226__005Z)
path_to_v227__005_ = DIAG_MULT(path_to_v228__0061,pv228__0061_pv227__005_)
del path_to_v228__0061

# op _005Q_power_combination_eval
# LANG: fs --> _005R
# SHAPES: (1, 3) --> (1, 3)
# full namespace: MeshPreprocessing_comp

# _005Q_power_combination_eval_pv221__005R_pv216_fs
temp_power = _005Q_coeff_temp*1
pv221__005R_pv216_fs = temp_power.flatten()
path_to_v216_fs = DIAG_MULT(path_to_v221__005R,pv221__005R_pv216_fs)
del pv221__005R_pv216_fs
del path_to_v221__005R

# op _008g_decompose_eval
# LANG: eel_wake_coords --> _008h
# SHAPES: (1, 69, 5, 3) --> (1, 1, 5, 3)
# full namespace: solve_gamma_b_group.prepossing_before_Solve.RHS_group

# _008g_decompose_eval_pv310__008h_pv308_eel_wake_coords
path_to_v308_eel_wake_coords += STD_MULT(path_to_v310__008h,pv310__008h_pv308_eel_wake_coords)
del path_to_v310__008h

# op _005v_decompose_eval
# LANG: eel --> _0065, _005w, _005z, _005W, _005Z, _005_, _0064, _006n, _006o, _006U, _006X, _0071
# SHAPES: (1, 51, 5, 3) --> (1, 50, 4, 3), (1, 50, 5, 3), (1, 50, 5, 3), (1, 1, 5, 3), (1, 50, 4, 3), (1, 50, 4, 3), (1, 50, 4, 3), (1, 51, 4, 3), (1, 51, 4, 3), (1, 50, 4, 3), (1, 50, 4, 3), (1, 50, 4, 3)
# full namespace: MeshPreprocessing_comp

# _005v_decompose_eval_pv266__0071_pv332_eel
path_to_v332_eel += STD_MULT(path_to_v231__0065,pv231__0065_pv332_eel)
path_to_v332_eel += STD_MULT(path_to_v209__005w,pv209__005w_pv332_eel)
path_to_v332_eel += STD_MULT(path_to_v211__005z,pv211__005z_pv332_eel)
path_to_v332_eel += STD_MULT(path_to_v224__005W,pv224__005W_pv332_eel)
path_to_v332_eel += STD_MULT(path_to_v226__005Z,pv226__005Z_pv332_eel)
path_to_v332_eel += STD_MULT(path_to_v227__005_,pv227__005__pv332_eel)
path_to_v332_eel += STD_MULT(path_to_v230__0064,pv230__0064_pv332_eel)
del path_to_v231__0065
del path_to_v230__0064
del path_to_v227__005_
del path_to_v224__005W
del path_to_v226__005Z
del path_to_v209__005w
del path_to_v211__005z

# op _005M_indexed_passthrough_eval
# LANG: _005L, _005P, w --> fs
# SHAPES: (1, 1), (1, 1), (1, 1) --> (1, 3)
# full namespace: MeshPreprocessing_comp

# _005M_indexed_passthrough_eval_pv216_fs_pv215_w
path_to_v218__005L = STD_MULT(path_to_v216_fs,pv216_fs_pv218__005L)
path_to_v220__005P = STD_MULT(path_to_v216_fs,pv216_fs_pv220__005P)
path_to_v215_w = STD_MULT(path_to_v216_fs,pv216_fs_pv215_w)
del path_to_v216_fs

# op _005O_linear_combination_eval
# LANG: _005N --> _005P
# SHAPES: (1, 1) --> (1, 1)
# full namespace: MeshPreprocessing_comp

# _005O_linear_combination_eval_pv220__005P_pv219__005N
path_to_v219__005N = DIAG_MULT(path_to_v220__005P,pv220__005P_pv219__005N)
del path_to_v220__005P

# op _005K_linear_combination_eval
# LANG: _005J --> _005L
# SHAPES: (1, 1) --> (1, 1)
# full namespace: MeshPreprocessing_comp

# _005K_linear_combination_eval_pv218__005L_pv217__005J
path_to_v217__005J = DIAG_MULT(path_to_v218__005L,pv218__005L_pv217__005J)
del path_to_v218__005L

# op _005I_decompose_eval
# LANG: frame_vel --> _005N, _005J
# SHAPES: (1, 3) --> (1, 1), (1, 1)
# full namespace: MeshPreprocessing_comp

# _005I_decompose_eval_pv217__005J_pv644_frame_vel
path_to_v644_frame_vel += STD_MULT(path_to_v219__005N,pv219__005N_pv644_frame_vel)
path_to_v644_frame_vel += STD_MULT(path_to_v217__005J,pv217__005J_pv644_frame_vel)
del path_to_v219__005N
del path_to_v217__005J

# op _005n_indexed_passthrough_eval
# LANG: _005m, _005p --> frame_vel
# SHAPES: (1, 1), (1, 1) --> (1, 3)
# full namespace: adapter_comp

# _005n_indexed_passthrough_eval_pv644_frame_vel_pv204__005p
path_to_v203__005m = STD_MULT(path_to_v644_frame_vel,pv644_frame_vel_pv203__005m)
path_to_v204__005p = STD_MULT(path_to_v644_frame_vel,pv644_frame_vel_pv204__005p)
del path_to_v644_frame_vel

# op _005o_linear_combination_eval
# LANG: w --> _005p
# SHAPES: (1, 1) --> (1, 1)
# full namespace: adapter_comp

# _005o_linear_combination_eval_pv204__005p_pv215_w
path_to_v215_w += DIAG_MULT(path_to_v204__005p,pv204__005p_pv215_w)
del path_to_v204__005p

# op _005l_linear_combination_eval
# LANG: u --> _005m
# SHAPES: (1, 1) --> (1, 1)
# full namespace: adapter_comp

# _005l_linear_combination_eval_pv203__005m_pv179_u
path_to_v179_u = DIAG_MULT(path_to_v203__005m,pv203__005m_pv179_u)
del path_to_v203__005m
path_to_v179_u = path_to_v179_u.copy()
# path_to_v180_v = zero
path_to_v180_v = np.zeros((1,1))
# path_to_v185_theta = zero
path_to_v185_theta = np.zeros((1,1))
# path_to_v186_psi = zero
path_to_v186_psi = np.zeros((1,1))
# path_to_v187_gamma = zero
path_to_v187_gamma = np.zeros((1,1))
# path_to_v188_psiw = zero
path_to_v188_psiw = np.zeros((1,1))
path_to_v215_w = path_to_v215_w.copy()
path_to_v290_eel_gamma_w = path_to_v290_eel_gamma_w.copy()
path_to_v308_eel_wake_coords = path_to_v308_eel_wake_coords.copy()
path_to_v315_p = path_to_v315_p.copy()
path_to_v316_q = path_to_v316_q.copy()
path_to_v317_r = path_to_v317_r.copy()
path_to_v327_eel_coll_vel = path_to_v327_eel_coll_vel.copy()
path_to_v332_eel = path_to_v332_eel.copy()