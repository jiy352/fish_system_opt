

# RUN_MODEL_

# system evaluation block

# op _02BV_power_combination_eval
# LANG: a_coeff, L --> _02BW
# SHAPES: (1,), (1,) --> (1,)
# full namespace: EelGeometryModel
v5708__02BW = (v5706_a_coeff)*(v5730_L)
v5708__02BW = v5708__02BW.reshape((1,))

# op _02BZ expand_scalar_eval
# LANG: L --> _02B_
# SHAPES: (1,) --> (51,)
# full namespace: EelGeometryModel
v5710__02B_ = np.empty((51,))
v5710__02B_.fill(v5730_L.item())

# op _02C0_power_combination_eval
# LANG: _02B_ --> _02C1
# SHAPES: (51,) --> (51,)
# full namespace: EelGeometryModel
v5711__02C1 = (v5710__02B_)
v5711__02C1 = (v5711__02C1*_02C0_coeff).reshape((51,))

# op _02C2 expand_scalar_eval
# LANG: _02BW --> _02C3
# SHAPES: (1,) --> (51,)
# full namespace: EelGeometryModel
v5712__02C3 = np.empty((51,))
v5712__02C3.fill(v5708__02BW.item())

# op _02C6_linear_combination_eval
# LANG: _02C1, _02C3 --> _02C7
# SHAPES: (51,), (51,) --> (51,)
# full namespace: EelGeometryModel
v5714__02C7 = v5711__02C1+-1*v5712__02C3

# op _02C8_power_combination_eval
# LANG: _02C7, _02C3 --> _02C9
# SHAPES: (51,), (51,) --> (51,)
# full namespace: EelGeometryModel
v5715__02C9 = (v5714__02C7)*(v5712__02C3**-1)
v5715__02C9 = v5715__02C9.reshape((51,))

# op _02Ca_power_combination_eval
# LANG: _02C9 --> _02Cb
# SHAPES: (51,) --> (51,)
# full namespace: EelGeometryModel
v5716__02Cb = (v5715__02C9**2)
v5716__02Cb = v5716__02Cb.reshape((51,))

# op _02BX_power_combination_eval
# LANG: b_coeff, L --> _02BY
# SHAPES: (1,), (1,) --> (1,)
# full namespace: EelGeometryModel
v5709__02BY = (v5707_b_coeff)*(v5730_L)
v5709__02BY = v5709__02BY.reshape((1,))

# op _02Cc_linear_combination_eval
# LANG: _02Cb --> _02Cd
# SHAPES: (51,) --> (51,)
# full namespace: EelGeometryModel
v5717__02Cd = _02Cc_constant+-1*v5716__02Cb

# op _02C4 expand_scalar_eval
# LANG: _02BY --> _02C5
# SHAPES: (1,) --> (51,)
# full namespace: EelGeometryModel
v5713__02C5 = np.empty((51,))
v5713__02C5.fill(v5709__02BY.item())

# op _02Ce_power_combination_eval
# LANG: _02Cd --> _02Cf
# SHAPES: (51,) --> (51,)
# full namespace: EelGeometryModel
v5718__02Cf = (v5717__02Cd**0.5)
v5718__02Cf = v5718__02Cf.reshape((51,))

# op _02Cg_power_combination_eval
# LANG: _02C5, _02Cf --> eel_height
# SHAPES: (51,), (51,) --> (51,)
# full namespace: EelGeometryModel
v5719_eel_height = (v5713__02C5)*(v5718__02Cf)
v5719_eel_height = v5719_eel_height.reshape((51,))

# op _02Cl expand_array_eval
# LANG: eel_height --> _02Cm
# SHAPES: (51,) --> (51, 6)
# full namespace: EelGeometryModel
v5722__02Cm = np.einsum('a,b->ab', v5719_eel_height.reshape((51,)) ,np.ones((6,))).reshape((51, 6))

# op _02Cq_power_combination_eval
# LANG: _02Cm --> _02Cr
# SHAPES: (51, 6) --> (51, 6)
# full namespace: EelGeometryModel
v5724__02Cr = (v5722__02Cm)
v5724__02Cr = (v5724__02Cr*_02Cq_coeff).reshape((51, 6))

# op _02Cj expand_array_eval
# LANG: _02C1 --> _02Ck
# SHAPES: (51,) --> (51, 6)
# full namespace: EelGeometryModel
v5721__02Ck = np.einsum('a,b->ab', v5711__02C1.reshape((51,)) ,np.ones((6,))).reshape((51, 6))

# op _02Cs_power_combination_eval
# LANG: _02Cr --> _02Ct
# SHAPES: (51, 6) --> (51, 6)
# full namespace: EelGeometryModel
v5725__02Ct = (v5724__02Cr)
v5725__02Ct = (v5725__02Ct*_02Cs_coeff).reshape((51, 6))

# op _02Cn reshape_eval
# LANG: _02Ck --> _02Co
# SHAPES: (51, 6) --> (51, 6, 1)
# full namespace: EelGeometryModel
v5723__02Co = v5721__02Ck.reshape((51, 6, 1))

# op _02Cu reshape_eval
# LANG: _02Ct --> _02Cv
# SHAPES: (51, 6) --> (51, 6, 1)
# full namespace: EelGeometryModel
v5726__02Cv = v5725__02Ct.reshape((51, 6, 1))

# op _02Cp_indexed_passthrough_eval
# LANG: _02Co, _02Cv --> eel_rigid_mesh
# SHAPES: (51, 6, 1), (51, 6, 1) --> (51, 6, 3)
# full namespace: EelGeometryModel
v5735_eel_rigid_mesh__temp[i_v5723__02Co__02Cp_indexed_passthrough_eval] = v5723__02Co.flatten()
v5735_eel_rigid_mesh = v5735_eel_rigid_mesh__temp.copy()
v5735_eel_rigid_mesh__temp[i_v5726__02Cv__02Cp_indexed_passthrough_eval] = v5726__02Cv.flatten()
v5735_eel_rigid_mesh = v5735_eel_rigid_mesh__temp.copy()

# op _02CN_decompose_eval
# LANG: eel_rigid_mesh --> _02CO
# SHAPES: (51, 6, 3) --> (51, 1, 1)
# full namespace: EelKinematicsModel
v5738__02CO = ((v5735_eel_rigid_mesh.flatten())[src_indices__02CO__02CN]).reshape((51, 1, 1))

# op _02CS_decompose_eval
# LANG: eel_amplitude_cp --> _02CW, _02CT, _02CU, _02CV
# SHAPES: (4,) --> (1,), (1,), (1,), (1,)
# full namespace: EelKinematicsModel
v5741__02CT = ((v5740_eel_amplitude_cp.flatten())[src_indices__02CT__02CS]).reshape((1,))
v5742__02CU = ((v5740_eel_amplitude_cp.flatten())[src_indices__02CU__02CS]).reshape((1,))
v5743__02CV = ((v5740_eel_amplitude_cp.flatten())[src_indices__02CV__02CS]).reshape((1,))
v5744__02CW = ((v5740_eel_amplitude_cp.flatten())[src_indices__02CW__02CS]).reshape((1,))

# op _02CP reshape_eval
# LANG: _02CO --> _02CQ
# SHAPES: (51, 1, 1) --> (51,)
# full namespace: EelKinematicsModel
v5739__02CQ = v5738__02CO.reshape((51,))

# op _02CZ expand_scalar_eval
# LANG: _02CU --> _02C_
# SHAPES: (1,) --> (51,)
# full namespace: EelKinematicsModel
v5746__02C_ = np.empty((51,))
v5746__02C_.fill(v5742__02CU.item())

# op _02CX expand_scalar_eval
# LANG: _02CT --> _02CY
# SHAPES: (1,) --> (51,)
# full namespace: EelKinematicsModel
v5745__02CY = np.empty((51,))
v5745__02CY.fill(v5741__02CT.item())

# op _02D0 expand_scalar_eval
# LANG: _02CV --> _02D1
# SHAPES: (1,) --> (51,)
# full namespace: EelKinematicsModel
v5747__02D1 = np.empty((51,))
v5747__02D1.fill(v5743__02CV.item())

# op _02D7_power_combination_eval
# LANG: _02CQ, _02C_ --> _02D8
# SHAPES: (51,), (51,) --> (51,)
# full namespace: EelKinematicsModel
v5751__02D8 = (v5746__02C_)*(v5739__02CQ)
v5751__02D8 = v5751__02D8.reshape((51,))

# op _02Db_power_combination_eval
# LANG: _02CQ --> _02Dc
# SHAPES: (51,) --> (51,)
# full namespace: EelKinematicsModel
v5753__02Dc = (v5739__02CQ**2)
v5753__02Dc = v5753__02Dc.reshape((51,))

# op _02D9_linear_combination_eval
# LANG: _02CY, _02D8 --> _02Da
# SHAPES: (51,), (51,) --> (51,)
# full namespace: EelKinematicsModel
v5752__02Da = v5745__02CY+v5751__02D8

# op _02Dd_power_combination_eval
# LANG: _02D1, _02Dc --> _02De
# SHAPES: (51,), (51,) --> (51,)
# full namespace: EelKinematicsModel
v5754__02De = (v5747__02D1)*(v5753__02Dc)
v5754__02De = v5754__02De.reshape((51,))

# op _02CJ expand_array_eval
# LANG: eel_rigid_mesh --> _02CK
# SHAPES: (51, 6, 3) --> (70, 51, 6, 3)
# full namespace: EelKinematicsModel
v5736__02CK = np.einsum('bcd,a->abcd', v5735_eel_rigid_mesh.reshape((51, 6, 3)) ,np.ones((70,))).reshape((70, 51, 6, 3))

# op _02D5 expand_scalar_eval
# LANG: amplitude_max --> _02D6
# SHAPES: (1,) --> (51,)
# full namespace: EelKinematicsModel
v5750__02D6 = np.empty((51,))
v5750__02D6.fill(v5749_amplitude_max.item())

# op _02Df_linear_combination_eval
# LANG: _02Da, _02De --> _02Dg
# SHAPES: (51,), (51,) --> (51,)
# full namespace: EelKinematicsModel
v5755__02Dg = v5752__02Da+v5754__02De

# op _02Dj_linear_combination_eval
# LANG: _02CY, _02C_ --> _02Dk
# SHAPES: (51,), (51,) --> (51,)
# full namespace: EelKinematicsModel
v5757__02Dk = v5745__02CY+v5746__02C_

# op _02Dp_linear_combination_eval
# LANG: _02CQ --> _02Dq
# SHAPES: (51,) --> (51,)
# full namespace: EelKinematicsModel
v5760__02Dq = _02Dp_constant+v5739__02CQ

# op _02CA expand_scalar_eval
# LANG: L --> _02CB
# SHAPES: (1,) --> (70, 51, 6, 1)
# full namespace: EelKinematicsModel
v5731__02CB = np.empty((70, 51, 6, 1))
v5731__02CB.fill(v5730_L.item())

# op _02CL_decompose_eval
# LANG: _02CK --> _02CM, _02DT, _02DW
# SHAPES: (70, 51, 6, 3) --> (70, 51, 6, 1), (70, 51, 6, 1), (70, 51, 6, 1)
# full namespace: EelKinematicsModel
v5737__02CM = ((v5736__02CK.flatten())[src_indices__02CM__02CL]).reshape((70, 51, 6, 1))
v5775__02DT = ((v5736__02CK.flatten())[src_indices__02DT__02CL]).reshape((70, 51, 6, 1))
v5777__02DW = ((v5736__02CK.flatten())[src_indices__02DW__02CL]).reshape((70, 51, 6, 1))

# op _02D2 expand_scalar_eval
# LANG: _02CW --> _02D3
# SHAPES: (1,) --> (51,)
# full namespace: EelKinematicsModel
v5748__02D3 = np.empty((51,))
v5748__02D3.fill(v5744__02CW.item())

# op _02Dh_power_combination_eval
# LANG: _02D6, _02Dg --> _02Di
# SHAPES: (51,), (51,) --> (51,)
# full namespace: EelKinematicsModel
v5756__02Di = (v5750__02D6)*(v5755__02Dg)
v5756__02Di = v5756__02Di.reshape((51,))

# op _02Dl_linear_combination_eval
# LANG: _02Dk, _02D1 --> _02Dm
# SHAPES: (51,), (51,) --> (51,)
# full namespace: EelKinematicsModel
v5758__02Dm = v5757__02Dk+v5747__02D1

# op _02Dr exp_eval
# LANG: _02Dq --> _02Ds
# SHAPES: (51,) --> (51,)
# full namespace: EelKinematicsModel
v5761__02Ds = np.exp(v5760__02Dq)

# op _02CC expand_scalar_eval
# LANG: wave_length --> _02CD
# SHAPES: (1,) --> (70, 51, 6, 1)
# full namespace: EelKinematicsModel
v5732__02CD = np.empty((70, 51, 6, 1))
v5732__02CD.fill(v5728_wave_length.item())

# op _02Dn_power_combination_eval
# LANG: _02Di, _02Dm --> _02Do
# SHAPES: (51,), (51,) --> (51,)
# full namespace: EelKinematicsModel
v5759__02Do = (v5756__02Di)*(v5758__02Dm**-1)
v5759__02Do = v5759__02Do.reshape((51,))

# op _02Dt_power_combination_eval
# LANG: _02D6, _02Ds --> _02Du
# SHAPES: (51,), (51,) --> (51,)
# full namespace: EelKinematicsModel
v5762__02Du = (v5750__02D6)*(v5761__02Ds)
v5762__02Du = v5762__02Du.reshape((51,))

# op _02Dv_linear_combination_eval
# LANG: _02D3 --> _02Dw
# SHAPES: (51,) --> (51,)
# full namespace: EelKinematicsModel
v5763__02Dw = _02Dv_constant+-1*v5748__02D3

# op _02E0_power_combination_eval
# LANG: _02CM, _02CB --> _02E1
# SHAPES: (70, 51, 6, 1), (70, 51, 6, 1) --> (70, 51, 6, 1)
# full namespace: EelKinematicsModel
v5780__02E1 = (v5737__02CM)*(v5731__02CB**-1)
v5780__02E1 = v5780__02E1.reshape((70, 51, 6, 1))

# op _02CG expand_array_eval
# LANG: time_vector --> _02CH
# SHAPES: (70,) --> (70, 51, 6, 1)
# full namespace: EelKinematicsModel
v5734__02CH = np.einsum('a,bcd->abcd', v5729_time_vector.reshape((70,)) ,np.ones((51, 6, 1))).reshape((70, 51, 6, 1))

# op _02Dx_power_combination_eval
# LANG: _02Do, _02Dw --> _02Dy
# SHAPES: (51,), (51,) --> (51,)
# full namespace: EelKinematicsModel
v5764__02Dy = (v5759__02Do)*(v5763__02Dw)
v5764__02Dy = v5764__02Dy.reshape((51,))

# op _02Dz_power_combination_eval
# LANG: _02Du, _02D3 --> _02DA
# SHAPES: (51,), (51,) --> (51,)
# full namespace: EelKinematicsModel
v5765__02DA = (v5762__02Du)*(v5748__02D3)
v5765__02DA = v5765__02DA.reshape((51,))

# op _02E2_power_combination_eval
# LANG: _02E1, _02CD --> _02E3
# SHAPES: (70, 51, 6, 1), (70, 51, 6, 1) --> (70, 51, 6, 1)
# full namespace: EelKinematicsModel
v5781__02E3 = (v5780__02E1)*(v5732__02CD**-1)
v5781__02E3 = v5781__02E3.reshape((70, 51, 6, 1))

# op _02CE expand_scalar_eval
# LANG: tail_frequency --> _02CF
# SHAPES: (1,) --> (70, 51, 6, 1)
# full namespace: EelKinematicsModel
v5733__02CF = np.empty((70, 51, 6, 1))
v5733__02CF.fill(v5727_tail_frequency.item())

# op _02DB_linear_combination_eval
# LANG: _02Dy, _02DA --> amplitude
# SHAPES: (51,), (51,) --> (51,)
# full namespace: EelKinematicsModel
v5766_amplitude = v5764__02Dy+v5765__02DA

# op _02E4_linear_combination_eval
# LANG: _02E3, _02CH --> _02E5
# SHAPES: (70, 51, 6, 1), (70, 51, 6, 1) --> (70, 51, 6, 1)
# full namespace: EelKinematicsModel
v5782__02E5 = v5781__02E3+-1*v5734__02CH

# op _02DD expand_array_eval
# LANG: amplitude --> _02DE
# SHAPES: (51,) --> (70, 51, 6, 1)
# full namespace: EelKinematicsModel
v5767__02DE = np.einsum('b,acd->abcd', v5766_amplitude.reshape((51,)) ,np.ones((70, 6, 1))).reshape((70, 51, 6, 1))

# op _02DX_power_combination_eval
# LANG: _02CF --> _02DY
# SHAPES: (70, 51, 6, 1) --> (70, 51, 6, 1)
# full namespace: EelKinematicsModel
v5778__02DY = (v5733__02CF)
v5778__02DY = (v5778__02DY*_02DX_coeff).reshape((70, 51, 6, 1))

# op _02E6_power_combination_eval
# LANG: _02E5 --> _02E7
# SHAPES: (70, 51, 6, 1) --> (70, 51, 6, 1)
# full namespace: EelKinematicsModel
v5783__02E7 = (v5782__02E5)
v5783__02E7 = (v5783__02E7*_02E6_coeff).reshape((70, 51, 6, 1))

# op _02DF_power_combination_eval
# LANG: _02CM, _02CB --> _02DG
# SHAPES: (70, 51, 6, 1), (70, 51, 6, 1) --> (70, 51, 6, 1)
# full namespace: EelKinematicsModel
v5768__02DG = (v5737__02CM)*(v5731__02CB**-1)
v5768__02DG = v5768__02DG.reshape((70, 51, 6, 1))

# op _02DZ_power_combination_eval
# LANG: _02DE, _02DY --> _02D_
# SHAPES: (70, 51, 6, 1), (70, 51, 6, 1) --> (70, 51, 6, 1)
# full namespace: EelKinematicsModel
v5779__02D_ = (v5767__02DE)*(v5778__02DY)
v5779__02D_ = v5779__02D_.reshape((70, 51, 6, 1))

# op _02E8_cos_eval
# LANG: _02E7 --> _02E9
# SHAPES: (70, 51, 6, 1) --> (70, 51, 6, 1)
# full namespace: EelKinematicsModel
v5784__02E9 = np.cos(v5783__02E7)

# op _02Bi expand_scalar_eval
# LANG: v_x --> u
# SHAPES: (1,) --> (70, 1)
# full namespace: 
v6396_u = np.empty((70, 1))
v6396_u.fill(v7073_v_x.item())

# op _02DH_power_combination_eval
# LANG: _02CD, _02DG --> _02DI
# SHAPES: (70, 51, 6, 1), (70, 51, 6, 1) --> (70, 51, 6, 1)
# full namespace: EelKinematicsModel
v5769__02DI = (v5768__02DG)*(v5732__02CD**-1)
v5769__02DI = v5769__02DI.reshape((70, 51, 6, 1))

# op _02Ea_power_combination_eval
# LANG: _02D_, _02E9 --> eel_lateral_velocity
# SHAPES: (70, 51, 6, 1), (70, 51, 6, 1) --> (70, 51, 6, 1)
# full namespace: EelKinematicsModel
v5785_eel_lateral_velocity = (v5779__02D_)*(v5784__02E9)
v5785_eel_lateral_velocity = v5785_eel_lateral_velocity.reshape((70, 51, 6, 1))

# op _02VF_power_combination_eval
# LANG: u --> _02VG
# SHAPES: (70, 1) --> (70, 1)
# full namespace: fish_model.adapter_comp
v6411__02VG = (v6396_u**2)
v6411__02VG = v6411__02VG.reshape((70, 1))

# op _02VH_power_combination_eval
# LANG: v --> _02VI
# SHAPES: (70, 1) --> (70, 1)
# full namespace: fish_model.adapter_comp
v6412__02VI = (v6397_v**2)
v6412__02VI = v6412__02VI.reshape((70, 1))

# op _02DJ_linear_combination_eval
# LANG: _02CH, _02DI --> _02DK
# SHAPES: (70, 51, 6, 1), (70, 51, 6, 1) --> (70, 51, 6, 1)
# full namespace: EelKinematicsModel
v5770__02DK = v5769__02DI+-1*v5734__02CH

# op _02Ed_decompose_eval
# LANG: eel_lateral_velocity --> _02El, _02Ee, _02Ef, _02Ei
# SHAPES: (70, 51, 6, 1) --> (70, 50, 5, 1), (70, 50, 5, 1), (70, 50, 5, 1), (70, 50, 5, 1)
# full namespace: EelKinematicsModel
v5787__02Ee = ((v5785_eel_lateral_velocity.flatten())[src_indices__02Ee__02Ed]).reshape((70, 50, 5, 1))
v5788__02Ef = ((v5785_eel_lateral_velocity.flatten())[src_indices__02Ef__02Ed]).reshape((70, 50, 5, 1))
v5790__02Ei = ((v5785_eel_lateral_velocity.flatten())[src_indices__02Ei__02Ed]).reshape((70, 50, 5, 1))
v5792__02El = ((v5785_eel_lateral_velocity.flatten())[src_indices__02El__02Ed]).reshape((70, 50, 5, 1))

# op _02VJ_linear_combination_eval
# LANG: _02VG, _02VI --> _02VK
# SHAPES: (70, 1), (70, 1) --> (70, 1)
# full namespace: fish_model.adapter_comp
v6413__02VK = v6411__02VG+v6412__02VI

# op _02VL_power_combination_eval
# LANG: w --> _02VM
# SHAPES: (70, 1) --> (70, 1)
# full namespace: fish_model.adapter_comp
v6414__02VM = (v6398_w**2)
v6414__02VM = v6414__02VM.reshape((70, 1))

# op _02DL_power_combination_eval
# LANG: _02DK --> _02DM
# SHAPES: (70, 51, 6, 1) --> (70, 51, 6, 1)
# full namespace: EelKinematicsModel
v5771__02DM = (v5770__02DK)
v5771__02DM = (v5771__02DM*_02DL_coeff).reshape((70, 51, 6, 1))

# op _02Eg_linear_combination_eval
# LANG: _02Ee, _02Ef --> _02Eh
# SHAPES: (70, 50, 5, 1), (70, 50, 5, 1) --> (70, 50, 5, 1)
# full namespace: EelKinematicsModel
v5789__02Eh = v5787__02Ee+v5788__02Ef

# op _02VN_linear_combination_eval
# LANG: _02VK, _02VM --> _02VO
# SHAPES: (70, 1), (70, 1) --> (70, 1)
# full namespace: fish_model.adapter_comp
v6415__02VO = v6413__02VK+v6414__02VM

# op _02DN_sin_eval
# LANG: _02DM --> _02DO
# SHAPES: (70, 51, 6, 1) --> (70, 51, 6, 1)
# full namespace: EelKinematicsModel
v5772__02DO = np.sin(v5771__02DM)

# op _02Ej_linear_combination_eval
# LANG: _02Ei, _02Eh --> _02Ek
# SHAPES: (70, 50, 5, 1), (70, 50, 5, 1) --> (70, 50, 5, 1)
# full namespace: EelKinematicsModel
v5791__02Ek = v5789__02Eh+v5790__02Ei

# op _02VP_power_combination_eval
# LANG: _02VO --> _02VQ
# SHAPES: (70, 1) --> (70, 1)
# full namespace: fish_model.adapter_comp
v6416__02VQ = (v6415__02VO**0.5)
v6416__02VQ = v6416__02VQ.reshape((70, 1))

# op _02VT_linear_combination_eval
# LANG: psi, psiw --> beta
# SHAPES: (70, 1), (70, 1) --> (70, 1)
# full namespace: fish_model.adapter_comp
v6885_beta = v6403_psi+v6405_psiw

# op _02B5_power_combination_eval
# LANG: tail_frequency --> _02B6
# SHAPES: (1,) --> (1,)
# full namespace: 
v5678__02B6 = (v5727_tail_frequency**-1)
v5678__02B6 = (v5678__02B6*_02B5_coeff).reshape((1,))

# op _02DP_power_combination_eval
# LANG: _02DE, _02DO --> eel_amplitude_along_body
# SHAPES: (70, 51, 6, 1), (70, 51, 6, 1) --> (70, 51, 6, 1)
# full namespace: EelKinematicsModel
v5773_eel_amplitude_along_body = (v5767__02DE)*(v5772__02DO)
v5773_eel_amplitude_along_body = v5773_eel_amplitude_along_body.reshape((70, 51, 6, 1))

# op _02Em_linear_combination_eval
# LANG: _02Ek, _02El --> _02En
# SHAPES: (70, 50, 5, 1), (70, 50, 5, 1) --> (70, 50, 5, 1)
# full namespace: EelKinematicsModel
v5793__02En = v5791__02Ek+v5792__02El

# op _02VR_linear_combination_eval
# LANG: theta, gamma --> alpha
# SHAPES: (70, 1), (70, 1) --> (70, 1)
# full namespace: fish_model.adapter_comp
v6884_alpha = v6402_theta+-1*v6404_gamma

# op _02VW_linear_combination_eval
# LANG: _02VQ --> _02VX
# SHAPES: (70, 1) --> (70, 1)
# full namespace: fish_model.adapter_comp
v6420__02VX = -1*v6416__02VQ

# op _02VY_cos_eval
# LANG: beta --> _02VZ
# SHAPES: (70, 1) --> (70, 1)
# full namespace: fish_model.adapter_comp
v6421__02VZ = np.cos(v6885_beta)

# op _02Wa_linear_combination_eval
# LANG: _02VQ --> _02Wb
# SHAPES: (70, 1) --> (70, 1)
# full namespace: fish_model.adapter_comp
v6427__02Wb = -1*v6416__02VQ

# op _02Wc_cos_eval
# LANG: beta --> _02Wd
# SHAPES: (70, 1) --> (70, 1)
# full namespace: fish_model.adapter_comp
v6428__02Wd = np.cos(v6885_beta)

# op _02B7_power_combination_eval
# LANG: _02B6 --> delta_t
# SHAPES: (1,) --> (1,)
# full namespace: 
v6921_delta_t = (v5678__02B6)
v6921_delta_t = (v6921_delta_t*_02B7_coeff).reshape((1,))

# op _02DU_linear_combination_eval
# LANG: _02DT, eel_amplitude_along_body --> _02DV
# SHAPES: (70, 51, 6, 1), (70, 51, 6, 1) --> (70, 51, 6, 1)
# full namespace: EelKinematicsModel
v5776__02DV = v5773_eel_amplitude_along_body+v5775__02DT

# op _02Eo_power_combination_eval
# LANG: _02En --> _02Ep
# SHAPES: (70, 50, 5, 1) --> (70, 50, 5, 1)
# full namespace: EelKinematicsModel
v5794__02Ep = (v5793__02En)
v5794__02Ep = (v5794__02Ep*_02Eo_coeff).reshape((70, 50, 5, 1))

# op _02V__power_combination_eval
# LANG: _02VX, _02VZ --> _02W0
# SHAPES: (70, 1), (70, 1) --> (70, 1)
# full namespace: fish_model.adapter_comp
v6422__02W0 = (v6420__02VX)*(v6421__02VZ)
v6422__02W0 = v6422__02W0.reshape((70, 1))

# op _02W1_cos_eval
# LANG: alpha --> _02W2
# SHAPES: (70, 1) --> (70, 1)
# full namespace: fish_model.adapter_comp
v6423__02W2 = np.cos(v6884_alpha)

# op _02W6_sin_eval
# LANG: beta --> _02W7
# SHAPES: (70, 1) --> (70, 1)
# full namespace: fish_model.adapter_comp
v6425__02W7 = np.sin(v6885_beta)

# op _02We_power_combination_eval
# LANG: _02Wb, _02Wd --> _02Wf
# SHAPES: (70, 1), (70, 1) --> (70, 1)
# full namespace: fish_model.adapter_comp
v6429__02Wf = (v6427__02Wb)*(v6428__02Wd)
v6429__02Wf = v6429__02Wf.reshape((70, 1))

# op _02Wg_sin_eval
# LANG: alpha --> _02Wh
# SHAPES: (70, 1) --> (70, 1)
# full namespace: fish_model.adapter_comp
v6430__02Wh = np.sin(v6884_alpha)

# op _02B9 expand_scalar_eval
# LANG: delta_t --> h
# SHAPES: (1,) --> (69,)
# full namespace: 
v6308_h = np.empty((69,))
v6308_h.fill(v6921_delta_t.item())

# op _02DS_indexed_passthrough_eval
# LANG: _02CM, _02DW, _02DV --> eel
# SHAPES: (70, 51, 6, 1), (70, 51, 6, 1), (70, 51, 6, 1) --> (70, 51, 6, 3)
# full namespace: EelKinematicsModel
v7074_eel__temp[i_v5737__02CM__02DS_indexed_passthrough_eval] = v5737__02CM.flatten()
v7074_eel = v7074_eel__temp.copy()
v7074_eel__temp[i_v5776__02DV__02DS_indexed_passthrough_eval] = v5776__02DV.flatten()
v7074_eel = v7074_eel__temp.copy()
v7074_eel__temp[i_v5777__02DW__02DS_indexed_passthrough_eval] = v5777__02DW.flatten()
v7074_eel = v7074_eel__temp.copy()

# op _02Eq_indexed_passthrough_eval
# LANG: _02Ep --> eel_coll_vel
# SHAPES: (70, 50, 5, 1) --> (70, 50, 5, 3)
# full namespace: EelKinematicsModel
v6470_eel_coll_vel__temp[i_v5794__02Ep__02Eq_indexed_passthrough_eval] = v5794__02Ep.flatten()
v6470_eel_coll_vel = v6470_eel_coll_vel__temp.copy()

# op _02W3_power_combination_eval
# LANG: _02W0, _02W2 --> _02W4
# SHAPES: (70, 1), (70, 1) --> (70, 1)
# full namespace: fish_model.adapter_comp
v6424__02W4 = (v6422__02W0)*(v6423__02W2)
v6424__02W4 = v6424__02W4.reshape((70, 1))

# op _02W8_power_combination_eval
# LANG: _02VQ, _02W7 --> _02W9
# SHAPES: (70, 1), (70, 1) --> (70, 1)
# full namespace: fish_model.adapter_comp
v6426__02W9 = (v6416__02VQ)*(v6425__02W7)
v6426__02W9 = v6426__02W9.reshape((70, 1))

# op _02Wi_power_combination_eval
# LANG: _02Wf, _02Wh --> _02Wj
# SHAPES: (70, 1), (70, 1) --> (70, 1)
# full namespace: fish_model.adapter_comp
v6431__02Wj = (v6429__02Wf)*(v6430__02Wh)
v6431__02Wj = v6431__02Wj.reshape((70, 1))

# op _02SY_custom_explicit_eval
# LANG: u, h, delta_t, v, w, p, q, r, theta, psi, gamma, psiw, eel_gamma_w_0, eel_wake_coords_0, eel_coll_vel, eel --> op_eel_wake_coords, op_eel_gamma_w
# SHAPES: (70, 1), 69, (1,), (70, 1), (70, 1), (70, 1), (70, 1), (70, 1), (70, 1), (70, 1), (70, 1), (70, 1), (69, 5), (69, 6, 3), (70, 50, 5, 3), (70, 51, 6, 3) --> (70, 69, 6, 3), (70, 69, 5)
# full namespace: fish_model.subgroup
temp = _02SY_custom_explicit_func_op_eel_gamma_w.solve(v6396_u, v6397_v, v6398_w, v6458_p, v6459_q, v6460_r, v6402_theta, v6403_psi, v6404_gamma, v6405_psiw, v6921_delta_t, v7074_eel, v6470_eel_coll_vel, v6306_eel_gamma_w_0, v6307_eel_wake_coords_0, v6308_h)
v6758_op_eel_gamma_w = temp[0].copy()
v6756_op_eel_wake_coords = temp[1].copy()

# op _02W5_indexed_passthrough_eval
# LANG: _02W4, _02W9, _02Wj --> frame_vel
# SHAPES: (70, 1), (70, 1), (70, 1) --> (70, 3)
# full namespace: fish_model.adapter_comp
v6880_frame_vel__temp[i_v6424__02W4__02W5_indexed_passthrough_eval] = v6424__02W4.flatten()
v6880_frame_vel = v6880_frame_vel__temp.copy()
v6880_frame_vel__temp[i_v6426__02W9__02W5_indexed_passthrough_eval] = v6426__02W9.flatten()
v6880_frame_vel = v6880_frame_vel__temp.copy()
v6880_frame_vel__temp[i_v6431__02Wj__02W5_indexed_passthrough_eval] = v6431__02Wj.flatten()
v6880_frame_vel = v6880_frame_vel__temp.copy()

# op _02Th_decompose_eval
# LANG: frame_vel --> _02Tm, _02Ti
# SHAPES: (70, 3) --> (70, 1), (70, 1)
# full namespace: fish_model.MeshPreprocessing_comp
v6322__02Ti = ((v6880_frame_vel.flatten())[src_indices__02Ti__02Th]).reshape((70, 1))
v6324__02Tm = ((v6880_frame_vel.flatten())[src_indices__02Tm__02Th]).reshape((70, 1))

# op _02Tj_linear_combination_eval
# LANG: _02Ti --> _02Tk
# SHAPES: (70, 1) --> (70, 1)
# full namespace: fish_model.MeshPreprocessing_comp
v6323__02Tk = -1*v6322__02Ti

# op _02Tn_linear_combination_eval
# LANG: _02Tm --> _02To
# SHAPES: (70, 1) --> (70, 1)
# full namespace: fish_model.MeshPreprocessing_comp
v6325__02To = -1*v6324__02Tm

# op _02Tl_indexed_passthrough_eval
# LANG: _02Tk, _02To, w --> fs
# SHAPES: (70, 1), (70, 1), (70, 1) --> (70, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6321_fs__temp[i_v6323__02Tk__02Tl_indexed_passthrough_eval] = v6323__02Tk.flatten()
v6321_fs = v6321_fs__temp.copy()
v6321_fs__temp[i_v6325__02To__02Tl_indexed_passthrough_eval] = v6325__02To.flatten()
v6321_fs = v6321_fs__temp.copy()
v6321_fs__temp[i_v6398_w__02Tl_indexed_passthrough_eval] = v6398_w.flatten()
v6321_fs = v6321_fs__temp.copy()

# op _02Tq expand_scalar_eval
# LANG: delta_t --> _02Tr
# SHAPES: (1,) --> (70, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6327__02Tr = np.empty((70, 3))
v6327__02Tr.fill(v6921_delta_t.item())

# op _02Ts_power_combination_eval
# LANG: fs --> _02Tt
# SHAPES: (70, 3) --> (70, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6328__02Tt = (v6321_fs)
v6328__02Tt = (v6328__02Tt*_02Ts_coeff).reshape((70, 3))

# op _02T4_decompose_eval
# LANG: eel --> _02TI, _02T5, _02T8, _02Ty, _02TB, _02TC, _02TH, _02T_, _02U0, _02Uw, _02Uz, _02UE
# SHAPES: (70, 51, 6, 3) --> (70, 50, 5, 3), (70, 50, 6, 3), (70, 50, 6, 3), (70, 1, 6, 3), (70, 50, 5, 3), (70, 50, 5, 3), (70, 50, 5, 3), (70, 51, 5, 3), (70, 51, 5, 3), (70, 50, 5, 3), (70, 50, 5, 3), (70, 50, 5, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6314__02T5 = ((v7074_eel.flatten())[src_indices__02T5__02T4]).reshape((70, 50, 6, 3))
v6316__02T8 = ((v7074_eel.flatten())[src_indices__02T8__02T4]).reshape((70, 50, 6, 3))
v6331__02Ty = ((v7074_eel.flatten())[src_indices__02Ty__02T4]).reshape((70, 1, 6, 3))
v6333__02TB = ((v7074_eel.flatten())[src_indices__02TB__02T4]).reshape((70, 50, 5, 3))
v6334__02TC = ((v7074_eel.flatten())[src_indices__02TC__02T4]).reshape((70, 50, 5, 3))
v6337__02TH = ((v7074_eel.flatten())[src_indices__02TH__02T4]).reshape((70, 50, 5, 3))
v6338__02TI = ((v7074_eel.flatten())[src_indices__02TI__02T4]).reshape((70, 50, 5, 3))
v6348__02T_ = ((v7074_eel.flatten())[src_indices__02T___02T4]).reshape((70, 51, 5, 3))
v6349__02U0 = ((v7074_eel.flatten())[src_indices__02U0__02T4]).reshape((70, 51, 5, 3))
v6368__02Uw = ((v7074_eel.flatten())[src_indices__02Uw__02T4]).reshape((70, 50, 5, 3))
v6370__02Uz = ((v7074_eel.flatten())[src_indices__02Uz__02T4]).reshape((70, 50, 5, 3))
v6373__02UE = ((v7074_eel.flatten())[src_indices__02UE__02T4]).reshape((70, 50, 5, 3))

# op _02Tu_power_combination_eval
# LANG: _02Tt, _02Tr --> _02Tv
# SHAPES: (70, 3), (70, 3) --> (70, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6329__02Tv = (v6328__02Tt)*(v6327__02Tr)
v6329__02Tv = v6329__02Tv.reshape((70, 3))

# op _02T6_power_combination_eval
# LANG: _02T5 --> _02T7
# SHAPES: (70, 50, 6, 3) --> (70, 50, 6, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6315__02T7 = (v6314__02T5)
v6315__02T7 = (v6315__02T7*_02T6_coeff).reshape((70, 50, 6, 3))

# op _02T9_power_combination_eval
# LANG: _02T8 --> _02Ta
# SHAPES: (70, 50, 6, 3) --> (70, 50, 6, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6317__02Ta = (v6316__02T8)
v6317__02Ta = (v6317__02Ta*_02T9_coeff).reshape((70, 50, 6, 3))

# op _02Tw expand_array_eval
# LANG: _02Tv --> _02Tx
# SHAPES: (70, 3) --> (70, 1, 6, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6330__02Tx = np.einsum('ad,bc->abcd', v6329__02Tv.reshape((70, 3)) ,np.ones((1, 6))).reshape((70, 1, 6, 3))

# op _02Tb_linear_combination_eval
# LANG: _02T7, _02Ta --> _02Tc
# SHAPES: (70, 50, 6, 3), (70, 50, 6, 3) --> (70, 50, 6, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6318__02Tc = v6315__02T7+v6317__02Ta

# op _02Tz_linear_combination_eval
# LANG: _02Ty, _02Tx --> _02TA
# SHAPES: (70, 1, 6, 3), (70, 1, 6, 3) --> (70, 1, 6, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6332__02TA = v6331__02Ty+v6330__02Tx

# op _02Td_indexed_passthrough_eval
# LANG: _02Tc, _02TA --> eel_bd_vtx_coords
# SHAPES: (70, 50, 6, 3), (70, 1, 6, 3) --> (70, 51, 6, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6755_eel_bd_vtx_coords__temp[i_v6318__02Tc__02Td_indexed_passthrough_eval] = v6318__02Tc.flatten()
v6755_eel_bd_vtx_coords = v6755_eel_bd_vtx_coords__temp.copy()
v6755_eel_bd_vtx_coords__temp[i_v6332__02TA__02Td_indexed_passthrough_eval] = v6332__02TA.flatten()
v6755_eel_bd_vtx_coords = v6755_eel_bd_vtx_coords__temp.copy()

# op _02TD_linear_combination_eval
# LANG: _02TB, _02TC --> _02TE
# SHAPES: (70, 50, 5, 3), (70, 50, 5, 3) --> (70, 50, 5, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6335__02TE = v6333__02TB+v6334__02TC

# op _02TJ_linear_combination_eval
# LANG: _02TI, _02TH --> _02TK
# SHAPES: (70, 50, 5, 3), (70, 50, 5, 3) --> (70, 50, 5, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6339__02TK = v6337__02TH+v6338__02TI

# op _02WS_decompose_eval
# LANG: eel_bd_vtx_coords --> _02WT
# SHAPES: (70, 51, 6, 3) --> (70, 1, 6, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group
v6454__02WT = ((v6755_eel_bd_vtx_coords.flatten())[src_indices__02WT__02WS]).reshape((70, 1, 6, 3))

# op _02TF_power_combination_eval
# LANG: _02TE --> _02TG
# SHAPES: (70, 50, 5, 3) --> (70, 50, 5, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6336__02TG = (v6335__02TE)
v6336__02TG = (v6336__02TG*_02TF_coeff).reshape((70, 50, 5, 3))

# op _02TL_power_combination_eval
# LANG: _02TK --> _02TM
# SHAPES: (70, 50, 5, 3) --> (70, 50, 5, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6340__02TM = (v6339__02TK)
v6340__02TM = (v6340__02TM*_02TL_coeff).reshape((70, 50, 5, 3))

# op _02WU_indexed_passthrough_eval
# LANG: _02WT, op_eel_wake_coords --> eel_TE_wake_coords
# SHAPES: (70, 1, 6, 3), (70, 69, 6, 3) --> (70, 70, 6, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group
v6499_eel_TE_wake_coords__temp[i_v6454__02WT__02WU_indexed_passthrough_eval] = v6454__02WT.flatten()
v6499_eel_TE_wake_coords = v6499_eel_TE_wake_coords__temp.copy()
v6499_eel_TE_wake_coords__temp[i_v6756_op_eel_wake_coords__02WU_indexed_passthrough_eval] = v6756_op_eel_wake_coords.flatten()
v6499_eel_TE_wake_coords = v6499_eel_TE_wake_coords__temp.copy()

# op _02TN_linear_combination_eval
# LANG: _02TG, _02TM --> eel_coll_pts_coords
# SHAPES: (70, 50, 5, 3), (70, 50, 5, 3) --> (70, 50, 5, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6621_eel_coll_pts_coords = v6336__02TG+v6340__02TM

# op _02Y6_decompose_eval
# LANG: eel_TE_wake_coords --> _02Y7, _02Y8, _02Y9, _02Ya
# SHAPES: (70, 70, 6, 3) --> (70, 69, 5, 3), (70, 69, 5, 3), (70, 69, 5, 3), (70, 69, 5, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6500__02Y7 = ((v6499_eel_TE_wake_coords.flatten())[src_indices__02Y7__02Y6]).reshape((70, 69, 5, 3))
v6501__02Y8 = ((v6499_eel_TE_wake_coords.flatten())[src_indices__02Y8__02Y6]).reshape((70, 69, 5, 3))
v6502__02Y9 = ((v6499_eel_TE_wake_coords.flatten())[src_indices__02Y9__02Y6]).reshape((70, 69, 5, 3))
v6503__02Ya = ((v6499_eel_TE_wake_coords.flatten())[src_indices__02Ya__02Y6]).reshape((70, 69, 5, 3))

# op _030S_decompose_eval
# LANG: eel_bd_vtx_coords --> _030T, _030U, _030V, _030W
# SHAPES: (70, 51, 6, 3) --> (70, 50, 5, 3), (70, 50, 5, 3), (70, 50, 5, 3), (70, 50, 5, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6623__030T = ((v6755_eel_bd_vtx_coords.flatten())[src_indices__030T__030S]).reshape((70, 50, 5, 3))
v6624__030U = ((v6755_eel_bd_vtx_coords.flatten())[src_indices__030U__030S]).reshape((70, 50, 5, 3))
v6625__030V = ((v6755_eel_bd_vtx_coords.flatten())[src_indices__030V__030S]).reshape((70, 50, 5, 3))
v6626__030W = ((v6755_eel_bd_vtx_coords.flatten())[src_indices__030W__030S]).reshape((70, 50, 5, 3))

# op _02YB reshape_eval
# LANG: _02Y8 --> _02YC
# SHAPES: (70, 69, 5, 3) --> (70, 345, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6517__02YC = v6501__02Y8.reshape((70, 345, 3))

# op _02YP reshape_eval
# LANG: eel_coll_pts_coords --> _02YQ
# SHAPES: (70, 50, 5, 3) --> (70, 250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6524__02YQ = v6621_eel_coll_pts_coords.reshape((70, 250, 3))

# op _02YV reshape_eval
# LANG: _02Y9 --> _02YW
# SHAPES: (70, 69, 5, 3) --> (70, 345, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6527__02YW = v6502__02Y9.reshape((70, 345, 3))

# op _02Yb reshape_eval
# LANG: eel_coll_pts_coords --> _02Yc
# SHAPES: (70, 50, 5, 3) --> (70, 250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6504__02Yc = v6621_eel_coll_pts_coords.reshape((70, 250, 3))

# op _02Yh reshape_eval
# LANG: _02Y7 --> _02Yi
# SHAPES: (70, 69, 5, 3) --> (70, 345, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6507__02Yi = v6500__02Y7.reshape((70, 345, 3))

# op _02Yv reshape_eval
# LANG: eel_coll_pts_coords --> _02Yw
# SHAPES: (70, 50, 5, 3) --> (70, 250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6514__02Yw = v6621_eel_coll_pts_coords.reshape((70, 250, 3))

# op _030X reshape_eval
# LANG: eel_coll_pts_coords --> _030Y
# SHAPES: (70, 50, 5, 3) --> (70, 250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6627__030Y = v6621_eel_coll_pts_coords.reshape((70, 250, 3))

# op _0312 reshape_eval
# LANG: _030T --> _0313
# SHAPES: (70, 50, 5, 3) --> (70, 250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6630__0313 = v6623__030T.reshape((70, 250, 3))

# op _031A reshape_eval
# LANG: eel_coll_pts_coords --> _031B
# SHAPES: (70, 50, 5, 3) --> (70, 250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6647__031B = v6621_eel_coll_pts_coords.reshape((70, 250, 3))

# op _031G reshape_eval
# LANG: _030V --> _031H
# SHAPES: (70, 50, 5, 3) --> (70, 250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6650__031H = v6625__030V.reshape((70, 250, 3))

# op _031g reshape_eval
# LANG: eel_coll_pts_coords --> _031h
# SHAPES: (70, 50, 5, 3) --> (70, 250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6637__031h = v6621_eel_coll_pts_coords.reshape((70, 250, 3))

# op _031m reshape_eval
# LANG: _030U --> _031n
# SHAPES: (70, 50, 5, 3) --> (70, 250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6640__031n = v6624__030U.reshape((70, 250, 3))

# op _02YD expand_array_eval
# LANG: _02YC --> _02YE
# SHAPES: (70, 345, 3) --> (70, 250, 345, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6518__02YE = np.einsum('acd,b->abcd', v6517__02YC.reshape((70, 345, 3)) ,np.ones((250,))).reshape((70, 250, 345, 3))

# op _02YR expand_array_eval
# LANG: _02YQ --> _02YS
# SHAPES: (70, 250, 3) --> (70, 250, 345, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6525__02YS = np.einsum('abd,c->abcd', v6524__02YQ.reshape((70, 250, 3)) ,np.ones((345,))).reshape((70, 250, 345, 3))

# op _02YX expand_array_eval
# LANG: _02YW --> _02YY
# SHAPES: (70, 345, 3) --> (70, 250, 345, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6528__02YY = np.einsum('acd,b->abcd', v6527__02YW.reshape((70, 345, 3)) ,np.ones((250,))).reshape((70, 250, 345, 3))

# op _02Yd expand_array_eval
# LANG: _02Yc --> _02Ye
# SHAPES: (70, 250, 3) --> (70, 250, 345, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6505__02Ye = np.einsum('abd,c->abcd', v6504__02Yc.reshape((70, 250, 3)) ,np.ones((345,))).reshape((70, 250, 345, 3))

# op _02Yj expand_array_eval
# LANG: _02Yi --> _02Yk
# SHAPES: (70, 345, 3) --> (70, 250, 345, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6508__02Yk = np.einsum('acd,b->abcd', v6507__02Yi.reshape((70, 345, 3)) ,np.ones((250,))).reshape((70, 250, 345, 3))

# op _02Yx expand_array_eval
# LANG: _02Yw --> _02Yy
# SHAPES: (70, 250, 3) --> (70, 250, 345, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6515__02Yy = np.einsum('abd,c->abcd', v6514__02Yw.reshape((70, 250, 3)) ,np.ones((345,))).reshape((70, 250, 345, 3))

# op _02Z8 reshape_eval
# LANG: eel_coll_pts_coords --> _02Z9
# SHAPES: (70, 50, 5, 3) --> (70, 250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6534__02Z9 = v6621_eel_coll_pts_coords.reshape((70, 250, 3))

# op _02Ze reshape_eval
# LANG: _02Ya --> _02Zf
# SHAPES: (70, 69, 5, 3) --> (70, 345, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6537__02Zf = v6503__02Ya.reshape((70, 345, 3))

# op _030Z expand_array_eval
# LANG: _030Y --> _030_
# SHAPES: (70, 250, 3) --> (70, 250, 250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6628__030_ = np.einsum('abd,c->abcd', v6627__030Y.reshape((70, 250, 3)) ,np.ones((250,))).reshape((70, 250, 250, 3))

# op _0314 expand_array_eval
# LANG: _0313 --> _0315
# SHAPES: (70, 250, 3) --> (70, 250, 250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6631__0315 = np.einsum('acd,b->abcd', v6630__0313.reshape((70, 250, 3)) ,np.ones((250,))).reshape((70, 250, 250, 3))

# op _031C expand_array_eval
# LANG: _031B --> _031D
# SHAPES: (70, 250, 3) --> (70, 250, 250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6648__031D = np.einsum('abd,c->abcd', v6647__031B.reshape((70, 250, 3)) ,np.ones((250,))).reshape((70, 250, 250, 3))

# op _031I expand_array_eval
# LANG: _031H --> _031J
# SHAPES: (70, 250, 3) --> (70, 250, 250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6651__031J = np.einsum('acd,b->abcd', v6650__031H.reshape((70, 250, 3)) ,np.ones((250,))).reshape((70, 250, 250, 3))

# op _031U reshape_eval
# LANG: eel_coll_pts_coords --> _031V
# SHAPES: (70, 50, 5, 3) --> (70, 250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6657__031V = v6621_eel_coll_pts_coords.reshape((70, 250, 3))

# op _031_ reshape_eval
# LANG: _030W --> _0320
# SHAPES: (70, 50, 5, 3) --> (70, 250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6660__0320 = v6626__030W.reshape((70, 250, 3))

# op _031i expand_array_eval
# LANG: _031h --> _031j
# SHAPES: (70, 250, 3) --> (70, 250, 250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6638__031j = np.einsum('abd,c->abcd', v6637__031h.reshape((70, 250, 3)) ,np.ones((250,))).reshape((70, 250, 250, 3))

# op _031o expand_array_eval
# LANG: _031n --> _031p
# SHAPES: (70, 250, 3) --> (70, 250, 250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6641__031p = np.einsum('acd,b->abcd', v6640__031n.reshape((70, 250, 3)) ,np.ones((250,))).reshape((70, 250, 250, 3))

# op _02YF reshape_eval
# LANG: _02YE --> _02YG
# SHAPES: (70, 250, 345, 3) --> (70, 86250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6519__02YG = v6518__02YE.reshape((70, 86250, 3))

# op _02YT reshape_eval
# LANG: _02YS --> _02YU
# SHAPES: (70, 250, 345, 3) --> (70, 86250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6526__02YU = v6525__02YS.reshape((70, 86250, 3))

# op _02YZ reshape_eval
# LANG: _02YY --> _02Y_
# SHAPES: (70, 250, 345, 3) --> (70, 86250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6529__02Y_ = v6528__02YY.reshape((70, 86250, 3))

# op _02Yf reshape_eval
# LANG: _02Ye --> _02Yg
# SHAPES: (70, 250, 345, 3) --> (70, 86250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6506__02Yg = v6505__02Ye.reshape((70, 86250, 3))

# op _02Yl reshape_eval
# LANG: _02Yk --> _02Ym
# SHAPES: (70, 250, 345, 3) --> (70, 86250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6509__02Ym = v6508__02Yk.reshape((70, 86250, 3))

# op _02Yz reshape_eval
# LANG: _02Yy --> _02YA
# SHAPES: (70, 250, 345, 3) --> (70, 86250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6516__02YA = v6515__02Yy.reshape((70, 86250, 3))

# op _02Za expand_array_eval
# LANG: _02Z9 --> _02Zb
# SHAPES: (70, 250, 3) --> (70, 250, 345, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6535__02Zb = np.einsum('abd,c->abcd', v6534__02Z9.reshape((70, 250, 3)) ,np.ones((345,))).reshape((70, 250, 345, 3))

# op _02Zg expand_array_eval
# LANG: _02Zf --> _02Zh
# SHAPES: (70, 345, 3) --> (70, 250, 345, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6538__02Zh = np.einsum('acd,b->abcd', v6537__02Zf.reshape((70, 345, 3)) ,np.ones((250,))).reshape((70, 250, 345, 3))

# op _0310 reshape_eval
# LANG: _030_ --> _0311
# SHAPES: (70, 250, 250, 3) --> (70, 62500, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6629__0311 = v6628__030_.reshape((70, 62500, 3))

# op _0316 reshape_eval
# LANG: _0315 --> _0317
# SHAPES: (70, 250, 250, 3) --> (70, 62500, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6632__0317 = v6631__0315.reshape((70, 62500, 3))

# op _031E reshape_eval
# LANG: _031D --> _031F
# SHAPES: (70, 250, 250, 3) --> (70, 62500, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6649__031F = v6648__031D.reshape((70, 62500, 3))

# op _031K reshape_eval
# LANG: _031J --> _031L
# SHAPES: (70, 250, 250, 3) --> (70, 62500, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6652__031L = v6651__031J.reshape((70, 62500, 3))

# op _031W expand_array_eval
# LANG: _031V --> _031X
# SHAPES: (70, 250, 3) --> (70, 250, 250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6658__031X = np.einsum('abd,c->abcd', v6657__031V.reshape((70, 250, 3)) ,np.ones((250,))).reshape((70, 250, 250, 3))

# op _031k reshape_eval
# LANG: _031j --> _031l
# SHAPES: (70, 250, 250, 3) --> (70, 62500, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6639__031l = v6638__031j.reshape((70, 62500, 3))

# op _031q reshape_eval
# LANG: _031p --> _031r
# SHAPES: (70, 250, 250, 3) --> (70, 62500, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6642__031r = v6641__031p.reshape((70, 62500, 3))

# op _0321 expand_array_eval
# LANG: _0320 --> _0322
# SHAPES: (70, 250, 3) --> (70, 250, 250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6661__0322 = np.einsum('acd,b->abcd', v6660__0320.reshape((70, 250, 3)) ,np.ones((250,))).reshape((70, 250, 250, 3))

# op _02YH_linear_combination_eval
# LANG: _02YA, _02YG --> _02YI
# SHAPES: (70, 86250, 3), (70, 86250, 3) --> (70, 86250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6520__02YI = v6516__02YA+-1*v6519__02YG

# op _02Yn_linear_combination_eval
# LANG: _02Yg, _02Ym --> _02Yo
# SHAPES: (70, 86250, 3), (70, 86250, 3) --> (70, 86250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6510__02Yo = v6506__02Yg+-1*v6509__02Ym

# op _02Z0_linear_combination_eval
# LANG: _02YU, _02Y_ --> _02Z1
# SHAPES: (70, 86250, 3), (70, 86250, 3) --> (70, 86250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6530__02Z1 = v6526__02YU+-1*v6529__02Y_

# op _02Zc reshape_eval
# LANG: _02Zb --> _02Zd
# SHAPES: (70, 250, 345, 3) --> (70, 86250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6536__02Zd = v6535__02Zb.reshape((70, 86250, 3))

# op _02Zi reshape_eval
# LANG: _02Zh --> _02Zj
# SHAPES: (70, 250, 345, 3) --> (70, 86250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6539__02Zj = v6538__02Zh.reshape((70, 86250, 3))

# op _0318_linear_combination_eval
# LANG: _0311, _0317 --> _0319
# SHAPES: (70, 62500, 3), (70, 62500, 3) --> (70, 62500, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6633__0319 = v6629__0311+-1*v6632__0317

# op _031M_linear_combination_eval
# LANG: _031F, _031L --> _031N
# SHAPES: (70, 62500, 3), (70, 62500, 3) --> (70, 62500, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6653__031N = v6649__031F+-1*v6652__031L

# op _031Y reshape_eval
# LANG: _031X --> _031Z
# SHAPES: (70, 250, 250, 3) --> (70, 62500, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6659__031Z = v6658__031X.reshape((70, 62500, 3))

# op _031s_linear_combination_eval
# LANG: _031l, _031r --> _031t
# SHAPES: (70, 62500, 3), (70, 62500, 3) --> (70, 62500, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6643__031t = v6639__031l+-1*v6642__031r

# op _0323 reshape_eval
# LANG: _0322 --> _0324
# SHAPES: (70, 250, 250, 3) --> (70, 62500, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6662__0324 = v6661__0322.reshape((70, 62500, 3))

# op _02YJ_power_combination_eval
# LANG: _02YI --> _02YK
# SHAPES: (70, 86250, 3) --> (70, 86250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6521__02YK = (v6520__02YI**2)
v6521__02YK = v6521__02YK.reshape((70, 86250, 3))

# op _02Yp_power_combination_eval
# LANG: _02Yo --> _02Yq
# SHAPES: (70, 86250, 3) --> (70, 86250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6511__02Yq = (v6510__02Yo**2)
v6511__02Yq = v6511__02Yq.reshape((70, 86250, 3))

# op _02Z2_power_combination_eval
# LANG: _02Z1 --> _02Z3
# SHAPES: (70, 86250, 3) --> (70, 86250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6531__02Z3 = (v6530__02Z1**2)
v6531__02Z3 = v6531__02Z3.reshape((70, 86250, 3))

# op _02Zk_linear_combination_eval
# LANG: _02Zd, _02Zj --> _02Zl
# SHAPES: (70, 86250, 3), (70, 86250, 3) --> (70, 86250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6540__02Zl = v6536__02Zd+-1*v6539__02Zj

# op _031O_power_combination_eval
# LANG: _031N --> _031P
# SHAPES: (70, 62500, 3) --> (70, 62500, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6654__031P = (v6653__031N**2)
v6654__031P = v6654__031P.reshape((70, 62500, 3))

# op _031a_power_combination_eval
# LANG: _0319 --> _031b
# SHAPES: (70, 62500, 3) --> (70, 62500, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6634__031b = (v6633__0319**2)
v6634__031b = v6634__031b.reshape((70, 62500, 3))

# op _031u_power_combination_eval
# LANG: _031t --> _031v
# SHAPES: (70, 62500, 3) --> (70, 62500, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6644__031v = (v6643__031t**2)
v6644__031v = v6644__031v.reshape((70, 62500, 3))

# op _0325_linear_combination_eval
# LANG: _031Z, _0324 --> _0326
# SHAPES: (70, 62500, 3), (70, 62500, 3) --> (70, 62500, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6663__0326 = v6659__031Z+-1*v6662__0324

# op _02YL_single_tensor_sum_with_axis_eval
# LANG: _02YK --> _02YM
# SHAPES: (70, 86250, 3) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6522__02YM = np.sum(v6521__02YK, axis = (2,)).reshape((70, 86250))

# op _02Yr_single_tensor_sum_with_axis_eval
# LANG: _02Yq --> _02Ys
# SHAPES: (70, 86250, 3) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6512__02Ys = np.sum(v6511__02Yq, axis = (2,)).reshape((70, 86250))

# op _02Z4_single_tensor_sum_with_axis_eval
# LANG: _02Z3 --> _02Z5
# SHAPES: (70, 86250, 3) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6532__02Z5 = np.sum(v6531__02Z3, axis = (2,)).reshape((70, 86250))

# op _02Zm_power_combination_eval
# LANG: _02Zl --> _02Zn
# SHAPES: (70, 86250, 3) --> (70, 86250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6541__02Zn = (v6540__02Zl**2)
v6541__02Zn = v6541__02Zn.reshape((70, 86250, 3))

# op _031Q_single_tensor_sum_with_axis_eval
# LANG: _031P --> _031R
# SHAPES: (70, 62500, 3) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6655__031R = np.sum(v6654__031P, axis = (2,)).reshape((70, 62500))

# op _031c_single_tensor_sum_with_axis_eval
# LANG: _031b --> _031d
# SHAPES: (70, 62500, 3) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6635__031d = np.sum(v6634__031b, axis = (2,)).reshape((70, 62500))

# op _031w_single_tensor_sum_with_axis_eval
# LANG: _031v --> _031x
# SHAPES: (70, 62500, 3) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6645__031x = np.sum(v6644__031v, axis = (2,)).reshape((70, 62500))

# op _0327_power_combination_eval
# LANG: _0326 --> _0328
# SHAPES: (70, 62500, 3) --> (70, 62500, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6664__0328 = (v6663__0326**2)
v6664__0328 = v6664__0328.reshape((70, 62500, 3))

# op _02YN_power_combination_eval
# LANG: _02YM --> _02YO
# SHAPES: (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6523__02YO = (v6522__02YM**0.5)
v6523__02YO = v6523__02YO.reshape((70, 86250))

# op _02Yt_power_combination_eval
# LANG: _02Ys --> _02Yu
# SHAPES: (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6513__02Yu = (v6512__02Ys**0.5)
v6513__02Yu = v6513__02Yu.reshape((70, 86250))

# op _02Z6_power_combination_eval
# LANG: _02Z5 --> _02Z7
# SHAPES: (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6533__02Z7 = (v6532__02Z5**0.5)
v6533__02Z7 = v6533__02Z7.reshape((70, 86250))

# op _02Zo_single_tensor_sum_with_axis_eval
# LANG: _02Zn --> _02Zp
# SHAPES: (70, 86250, 3) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6542__02Zp = np.sum(v6541__02Zn, axis = (2,)).reshape((70, 86250))

# op _02Zw_power_combination_eval
# LANG: _02Yo, _02YI --> _02Zx
# SHAPES: (70, 86250, 3), (70, 86250, 3) --> (70, 86250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6546__02Zx = (v6510__02Yo)*(v6520__02YI)
v6546__02Zx = v6546__02Zx.reshape((70, 86250, 3))

# op _02_1_power_combination_eval
# LANG: _02Z1, _02YI --> _02_2
# SHAPES: (70, 86250, 3), (70, 86250, 3) --> (70, 86250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6562__02_2 = (v6520__02YI)*(v6530__02Z1)
v6562__02_2 = v6562__02_2.reshape((70, 86250, 3))

# op _031S_power_combination_eval
# LANG: _031R --> _031T
# SHAPES: (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6656__031T = (v6655__031R**0.5)
v6656__031T = v6656__031T.reshape((70, 62500))

# op _031e_power_combination_eval
# LANG: _031d --> _031f
# SHAPES: (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6636__031f = (v6635__031d**0.5)
v6636__031f = v6636__031f.reshape((70, 62500))

# op _031y_power_combination_eval
# LANG: _031x --> _031z
# SHAPES: (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6646__031z = (v6645__031x**0.5)
v6646__031z = v6646__031z.reshape((70, 62500))

# op _0329_single_tensor_sum_with_axis_eval
# LANG: _0328 --> _032a
# SHAPES: (70, 62500, 3) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6665__032a = np.sum(v6664__0328, axis = (2,)).reshape((70, 62500))

# op _032N_power_combination_eval
# LANG: _031N, _031t --> _032O
# SHAPES: (70, 62500, 3), (70, 62500, 3) --> (70, 62500, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6685__032O = (v6643__031t)*(v6653__031N)
v6685__032O = v6685__032O.reshape((70, 62500, 3))

# op _032h_power_combination_eval
# LANG: _0319, _031t --> _032i
# SHAPES: (70, 62500, 3), (70, 62500, 3) --> (70, 62500, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6669__032i = (v6633__0319)*(v6643__031t)
v6669__032i = v6669__032i.reshape((70, 62500, 3))

# op _02ZA_power_combination_eval
# LANG: _02Yu, _02YO --> _02ZB
# SHAPES: (70, 86250), (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6548__02ZB = (v6513__02Yu)*(v6523__02YO)
v6548__02ZB = v6548__02ZB.reshape((70, 86250))

# op _02Zq_power_combination_eval
# LANG: _02Zp --> _02Zr
# SHAPES: (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6543__02Zr = (v6542__02Zp**0.5)
v6543__02Zr = v6543__02Zr.reshape((70, 86250))

# op _02Zy_single_tensor_sum_with_axis_eval
# LANG: _02Zx --> _02Zz
# SHAPES: (70, 86250, 3) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6547__02Zz = np.sum(v6546__02Zx, axis = (2,)).reshape((70, 86250))

# op _02_3_single_tensor_sum_with_axis_eval
# LANG: _02_2 --> _02_4
# SHAPES: (70, 86250, 3) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6563__02_4 = np.sum(v6562__02_2, axis = (2,)).reshape((70, 86250))

# op _02_5_power_combination_eval
# LANG: _02Z7, _02YO --> _02_6
# SHAPES: (70, 86250), (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6564__02_6 = (v6523__02YO)*(v6533__02Z7)
v6564__02_6 = v6564__02_6.reshape((70, 86250))

# op _02_x_power_combination_eval
# LANG: _02Zl, _02Z1 --> _02_y
# SHAPES: (70, 86250, 3), (70, 86250, 3) --> (70, 86250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6578__02_y = (v6530__02Z1)*(v6540__02Zl)
v6578__02_y = v6578__02_y.reshape((70, 86250, 3))

# op _032P_single_tensor_sum_with_axis_eval
# LANG: _032O --> _032Q
# SHAPES: (70, 62500, 3) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6686__032Q = np.sum(v6685__032O, axis = (2,)).reshape((70, 62500))

# op _032R_power_combination_eval
# LANG: _031T, _031z --> _032S
# SHAPES: (70, 62500), (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6687__032S = (v6646__031z)*(v6656__031T)
v6687__032S = v6687__032S.reshape((70, 62500))

# op _032b_power_combination_eval
# LANG: _032a --> _032c
# SHAPES: (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6666__032c = (v6665__032a**0.5)
v6666__032c = v6666__032c.reshape((70, 62500))

# op _032j_single_tensor_sum_with_axis_eval
# LANG: _032i --> _032k
# SHAPES: (70, 62500, 3) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6670__032k = np.sum(v6669__032i, axis = (2,)).reshape((70, 62500))

# op _032l_power_combination_eval
# LANG: _031f, _031z --> _032m
# SHAPES: (70, 62500), (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6671__032m = (v6636__031f)*(v6646__031z)
v6671__032m = v6671__032m.reshape((70, 62500))

# op _033i_power_combination_eval
# LANG: _0326, _031N --> _033j
# SHAPES: (70, 62500, 3), (70, 62500, 3) --> (70, 62500, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6701__033j = (v6653__031N)*(v6663__0326)
v6701__033j = v6701__033j.reshape((70, 62500, 3))

# op _02ZC_linear_combination_eval
# LANG: _02ZB, _02Zz --> _02ZD
# SHAPES: (70, 86250), (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6549__02ZD = v6548__02ZB+v6547__02Zz

# op _02ZI_linear_combination_eval
# LANG: _02Yu --> _02ZJ
# SHAPES: (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6552__02ZJ = _02ZI_constant+v6513__02Yu

# op _02ZM_linear_combination_eval
# LANG: _02YO --> _02ZN
# SHAPES: (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6554__02ZN = _02ZM_constant+v6523__02YO

# op _02_7_linear_combination_eval
# LANG: _02_6, _02_4 --> _02_8
# SHAPES: (70, 86250), (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6565__02_8 = v6564__02_6+v6563__02_4

# op _02_B_power_combination_eval
# LANG: _02Zr, _02Z7 --> _02_C
# SHAPES: (70, 86250), (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6580__02_C = (v6533__02Z7)*(v6543__02Zr)
v6580__02_C = v6580__02_C.reshape((70, 86250))

# op _02_d_linear_combination_eval
# LANG: _02YO --> _02_e
# SHAPES: (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6568__02_e = _02_d_constant+v6523__02YO

# op _02_h_linear_combination_eval
# LANG: _02Z7 --> _02_i
# SHAPES: (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6570__02_i = _02_h_constant+v6533__02Z7

# op _02_z_single_tensor_sum_with_axis_eval
# LANG: _02_y --> _02_A
# SHAPES: (70, 86250, 3) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6579__02_A = np.sum(v6578__02_y, axis = (2,)).reshape((70, 86250))

# op _0302_power_combination_eval
# LANG: _02Zl, _02Yo --> _0303
# SHAPES: (70, 86250, 3), (70, 86250, 3) --> (70, 86250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6594__0303 = (v6540__02Zl)*(v6510__02Yo)
v6594__0303 = v6594__0303.reshape((70, 86250, 3))

# op _032T_linear_combination_eval
# LANG: _032S, _032Q --> _032U
# SHAPES: (70, 62500), (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6688__032U = v6687__032S+v6686__032Q

# op _032Z_linear_combination_eval
# LANG: _031z --> _032_
# SHAPES: (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6691__032_ = _032Z_constant+v6646__031z

# op _032n_linear_combination_eval
# LANG: _032m, _032k --> _032o
# SHAPES: (70, 62500), (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6672__032o = v6671__032m+v6670__032k

# op _032t_linear_combination_eval
# LANG: _031f --> _032u
# SHAPES: (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6675__032u = _032t_constant+v6636__031f

# op _032x_linear_combination_eval
# LANG: _031z --> _032y
# SHAPES: (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6677__032y = _032x_constant+v6646__031z

# op _0332_linear_combination_eval
# LANG: _031T --> _0333
# SHAPES: (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6693__0333 = _0332_constant+v6656__031T

# op _033O_power_combination_eval
# LANG: _0326, _0319 --> _033P
# SHAPES: (70, 62500, 3), (70, 62500, 3) --> (70, 62500, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6717__033P = (v6663__0326)*(v6633__0319)
v6717__033P = v6717__033P.reshape((70, 62500, 3))

# op _033k_single_tensor_sum_with_axis_eval
# LANG: _033j --> _033l
# SHAPES: (70, 62500, 3) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6702__033l = np.sum(v6701__033j, axis = (2,)).reshape((70, 62500))

# op _033m_power_combination_eval
# LANG: _032c, _031T --> _033n
# SHAPES: (70, 62500), (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6703__033n = (v6656__031T)*(v6666__032c)
v6703__033n = v6703__033n.reshape((70, 62500))

# op _02Xu_decompose_eval
# LANG: eel --> _02XA, _02Xv, _02Xw, _02Xz
# SHAPES: (70, 51, 6, 3) --> (70, 50, 5, 3), (70, 50, 5, 3), (70, 50, 5, 3), (70, 50, 5, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal
v6476__02Xv = ((v7074_eel.flatten())[src_indices__02Xv__02Xu]).reshape((70, 50, 5, 3))
v6477__02Xw = ((v7074_eel.flatten())[src_indices__02Xw__02Xu]).reshape((70, 50, 5, 3))
v6479__02Xz = ((v7074_eel.flatten())[src_indices__02Xz__02Xu]).reshape((70, 50, 5, 3))
v6480__02XA = ((v7074_eel.flatten())[src_indices__02XA__02Xu]).reshape((70, 50, 5, 3))

# op _02ZE_linear_combination_eval
# LANG: _02ZD --> _02ZF
# SHAPES: (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6550__02ZF = _02ZE_constant+v6549__02ZD

# op _02ZK_power_combination_eval
# LANG: _02ZJ --> _02ZL
# SHAPES: (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6553__02ZL = (v6552__02ZJ**-1)
v6553__02ZL = v6553__02ZL.reshape((70, 86250))

# op _02ZO_power_combination_eval
# LANG: _02ZN --> _02ZP
# SHAPES: (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6555__02ZP = (v6554__02ZN**-1)
v6555__02ZP = v6555__02ZP.reshape((70, 86250))

# op _02_9_linear_combination_eval
# LANG: _02_8 --> _02_a
# SHAPES: (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6566__02_a = _02_9_constant+v6565__02_8

# op _02_D_linear_combination_eval
# LANG: _02_C, _02_A --> _02_E
# SHAPES: (70, 86250), (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6581__02_E = v6580__02_C+v6579__02_A

# op _02_J_linear_combination_eval
# LANG: _02Z7 --> _02_K
# SHAPES: (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6584__02_K = _02_J_constant+v6533__02Z7

# op _02_N_linear_combination_eval
# LANG: _02Zr --> _02_O
# SHAPES: (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6586__02_O = _02_N_constant+v6543__02Zr

# op _02_f_power_combination_eval
# LANG: _02_e --> _02_g
# SHAPES: (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6569__02_g = (v6568__02_e**-1)
v6569__02_g = v6569__02_g.reshape((70, 86250))

# op _02_j_power_combination_eval
# LANG: _02_i --> _02_k
# SHAPES: (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6571__02_k = (v6570__02_i**-1)
v6571__02_k = v6571__02_k.reshape((70, 86250))

# op _0304_single_tensor_sum_with_axis_eval
# LANG: _0303 --> _0305
# SHAPES: (70, 86250, 3) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6595__0305 = np.sum(v6594__0303, axis = (2,)).reshape((70, 86250))

# op _0306_power_combination_eval
# LANG: _02Yu, _02Zr --> _0307
# SHAPES: (70, 86250), (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6596__0307 = (v6543__02Zr)*(v6513__02Yu)
v6596__0307 = v6596__0307.reshape((70, 86250))

# op _032V_linear_combination_eval
# LANG: _032U --> _032W
# SHAPES: (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6689__032W = _032V_constant+v6688__032U

# op _032p_linear_combination_eval
# LANG: _032o --> _032q
# SHAPES: (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6673__032q = _032p_constant+v6672__032o

# op _032v_power_combination_eval
# LANG: _032u --> _032w
# SHAPES: (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6676__032w = (v6675__032u**-1)
v6676__032w = v6676__032w.reshape((70, 62500))

# op _032z_power_combination_eval
# LANG: _032y --> _032A
# SHAPES: (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6678__032A = (v6677__032y**-1)
v6678__032A = v6678__032A.reshape((70, 62500))

# op _0330_power_combination_eval
# LANG: _032_ --> _0331
# SHAPES: (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6692__0331 = (v6691__032_**-1)
v6692__0331 = v6692__0331.reshape((70, 62500))

# op _0334_power_combination_eval
# LANG: _0333 --> _0335
# SHAPES: (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6694__0335 = (v6693__0333**-1)
v6694__0335 = v6694__0335.reshape((70, 62500))

# op _033Q_single_tensor_sum_with_axis_eval
# LANG: _033P --> _033R
# SHAPES: (70, 62500, 3) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6718__033R = np.sum(v6717__033P, axis = (2,)).reshape((70, 62500))

# op _033S_power_combination_eval
# LANG: _031f, _032c --> _033T
# SHAPES: (70, 62500), (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6719__033T = (v6666__032c)*(v6636__031f)
v6719__033T = v6719__033T.reshape((70, 62500))

# op _033o_linear_combination_eval
# LANG: _033n, _033l --> _033p
# SHAPES: (70, 62500), (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6704__033p = v6703__033n+v6702__033l

# op _033u_linear_combination_eval
# LANG: _031T --> _033v
# SHAPES: (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6707__033v = _033u_constant+v6656__031T

# op _033y_linear_combination_eval
# LANG: _032c --> _033z
# SHAPES: (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6709__033z = _033y_constant+v6666__032c

# op _02XB_linear_combination_eval
# LANG: _02Xz, _02XA --> _02XC
# SHAPES: (70, 50, 5, 3), (70, 50, 5, 3) --> (70, 50, 5, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal
v6481__02XC = v6479__02Xz+-1*v6480__02XA

# op _02Xx_linear_combination_eval
# LANG: _02Xv, _02Xw --> _02Xy
# SHAPES: (70, 50, 5, 3), (70, 50, 5, 3) --> (70, 50, 5, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal
v6478__02Xy = v6476__02Xv+-1*v6477__02Xw

# op _02ZG_power_combination_eval
# LANG: _02ZF --> _02ZH
# SHAPES: (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6551__02ZH = (v6550__02ZF**-1)
v6551__02ZH = v6551__02ZH.reshape((70, 86250))

# op _02ZQ_linear_combination_eval
# LANG: _02ZL, _02ZP --> _02ZR
# SHAPES: (70, 86250), (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6556__02ZR = v6553__02ZL+v6555__02ZP

# op _02_F_linear_combination_eval
# LANG: _02_E --> _02_G
# SHAPES: (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6582__02_G = _02_F_constant+v6581__02_E

# op _02_L_power_combination_eval
# LANG: _02_K --> _02_M
# SHAPES: (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6585__02_M = (v6584__02_K**-1)
v6585__02_M = v6585__02_M.reshape((70, 86250))

# op _02_P_power_combination_eval
# LANG: _02_O --> _02_Q
# SHAPES: (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6587__02_Q = (v6586__02_O**-1)
v6587__02_Q = v6587__02_Q.reshape((70, 86250))

# op _02_b_power_combination_eval
# LANG: _02_a --> _02_c
# SHAPES: (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6567__02_c = (v6566__02_a**-1)
v6567__02_c = v6567__02_c.reshape((70, 86250))

# op _02_l_linear_combination_eval
# LANG: _02_g, _02_k --> _02_m
# SHAPES: (70, 86250), (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6572__02_m = v6569__02_g+v6571__02_k

# op _0308_linear_combination_eval
# LANG: _0307, _0305 --> _0309
# SHAPES: (70, 86250), (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6597__0309 = v6596__0307+v6595__0305

# op _030e_linear_combination_eval
# LANG: _02Zr --> _030f
# SHAPES: (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6600__030f = _030e_constant+v6543__02Zr

# op _030i_linear_combination_eval
# LANG: _02Yu --> _030j
# SHAPES: (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6602__030j = _030i_constant+v6513__02Yu

# op _032B_linear_combination_eval
# LANG: _032w, _032A --> _032C
# SHAPES: (70, 62500), (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6679__032C = v6676__032w+v6678__032A

# op _032X_power_combination_eval
# LANG: _032W --> _032Y
# SHAPES: (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6690__032Y = (v6689__032W**-1)
v6690__032Y = v6690__032Y.reshape((70, 62500))

# op _032r_power_combination_eval
# LANG: _032q --> _032s
# SHAPES: (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6674__032s = (v6673__032q**-1)
v6674__032s = v6674__032s.reshape((70, 62500))

# op _0336_linear_combination_eval
# LANG: _0331, _0335 --> _0337
# SHAPES: (70, 62500), (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6695__0337 = v6692__0331+v6694__0335

# op _033A_power_combination_eval
# LANG: _033z --> _033B
# SHAPES: (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6710__033B = (v6709__033z**-1)
v6710__033B = v6710__033B.reshape((70, 62500))

# op _033U_linear_combination_eval
# LANG: _033T, _033R --> _033V
# SHAPES: (70, 62500), (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6720__033V = v6719__033T+v6718__033R

# op _033__linear_combination_eval
# LANG: _032c --> _0340
# SHAPES: (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6723__0340 = _033__constant+v6666__032c

# op _033q_linear_combination_eval
# LANG: _033p --> _033r
# SHAPES: (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6705__033r = _033q_constant+v6704__033p

# op _033w_power_combination_eval
# LANG: _033v --> _033x
# SHAPES: (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6708__033x = (v6707__033v**-1)
v6708__033x = v6708__033x.reshape((70, 62500))

# op _0343_linear_combination_eval
# LANG: _031f --> _0344
# SHAPES: (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6725__0344 = _0343_constant+v6636__031f

# op _02XD cross_product_eval
# LANG: _02Xy, _02XC --> _02XE
# SHAPES: (70, 50, 5, 3), (70, 50, 5, 3) --> (70, 50, 5, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal
v6482__02XE = np.cross(v6478__02Xy, v6481__02XC, axisa = 3, axisb = 3, axisc = 3)

# op _02ZS_power_combination_eval
# LANG: _02ZH, _02ZR --> num_02ZT
# SHAPES: (70, 86250), (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6557_num_02ZT = (v6551__02ZH)*(v6556__02ZR)
v6557_num_02ZT = v6557_num_02ZT.reshape((70, 86250))

# op _02ZY cross_product_eval
# LANG: _02Z1, _02YI --> _02ZZ
# SHAPES: (70, 86250, 3), (70, 86250, 3) --> (70, 86250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6560__02ZZ = np.cross(v6520__02YI, v6530__02Z1, axisa = 2, axisb = 2, axisc = 2)

# op _02Zs cross_product_eval
# LANG: _02Yo, _02YI --> _02Zt
# SHAPES: (70, 86250, 3), (70, 86250, 3) --> (70, 86250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6544__02Zt = np.cross(v6510__02Yo, v6520__02YI, axisa = 2, axisb = 2, axisc = 2)

# op _02_H_power_combination_eval
# LANG: _02_G --> _02_I
# SHAPES: (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6583__02_I = (v6582__02_G**-1)
v6583__02_I = v6583__02_I.reshape((70, 86250))

# op _02_R_linear_combination_eval
# LANG: _02_M, _02_Q --> _02_S
# SHAPES: (70, 86250), (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6588__02_S = v6585__02_M+v6587__02_Q

# op _02_n_power_combination_eval
# LANG: _02_c, _02_m --> num_02_o
# SHAPES: (70, 86250), (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6573_num_02_o = (v6567__02_c)*(v6572__02_m)
v6573_num_02_o = v6573_num_02_o.reshape((70, 86250))

# op _030a_linear_combination_eval
# LANG: _0309 --> _030b
# SHAPES: (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6598__030b = _030a_constant+v6597__0309

# op _030g_power_combination_eval
# LANG: _030f --> _030h
# SHAPES: (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6601__030h = (v6600__030f**-1)
v6601__030h = v6601__030h.reshape((70, 86250))

# op _030k_power_combination_eval
# LANG: _030j --> _030l
# SHAPES: (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6603__030l = (v6602__030j**-1)
v6603__030l = v6603__030l.reshape((70, 86250))

# op _032D_power_combination_eval
# LANG: _032s, _032C --> num_032E
# SHAPES: (70, 62500), (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6680_num_032E = (v6674__032s)*(v6679__032C)
v6680_num_032E = v6680_num_032E.reshape((70, 62500))

# op _032J cross_product_eval
# LANG: _031N, _031t --> _032K
# SHAPES: (70, 62500, 3), (70, 62500, 3) --> (70, 62500, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6683__032K = np.cross(v6643__031t, v6653__031N, axisa = 2, axisb = 2, axisc = 2)

# op _032d cross_product_eval
# LANG: _0319, _031t --> _032e
# SHAPES: (70, 62500, 3), (70, 62500, 3) --> (70, 62500, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6667__032e = np.cross(v6633__0319, v6643__031t, axisa = 2, axisb = 2, axisc = 2)

# op _0338_power_combination_eval
# LANG: _032Y, _0337 --> num_0339
# SHAPES: (70, 62500), (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6696_num_0339 = (v6690__032Y)*(v6695__0337)
v6696_num_0339 = v6696_num_0339.reshape((70, 62500))

# op _033C_linear_combination_eval
# LANG: _033x, _033B --> _033D
# SHAPES: (70, 62500), (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6711__033D = v6708__033x+v6710__033B

# op _033W_linear_combination_eval
# LANG: _033V --> _033X
# SHAPES: (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6721__033X = _033W_constant+v6720__033V

# op _033s_power_combination_eval
# LANG: _033r --> _033t
# SHAPES: (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6706__033t = (v6705__033r**-1)
v6706__033t = v6706__033t.reshape((70, 62500))

# op _0341_power_combination_eval
# LANG: _0340 --> _0342
# SHAPES: (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6724__0342 = (v6723__0340**-1)
v6724__0342 = v6724__0342.reshape((70, 62500))

# op _0345_power_combination_eval
# LANG: _0344 --> _0346
# SHAPES: (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6726__0346 = (v6725__0344**-1)
v6726__0346 = v6726__0346.reshape((70, 62500))

# op _02X5_indexed_passthrough_eval
# LANG: p, q, r --> ang_vel
# SHAPES: (70, 1), (70, 1), (70, 1) --> (70, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp
v6461_ang_vel__temp[i_v6458_p__02X5_indexed_passthrough_eval] = v6458_p.flatten()
v6461_ang_vel = v6461_ang_vel__temp.copy()
v6461_ang_vel__temp[i_v6459_q__02X5_indexed_passthrough_eval] = v6459_q.flatten()
v6461_ang_vel = v6461_ang_vel__temp.copy()
v6461_ang_vel__temp[i_v6460_r__02X5_indexed_passthrough_eval] = v6460_r.flatten()
v6461_ang_vel = v6461_ang_vel__temp.copy()

# op _02X8 expand_array_eval
# LANG: eel_rot_ref --> _02X9
# SHAPES: (70, 3) --> (70, 50, 5, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp
v6464__02X9 = np.einsum('ad,bc->abcd', v6463_eel_rot_ref.reshape((70, 3)) ,np.ones((50, 5))).reshape((70, 50, 5, 3))

# op _02XF_power_combination_eval
# LANG: _02XE --> _02XG
# SHAPES: (70, 50, 5, 3) --> (70, 50, 5, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal
v6483__02XG = (v6482__02XE**2)
v6483__02XG = v6483__02XG.reshape((70, 50, 5, 3))

# op _02ZU expand_array_eval
# LANG: num_02ZT --> _02ZV
# SHAPES: (70, 86250) --> (70, 86250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6558__02ZV = np.einsum('ab,c->abc', v6557_num_02ZT.reshape((70, 86250)) ,np.ones((3,))).reshape((70, 86250, 3))

# op _02Z__power_combination_eval
# LANG: _02ZZ --> _02_0
# SHAPES: (70, 86250, 3) --> (70, 86250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6561__02_0 = (v6560__02ZZ)
v6561__02_0 = (v6561__02_0*_02Z__coeff).reshape((70, 86250, 3))

# op _02Zu_power_combination_eval
# LANG: _02Zt --> _02Zv
# SHAPES: (70, 86250, 3) --> (70, 86250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6545__02Zv = (v6544__02Zt)
v6545__02Zv = (v6545__02Zv*_02Zu_coeff).reshape((70, 86250, 3))

# op _02_T_power_combination_eval
# LANG: _02_I, _02_S --> num_02_U
# SHAPES: (70, 86250), (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6589_num_02_U = (v6583__02_I)*(v6588__02_S)
v6589_num_02_U = v6589_num_02_U.reshape((70, 86250))

# op _02_p expand_array_eval
# LANG: num_02_o --> _02_q
# SHAPES: (70, 86250) --> (70, 86250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6574__02_q = np.einsum('ab,c->abc', v6573_num_02_o.reshape((70, 86250)) ,np.ones((3,))).reshape((70, 86250, 3))

# op _02_t cross_product_eval
# LANG: _02Zl, _02Z1 --> _02_u
# SHAPES: (70, 86250, 3), (70, 86250, 3) --> (70, 86250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6576__02_u = np.cross(v6530__02Z1, v6540__02Zl, axisa = 2, axisb = 2, axisc = 2)

# op _030c_power_combination_eval
# LANG: _030b --> _030d
# SHAPES: (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6599__030d = (v6598__030b**-1)
v6599__030d = v6599__030d.reshape((70, 86250))

# op _030m_linear_combination_eval
# LANG: _030h, _030l --> _030n
# SHAPES: (70, 86250), (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6604__030n = v6601__030h+v6603__030l

# op _032F expand_array_eval
# LANG: num_032E --> _032G
# SHAPES: (70, 62500) --> (70, 62500, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6681__032G = np.einsum('ab,c->abc', v6680_num_032E.reshape((70, 62500)) ,np.ones((3,))).reshape((70, 62500, 3))

# op _032L_power_combination_eval
# LANG: _032K --> _032M
# SHAPES: (70, 62500, 3) --> (70, 62500, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6684__032M = (v6683__032K)
v6684__032M = (v6684__032M*_032L_coeff).reshape((70, 62500, 3))

# op _032f_power_combination_eval
# LANG: _032e --> _032g
# SHAPES: (70, 62500, 3) --> (70, 62500, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6668__032g = (v6667__032e)
v6668__032g = (v6668__032g*_032f_coeff).reshape((70, 62500, 3))

# op _033E_power_combination_eval
# LANG: _033t, _033D --> num_033F
# SHAPES: (70, 62500), (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6712_num_033F = (v6706__033t)*(v6711__033D)
v6712_num_033F = v6712_num_033F.reshape((70, 62500))

# op _033Y_power_combination_eval
# LANG: _033X --> _033Z
# SHAPES: (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6722__033Z = (v6721__033X**-1)
v6722__033Z = v6722__033Z.reshape((70, 62500))

# op _033a expand_array_eval
# LANG: num_0339 --> _033b
# SHAPES: (70, 62500) --> (70, 62500, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6697__033b = np.einsum('ab,c->abc', v6696_num_0339.reshape((70, 62500)) ,np.ones((3,))).reshape((70, 62500, 3))

# op _033e cross_product_eval
# LANG: _0326, _031N --> _033f
# SHAPES: (70, 62500, 3), (70, 62500, 3) --> (70, 62500, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6699__033f = np.cross(v6653__031N, v6663__0326, axisa = 2, axisb = 2, axisc = 2)

# op _0347_linear_combination_eval
# LANG: _0342, _0346 --> _0348
# SHAPES: (70, 62500), (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6727__0348 = v6724__0342+v6726__0346

# op _02XH_single_tensor_sum_with_axis_eval
# LANG: _02XG --> _02XI
# SHAPES: (70, 50, 5, 3) --> (70, 50, 5)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal
v6484__02XI = np.sum(v6483__02XG, axis = (3,)).reshape((70, 50, 5))

# op _02Xa_linear_combination_eval
# LANG: _02X9, eel_coll_pts_coords --> _02Xb
# SHAPES: (70, 50, 5, 3), (70, 50, 5, 3) --> (70, 50, 5, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp
v6465__02Xb = v6621_eel_coll_pts_coords+-1*v6464__02X9

# op _02Xc expand_array_eval
# LANG: ang_vel --> _02Xd
# SHAPES: (70, 3) --> (70, 50, 5, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp
v6466__02Xd = np.einsum('ad,bc->abcd', v6461_ang_vel.reshape((70, 3)) ,np.ones((50, 5))).reshape((70, 50, 5, 3))

# op _02ZW_power_combination_eval
# LANG: _02ZV, _02Zv --> _02ZX
# SHAPES: (70, 86250, 3), (70, 86250, 3) --> (70, 86250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6559__02ZX = (v6558__02ZV)*(v6545__02Zv)
v6559__02ZX = v6559__02ZX.reshape((70, 86250, 3))

# op _02_V expand_array_eval
# LANG: num_02_U --> _02_W
# SHAPES: (70, 86250) --> (70, 86250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6590__02_W = np.einsum('ab,c->abc', v6589_num_02_U.reshape((70, 86250)) ,np.ones((3,))).reshape((70, 86250, 3))

# op _02_Z cross_product_eval
# LANG: _02Zl, _02Yo --> _02__
# SHAPES: (70, 86250, 3), (70, 86250, 3) --> (70, 86250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6592__02__ = np.cross(v6540__02Zl, v6510__02Yo, axisa = 2, axisb = 2, axisc = 2)

# op _02_r_power_combination_eval
# LANG: _02_q, _02_0 --> _02_s
# SHAPES: (70, 86250, 3), (70, 86250, 3) --> (70, 86250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6575__02_s = (v6574__02_q)*(v6561__02_0)
v6575__02_s = v6575__02_s.reshape((70, 86250, 3))

# op _02_v_power_combination_eval
# LANG: _02_u --> _02_w
# SHAPES: (70, 86250, 3) --> (70, 86250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6577__02_w = (v6576__02_u)
v6577__02_w = (v6577__02_w*_02_v_coeff).reshape((70, 86250, 3))

# op _030o_power_combination_eval
# LANG: _030d, _030n --> num_030p
# SHAPES: (70, 86250), (70, 86250) --> (70, 86250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6605_num_030p = (v6599__030d)*(v6604__030n)
v6605_num_030p = v6605_num_030p.reshape((70, 86250))

# op _032H_power_combination_eval
# LANG: _032G, _032g --> _032I
# SHAPES: (70, 62500, 3), (70, 62500, 3) --> (70, 62500, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6682__032I = (v6681__032G)*(v6668__032g)
v6682__032I = v6682__032I.reshape((70, 62500, 3))

# op _033G expand_array_eval
# LANG: num_033F --> _033H
# SHAPES: (70, 62500) --> (70, 62500, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6713__033H = np.einsum('ab,c->abc', v6712_num_033F.reshape((70, 62500)) ,np.ones((3,))).reshape((70, 62500, 3))

# op _033K cross_product_eval
# LANG: _0326, _0319 --> _033L
# SHAPES: (70, 62500, 3), (70, 62500, 3) --> (70, 62500, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6715__033L = np.cross(v6663__0326, v6633__0319, axisa = 2, axisb = 2, axisc = 2)

# op _033c_power_combination_eval
# LANG: _033b, _032M --> _033d
# SHAPES: (70, 62500, 3), (70, 62500, 3) --> (70, 62500, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6698__033d = (v6697__033b)*(v6684__032M)
v6698__033d = v6698__033d.reshape((70, 62500, 3))

# op _033g_power_combination_eval
# LANG: _033f --> _033h
# SHAPES: (70, 62500, 3) --> (70, 62500, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6700__033h = (v6699__033f)
v6700__033h = (v6700__033h*_033g_coeff).reshape((70, 62500, 3))

# op _0349_power_combination_eval
# LANG: _033Z, _0348 --> num_034a
# SHAPES: (70, 62500), (70, 62500) --> (70, 62500)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6728_num_034a = (v6722__033Z)*(v6727__0348)
v6728_num_034a = v6728_num_034a.reshape((70, 62500))

# op _02XJ_power_combination_eval
# LANG: _02XI --> _02XK
# SHAPES: (70, 50, 5) --> (70, 50, 5)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal
v6485__02XK = (v6484__02XI**0.5)
v6485__02XK = v6485__02XK.reshape((70, 50, 5))

# op _02Xe cross_product_eval
# LANG: _02Xd, _02Xb --> _02Xf
# SHAPES: (70, 50, 5, 3), (70, 50, 5, 3) --> (70, 50, 5, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp
v6467__02Xf = np.cross(v6466__02Xd, v6465__02Xb, axisa = 3, axisb = 3, axisc = 3)

# op _02_X_power_combination_eval
# LANG: _02_W, _02_w --> _02_Y
# SHAPES: (70, 86250, 3), (70, 86250, 3) --> (70, 86250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6591__02_Y = (v6590__02_W)*(v6577__02_w)
v6591__02_Y = v6591__02_Y.reshape((70, 86250, 3))

# op _0300_power_combination_eval
# LANG: _02__ --> _0301
# SHAPES: (70, 86250, 3) --> (70, 86250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6593__0301 = (v6592__02__)
v6593__0301 = (v6593__0301*_0300_coeff).reshape((70, 86250, 3))

# op _030q expand_array_eval
# LANG: num_030p --> _030r
# SHAPES: (70, 86250) --> (70, 86250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6606__030r = np.einsum('ab,c->abc', v6605_num_030p.reshape((70, 86250)) ,np.ones((3,))).reshape((70, 86250, 3))

# op _030u_linear_combination_eval
# LANG: _02ZX, _02_s --> _030v
# SHAPES: (70, 86250, 3), (70, 86250, 3) --> (70, 86250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6608__030v = v6559__02ZX+v6575__02_s

# op _033I_power_combination_eval
# LANG: _033H, _033h --> _033J
# SHAPES: (70, 62500, 3), (70, 62500, 3) --> (70, 62500, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6714__033J = (v6713__033H)*(v6700__033h)
v6714__033J = v6714__033J.reshape((70, 62500, 3))

# op _033M_power_combination_eval
# LANG: _033L --> _033N
# SHAPES: (70, 62500, 3) --> (70, 62500, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6716__033N = (v6715__033L)
v6716__033N = (v6716__033N*_033M_coeff).reshape((70, 62500, 3))

# op _034b expand_array_eval
# LANG: num_034a --> _034c
# SHAPES: (70, 62500) --> (70, 62500, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6729__034c = np.einsum('ab,c->abc', v6728_num_034a.reshape((70, 62500)) ,np.ones((3,))).reshape((70, 62500, 3))

# op _034f_linear_combination_eval
# LANG: _032I, _033d --> _034g
# SHAPES: (70, 62500, 3), (70, 62500, 3) --> (70, 62500, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6731__034g = v6682__032I+v6698__033d

# op _02XL expand_array_eval
# LANG: _02XK --> _02XM
# SHAPES: (70, 50, 5) --> (70, 50, 5, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal
v6486__02XM = np.einsum('abc,d->abcd', v6485__02XK.reshape((70, 50, 5)) ,np.ones((3,))).reshape((70, 50, 5, 3))

# op _02Xg reshape_eval
# LANG: _02Xf --> _02Xh
# SHAPES: (70, 50, 5, 3) --> (70, 250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp
v6468__02Xh = v6467__02Xf.reshape((70, 250, 3))

# op _02Xi expand_array_eval
# LANG: frame_vel --> _02Xj
# SHAPES: (70, 3) --> (70, 250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp
v6469__02Xj = np.einsum('ac,b->abc', v6880_frame_vel.reshape((70, 3)) ,np.ones((250,))).reshape((70, 250, 3))

# op _030s_power_combination_eval
# LANG: _030r, _0301 --> _030t
# SHAPES: (70, 86250, 3), (70, 86250, 3) --> (70, 86250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6607__030t = (v6606__030r)*(v6593__0301)
v6607__030t = v6607__030t.reshape((70, 86250, 3))

# op _030w_linear_combination_eval
# LANG: _030v, _02_Y --> _030x
# SHAPES: (70, 86250, 3), (70, 86250, 3) --> (70, 86250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6609__030x = v6608__030v+v6591__02_Y

# op _034d_power_combination_eval
# LANG: _034c, _033N --> _034e
# SHAPES: (70, 62500, 3), (70, 62500, 3) --> (70, 62500, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6730__034e = (v6729__034c)*(v6716__033N)
v6730__034e = v6730__034e.reshape((70, 62500, 3))

# op _034h_linear_combination_eval
# LANG: _034g, _033J --> _034i
# SHAPES: (70, 62500, 3), (70, 62500, 3) --> (70, 62500, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6732__034i = v6731__034g+v6714__033J

# op _02XN_power_combination_eval
# LANG: _02XE, _02XM --> eel_bd_vtx_normals
# SHAPES: (70, 50, 5, 3), (70, 50, 5, 3) --> (70, 50, 5, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.ComputeNormal
v6930_eel_bd_vtx_normals = (v6482__02XE)*(v6486__02XM**-1)
v6930_eel_bd_vtx_normals = v6930_eel_bd_vtx_normals.reshape((70, 50, 5, 3))

# op _02Xl_linear_combination_eval
# LANG: _02Xh, _02Xj --> _02Xm
# SHAPES: (70, 250, 3), (70, 250, 3) --> (70, 250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp
v6471__02Xm = v6468__02Xh+v6469__02Xj

# op _02Xn reshape_eval
# LANG: eel_coll_vel --> _02Xo
# SHAPES: (70, 50, 5, 3) --> (70, 250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp
v6472__02Xo = v6470_eel_coll_vel.reshape((70, 250, 3))

# op _030y_linear_combination_eval
# LANG: _030x, _030t --> aic_M00
# SHAPES: (70, 86250, 3), (70, 86250, 3) --> (70, 86250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic.aic_bd_w_seperate
v6610_aic_M00 = v6609__030x+v6607__030t

# op _034j_linear_combination_eval
# LANG: _034i, _034e --> aic_bd00
# SHAPES: (70, 62500, 3), (70, 62500, 3) --> (70, 62500, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd.aic_bd_w_seperate
v6733_aic_bd00 = v6732__034i+v6730__034e

# op _02Xp_linear_combination_eval
# LANG: _02Xm, _02Xo --> _02Xq
# SHAPES: (70, 250, 3), (70, 250, 3) --> (70, 250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp
v6473__02Xq = v6471__02Xm+v6472__02Xo

# op _02Y1 reshape_eval
# LANG: aic_M00 --> _02Y2
# SHAPES: (70, 86250, 3) --> (70, 250, 345, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic
v6497__02Y2 = v6610_aic_M00.reshape((70, 250, 345, 3))

# op _030D reshape_eval
# LANG: eel_bd_vtx_normals --> _030E
# SHAPES: (70, 50, 5, 3) --> (70, 250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_aic
v6614__030E = v6930_eel_bd_vtx_normals.reshape((70, 250, 3))

# op _030N reshape_eval
# LANG: aic_bd00 --> _030O
# SHAPES: (70, 62500, 3) --> (70, 250, 250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd
v6620__030O = v6733_aic_bd00.reshape((70, 250, 250, 3))

# op _034o reshape_eval
# LANG: eel_bd_vtx_normals --> _034p
# SHAPES: (70, 50, 5, 3) --> (70, 250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_aic_bd
v6737__034p = v6930_eel_bd_vtx_normals.reshape((70, 250, 3))

# op _02XS reshape_eval
# LANG: eel_bd_vtx_normals --> _02XT
# SHAPES: (70, 50, 5, 3) --> (70, 250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_k_vel
v6491__02XT = v6930_eel_bd_vtx_normals.reshape((70, 250, 3))

# op _02Xr_linear_combination_eval
# LANG: _02Xq --> eel_kinematic_vel
# SHAPES: (70, 250, 3) --> (70, 250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.KinematicVelocityComp
v7036_eel_kinematic_vel = -1*v6473__02Xq

# op _02Y3_indexed_passthrough_eval
# LANG: _02Y2 --> aic_M
# SHAPES: (70, 250, 345, 3) --> (70, 250, 345, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic
v6612_aic_M__temp[i_v6497__02Y2__02Y3_indexed_passthrough_eval] = v6497__02Y2.flatten()
v6612_aic_M = v6612_aic_M__temp.copy()

# op _030F_indexed_passthrough_eval
# LANG: _030E --> normal_concatenated_M_mat
# SHAPES: (70, 250, 3) --> (70, 250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_aic
v6611_normal_concatenated_M_mat__temp[i_v6614__030E__030F_indexed_passthrough_eval] = v6614__030E.flatten()
v6611_normal_concatenated_M_mat = v6611_normal_concatenated_M_mat__temp.copy()

# op _030P_indexed_passthrough_eval
# LANG: _030O --> aic_bd
# SHAPES: (70, 250, 250, 3) --> (70, 250, 250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.AssembleAic_bd
v6735_aic_bd__temp[i_v6620__030O__030P_indexed_passthrough_eval] = v6620__030O.flatten()
v6735_aic_bd = v6735_aic_bd__temp.copy()

# op _034q_indexed_passthrough_eval
# LANG: _034p --> normal_concatenated_aic_bd_proj
# SHAPES: (70, 250, 3) --> (70, 250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_aic_bd
v6734_normal_concatenated_aic_bd_proj__temp[i_v6737__034p__034q_indexed_passthrough_eval] = v6737__034p.flatten()
v6734_normal_concatenated_aic_bd_proj = v6734_normal_concatenated_aic_bd_proj__temp.copy()

# op _02XU_custom_explicit_eval
# LANG: _02XT, eel_kinematic_vel --> b
# SHAPES: (70, 250, 3), (70, 250, 3) --> (70, 250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_k_vel
temp = _02XU_custom_explicit_func_b.solve(v7036_eel_kinematic_vel, v6491__02XT)
v6492_b = temp[0].copy()

# op _030G_custom_explicit_eval
# LANG: normal_concatenated_M_mat, aic_M --> M_mat
# SHAPES: (70, 250, 3), (70, 250, 345, 3) --> (70, 250, 345)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_aic
temp = _030G_custom_explicit_func_M_mat.solve(v6612_aic_M, v6611_normal_concatenated_M_mat)
v6615_M_mat = temp[0].copy()

# op _034r_custom_explicit_eval
# LANG: normal_concatenated_aic_bd_proj, aic_bd --> aic_bd_proj
# SHAPES: (70, 250, 3), (70, 250, 250, 3) --> (70, 250, 250)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_aic_bd
temp = _034r_custom_explicit_func_aic_bd_proj.solve(v6735_aic_bd, v6734_normal_concatenated_aic_bd_proj)
v6738_aic_bd_proj = temp[0].copy()

# op _02Wn_indexed_passthrough_eval
# LANG: op_eel_gamma_w --> gamma_w
# SHAPES: (70, 69, 5) --> (70, 69, 5)
# full namespace: fish_model.combine_gamma_w
v6446_gamma_w__temp[i_v6758_op_eel_gamma_w__02Wn_indexed_passthrough_eval] = v6758_op_eel_gamma_w.flatten()
v6446_gamma_w = v6446_gamma_w__temp.copy()

# op _02WJ_newton_implict_eval
# LANG: M_mat, b, aic_bd_proj, gamma_w --> gamma_b
# SHAPES: (70, 250, 345), (70, 250), (70, 250, 250), (70, 69, 5) --> (70, 250)
# full namespace: fish_model.solve_gamma_b_group
_02WJ_newton.set_guess(initial_guess_v6911_gamma_b)
_02WJ_newton_out = _02WJ_newton.solve(v6738_aic_bd_proj, v6615_M_mat, v6446_gamma_w, v6492_b)
v6911_gamma_b = _02WJ_newton_out[0]

# op _02US_power_combination_eval
# LANG: _02Uw --> _02UT
# SHAPES: (70, 50, 5, 3) --> (70, 50, 5, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6380__02UT = (v6368__02Uw)
v6380__02UT = (v6380__02UT*_02US_coeff).reshape((70, 50, 5, 3))

# op _02UU_power_combination_eval
# LANG: _02UE --> _02UV
# SHAPES: (70, 50, 5, 3) --> (70, 50, 5, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6381__02UV = (v6373__02UE)
v6381__02UV = (v6381__02UV*_02UU_coeff).reshape((70, 50, 5, 3))

# op _02UW_linear_combination_eval
# LANG: _02UT, _02UV --> _02UX
# SHAPES: (70, 50, 5, 3), (70, 50, 5, 3) --> (70, 50, 5, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6382__02UX = v6380__02UT+v6381__02UV

# op _02UY_power_combination_eval
# LANG: _02Uz --> _02UZ
# SHAPES: (70, 50, 5, 3) --> (70, 50, 5, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6383__02UZ = (v6370__02Uz)
v6383__02UZ = (v6383__02UZ*_02UY_coeff).reshape((70, 50, 5, 3))

# op _0350_decompose_eval
# LANG: op_eel_wake_coords --> _0351
# SHAPES: (70, 69, 6, 3) --> (70, 69, 6, 3)
# full namespace: fish_model.EvalPtsVel.BdnWakeCombine
v6760__0351 = ((v6756_op_eel_wake_coords.flatten())[src_indices__0351__0350]).reshape((70, 69, 6, 3))

# op _02U__linear_combination_eval
# LANG: _02UX, _02UZ --> _02V0
# SHAPES: (70, 50, 5, 3), (70, 50, 5, 3) --> (70, 50, 5, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6384__02V0 = v6382__02UX+v6383__02UZ

# op _02V1_power_combination_eval
# LANG: _02TI --> _02V2
# SHAPES: (70, 50, 5, 3) --> (70, 50, 5, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6385__02V2 = (v6338__02TI)
v6385__02V2 = (v6385__02V2*_02V1_coeff).reshape((70, 50, 5, 3))

# op _034__indexed_passthrough_eval
# LANG: _0351, eel_bd_vtx_coords --> eel_bdnwake_coords
# SHAPES: (70, 69, 6, 3), (70, 51, 6, 3) --> (70, 120, 6, 3)
# full namespace: fish_model.EvalPtsVel.BdnWakeCombine
v6764_eel_bdnwake_coords__temp[i_v6755_eel_bd_vtx_coords__034__indexed_passthrough_eval] = v6755_eel_bd_vtx_coords.flatten()
v6764_eel_bdnwake_coords = v6764_eel_bdnwake_coords__temp.copy()
v6764_eel_bdnwake_coords__temp[i_v6760__0351__034__indexed_passthrough_eval] = v6760__0351.flatten()
v6764_eel_bdnwake_coords = v6764_eel_bdnwake_coords__temp.copy()

# op _02V3_linear_combination_eval
# LANG: _02V0, _02V2 --> eel_eval_pts_coords
# SHAPES: (70, 50, 5, 3), (70, 50, 5, 3) --> (70, 50, 5, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6896_eel_eval_pts_coords = v6384__02V0+v6385__02V2

# op _0358_decompose_eval
# LANG: eel_bdnwake_coords --> _0359, _035a, _035b, _035c
# SHAPES: (70, 120, 6, 3) --> (70, 119, 5, 3), (70, 119, 5, 3), (70, 119, 5, 3), (70, 119, 5, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6765__0359 = ((v6764_eel_bdnwake_coords.flatten())[src_indices__0359__0358]).reshape((70, 119, 5, 3))
v6766__035a = ((v6764_eel_bdnwake_coords.flatten())[src_indices__035a__0358]).reshape((70, 119, 5, 3))
v6767__035b = ((v6764_eel_bdnwake_coords.flatten())[src_indices__035b__0358]).reshape((70, 119, 5, 3))
v6768__035c = ((v6764_eel_bdnwake_coords.flatten())[src_indices__035c__0358]).reshape((70, 119, 5, 3))

# op _035D reshape_eval
# LANG: _035a --> _035E
# SHAPES: (70, 119, 5, 3) --> (70, 595, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6782__035E = v6766__035a.reshape((70, 595, 3))

# op _035R reshape_eval
# LANG: eel_eval_pts_coords --> _035S
# SHAPES: (70, 50, 5, 3) --> (70, 250, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6789__035S = v6896_eel_eval_pts_coords.reshape((70, 250, 3))

# op _035X reshape_eval
# LANG: _035b --> _035Y
# SHAPES: (70, 119, 5, 3) --> (70, 595, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6792__035Y = v6767__035b.reshape((70, 595, 3))

# op _035d reshape_eval
# LANG: eel_eval_pts_coords --> _035e
# SHAPES: (70, 50, 5, 3) --> (70, 250, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6769__035e = v6896_eel_eval_pts_coords.reshape((70, 250, 3))

# op _035j reshape_eval
# LANG: _0359 --> _035k
# SHAPES: (70, 119, 5, 3) --> (70, 595, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6772__035k = v6765__0359.reshape((70, 595, 3))

# op _035x reshape_eval
# LANG: eel_eval_pts_coords --> _035y
# SHAPES: (70, 50, 5, 3) --> (70, 250, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6779__035y = v6896_eel_eval_pts_coords.reshape((70, 250, 3))

# op _035F expand_array_eval
# LANG: _035E --> _035G
# SHAPES: (70, 595, 3) --> (70, 250, 595, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6783__035G = np.einsum('acd,b->abcd', v6782__035E.reshape((70, 595, 3)) ,np.ones((250,))).reshape((70, 250, 595, 3))

# op _035T expand_array_eval
# LANG: _035S --> _035U
# SHAPES: (70, 250, 3) --> (70, 250, 595, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6790__035U = np.einsum('abd,c->abcd', v6789__035S.reshape((70, 250, 3)) ,np.ones((595,))).reshape((70, 250, 595, 3))

# op _035Z expand_array_eval
# LANG: _035Y --> _035_
# SHAPES: (70, 595, 3) --> (70, 250, 595, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6793__035_ = np.einsum('acd,b->abcd', v6792__035Y.reshape((70, 595, 3)) ,np.ones((250,))).reshape((70, 250, 595, 3))

# op _035f expand_array_eval
# LANG: _035e --> _035g
# SHAPES: (70, 250, 3) --> (70, 250, 595, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6770__035g = np.einsum('abd,c->abcd', v6769__035e.reshape((70, 250, 3)) ,np.ones((595,))).reshape((70, 250, 595, 3))

# op _035l expand_array_eval
# LANG: _035k --> _035m
# SHAPES: (70, 595, 3) --> (70, 250, 595, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6773__035m = np.einsum('acd,b->abcd', v6772__035k.reshape((70, 595, 3)) ,np.ones((250,))).reshape((70, 250, 595, 3))

# op _035z expand_array_eval
# LANG: _035y --> _035A
# SHAPES: (70, 250, 3) --> (70, 250, 595, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6780__035A = np.einsum('abd,c->abcd', v6779__035y.reshape((70, 250, 3)) ,np.ones((595,))).reshape((70, 250, 595, 3))

# op _036a reshape_eval
# LANG: eel_eval_pts_coords --> _036b
# SHAPES: (70, 50, 5, 3) --> (70, 250, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6799__036b = v6896_eel_eval_pts_coords.reshape((70, 250, 3))

# op _036g reshape_eval
# LANG: _035c --> _036h
# SHAPES: (70, 119, 5, 3) --> (70, 595, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6802__036h = v6768__035c.reshape((70, 595, 3))

# op _035B reshape_eval
# LANG: _035A --> _035C
# SHAPES: (70, 250, 595, 3) --> (70, 148750, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6781__035C = v6780__035A.reshape((70, 148750, 3))

# op _035H reshape_eval
# LANG: _035G --> _035I
# SHAPES: (70, 250, 595, 3) --> (70, 148750, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6784__035I = v6783__035G.reshape((70, 148750, 3))

# op _035V reshape_eval
# LANG: _035U --> _035W
# SHAPES: (70, 250, 595, 3) --> (70, 148750, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6791__035W = v6790__035U.reshape((70, 148750, 3))

# op _035h reshape_eval
# LANG: _035g --> _035i
# SHAPES: (70, 250, 595, 3) --> (70, 148750, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6771__035i = v6770__035g.reshape((70, 148750, 3))

# op _035n reshape_eval
# LANG: _035m --> _035o
# SHAPES: (70, 250, 595, 3) --> (70, 148750, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6774__035o = v6773__035m.reshape((70, 148750, 3))

# op _0360 reshape_eval
# LANG: _035_ --> _0361
# SHAPES: (70, 250, 595, 3) --> (70, 148750, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6794__0361 = v6793__035_.reshape((70, 148750, 3))

# op _036c expand_array_eval
# LANG: _036b --> _036d
# SHAPES: (70, 250, 3) --> (70, 250, 595, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6800__036d = np.einsum('abd,c->abcd', v6799__036b.reshape((70, 250, 3)) ,np.ones((595,))).reshape((70, 250, 595, 3))

# op _036i expand_array_eval
# LANG: _036h --> _036j
# SHAPES: (70, 595, 3) --> (70, 250, 595, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6803__036j = np.einsum('acd,b->abcd', v6802__036h.reshape((70, 595, 3)) ,np.ones((250,))).reshape((70, 250, 595, 3))

# op _035J_linear_combination_eval
# LANG: _035C, _035I --> _035K
# SHAPES: (70, 148750, 3), (70, 148750, 3) --> (70, 148750, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6785__035K = v6781__035C+-1*v6784__035I

# op _035p_linear_combination_eval
# LANG: _035i, _035o --> _035q
# SHAPES: (70, 148750, 3), (70, 148750, 3) --> (70, 148750, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6775__035q = v6771__035i+-1*v6774__035o

# op _0362_linear_combination_eval
# LANG: _035W, _0361 --> _0363
# SHAPES: (70, 148750, 3), (70, 148750, 3) --> (70, 148750, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6795__0363 = v6791__035W+-1*v6794__0361

# op _036e reshape_eval
# LANG: _036d --> _036f
# SHAPES: (70, 250, 595, 3) --> (70, 148750, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6801__036f = v6800__036d.reshape((70, 148750, 3))

# op _036k reshape_eval
# LANG: _036j --> _036l
# SHAPES: (70, 250, 595, 3) --> (70, 148750, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6804__036l = v6803__036j.reshape((70, 148750, 3))

# op _035L_power_combination_eval
# LANG: _035K --> _035M
# SHAPES: (70, 148750, 3) --> (70, 148750, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6786__035M = (v6785__035K**2)
v6786__035M = v6786__035M.reshape((70, 148750, 3))

# op _035r_power_combination_eval
# LANG: _035q --> _035s
# SHAPES: (70, 148750, 3) --> (70, 148750, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6776__035s = (v6775__035q**2)
v6776__035s = v6776__035s.reshape((70, 148750, 3))

# op _0364_power_combination_eval
# LANG: _0363 --> _0365
# SHAPES: (70, 148750, 3) --> (70, 148750, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6796__0365 = (v6795__0363**2)
v6796__0365 = v6796__0365.reshape((70, 148750, 3))

# op _036m_linear_combination_eval
# LANG: _036f, _036l --> _036n
# SHAPES: (70, 148750, 3), (70, 148750, 3) --> (70, 148750, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6805__036n = v6801__036f+-1*v6804__036l

# op _035N_single_tensor_sum_with_axis_eval
# LANG: _035M --> _035O
# SHAPES: (70, 148750, 3) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6787__035O = np.sum(v6786__035M, axis = (2,)).reshape((70, 148750))

# op _035t_single_tensor_sum_with_axis_eval
# LANG: _035s --> _035u
# SHAPES: (70, 148750, 3) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6777__035u = np.sum(v6776__035s, axis = (2,)).reshape((70, 148750))

# op _0366_single_tensor_sum_with_axis_eval
# LANG: _0365 --> _0367
# SHAPES: (70, 148750, 3) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6797__0367 = np.sum(v6796__0365, axis = (2,)).reshape((70, 148750))

# op _036o_power_combination_eval
# LANG: _036n --> _036p
# SHAPES: (70, 148750, 3) --> (70, 148750, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6806__036p = (v6805__036n**2)
v6806__036p = v6806__036p.reshape((70, 148750, 3))

# op _035P_power_combination_eval
# LANG: _035O --> _035Q
# SHAPES: (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6788__035Q = (v6787__035O**0.5)
v6788__035Q = v6788__035Q.reshape((70, 148750))

# op _035v_power_combination_eval
# LANG: _035u --> _035w
# SHAPES: (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6778__035w = (v6777__035u**0.5)
v6778__035w = v6778__035w.reshape((70, 148750))

# op _0368_power_combination_eval
# LANG: _0367 --> _0369
# SHAPES: (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6798__0369 = (v6797__0367**0.5)
v6798__0369 = v6798__0369.reshape((70, 148750))

# op _036q_single_tensor_sum_with_axis_eval
# LANG: _036p --> _036r
# SHAPES: (70, 148750, 3) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6807__036r = np.sum(v6806__036p, axis = (2,)).reshape((70, 148750))

# op _036y_power_combination_eval
# LANG: _035q, _035K --> _036z
# SHAPES: (70, 148750, 3), (70, 148750, 3) --> (70, 148750, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6811__036z = (v6775__035q)*(v6785__035K)
v6811__036z = v6811__036z.reshape((70, 148750, 3))

# op _0373_power_combination_eval
# LANG: _0363, _035K --> _0374
# SHAPES: (70, 148750, 3), (70, 148750, 3) --> (70, 148750, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6827__0374 = (v6785__035K)*(v6795__0363)
v6827__0374 = v6827__0374.reshape((70, 148750, 3))

# op _036A_single_tensor_sum_with_axis_eval
# LANG: _036z --> _036B
# SHAPES: (70, 148750, 3) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6812__036B = np.sum(v6811__036z, axis = (2,)).reshape((70, 148750))

# op _036C_power_combination_eval
# LANG: _035w, _035Q --> _036D
# SHAPES: (70, 148750), (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6813__036D = (v6778__035w)*(v6788__035Q)
v6813__036D = v6813__036D.reshape((70, 148750))

# op _036s_power_combination_eval
# LANG: _036r --> _036t
# SHAPES: (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6808__036t = (v6807__036r**0.5)
v6808__036t = v6808__036t.reshape((70, 148750))

# op _0375_single_tensor_sum_with_axis_eval
# LANG: _0374 --> _0376
# SHAPES: (70, 148750, 3) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6828__0376 = np.sum(v6827__0374, axis = (2,)).reshape((70, 148750))

# op _0377_power_combination_eval
# LANG: _0369, _035Q --> _0378
# SHAPES: (70, 148750), (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6829__0378 = (v6788__035Q)*(v6798__0369)
v6829__0378 = v6829__0378.reshape((70, 148750))

# op _037z_power_combination_eval
# LANG: _036n, _0363 --> _037A
# SHAPES: (70, 148750, 3), (70, 148750, 3) --> (70, 148750, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6843__037A = (v6795__0363)*(v6805__036n)
v6843__037A = v6843__037A.reshape((70, 148750, 3))

# op _036E_linear_combination_eval
# LANG: _036D, _036B --> _036F
# SHAPES: (70, 148750), (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6814__036F = v6813__036D+v6812__036B

# op _036K_linear_combination_eval
# LANG: _035w --> _036L
# SHAPES: (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6817__036L = _036K_constant+v6778__035w

# op _036O_linear_combination_eval
# LANG: _035Q --> _036P
# SHAPES: (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6819__036P = _036O_constant+v6788__035Q

# op _0379_linear_combination_eval
# LANG: _0378, _0376 --> _037a
# SHAPES: (70, 148750), (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6830__037a = v6829__0378+v6828__0376

# op _037B_single_tensor_sum_with_axis_eval
# LANG: _037A --> _037C
# SHAPES: (70, 148750, 3) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6844__037C = np.sum(v6843__037A, axis = (2,)).reshape((70, 148750))

# op _037D_power_combination_eval
# LANG: _036t, _0369 --> _037E
# SHAPES: (70, 148750), (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6845__037E = (v6798__0369)*(v6808__036t)
v6845__037E = v6845__037E.reshape((70, 148750))

# op _037f_linear_combination_eval
# LANG: _035Q --> _037g
# SHAPES: (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6833__037g = _037f_constant+v6788__035Q

# op _037j_linear_combination_eval
# LANG: _0369 --> _037k
# SHAPES: (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6835__037k = _037j_constant+v6798__0369

# op _0384_power_combination_eval
# LANG: _036n, _035q --> _0385
# SHAPES: (70, 148750, 3), (70, 148750, 3) --> (70, 148750, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6859__0385 = (v6805__036n)*(v6775__035q)
v6859__0385 = v6859__0385.reshape((70, 148750, 3))

# op _036G_linear_combination_eval
# LANG: _036F --> _036H
# SHAPES: (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6815__036H = _036G_constant+v6814__036F

# op _036M_power_combination_eval
# LANG: _036L --> _036N
# SHAPES: (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6818__036N = (v6817__036L**-1)
v6818__036N = v6818__036N.reshape((70, 148750))

# op _036Q_power_combination_eval
# LANG: _036P --> _036R
# SHAPES: (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6820__036R = (v6819__036P**-1)
v6820__036R = v6820__036R.reshape((70, 148750))

# op _037F_linear_combination_eval
# LANG: _037E, _037C --> _037G
# SHAPES: (70, 148750), (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6846__037G = v6845__037E+v6844__037C

# op _037L_linear_combination_eval
# LANG: _0369 --> _037M
# SHAPES: (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6849__037M = _037L_constant+v6798__0369

# op _037P_linear_combination_eval
# LANG: _036t --> _037Q
# SHAPES: (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6851__037Q = _037P_constant+v6808__036t

# op _037b_linear_combination_eval
# LANG: _037a --> _037c
# SHAPES: (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6831__037c = _037b_constant+v6830__037a

# op _037h_power_combination_eval
# LANG: _037g --> _037i
# SHAPES: (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6834__037i = (v6833__037g**-1)
v6834__037i = v6834__037i.reshape((70, 148750))

# op _037l_power_combination_eval
# LANG: _037k --> _037m
# SHAPES: (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6836__037m = (v6835__037k**-1)
v6836__037m = v6836__037m.reshape((70, 148750))

# op _0386_single_tensor_sum_with_axis_eval
# LANG: _0385 --> _0387
# SHAPES: (70, 148750, 3) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6860__0387 = np.sum(v6859__0385, axis = (2,)).reshape((70, 148750))

# op _0388_power_combination_eval
# LANG: _035w, _036t --> _0389
# SHAPES: (70, 148750), (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6861__0389 = (v6808__036t)*(v6778__035w)
v6861__0389 = v6861__0389.reshape((70, 148750))

# op _036I_power_combination_eval
# LANG: _036H --> _036J
# SHAPES: (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6816__036J = (v6815__036H**-1)
v6816__036J = v6816__036J.reshape((70, 148750))

# op _036S_linear_combination_eval
# LANG: _036N, _036R --> _036T
# SHAPES: (70, 148750), (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6821__036T = v6818__036N+v6820__036R

# op _037H_linear_combination_eval
# LANG: _037G --> _037I
# SHAPES: (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6847__037I = _037H_constant+v6846__037G

# op _037N_power_combination_eval
# LANG: _037M --> _037O
# SHAPES: (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6850__037O = (v6849__037M**-1)
v6850__037O = v6850__037O.reshape((70, 148750))

# op _037R_power_combination_eval
# LANG: _037Q --> _037S
# SHAPES: (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6852__037S = (v6851__037Q**-1)
v6852__037S = v6852__037S.reshape((70, 148750))

# op _037d_power_combination_eval
# LANG: _037c --> _037e
# SHAPES: (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6832__037e = (v6831__037c**-1)
v6832__037e = v6832__037e.reshape((70, 148750))

# op _037n_linear_combination_eval
# LANG: _037i, _037m --> _037o
# SHAPES: (70, 148750), (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6837__037o = v6834__037i+v6836__037m

# op _038a_linear_combination_eval
# LANG: _0389, _0387 --> _038b
# SHAPES: (70, 148750), (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6862__038b = v6861__0389+v6860__0387

# op _038g_linear_combination_eval
# LANG: _036t --> _038h
# SHAPES: (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6865__038h = _038g_constant+v6808__036t

# op _038k_linear_combination_eval
# LANG: _035w --> _038l
# SHAPES: (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6867__038l = _038k_constant+v6778__035w

# op _036U_power_combination_eval
# LANG: _036J, _036T --> num_036V
# SHAPES: (70, 148750), (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6822_num_036V = (v6816__036J)*(v6821__036T)
v6822_num_036V = v6822_num_036V.reshape((70, 148750))

# op _036_ cross_product_eval
# LANG: _0363, _035K --> _0370
# SHAPES: (70, 148750, 3), (70, 148750, 3) --> (70, 148750, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6825__0370 = np.cross(v6785__035K, v6795__0363, axisa = 2, axisb = 2, axisc = 2)

# op _036u cross_product_eval
# LANG: _035q, _035K --> _036v
# SHAPES: (70, 148750, 3), (70, 148750, 3) --> (70, 148750, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6809__036v = np.cross(v6775__035q, v6785__035K, axisa = 2, axisb = 2, axisc = 2)

# op _037J_power_combination_eval
# LANG: _037I --> _037K
# SHAPES: (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6848__037K = (v6847__037I**-1)
v6848__037K = v6848__037K.reshape((70, 148750))

# op _037T_linear_combination_eval
# LANG: _037O, _037S --> _037U
# SHAPES: (70, 148750), (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6853__037U = v6850__037O+v6852__037S

# op _037p_power_combination_eval
# LANG: _037e, _037o --> num_037q
# SHAPES: (70, 148750), (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6838_num_037q = (v6832__037e)*(v6837__037o)
v6838_num_037q = v6838_num_037q.reshape((70, 148750))

# op _038c_linear_combination_eval
# LANG: _038b --> _038d
# SHAPES: (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6863__038d = _038c_constant+v6862__038b

# op _038i_power_combination_eval
# LANG: _038h --> _038j
# SHAPES: (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6866__038j = (v6865__038h**-1)
v6866__038j = v6866__038j.reshape((70, 148750))

# op _038m_power_combination_eval
# LANG: _038l --> _038n
# SHAPES: (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6868__038n = (v6867__038l**-1)
v6868__038n = v6868__038n.reshape((70, 148750))

# op _036W expand_array_eval
# LANG: num_036V --> _036X
# SHAPES: (70, 148750) --> (70, 148750, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6823__036X = np.einsum('ab,c->abc', v6822_num_036V.reshape((70, 148750)) ,np.ones((3,))).reshape((70, 148750, 3))

# op _036w_power_combination_eval
# LANG: _036v --> _036x
# SHAPES: (70, 148750, 3) --> (70, 148750, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6810__036x = (v6809__036v)
v6810__036x = (v6810__036x*_036w_coeff).reshape((70, 148750, 3))

# op _0371_power_combination_eval
# LANG: _0370 --> _0372
# SHAPES: (70, 148750, 3) --> (70, 148750, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6826__0372 = (v6825__0370)
v6826__0372 = (v6826__0372*_0371_coeff).reshape((70, 148750, 3))

# op _037V_power_combination_eval
# LANG: _037K, _037U --> num_037W
# SHAPES: (70, 148750), (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6854_num_037W = (v6848__037K)*(v6853__037U)
v6854_num_037W = v6854_num_037W.reshape((70, 148750))

# op _037r expand_array_eval
# LANG: num_037q --> _037s
# SHAPES: (70, 148750) --> (70, 148750, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6839__037s = np.einsum('ab,c->abc', v6838_num_037q.reshape((70, 148750)) ,np.ones((3,))).reshape((70, 148750, 3))

# op _037v cross_product_eval
# LANG: _036n, _0363 --> _037w
# SHAPES: (70, 148750, 3), (70, 148750, 3) --> (70, 148750, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6841__037w = np.cross(v6795__0363, v6805__036n, axisa = 2, axisb = 2, axisc = 2)

# op _038e_power_combination_eval
# LANG: _038d --> _038f
# SHAPES: (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6864__038f = (v6863__038d**-1)
v6864__038f = v6864__038f.reshape((70, 148750))

# op _038o_linear_combination_eval
# LANG: _038j, _038n --> _038p
# SHAPES: (70, 148750), (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6869__038p = v6866__038j+v6868__038n

# op _036Y_power_combination_eval
# LANG: _036X, _036x --> _036Z
# SHAPES: (70, 148750, 3), (70, 148750, 3) --> (70, 148750, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6824__036Z = (v6823__036X)*(v6810__036x)
v6824__036Z = v6824__036Z.reshape((70, 148750, 3))

# op _037X expand_array_eval
# LANG: num_037W --> _037Y
# SHAPES: (70, 148750) --> (70, 148750, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6855__037Y = np.einsum('ab,c->abc', v6854_num_037W.reshape((70, 148750)) ,np.ones((3,))).reshape((70, 148750, 3))

# op _037t_power_combination_eval
# LANG: _037s, _0372 --> _037u
# SHAPES: (70, 148750, 3), (70, 148750, 3) --> (70, 148750, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6840__037u = (v6839__037s)*(v6826__0372)
v6840__037u = v6840__037u.reshape((70, 148750, 3))

# op _037x_power_combination_eval
# LANG: _037w --> _037y
# SHAPES: (70, 148750, 3) --> (70, 148750, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6842__037y = (v6841__037w)
v6842__037y = (v6842__037y*_037x_coeff).reshape((70, 148750, 3))

# op _0380 cross_product_eval
# LANG: _036n, _035q --> _0381
# SHAPES: (70, 148750, 3), (70, 148750, 3) --> (70, 148750, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6857__0381 = np.cross(v6805__036n, v6775__035q, axisa = 2, axisb = 2, axisc = 2)

# op _038q_power_combination_eval
# LANG: _038f, _038p --> num_038r
# SHAPES: (70, 148750), (70, 148750) --> (70, 148750)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6870_num_038r = (v6864__038f)*(v6869__038p)
v6870_num_038r = v6870_num_038r.reshape((70, 148750))

# op _037Z_power_combination_eval
# LANG: _037Y, _037y --> _037_
# SHAPES: (70, 148750, 3), (70, 148750, 3) --> (70, 148750, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6856__037_ = (v6855__037Y)*(v6842__037y)
v6856__037_ = v6856__037_.reshape((70, 148750, 3))

# op _0382_power_combination_eval
# LANG: _0381 --> _0383
# SHAPES: (70, 148750, 3) --> (70, 148750, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6858__0383 = (v6857__0381)
v6858__0383 = (v6858__0383*_0382_coeff).reshape((70, 148750, 3))

# op _038s expand_array_eval
# LANG: num_038r --> _038t
# SHAPES: (70, 148750) --> (70, 148750, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6871__038t = np.einsum('ab,c->abc', v6870_num_038r.reshape((70, 148750)) ,np.ones((3,))).reshape((70, 148750, 3))

# op _038w_linear_combination_eval
# LANG: _036Z, _037u --> _038x
# SHAPES: (70, 148750, 3), (70, 148750, 3) --> (70, 148750, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6873__038x = v6824__036Z+v6840__037u

# op _038u_power_combination_eval
# LANG: _038t, _0383 --> _038v
# SHAPES: (70, 148750, 3), (70, 148750, 3) --> (70, 148750, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6872__038v = (v6871__038t)*(v6858__0383)
v6872__038v = v6872__038v.reshape((70, 148750, 3))

# op _038y_linear_combination_eval
# LANG: _038x, _037_ --> _038z
# SHAPES: (70, 148750, 3), (70, 148750, 3) --> (70, 148750, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6874__038z = v6873__038x+v6856__037_

# op _034u_decompose_eval
# LANG: gamma_b --> eel_gamma_b
# SHAPES: (70, 250) --> (70, 250)
# full namespace: fish_model.seperate_gamma_b
v6757_eel_gamma_b = ((v6911_gamma_b.flatten())[src_indices_eel_gamma_b__034u]).reshape((70, 250))

# op _0354 reshape_eval
# LANG: op_eel_gamma_w --> _0355
# SHAPES: (70, 69, 5) --> (70, 345)
# full namespace: fish_model.EvalPtsVel.BdnWakeCombine
v6762__0355 = v6758_op_eel_gamma_w.reshape((70, 345))

# op _038A_linear_combination_eval
# LANG: _038z, _038v --> eel_eval_pts_coordseel_bdnwake_coords_out
# SHAPES: (70, 148750, 3), (70, 148750, 3) --> (70, 148750, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_aics0
v6876_eel_eval_pts_coordseel_bdnwake_coords_out = v6874__038z+v6872__038v

# op _0353_indexed_passthrough_eval
# LANG: _0355, eel_gamma_b --> eel_bdnwake_gamma
# SHAPES: (70, 345), (70, 250) --> (70, 595)
# full namespace: fish_model.EvalPtsVel.BdnWakeCombine
v6877_eel_bdnwake_gamma__temp[i_v6757_eel_gamma_b__0353_indexed_passthrough_eval] = v6757_eel_gamma_b.flatten()
v6877_eel_bdnwake_gamma = v6877_eel_bdnwake_gamma__temp.copy()
v6877_eel_bdnwake_gamma__temp[i_v6762__0355__0353_indexed_passthrough_eval] = v6762__0355.flatten()
v6877_eel_bdnwake_gamma = v6877_eel_bdnwake_gamma__temp.copy()

# op _038E reshape_eval
# LANG: eel_eval_pts_coordseel_bdnwake_coords_out --> eel_eval_pts_coordseel_bdnwake_coords_out_reshaped
# SHAPES: (70, 148750, 3) --> (70, 250, 595, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_ind_vel0
v6878_eel_eval_pts_coordseel_bdnwake_coords_out_reshaped = v6876_eel_eval_pts_coordseel_bdnwake_coords_out.reshape((70, 250, 595, 3))

# op _02T1_linear_combination_eval
# LANG: eel --> _02T2
# SHAPES: (70, 51, 6, 3) --> (70, 51, 6, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6312__02T2 = v7074_eel

# op _038G_custom_explicit_eval
# LANG: eel_eval_pts_coordseel_bdnwake_coords_out_reshaped, eel_bdnwake_gamma --> eel_eval_pts_coordseel_bdnwake_coords_induced_vel
# SHAPES: (70, 250, 595, 3), (70, 595) --> (70, 250, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_ind_vel0
temp = _038G_custom_explicit_func_eel_eval_pts_coordseel_bdnwake_coords_induced_vel.solve(v6878_eel_eval_pts_coordseel_bdnwake_coords_out_reshaped, v6877_eel_bdnwake_gamma)
v6879_eel_eval_pts_coordseel_bdnwake_coords_induced_vel = temp[0].copy()

# op _02Uc_decompose_eval
# LANG: _02T2 --> _02Ui, _02Ud, _02Ue, _02Uh
# SHAPES: (70, 51, 6, 3) --> (70, 50, 5, 3), (70, 50, 5, 3), (70, 50, 5, 3), (70, 50, 5, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6356__02Ud = ((v6312__02T2.flatten())[src_indices__02Ud__02Uc]).reshape((70, 50, 5, 3))
v6357__02Ue = ((v6312__02T2.flatten())[src_indices__02Ue__02Uc]).reshape((70, 50, 5, 3))
v6359__02Uh = ((v6312__02T2.flatten())[src_indices__02Uh__02Uc]).reshape((70, 50, 5, 3))
v6360__02Ui = ((v6312__02T2.flatten())[src_indices__02Ui__02Uc]).reshape((70, 50, 5, 3))

# op _02Uf_linear_combination_eval
# LANG: _02Ud, _02Ue --> _02Ug
# SHAPES: (70, 50, 5, 3), (70, 50, 5, 3) --> (70, 50, 5, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6358__02Ug = v6356__02Ud+-1*v6357__02Ue

# op _02Uj_linear_combination_eval
# LANG: _02Uh, _02Ui --> _02Uk
# SHAPES: (70, 50, 5, 3), (70, 50, 5, 3) --> (70, 50, 5, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6361__02Uk = v6359__02Uh+-1*v6360__02Ui

# op _02Ul cross_product_eval
# LANG: _02Ug, _02Uk --> _02Um
# SHAPES: (70, 50, 5, 3), (70, 50, 5, 3) --> (70, 50, 5, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6362__02Um = np.cross(v6358__02Ug, v6361__02Uk, axisa = 3, axisb = 3, axisc = 3)

# op _02Un_power_combination_eval
# LANG: _02Um --> _02Uo
# SHAPES: (70, 50, 5, 3) --> (70, 50, 5, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6363__02Uo = (v6362__02Um**2)
v6363__02Uo = v6363__02Uo.reshape((70, 50, 5, 3))

# op _02Up_single_tensor_sum_with_axis_eval
# LANG: _02Uo --> _02Uq
# SHAPES: (70, 50, 5, 3) --> (70, 50, 5)
# full namespace: fish_model.MeshPreprocessing_comp
v6364__02Uq = np.sum(v6363__02Uo, axis = (3,)).reshape((70, 50, 5))

# op _034y_custom_explicit_eval
# LANG: mtx, gamma_b --> horseshoe_circulation
# SHAPES: (250, 250), (70, 250) --> (70, 250)
# full namespace: fish_model.compute_horseshoe_circulation
temp = _034y_custom_explicit_func_horseshoe_circulation.solve(v6741_mtx, v6911_gamma_b)
v6887_horseshoe_circulation = temp[0].copy()

# op _02Ur_power_combination_eval
# LANG: _02Uq --> _02Us
# SHAPES: (70, 50, 5) --> (70, 50, 5)
# full namespace: fish_model.MeshPreprocessing_comp
v6365__02Us = (v6364__02Uq**0.5)
v6365__02Us = v6365__02Us.reshape((70, 50, 5))

# op _02Ut_power_combination_eval
# LANG: _02Us --> eel_s_panel
# SHAPES: (70, 50, 5) --> (70, 50, 5)
# full namespace: fish_model.MeshPreprocessing_comp
v7085_eel_s_panel = (v6365__02Us)
v7085_eel_s_panel = (v7085_eel_s_panel*_02Ut_coeff).reshape((70, 50, 5))

# op _0392 reshape_eval
# LANG: eel_s_panel --> _0393
# SHAPES: (70, 50, 5) --> (70, 250)
# full namespace: fish_model.ThrustDrag
v6897__0393 = v7085_eel_s_panel.reshape((70, 250))

# op _02UA_power_combination_eval
# LANG: _02Uz --> _02UB
# SHAPES: (70, 50, 5, 3) --> (70, 50, 5, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6371__02UB = (v6370__02Uz)
v6371__02UB = (v6371__02UB*_02UA_coeff).reshape((70, 50, 5, 3))

# op _02Ux_power_combination_eval
# LANG: _02Uw --> _02Uy
# SHAPES: (70, 50, 5, 3) --> (70, 50, 5, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6369__02Uy = (v6368__02Uw)
v6369__02Uy = (v6369__02Uy*_02Ux_coeff).reshape((70, 50, 5, 3))

# op _0394_indexed_passthrough_eval
# LANG: _0393 --> s_panels_all
# SHAPES: (70, 250) --> (70, 250)
# full namespace: fish_model.ThrustDrag
v6890_s_panels_all__temp[i_v6897__0393__0394_indexed_passthrough_eval] = v6897__0393.flatten()
v6890_s_panels_all = v6890_s_panels_all__temp.copy()

# op _02UC_linear_combination_eval
# LANG: _02Uy, _02UB --> _02UD
# SHAPES: (70, 50, 5, 3), (70, 50, 5, 3) --> (70, 50, 5, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6372__02UD = v6369__02Uy+v6371__02UB

# op _02UF_power_combination_eval
# LANG: _02UE --> _02UG
# SHAPES: (70, 50, 5, 3) --> (70, 50, 5, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6374__02UG = (v6373__02UE)
v6374__02UG = (v6374__02UG*_02UF_coeff).reshape((70, 50, 5, 3))

# op _034G reshape_eval
# LANG: eel_eval_pts_coordseel_bdnwake_coords_induced_vel --> _034H
# SHAPES: (70, 250, 3) --> (70, 1, 250, 3)
# full namespace: fish_model.EvalPtsVel
v6747__034H = v6879_eel_eval_pts_coordseel_bdnwake_coords_induced_vel.reshape((70, 1, 250, 3))

# op _039w_power_combination_eval
# LANG: s_panels_all, gamma_b --> _039x
# SHAPES: (70, 250), (70, 250) --> (70, 250)
# full namespace: fish_model.ThrustDrag
v6912__039x = (v6911_gamma_b)*(v6890_s_panels_all)
v6912__039x = v6912__039x.reshape((70, 250))

# op _02UH_linear_combination_eval
# LANG: _02UD, _02UG --> _02UI
# SHAPES: (70, 50, 5, 3), (70, 50, 5, 3) --> (70, 50, 5, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6375__02UI = v6372__02UD+v6374__02UG

# op _02UJ_power_combination_eval
# LANG: _02TI --> _02UK
# SHAPES: (70, 50, 5, 3) --> (70, 50, 5, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6376__02UK = (v6338__02TI)
v6376__02UK = (v6376__02UK*_02UJ_coeff).reshape((70, 50, 5, 3))

# op _034I_indexed_passthrough_eval
# LANG: _034H --> eel_eval_pts_coords_eval_pts_induced_vel_col
# SHAPES: (70, 1, 250, 3) --> (70, 1, 250, 3)
# full namespace: fish_model.EvalPtsVel
v6745_eel_eval_pts_coords_eval_pts_induced_vel_col__temp[i_v6747__034H__034I_indexed_passthrough_eval] = v6747__034H.flatten()
v6745_eel_eval_pts_coords_eval_pts_induced_vel_col = v6745_eel_eval_pts_coords_eval_pts_induced_vel_col__temp.copy()

# op _039y expand_array_eval
# LANG: _039x --> _039z
# SHAPES: (70, 250) --> (70, 250, 3)
# full namespace: fish_model.ThrustDrag
v6913__039z = np.einsum('ab,c->abc', v6912__039x.reshape((70, 250)) ,np.ones((3,))).reshape((70, 250, 3))

# op _02UL_linear_combination_eval
# LANG: _02UI, _02UK --> _02UM
# SHAPES: (70, 50, 5, 3), (70, 50, 5, 3) --> (70, 50, 5, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6377__02UM = v6375__02UI+v6376__02UK

# op _034J_single_tensor_sum_with_axis_eval
# LANG: eel_eval_pts_coords_eval_pts_induced_vel_col --> eel_eval_pts_induced_vel
# SHAPES: (70, 1, 250, 3) --> (70, 250, 3)
# full namespace: fish_model.EvalPtsVel
v6749_eel_eval_pts_induced_vel = np.sum(v6745_eel_eval_pts_coords_eval_pts_induced_vel_col, axis = (1,)).reshape((70, 250, 3))

# op _039N_decompose_eval
# LANG: _039z --> _039V, _039O, _039U
# SHAPES: (70, 250, 3) --> (69, 250, 3), (1, 250, 3), (69, 250, 3)
# full namespace: fish_model.ThrustDrag
v6922__039O = ((v6913__039z.flatten())[src_indices__039O__039N]).reshape((1, 250, 3))
v6925__039U = ((v6913__039z.flatten())[src_indices__039U__039N]).reshape((69, 250, 3))
v6926__039V = ((v6913__039z.flatten())[src_indices__039V__039N]).reshape((69, 250, 3))

# op _02UN reshape_eval
# LANG: _02UM --> _02UO
# SHAPES: (70, 50, 5, 3) --> (70, 250, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6378__02UO = v6377__02UM.reshape((70, 250, 3))

# op _034Q_linear_combination_eval
# LANG: eel_kinematic_vel, eel_eval_pts_induced_vel --> _034R
# SHAPES: (70, 250, 3), (70, 250, 3) --> (70, 250, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_total_vel
v6753__034R = v6749_eel_eval_pts_induced_vel+v7036_eel_kinematic_vel

# op _039P expand_scalar_eval
# LANG: delta_t --> _039Q
# SHAPES: (1,) --> (1, 250, 3)
# full namespace: fish_model.ThrustDrag
v6923__039Q = np.empty((1, 250, 3))
v6923__039Q.fill(v6921_delta_t.item())

# op _039W_linear_combination_eval
# LANG: _039U, _039V --> _039X
# SHAPES: (69, 250, 3), (69, 250, 3) --> (69, 250, 3)
# full namespace: fish_model.ThrustDrag
v6927__039X = v6925__039U+-1*v6926__039V

# op _039Y expand_scalar_eval
# LANG: delta_t --> _039Z
# SHAPES: (1,) --> (69, 250, 3)
# full namespace: fish_model.ThrustDrag
v6928__039Z = np.empty((69, 250, 3))
v6928__039Z.fill(v6921_delta_t.item())

# op _02UP_linear_combination_eval
# LANG: _02UO --> _02UQ
# SHAPES: (70, 250, 3) --> (70, 250, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6379__02UQ = -1*v6378__02UO

# op _034S reshape_eval
# LANG: _034R --> eel_eval_total_vel
# SHAPES: (70, 250, 3) --> (70, 250, 3)
# full namespace: fish_model.EvalPtsVel.eval_pts_total_vel
v6892_eel_eval_total_vel = v6753__034R.reshape((70, 250, 3))

# op _038K reshape_eval
# LANG: density --> _038L
# SHAPES: (70, 1) --> (70,)
# full namespace: fish_model.ThrustDrag
v6882__038L = v6881_density.reshape((70,))

# op _039R_power_combination_eval
# LANG: _039O, _039Q --> _039S
# SHAPES: (1, 250, 3), (1, 250, 3) --> (1, 250, 3)
# full namespace: fish_model.ThrustDrag
v6924__039S = (v6922__039O)*(v6923__039Q**-1)
v6924__039S = v6924__039S.reshape((1, 250, 3))

# op _039__power_combination_eval
# LANG: _039X, _039Z --> _03a0
# SHAPES: (69, 250, 3), (69, 250, 3) --> (69, 250, 3)
# full namespace: fish_model.ThrustDrag
v6929__03a0 = (v6927__039X)*(v6928__039Z**-1)
v6929__03a0 = v6929__03a0.reshape((69, 250, 3))

# op _02UR_indexed_passthrough_eval
# LANG: _02UQ --> bd_vec
# SHAPES: (70, 250, 3) --> (70, 250, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6886_bd_vec__temp[i_v6379__02UQ__02UR_indexed_passthrough_eval] = v6379__02UQ.flatten()
v6886_bd_vec = v6886_bd_vec__temp.copy()

# op _038M expand_array_eval
# LANG: _038L --> rho_expand
# SHAPES: (70,) --> (70, 250, 3)
# full namespace: fish_model.ThrustDrag
v6883_rho_expand = np.einsum('a,bc->abc', v6882__038L.reshape((70,)) ,np.ones((250, 3))).reshape((70, 250, 3))

# op _038S expand_array_eval
# LANG: horseshoe_circulation --> _038T
# SHAPES: (70, 250) --> (70, 250, 3)
# full namespace: fish_model.ThrustDrag
v6888__038T = np.einsum('ab,c->abc', v6887_horseshoe_circulation.reshape((70, 250)) ,np.ones((3,))).reshape((70, 250, 3))

# op _0391_indexed_passthrough_eval
# LANG: eel_eval_total_vel --> eval_total_vel
# SHAPES: (70, 250, 3) --> (70, 250, 3)
# full namespace: fish_model.ThrustDrag
v6889_eval_total_vel__temp[i_v6892_eel_eval_total_vel__0391_indexed_passthrough_eval] = v6892_eel_eval_total_vel.flatten()
v6889_eval_total_vel = v6889_eval_total_vel__temp.copy()

# op _039T_indexed_passthrough_eval
# LANG: _039S, _03a0 --> dcirculation_repeat_dt
# SHAPES: (1, 250, 3), (69, 250, 3) --> (70, 250, 3)
# full namespace: fish_model.ThrustDrag
v6920_dcirculation_repeat_dt__temp[i_v6924__039S__039T_indexed_passthrough_eval] = v6924__039S.flatten()
v6920_dcirculation_repeat_dt = v6920_dcirculation_repeat_dt__temp.copy()
v6920_dcirculation_repeat_dt__temp[i_v6929__03a0__039T_indexed_passthrough_eval] = v6929__03a0.flatten()
v6920_dcirculation_repeat_dt = v6920_dcirculation_repeat_dt__temp.copy()

# op _03ec_decompose_eval
# LANG: eel --> _03ed
# SHAPES: (70, 51, 6, 3) --> (1, 50, 1, 1)
# full namespace: EelViscousModel
v7075__03ed = ((v7074_eel.flatten())[src_indices__03ed__03ec]).reshape((1, 50, 1, 1))

# op _039o_power_combination_eval
# LANG: rho_expand, _038T --> _039p
# SHAPES: (70, 250, 3), (70, 250, 3) --> (70, 250, 3)
# full namespace: fish_model.ThrustDrag
v6907__039p = (v6883_rho_expand)*(v6888__038T)
v6907__039p = v6907__039p.reshape((70, 250, 3))

# op _039q cross_product_eval
# LANG: eval_total_vel, bd_vec --> _039r
# SHAPES: (70, 250, 3), (70, 250, 3) --> (70, 250, 3)
# full namespace: fish_model.ThrustDrag
v6908__039r = np.cross(v6889_eval_total_vel, v6886_bd_vec, axisa = 2, axisb = 2, axisc = 2)

# op _03a2_power_combination_eval
# LANG: rho_expand, dcirculation_repeat_dt --> _03a3
# SHAPES: (70, 250, 3), (70, 250, 3) --> (70, 250, 3)
# full namespace: fish_model.ThrustDrag
v6931__03a3 = (v6883_rho_expand)*(v6920_dcirculation_repeat_dt)
v6931__03a3 = v6931__03a3.reshape((70, 250, 3))

# op _03ee reshape_eval
# LANG: _03ed --> _03ef
# SHAPES: (1, 50, 1, 1) --> (50,)
# full namespace: EelViscousModel
v7076__03ef = v7075__03ed.reshape((50,))

# op _039s_power_combination_eval
# LANG: _039p, _039r --> panel_forces
# SHAPES: (70, 250, 3), (70, 250, 3) --> (70, 250, 3)
# full namespace: fish_model.ThrustDrag
v6909_panel_forces = (v6907__039p)*(v6908__039r)
v6909_panel_forces = v6909_panel_forces.reshape((70, 250, 3))

# op _03a4_power_combination_eval
# LANG: _03a3, eel_bd_vtx_normals --> panel_forces_dynamic
# SHAPES: (70, 250, 3), (70, 250, 3) --> (70, 250, 3)
# full namespace: fish_model.ThrustDrag
v6930_eel_bd_vtx_normals = v6930_eel_bd_vtx_normals.reshape((70, 250, 3))
v6932_panel_forces_dynamic = (v6931__03a3)*(v6930_eel_bd_vtx_normals)
v6932_panel_forces_dynamic = v6932_panel_forces_dynamic.reshape((70, 250, 3))
v6930_eel_bd_vtx_normals = v6930_eel_bd_vtx_normals.reshape((70, 50, 5, 3))

# op _03ak_decompose_eval
# LANG: frame_vel --> _03at, _03al, _03ao
# SHAPES: (70, 3) --> (70, 1), (70, 1), (70, 1)
# full namespace: fish_model.ThrustDrag
v6942__03al = ((v6880_frame_vel.flatten())[src_indices__03al__03ak]).reshape((70, 1))
v6944__03ao = ((v6880_frame_vel.flatten())[src_indices__03ao__03ak]).reshape((70, 1))
v6947__03at = ((v6880_frame_vel.flatten())[src_indices__03at__03ak]).reshape((70, 1))

# op _03eg expand_scalar_eval
# LANG: v_x --> _03eh
# SHAPES: (1,) --> (50,)
# full namespace: EelViscousModel
v7077__03eh = np.empty((50,))
v7077__03eh.fill(v7073_v_x.item())

# op _03ek_power_combination_eval
# LANG: _03ef --> _03el
# SHAPES: (50,) --> (50,)
# full namespace: EelViscousModel
v7079__03el = (v7076__03ef)
v7079__03el = (v7079__03el*_03ek_coeff).reshape((50,))

# op _0398_sin_eval
# LANG: alpha --> _0399
# SHAPES: (70, 1) --> (70, 1)
# full namespace: fish_model.ThrustDrag
v6899__0399 = np.sin(v6884_alpha)

# op _039c_cos_eval
# LANG: alpha --> _039d
# SHAPES: (70, 1) --> (70, 1)
# full namespace: fish_model.ThrustDrag
v6901__039d = np.cos(v6884_alpha)

# op _03a6_decompose_eval
# LANG: panel_forces --> _03ag, _03a7, _03ac
# SHAPES: (70, 250, 3) --> (70, 250, 1), (70, 250, 1), (70, 250, 1)
# full namespace: fish_model.ThrustDrag
v6933__03a7 = ((v6909_panel_forces.flatten())[src_indices__03a7__03a6]).reshape((70, 250, 1))
v6936__03ac = ((v6909_panel_forces.flatten())[src_indices__03ac__03a6]).reshape((70, 250, 1))
v6939__03ag = ((v6909_panel_forces.flatten())[src_indices__03ag__03a6]).reshape((70, 250, 1))

# op _03a8_decompose_eval
# LANG: panel_forces_dynamic --> _03ah, _03a9, _03ad
# SHAPES: (70, 250, 3) --> (70, 250, 1), (70, 250, 1), (70, 250, 1)
# full namespace: fish_model.ThrustDrag
v6934__03a9 = ((v6932_panel_forces_dynamic.flatten())[src_indices__03a9__03a8]).reshape((70, 250, 1))
v6937__03ad = ((v6932_panel_forces_dynamic.flatten())[src_indices__03ad__03a8]).reshape((70, 250, 1))
v6940__03ah = ((v6932_panel_forces_dynamic.flatten())[src_indices__03ah__03a8]).reshape((70, 250, 1))

# op _03am_power_combination_eval
# LANG: _03al --> _03an
# SHAPES: (70, 1) --> (70, 1)
# full namespace: fish_model.ThrustDrag
v6943__03an = (v6942__03al**2)
v6943__03an = v6943__03an.reshape((70, 1))

# op _03ap_power_combination_eval
# LANG: _03ao --> _03aq
# SHAPES: (70, 1) --> (70, 1)
# full namespace: fish_model.ThrustDrag
v6945__03aq = (v6944__03ao**2)
v6945__03aq = v6945__03aq.reshape((70, 1))

# op _03bA_single_tensor_sum_with_axis_eval
# LANG: panel_forces --> _03bB
# SHAPES: (70, 250, 3) --> (70, 3)
# full namespace: fish_model.ThrustDrag
v6983__03bB = np.sum(v6909_panel_forces, axis = (1,)).reshape((70, 3))

# op _03dh_decompose_eval
# LANG: eel_kinematic_vel --> _03dp, _03di, _03do
# SHAPES: (70, 250, 3) --> (70, 250, 1), (70, 250, 1), (70, 250, 1)
# full namespace: EfficiencyModel
v7042__03di = ((v7036_eel_kinematic_vel.flatten())[src_indices__03di__03dh]).reshape((70, 250, 1))
v7045__03do = ((v7036_eel_kinematic_vel.flatten())[src_indices__03do__03dh]).reshape((70, 250, 1))
v7046__03dp = ((v7036_eel_kinematic_vel.flatten())[src_indices__03dp__03dh]).reshape((70, 250, 1))

# op _03dj expand_scalar_eval
# LANG: v_x --> _03dk
# SHAPES: (1,) --> (70, 250, 1)
# full namespace: EfficiencyModel
v7043__03dk = np.empty((70, 250, 1))
v7043__03dk.fill(v7073_v_x.item())

# op _03em_power_combination_eval
# LANG: _03eh, _03el --> _03en
# SHAPES: (50,), (50,) --> (50,)
# full namespace: EelViscousModel
v7080__03en = (v7077__03eh)*(v7079__03el)
v7080__03en = v7080__03en.reshape((50,))

# op _02TP_linear_combination_eval
# LANG: _02T5, _02T8 --> _02TQ
# SHAPES: (70, 50, 6, 3), (70, 50, 6, 3) --> (70, 50, 6, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6342__02TQ = v6314__02T5+-1*v6316__02T8

# op _0395 reshape_eval
# LANG: eel_eval_pts_coords --> _0396
# SHAPES: (70, 50, 5, 3) --> (70, 250, 3)
# full namespace: fish_model.ThrustDrag
v6898__0396 = v6896_eel_eval_pts_coords.reshape((70, 250, 3))

# op _039a expand_array_eval
# LANG: _0399 --> _039b
# SHAPES: (70, 1) --> (70, 250, 1)
# full namespace: fish_model.ThrustDrag
v6900__039b = np.einsum('ac,b->abc', v6899__0399.reshape((70, 1)) ,np.ones((250,))).reshape((70, 250, 1))

# op _039e expand_array_eval
# LANG: _039d --> _039f
# SHAPES: (70, 1) --> (70, 250, 1)
# full namespace: fish_model.ThrustDrag
v6902__039f = np.einsum('ac,b->abc', v6901__039d.reshape((70, 1)) ,np.ones((250,))).reshape((70, 250, 1))

# op _039k_cos_eval
# LANG: beta --> _039l
# SHAPES: (70, 1) --> (70, 1)
# full namespace: fish_model.ThrustDrag
v6905__039l = np.cos(v6885_beta)

# op _03aa_linear_combination_eval
# LANG: _03a9, _03a7 --> panel_forces_x
# SHAPES: (70, 250, 1), (70, 250, 1) --> (70, 250, 1)
# full namespace: fish_model.ThrustDrag
v6935_panel_forces_x = v6933__03a7+v6934__03a9

# op _03ai_linear_combination_eval
# LANG: _03ag, _03ah --> panel_forces_z
# SHAPES: (70, 250, 1), (70, 250, 1) --> (70, 250, 1)
# full namespace: fish_model.ThrustDrag
v6941_panel_forces_z = v6939__03ag+v6940__03ah

# op _03ar_linear_combination_eval
# LANG: _03an, _03aq --> _03as
# SHAPES: (70, 1), (70, 1) --> (70, 1)
# full namespace: fish_model.ThrustDrag
v6946__03as = v6943__03an+v6945__03aq

# op _03au_power_combination_eval
# LANG: _03at --> _03av
# SHAPES: (70, 1) --> (70, 1)
# full namespace: fish_model.ThrustDrag
v6948__03av = (v6947__03at**2)
v6948__03av = v6948__03av.reshape((70, 1))

# op _03bC_single_tensor_sum_with_axis_eval
# LANG: panel_forces_dynamic --> total_forces_temp_dynamic
# SHAPES: (70, 250, 3) --> (70, 3)
# full namespace: fish_model.ThrustDrag
v6984_total_forces_temp_dynamic = np.sum(v6932_panel_forces_dynamic, axis = (1,)).reshape((70, 3))

# op _03bG_linear_combination_eval
# LANG: panel_forces, panel_forces_dynamic --> panel_forces_all
# SHAPES: (70, 250, 3), (70, 250, 3) --> (70, 250, 3)
# full namespace: fish_model.ThrustDrag
v7035_panel_forces_all = v6909_panel_forces+v6932_panel_forces_dynamic

# op _03c0_decompose_eval
# LANG: _03bB --> _03cb, _03c1, _03c7
# SHAPES: (70, 3) --> (70, 1), (70, 1), (70, 1)
# full namespace: fish_model.ThrustDrag
v6997__03c1 = ((v6983__03bB.flatten())[src_indices__03c1__03c0]).reshape((70, 1))
v7000__03c7 = ((v6983__03bB.flatten())[src_indices__03c7__03c0]).reshape((70, 1))
v7003__03cb = ((v6983__03bB.flatten())[src_indices__03cb__03c0]).reshape((70, 1))

# op _03dl_linear_combination_eval
# LANG: _03di, _03dk --> _03dm
# SHAPES: (70, 250, 1), (70, 250, 1) --> (70, 250, 1)
# full namespace: EfficiencyModel
v7044__03dm = v7042__03di+-1*v7043__03dk

# op _03ei_power_combination_eval
# LANG: _03ef --> _03ej
# SHAPES: (50,) --> (50,)
# full namespace: EelViscousModel
v7078__03ej = (v7076__03ef)
v7078__03ej = (v7078__03ej*_03ei_coeff).reshape((50,))

# op _03eo_power_combination_eval
# LANG: _03en --> _03ep
# SHAPES: (50,) --> (50,)
# full namespace: EelViscousModel
v7081__03ep = (v7080__03en**0.5)
v7081__03ep = v7081__03ep.reshape((50,))

# op _02TR pnorm_axis_eval
# LANG: _02TQ --> _02TS
# SHAPES: (70, 50, 6, 3) --> (70, 50, 6)
# full namespace: fish_model.MeshPreprocessing_comp
v6343__02TS = np.sum(v6342__02TQ**2,axis=(3,))**(1 / 2)

# op _02Vv_power_combination_eval
# LANG: u --> _02Vw
# SHAPES: (70, 1) --> (70, 1)
# full namespace: fish_model.adapter_comp
v6406__02Vw = (v6396_u**2)
v6406__02Vw = v6406__02Vw.reshape((70, 1))

# op _02Vx_power_combination_eval
# LANG: v --> _02Vy
# SHAPES: (70, 1) --> (70, 1)
# full namespace: fish_model.adapter_comp
v6407__02Vy = (v6397_v**2)
v6407__02Vy = v6407__02Vy.reshape((70, 1))

# op _0397_indexed_passthrough_eval
# LANG: _0396 --> eval_pts_all
# SHAPES: (70, 250, 3) --> (70, 250, 3)
# full namespace: fish_model.ThrustDrag
v6891_eval_pts_all__temp[i_v6898__0396__0397_indexed_passthrough_eval] = v6898__0396.flatten()
v6891_eval_pts_all = v6891_eval_pts_all__temp.copy()

# op _039g_sin_eval
# LANG: beta --> _039h
# SHAPES: (70, 1) --> (70, 1)
# full namespace: fish_model.ThrustDrag
v6903__039h = np.sin(v6885_beta)

# op _039m expand_array_eval
# LANG: _039l --> _039n
# SHAPES: (70, 1) --> (70, 250, 1)
# full namespace: fish_model.ThrustDrag
v6906__039n = np.einsum('ac,b->abc', v6905__039l.reshape((70, 1)) ,np.ones((250,))).reshape((70, 250, 1))

# op _03aG_power_combination_eval
# LANG: panel_forces_x, _039f --> _03aH
# SHAPES: (70, 250, 1), (70, 250, 1) --> (70, 250, 1)
# full namespace: fish_model.ThrustDrag
v6954__03aH = (v6935_panel_forces_x)*(v6902__039f)
v6954__03aH = v6954__03aH.reshape((70, 250, 1))

# op _03aK_power_combination_eval
# LANG: panel_forces_z, _039b --> _03aL
# SHAPES: (70, 250, 1), (70, 250, 1) --> (70, 250, 1)
# full namespace: fish_model.ThrustDrag
v6956__03aL = (v6941_panel_forces_z)*(v6900__039b)
v6956__03aL = v6956__03aL.reshape((70, 250, 1))

# op _03aw_linear_combination_eval
# LANG: _03as, _03av --> b_thrust
# SHAPES: (70, 1), (70, 1) --> (70, 1)
# full namespace: fish_model.ThrustDrag
v6949_b_thrust = v6946__03as+v6948__03av

# op _03c2_decompose_eval
# LANG: total_forces_temp_dynamic --> _03ce, _03c3, _03c8
# SHAPES: (70, 3) --> (70, 1), (70, 1), (70, 1)
# full namespace: fish_model.ThrustDrag
v6998__03c3 = ((v6984_total_forces_temp_dynamic.flatten())[src_indices__03c3__03c2]).reshape((70, 1))
v7001__03c8 = ((v6984_total_forces_temp_dynamic.flatten())[src_indices__03c8__03c2]).reshape((70, 1))
v7005__03ce = ((v6984_total_forces_temp_dynamic.flatten())[src_indices__03ce__03c2]).reshape((70, 1))

# op _03cM expand_array_eval
# LANG: evaluation_pt --> _03cN
# SHAPES: (3,) --> (70, 250, 3)
# full namespace: fish_model.ThrustDrag
v7023__03cN = np.einsum('c,ab->abc', v7022_evaluation_pt.reshape((3,)) ,np.ones((70, 250))).reshape((70, 250, 3))

# op _03cc_linear_combination_eval
# LANG: _03cb --> _03cd
# SHAPES: (70, 1) --> (70, 1)
# full namespace: fish_model.ThrustDrag
v7004__03cd = -1*v7003__03cb

# op _03cl_single_tensor_sum_with_axis_eval
# LANG: s_panels_all --> _03cm
# SHAPES: (70, 250) --> (70,)
# full namespace: fish_model.ThrustDrag
v7009__03cm = np.sum(v6890_s_panels_all, axis = (1,)).reshape((70,))

# op _03cp_power_combination_eval
# LANG: density --> _03cq
# SHAPES: (70, 1) --> (70, 1)
# full namespace: fish_model.ThrustDrag
v7011__03cq = (v6881_density)
v7011__03cq = (v7011__03cq*_03cp_coeff).reshape((70, 1))

# op _03da_single_tensor_sum_with_axis_eval
# LANG: panel_forces_all --> _03db
# SHAPES: (70, 250, 3) --> (70, 3)
# full namespace: EfficiencyModel
v7038__03db = np.sum(v7035_panel_forces_all, axis = (1,)).reshape((70, 3))

# op _03dn_indexed_passthrough_eval
# LANG: _03dm, _03do, _03dp --> velocities_x
# SHAPES: (70, 250, 1), (70, 250, 1), (70, 250, 1) --> (70, 250, 3)
# full namespace: EfficiencyModel
v7041_velocities_x__temp[i_v7044__03dm__03dn_indexed_passthrough_eval] = v7044__03dm.flatten()
v7041_velocities_x = v7041_velocities_x__temp.copy()
v7041_velocities_x__temp[i_v7045__03do__03dn_indexed_passthrough_eval] = v7045__03do.flatten()
v7041_velocities_x = v7041_velocities_x__temp.copy()
v7041_velocities_x__temp[i_v7046__03dp__03dn_indexed_passthrough_eval] = v7046__03dp.flatten()
v7041_velocities_x = v7041_velocities_x__temp.copy()

# op _03eq_power_combination_eval
# LANG: _03ej, _03ep --> _03er
# SHAPES: (50,), (50,) --> (50,)
# full namespace: EelViscousModel
v7082__03er = (v7078__03ej)*(v7081__03ep**-1)
v7082__03er = v7082__03er.reshape((50,))

# op _03ex_decompose_eval
# LANG: eel_s_panel --> _03ey
# SHAPES: (70, 50, 5) --> (1, 50, 5)
# full namespace: EelViscousModel
v7086__03ey = ((v7085_eel_s_panel.flatten())[src_indices__03ey__03ex]).reshape((1, 50, 5))

# op _02BE_decompose_eval
# LANG: density --> _02BF
# SHAPES: (70, 1) --> (1, 1)
# full namespace: 
v5698__02BF = ((v6881_density.flatten())[src_indices__02BF__02BE]).reshape((1, 1))

# op _02TT_decompose_eval
# LANG: _02TS --> _02TV, _02TU
# SHAPES: (70, 50, 6) --> (70, 50, 5), (70, 50, 5)
# full namespace: fish_model.MeshPreprocessing_comp
v6344__02TU = ((v6343__02TS.flatten())[src_indices__02TU__02TT]).reshape((70, 50, 5))
v6345__02TV = ((v6343__02TS.flatten())[src_indices__02TV__02TT]).reshape((70, 50, 5))

# op _02VB_power_combination_eval
# LANG: w --> _02VC
# SHAPES: (70, 1) --> (70, 1)
# full namespace: fish_model.adapter_comp
v6409__02VC = (v6398_w**2)
v6409__02VC = v6409__02VC.reshape((70, 1))

# op _02Vz_linear_combination_eval
# LANG: _02Vw, _02Vy --> _02VA
# SHAPES: (70, 1), (70, 1) --> (70, 1)
# full namespace: fish_model.adapter_comp
v6408__02VA = v6406__02Vw+v6407__02Vy

# op _039i expand_array_eval
# LANG: _039h --> _039j
# SHAPES: (70, 1) --> (70, 250, 1)
# full namespace: fish_model.ThrustDrag
v6904__039j = np.einsum('ac,b->abc', v6903__039h.reshape((70, 1)) ,np.ones((250,))).reshape((70, 250, 1))

# op _03aI_power_combination_eval
# LANG: _039n, _03aH --> _03aJ
# SHAPES: (70, 250, 1), (70, 250, 1) --> (70, 250, 1)
# full namespace: fish_model.ThrustDrag
v6955__03aJ = (v6954__03aH)*(v6906__039n)
v6955__03aJ = v6955__03aJ.reshape((70, 250, 1))

# op _03aM_power_combination_eval
# LANG: _03aL, _039n --> _03aN
# SHAPES: (70, 250, 1), (70, 250, 1) --> (70, 250, 1)
# full namespace: fish_model.ThrustDrag
v6957__03aN = (v6956__03aL)*(v6906__039n)
v6957__03aN = v6957__03aN.reshape((70, 250, 1))

# op _03ae_linear_combination_eval
# LANG: _03ad, _03ac --> panel_forces_y
# SHAPES: (70, 250, 1), (70, 250, 1) --> (70, 250, 1)
# full namespace: fish_model.ThrustDrag
v6938_panel_forces_y = v6936__03ac+v6937__03ad

# op _03ay_linear_combination_eval
# LANG: panel_forces_x --> _03az
# SHAPES: (70, 250, 1) --> (70, 250, 1)
# full namespace: fish_model.ThrustDrag
v6950__03az = -1*v6935_panel_forces_x

# op _03c4_linear_combination_eval
# LANG: _03c1, _03c3 --> _03c5
# SHAPES: (70, 1), (70, 1) --> (70, 1)
# full namespace: fish_model.ThrustDrag
v6999__03c5 = v6997__03c1+v6998__03c3

# op _03c9_linear_combination_eval
# LANG: _03c7, _03c8 --> _03ca
# SHAPES: (70, 1), (70, 1) --> (70, 1)
# full namespace: fish_model.ThrustDrag
v7002__03ca = v7000__03c7+v7001__03c8

# op _03cO_linear_combination_eval
# LANG: eval_pts_all, _03cN --> _03cP
# SHAPES: (70, 250, 3), (70, 250, 3) --> (70, 250, 3)
# full namespace: fish_model.ThrustDrag
v7024__03cP = v6891_eval_pts_all+-1*v7023__03cN

# op _03cf_linear_combination_eval
# LANG: _03cd, _03ce --> _03cg
# SHAPES: (70, 1), (70, 1) --> (70, 1)
# full namespace: fish_model.ThrustDrag
v7006__03cg = v7004__03cd+-1*v7005__03ce

# op _03cn reshape_eval
# LANG: _03cm --> s_panels_sum
# SHAPES: (70,) --> (70, 1)
# full namespace: fish_model.ThrustDrag
v7010_s_panels_sum = v7009__03cm.reshape((70, 1))

# op _03cr_power_combination_eval
# LANG: _03cq, b_thrust --> _03cs
# SHAPES: (70, 1), (70, 1) --> (70, 1)
# full namespace: fish_model.ThrustDrag
v7012__03cs = (v7011__03cq)*(v6949_b_thrust)
v7012__03cs = v7012__03cs.reshape((70, 1))

# op _03dD_decompose_eval
# LANG: velocities_x --> _03d_, _03dE, _03dO
# SHAPES: (70, 250, 3) --> (34, 250, 1), (34, 250, 1), (34, 250, 1)
# full namespace: EfficiencyModel
v7054__03dE = ((v7041_velocities_x.flatten())[src_indices__03dE__03dD]).reshape((34, 250, 1))
v7060__03dO = ((v7041_velocities_x.flatten())[src_indices__03dO__03dD]).reshape((34, 250, 1))
v7067__03d_ = ((v7041_velocities_x.flatten())[src_indices__03d___03dD]).reshape((34, 250, 1))

# op _03dc_decompose_eval
# LANG: _03db --> thrust
# SHAPES: (70, 3) --> (70, 1)
# full namespace: EfficiencyModel
v7039_thrust = ((v7038__03db.flatten())[src_indices_thrust__03dc]).reshape((70, 1))

# op _03de_decompose_eval
# LANG: panel_forces_all --> _03dX, _03df, _03dA, _03dL
# SHAPES: (70, 250, 3) --> (34, 250, 1), (70, 250, 1), (34, 250, 1), (34, 250, 1)
# full namespace: EfficiencyModel
v7040__03df = ((v7035_panel_forces_all.flatten())[src_indices__03df__03de]).reshape((70, 250, 1))
v7052__03dA = ((v7035_panel_forces_all.flatten())[src_indices__03dA__03de]).reshape((34, 250, 1))
v7058__03dL = ((v7035_panel_forces_all.flatten())[src_indices__03dL__03de]).reshape((34, 250, 1))
v7065__03dX = ((v7035_panel_forces_all.flatten())[src_indices__03dX__03de]).reshape((34, 250, 1))

# op _03es_power_combination_eval
# LANG: _03er, _03eh --> _03et
# SHAPES: (50,), (50,) --> (50,)
# full namespace: EelViscousModel
v7083__03et = (v7082__03er)*(v7077__03eh)
v7083__03et = v7083__03et.reshape((50,))

# op _03ez_single_tensor_sum_with_axis_eval
# LANG: _03ey --> _03eA
# SHAPES: (1, 50, 5) --> (1, 50)
# full namespace: EelViscousModel
v7087__03eA = np.sum(v7086__03ey, axis = (2,)).reshape((1, 50))

# op _02BG reshape_eval
# LANG: _02BF --> _02BH
# SHAPES: (1, 1) --> (1,)
# full namespace: 
v5699__02BH = v5698__02BF.reshape((1,))

# op _02TW_linear_combination_eval
# LANG: _02TU, _02TV --> _02TX
# SHAPES: (70, 50, 5), (70, 50, 5) --> (70, 50, 5)
# full namespace: fish_model.MeshPreprocessing_comp
v6346__02TX = v6344__02TU+v6345__02TV

# op _02VD_linear_combination_eval
# LANG: _02VA, _02VC --> v_inf_sq
# SHAPES: (70, 1), (70, 1) --> (70, 1)
# full namespace: fish_model.adapter_comp
v6410_v_inf_sq = v6408__02VA+v6409__02VC

# op _03aA_power_combination_eval
# LANG: _039b, _03az --> _03aB
# SHAPES: (70, 250, 1), (70, 250, 1) --> (70, 250, 1)
# full namespace: fish_model.ThrustDrag
v6951__03aB = (v6950__03az)*(v6900__039b)
v6951__03aB = v6951__03aB.reshape((70, 250, 1))

# op _03aC_power_combination_eval
# LANG: panel_forces_z, _039f --> _03aD
# SHAPES: (70, 250, 1), (70, 250, 1) --> (70, 250, 1)
# full namespace: fish_model.ThrustDrag
v6952__03aD = (v6941_panel_forces_z)*(v6902__039f)
v6952__03aD = v6952__03aD.reshape((70, 250, 1))

# op _03aO_linear_combination_eval
# LANG: _03aJ, _03aN --> _03aP
# SHAPES: (70, 250, 1), (70, 250, 1) --> (70, 250, 1)
# full namespace: fish_model.ThrustDrag
v6958__03aP = v6955__03aJ+v6957__03aN

# op _03aQ_power_combination_eval
# LANG: panel_forces_y, _039j --> _03aR
# SHAPES: (70, 250, 1), (70, 250, 1) --> (70, 250, 1)
# full namespace: fish_model.ThrustDrag
v6959__03aR = (v6938_panel_forces_y)*(v6904__039j)
v6959__03aR = v6959__03aR.reshape((70, 250, 1))

# op _03aY_single_tensor_sum_with_axis_eval
# LANG: s_panels_all --> _03aZ
# SHAPES: (70, 250) --> (70,)
# full namespace: fish_model.ThrustDrag
v6963__03aZ = np.sum(v6890_s_panels_all, axis = (1,)).reshape((70,))

# op _03c6_indexed_passthrough_eval
# LANG: _03c5, _03ca, _03cg --> F
# SHAPES: (70, 1), (70, 1), (70, 1) --> (70, 3)
# full namespace: fish_model.ThrustDrag
v6996_F__temp[i_v6999__03c5__03c6_indexed_passthrough_eval] = v6999__03c5.flatten()
v6996_F = v6996_F__temp.copy()
v6996_F__temp[i_v7002__03ca__03c6_indexed_passthrough_eval] = v7002__03ca.flatten()
v6996_F = v6996_F__temp.copy()
v6996_F__temp[i_v7006__03cg__03c6_indexed_passthrough_eval] = v7006__03cg.flatten()
v6996_F = v6996_F__temp.copy()

# op _03cQ cross_product_eval
# LANG: _03cP, panel_forces --> _03cR
# SHAPES: (70, 250, 3), (70, 250, 3) --> (70, 250, 3)
# full namespace: fish_model.ThrustDrag
v7025__03cR = np.cross(v7024__03cP, v6909_panel_forces, axisa = 2, axisb = 2, axisc = 2)

# op _03ct_power_combination_eval
# LANG: _03cs, s_panels_sum --> _03cu
# SHAPES: (70, 1), (70, 1) --> (70, 1)
# full namespace: fish_model.ThrustDrag
v7013__03cu = (v7012__03cs)*(v7010_s_panels_sum)
v7013__03cu = v7013__03cu.reshape((70, 1))

# op _03dB_linear_combination_eval
# LANG: _03dA --> _03dC
# SHAPES: (34, 250, 1) --> (34, 250, 1)
# full namespace: EfficiencyModel
v7053__03dC = -1*v7052__03dA

# op _03dF_linear_combination_eval
# LANG: _03dE --> _03dG
# SHAPES: (34, 250, 1) --> (34, 250, 1)
# full namespace: EfficiencyModel
v7055__03dG = -1*v7054__03dE

# op _03dM_linear_combination_eval
# LANG: _03dL --> _03dN
# SHAPES: (34, 250, 1) --> (34, 250, 1)
# full namespace: EfficiencyModel
v7059__03dN = -1*v7058__03dL

# op _03dP_linear_combination_eval
# LANG: _03dO --> _03dQ
# SHAPES: (34, 250, 1) --> (34, 250, 1)
# full namespace: EfficiencyModel
v7061__03dQ = -1*v7060__03dO

# op _03dq_decompose_eval
# LANG: thrust --> _03dr
# SHAPES: (70, 1) --> (34, 1)
# full namespace: EfficiencyModel
v7047__03dr = ((v7039_thrust.flatten())[src_indices__03dr__03dq]).reshape((34, 1))

# op _03eB reshape_eval
# LANG: _03eA --> _03eC
# SHAPES: (1, 50) --> (50,)
# full namespace: EelViscousModel
v7088__03eC = v7087__03eA.reshape((50,))

# op _03eu_power_combination_eval
# LANG: _03et --> _03ev
# SHAPES: (50,) --> (50,)
# full namespace: EelViscousModel
v7084__03ev = (v7083__03et**-1)
v7084__03ev = (v7084__03ev*_03eu_coeff).reshape((50,))

# op _02BI_power_combination_eval
# LANG: _02BH --> _02BJ
# SHAPES: (1,) --> (1,)
# full namespace: 
v5700__02BJ = (v5699__02BH)
v5700__02BJ = (v5700__02BJ*_02BI_coeff).reshape((1,))

# op _02Br_decompose_eval
# LANG: thrust --> _02Bs
# SHAPES: (70, 1) --> (35, 1)
# full namespace: 
v5690__02Bs = ((v7039_thrust.flatten())[src_indices__02Bs__02Br]).reshape((35, 1))

# op _02Bv single_tensor_sum_no_axis_eval
# LANG: eel_s_panel --> _02Bw
# SHAPES: (70, 250) --> (1,)
# full namespace: 
v7085_eel_s_panel = v7085_eel_s_panel.reshape((70, 250))
v5693__02Bw = np.sum(v7085_eel_s_panel).reshape((1,))
v7085_eel_s_panel = v7085_eel_s_panel.reshape((70, 50, 5))

# op _02TY_power_combination_eval
# LANG: _02TX --> eel_chord_length
# SHAPES: (70, 50, 5) --> (70, 50, 5)
# full namespace: fish_model.MeshPreprocessing_comp
v6347_eel_chord_length = (v6346__02TX)
v6347_eel_chord_length = (v6347_eel_chord_length*_02TY_coeff).reshape((70, 50, 5))

# op _02U1_linear_combination_eval
# LANG: _02T_, _02U0 --> _02U2
# SHAPES: (70, 51, 5, 3), (70, 51, 5, 3) --> (70, 51, 5, 3)
# full namespace: fish_model.MeshPreprocessing_comp
v6350__02U2 = v6348__02T_+-1*v6349__02U0

# op _02Vb_power_combination_eval
# LANG: v_inf_sq --> _02Vc
# SHAPES: (70, 1) --> (70, 1)
# full namespace: fish_model.MeshPreprocessing_comp
v6391__02Vc = (v6410_v_inf_sq**0.5)
v6391__02Vc = v6391__02Vc.reshape((70, 1))

# op _039A_decompose_eval
# LANG: eel --> _039C, _039B
# SHAPES: (70, 51, 6, 3) --> (1, 1, 1, 1), (1, 1, 1, 1)
# full namespace: fish_model.ThrustDrag
v6914__039B = ((v7074_eel.flatten())[src_indices__039B__039A]).reshape((1, 1, 1, 1))
v6915__039C = ((v7074_eel.flatten())[src_indices__039C__039A]).reshape((1, 1, 1, 1))

# op _03aE_linear_combination_eval
# LANG: _03aB, _03aD --> _03aF
# SHAPES: (70, 250, 1), (70, 250, 1) --> (70, 250, 1)
# full namespace: fish_model.ThrustDrag
v6953__03aF = v6951__03aB+v6952__03aD

# op _03aS_linear_combination_eval
# LANG: _03aP, _03aR --> _03aT
# SHAPES: (70, 250, 1), (70, 250, 1) --> (70, 250, 1)
# full namespace: fish_model.ThrustDrag
v6960__03aT = v6958__03aP+-1*v6959__03aR

# op _03a_ reshape_eval
# LANG: _03aZ --> _03b0
# SHAPES: (70,) --> (70, 1)
# full namespace: fish_model.ThrustDrag
v6964__03b0 = v6963__03aZ.reshape((70, 1))

# op _03bK_power_combination_eval
# LANG: panel_forces_all --> _03bL
# SHAPES: (70, 250, 3) --> (70, 250, 3)
# full namespace: fish_model.ThrustDrag
v6988__03bL = (v7035_panel_forces_all**2)
v6988__03bL = v6988__03bL.reshape((70, 250, 3))

# op _03bQ_power_combination_eval
# LANG: eval_total_vel --> _03bR
# SHAPES: (70, 250, 3) --> (70, 250, 3)
# full namespace: fish_model.ThrustDrag
v6991__03bR = (v6889_eval_total_vel**2)
v6991__03bR = v6991__03bR.reshape((70, 250, 3))

# op _03bg_power_combination_eval
# LANG: density --> _03bh
# SHAPES: (70, 1) --> (70, 1)
# full namespace: fish_model.ThrustDrag
v6973__03bh = (v6881_density)
v6973__03bh = (v6973__03bh*_03bg_coeff).reshape((70, 1))

# op _03bq_power_combination_eval
# LANG: density --> _03br
# SHAPES: (70, 1) --> (70, 1)
# full namespace: fish_model.ThrustDrag
v6978__03br = (v6881_density)
v6978__03br = (v6978__03br*_03bq_coeff).reshape((70, 1))

# op _03cS_single_tensor_sum_with_axis_eval
# LANG: _03cR --> _03cT
# SHAPES: (70, 250, 3) --> (70, 3)
# full namespace: fish_model.ThrustDrag
v7026__03cT = np.sum(v7025__03cR, axis = (1,)).reshape((70, 3))

# op _03cv_power_combination_eval
# LANG: _03cu --> Drag
# SHAPES: (70, 1) --> (70, 1)
# full namespace: fish_model.ThrustDrag
v7014_Drag = (v7013__03cu)
v7014_Drag = (v7014_Drag*_03cv_coeff).reshape((70, 1))

# op _03cx_decompose_eval
# LANG: F --> _03cy
# SHAPES: (70, 3) --> (70, 1)
# full namespace: fish_model.ThrustDrag
v7015__03cy = ((v6996_F.flatten())[src_indices__03cy__03cx]).reshape((70, 1))

# op _03dH_power_combination_eval
# LANG: _03dC, _03dG --> _03dI
# SHAPES: (34, 250, 1), (34, 250, 1) --> (34, 250, 1)
# full namespace: EfficiencyModel
v7056__03dI = (v7053__03dC)*(v7055__03dG)
v7056__03dI = v7056__03dI.reshape((34, 250, 1))

# op _03dR_power_combination_eval
# LANG: _03dN, _03dQ --> _03dS
# SHAPES: (34, 250, 1), (34, 250, 1) --> (34, 250, 1)
# full namespace: EfficiencyModel
v7062__03dS = (v7059__03dN)*(v7061__03dQ)
v7062__03dS = v7062__03dS.reshape((34, 250, 1))

# op _03dY_linear_combination_eval
# LANG: _03dX --> _03dZ
# SHAPES: (34, 250, 1) --> (34, 250, 1)
# full namespace: EfficiencyModel
v7066__03dZ = -1*v7065__03dX

# op _03ds_single_tensor_sum_with_axis_eval
# LANG: _03dr --> _03dt
# SHAPES: (34, 1) --> (1,)
# full namespace: EfficiencyModel
v7048__03dt = np.sum(v7047__03dr, axis = (0,)).reshape((1,))

# op _03e0_linear_combination_eval
# LANG: _03d_ --> _03e1
# SHAPES: (34, 250, 1) --> (34, 250, 1)
# full namespace: EfficiencyModel
v7068__03e1 = -1*v7067__03d_

# op _03eF_power_combination_eval
# LANG: _03eC, _03ev --> _03eG
# SHAPES: (50,), (50,) --> (50,)
# full namespace: EelViscousModel
v7090__03eG = (v7088__03eC)*(v7084__03ev)
v7090__03eG = v7090__03eG.reshape((50,))

# op _02BA single_tensor_sum_no_axis_eval
# LANG: _02Bs --> _02BB
# SHAPES: (35, 1) --> (1,)
# full namespace: 
v5696__02BB = np.sum(v5690__02Bs).reshape((1,))

# op _02BK_power_combination_eval
# LANG: _02BJ --> _02BL
# SHAPES: (1,) --> (1,)
# full namespace: 
v5701__02BL = (v5700__02BJ)
v5701__02BL = (v5701__02BL*_02BK_coeff).reshape((1,))

# op _02Bx_power_combination_eval
# LANG: _02Bw --> _02By
# SHAPES: (1,) --> (1,)
# full namespace: 
v5694__02By = (v5693__02Bw)
v5694__02By = (v5694__02By*_02Bx_coeff).reshape((1,))

# op _02U3 pnorm_axis_eval
# LANG: _02U2 --> _02U4
# SHAPES: (70, 51, 5, 3) --> (70, 51, 5)
# full namespace: fish_model.MeshPreprocessing_comp
v6351__02U4 = np.sum(v6350__02U2**2,axis=(3,))**(1 / 2)

# op _02V7_single_tensor_sum_with_axis_eval
# LANG: eel_chord_length --> _02V8
# SHAPES: (70, 50, 5) --> (70, 5)
# full namespace: fish_model.MeshPreprocessing_comp
v6389__02V8 = np.sum(v6347_eel_chord_length, axis = (1,)).reshape((70, 5))

# op _02Vd_power_combination_eval
# LANG: _02Vc, density --> _02Ve
# SHAPES: (70, 1), (70, 1) --> (70, 1)
# full namespace: fish_model.MeshPreprocessing_comp
v6392__02Ve = (v6881_density)*(v6391__02Vc)
v6392__02Ve = v6392__02Ve.reshape((70, 1))

# op _039D_linear_combination_eval
# LANG: _039B, _039C --> c_bar
# SHAPES: (1, 1, 1, 1), (1, 1, 1, 1) --> (1, 1, 1, 1)
# full namespace: fish_model.ThrustDrag
v6916_c_bar = v6914__039B+-1*v6915__039C

# op _03b2_decompose_eval
# LANG: _03aF --> eel_L_panel
# SHAPES: (70, 250, 1) --> (70, 250, 1)
# full namespace: fish_model.ThrustDrag
v6966_eel_L_panel = ((v6953__03aF.flatten())[src_indices_eel_L_panel__03b2]).reshape((70, 250, 1))

# op _03b4_decompose_eval
# LANG: _03aT --> eel_D_panel
# SHAPES: (70, 250, 1) --> (70, 250, 1)
# full namespace: fish_model.ThrustDrag
v6967_eel_D_panel = ((v6960__03aT.flatten())[src_indices_eel_D_panel__03b4]).reshape((70, 250, 1))

# op _03bM_single_tensor_sum_with_axis_eval
# LANG: _03bL --> _03bN
# SHAPES: (70, 250, 3) --> (70, 250)
# full namespace: fish_model.ThrustDrag
v6989__03bN = np.sum(v6988__03bL, axis = (2,)).reshape((70, 250))

# op _03bS_single_tensor_sum_with_axis_eval
# LANG: _03bR --> _03bT
# SHAPES: (70, 250, 3) --> (70, 250)
# full namespace: fish_model.ThrustDrag
v6992__03bT = np.sum(v6991__03bR, axis = (2,)).reshape((70, 250))

# op _03bi_power_combination_eval
# LANG: _03b0, _03bh --> _03bj
# SHAPES: (70, 1), (70, 1) --> (70, 1)
# full namespace: fish_model.ThrustDrag
v6974__03bj = (v6973__03bh)*(v6964__03b0)
v6974__03bj = v6974__03bj.reshape((70, 1))

# op _03bs_power_combination_eval
# LANG: _03br, _03b0 --> _03bt
# SHAPES: (70, 1), (70, 1) --> (70, 1)
# full namespace: fish_model.ThrustDrag
v6979__03bt = (v6978__03br)*(v6964__03b0)
v6979__03bt = v6979__03bt.reshape((70, 1))

# op _03cD single_tensor_sum_no_axis_eval
# LANG: Drag --> _03cE
# SHAPES: (70, 1) --> (1,)
# full namespace: fish_model.ThrustDrag
v7018__03cE = np.sum(v7014_Drag).reshape((1,))

# op _03cV_decompose_eval
# LANG: _03cT --> _03d4, _03cW, _03c_
# SHAPES: (70, 3) --> (70, 1), (70, 1), (70, 1)
# full namespace: fish_model.ThrustDrag
v7028__03cW = ((v7026__03cT.flatten())[src_indices__03cW__03cV]).reshape((70, 1))
v7030__03c_ = ((v7026__03cT.flatten())[src_indices__03c___03cV]).reshape((70, 1))
v7033__03d4 = ((v7026__03cT.flatten())[src_indices__03d4__03cV]).reshape((70, 1))

# op _03cz single_tensor_sum_no_axis_eval
# LANG: _03cy --> _03cA
# SHAPES: (70, 1) --> (1,)
# full namespace: fish_model.ThrustDrag
v7016__03cA = np.sum(v7015__03cy).reshape((1,))

# op _03dJ single_tensor_sum_no_axis_eval
# LANG: _03dI --> _03dK
# SHAPES: (34, 250, 1) --> (1,)
# full namespace: EfficiencyModel
v7057__03dK = np.sum(v7056__03dI).reshape((1,))

# op _03dT single_tensor_sum_no_axis_eval
# LANG: _03dS --> _03dU
# SHAPES: (34, 250, 1) --> (1,)
# full namespace: EfficiencyModel
v7063__03dU = np.sum(v7062__03dS).reshape((1,))

# op _03du_power_combination_eval
# LANG: _03dt, v_x --> _03dv
# SHAPES: (1,), (1,) --> (1,)
# full namespace: EfficiencyModel
v7049__03dv = (v7048__03dt)*(v7073_v_x)
v7049__03dv = v7049__03dv.reshape((1,))

# op _03e2_power_combination_eval
# LANG: _03dZ, _03e1 --> _03e3
# SHAPES: (34, 250, 1), (34, 250, 1) --> (34, 250, 1)
# full namespace: EfficiencyModel
v7069__03e3 = (v7066__03dZ)*(v7068__03e1)
v7069__03e3 = v7069__03e3.reshape((34, 250, 1))

# op _03eD single_tensor_sum_no_axis_eval
# LANG: _03ey --> _03eE
# SHAPES: (1, 50, 5) --> (1,)
# full namespace: EelViscousModel
v7089__03eE = np.sum(v7086__03ey).reshape((1,))

# op _03eH single_tensor_sum_no_axis_eval
# LANG: _03eG --> _03eI
# SHAPES: (50,) --> (1,)
# full namespace: EelViscousModel
v7091__03eI = np.sum(v7090__03eG).reshape((1,))

# op _02BC_linear_combination_eval
# LANG: _02BB --> _02BD
# SHAPES: (1,) --> (1,)
# full namespace: 
v5697__02BD = -1*v5696__02BB

# op _02BM_power_combination_eval
# LANG: _02BL, _02By --> _02BN
# SHAPES: (1,), (1,) --> (1,)
# full namespace: 
v5702__02BN = (v5701__02BL)*(v5694__02By)
v5702__02BN = v5702__02BN.reshape((1,))

# op _02U5_decompose_eval
# LANG: _02U4 --> _02U7, _02U6
# SHAPES: (70, 51, 5) --> (70, 50, 5), (70, 50, 5)
# full namespace: fish_model.MeshPreprocessing_comp
v6352__02U6 = ((v6351__02U4.flatten())[src_indices__02U6__02U5]).reshape((70, 50, 5))
v6353__02U7 = ((v6351__02U4.flatten())[src_indices__02U7__02U5]).reshape((70, 50, 5))

# op _02V9 reshape_eval
# LANG: _02V8 --> _02Va
# SHAPES: (70, 5) --> (70, 5, 1)
# full namespace: fish_model.MeshPreprocessing_comp
v6390__02Va = v6389__02V8.reshape((70, 5, 1))

# op _02Vf expand_array_eval
# LANG: _02Ve --> _02Vg
# SHAPES: (70, 1) --> (70, 5, 1)
# full namespace: fish_model.MeshPreprocessing_comp
v6393__02Vg = np.einsum('ac,b->abc', v6392__02Ve.reshape((70, 1)) ,np.ones((5,))).reshape((70, 5, 1))

# op _039F reshape_eval
# LANG: c_bar --> _039G
# SHAPES: (1, 1, 1, 1) --> (1,)
# full namespace: fish_model.ThrustDrag
v6917__039G = v6916_c_bar.reshape((1,))

# op _03aU expand_array_eval
# LANG: s_panels_all --> _03aV
# SHAPES: (70, 250) --> (70, 250, 3)
# full namespace: fish_model.ThrustDrag
v6961__03aV = np.einsum('ab,c->abc', v6890_s_panels_all.reshape((70, 250)) ,np.ones((3,))).reshape((70, 250, 3))

# op _03b8_single_tensor_sum_with_axis_eval
# LANG: eel_L_panel --> _03b9
# SHAPES: (70, 250, 1) --> (70, 1)
# full namespace: fish_model.ThrustDrag
v6969__03b9 = np.sum(v6966_eel_L_panel, axis = (1,)).reshape((70, 1))

# op _03bO_power_combination_eval
# LANG: _03bN --> _03bP
# SHAPES: (70, 250) --> (70, 250)
# full namespace: fish_model.ThrustDrag
v6990__03bP = (v6989__03bN**0.5)
v6990__03bP = v6990__03bP.reshape((70, 250))

# op _03bU_power_combination_eval
# LANG: _03bT --> _03bV
# SHAPES: (70, 250) --> (70, 250)
# full namespace: fish_model.ThrustDrag
v6993__03bV = (v6992__03bT**0.5)
v6993__03bV = v6993__03bV.reshape((70, 250))

# op _03ba_single_tensor_sum_with_axis_eval
# LANG: eel_D_panel --> _03bb
# SHAPES: (70, 250, 1) --> (70, 1)
# full namespace: fish_model.ThrustDrag
v6970__03bb = np.sum(v6967_eel_D_panel, axis = (1,)).reshape((70, 1))

# op _03bk_power_combination_eval
# LANG: b_thrust, _03bj --> _03bl
# SHAPES: (70, 1), (70, 1) --> (70, 1)
# full namespace: fish_model.ThrustDrag
v6975__03bl = (v6974__03bj)*(v6949_b_thrust)
v6975__03bl = v6975__03bl.reshape((70, 1))

# op _03bu_power_combination_eval
# LANG: b_thrust, _03bt --> _03bv
# SHAPES: (70, 1), (70, 1) --> (70, 1)
# full namespace: fish_model.ThrustDrag
v6980__03bv = (v6979__03bt)*(v6949_b_thrust)
v6980__03bv = v6980__03bv.reshape((70, 1))

# op _03cB_power_combination_eval
# LANG: _03cA --> _03cC
# SHAPES: (1,) --> (1,)
# full namespace: fish_model.ThrustDrag
v7017__03cC = (v7016__03cA)
v7017__03cC = (v7017__03cC*_03cB_coeff).reshape((1,))

# op _03cF_power_combination_eval
# LANG: _03cE --> _03cG
# SHAPES: (1,) --> (1,)
# full namespace: fish_model.ThrustDrag
v7019__03cG = (v7018__03cE)
v7019__03cG = (v7019__03cG*_03cF_coeff).reshape((1,))

# op _03d0_linear_combination_eval
# LANG: _03c_ --> _03d1
# SHAPES: (70, 1) --> (70, 1)
# full namespace: fish_model.ThrustDrag
v7031__03d1 = -1*v7030__03c_

# op _03dV_linear_combination_eval
# LANG: _03dK, _03dU --> _03dW
# SHAPES: (1,), (1,) --> (1,)
# full namespace: EfficiencyModel
v7064__03dW = v7057__03dK+v7063__03dU

# op _03dw single_tensor_sum_no_axis_eval
# LANG: _03dv --> _03dx
# SHAPES: (1,) --> (1,)
# full namespace: EfficiencyModel
v7050__03dx = np.sum(v7049__03dv).reshape((1,))

# op _03e4 single_tensor_sum_no_axis_eval
# LANG: _03e3 --> _03e5
# SHAPES: (34, 250, 1) --> (1,)
# full namespace: EfficiencyModel
v7070__03e5 = np.sum(v7069__03e3).reshape((1,))

# op _03eJ_power_combination_eval
# LANG: _03eI, _03eE --> _03eK
# SHAPES: (1,), (1,) --> (1,)
# full namespace: EelViscousModel
v7092__03eK = (v7091__03eI)*(v7089__03eE**-1)
v7092__03eK = v7092__03eK.reshape((1,))

# op _02BO_power_combination_eval
# LANG: _02BD, _02BN --> _02BP
# SHAPES: (1,), (1,) --> (1,)
# full namespace: 
v5703__02BP = (v5697__02BD)*(v5702__02BN**-1)
v5703__02BP = v5703__02BP.reshape((1,))

# op _02U8_linear_combination_eval
# LANG: _02U6, _02U7 --> _02U9
# SHAPES: (70, 50, 5), (70, 50, 5) --> (70, 50, 5)
# full namespace: fish_model.MeshPreprocessing_comp
v6354__02U9 = v6352__02U6+v6353__02U7

# op _02Vh_power_combination_eval
# LANG: _02Vg, _02Va --> _02Vi
# SHAPES: (70, 5, 1), (70, 5, 1) --> (70, 5, 1)
# full namespace: fish_model.MeshPreprocessing_comp
v6394__02Vi = (v6393__02Vg)*(v6390__02Va)
v6394__02Vi = v6394__02Vi.reshape((70, 5, 1))

# op _039H expand_scalar_eval
# LANG: _039G --> _039I
# SHAPES: (1,) --> (52500, 1)
# full namespace: fish_model.ThrustDrag
v6918__039I = np.empty((52500, 1))
v6918__039I.fill(v6917__039G.item())

# op _03aW_power_combination_eval
# LANG: panel_forces, _03aV --> _03aX
# SHAPES: (70, 250, 3), (70, 250, 3) --> (70, 250, 3)
# full namespace: fish_model.ThrustDrag
v6962__03aX = (v6909_panel_forces)*(v6961__03aV**-1)
v6962__03aX = v6962__03aX.reshape((70, 250, 3))

# op _03bW_power_combination_eval
# LANG: _03bP, _03bV --> _03bX
# SHAPES: (70, 250), (70, 250) --> (70, 250)
# full namespace: fish_model.ThrustDrag
v6994__03bX = (v6990__03bP)*(v6993__03bV)
v6994__03bX = v6994__03bX.reshape((70, 250))

# op _03bm_power_combination_eval
# LANG: _03b9, _03bl --> _03bn
# SHAPES: (70, 1), (70, 1) --> (70, 1)
# full namespace: fish_model.ThrustDrag
v6976__03bn = (v6969__03b9)*(v6975__03bl**-1)
v6976__03bn = v6976__03bn.reshape((70, 1))

# op _03bw_power_combination_eval
# LANG: _03bb, _03bv --> _03bx
# SHAPES: (70, 1), (70, 1) --> (70, 1)
# full namespace: fish_model.ThrustDrag
v6981__03bx = (v6970__03bb)*(v6980__03bv**-1)
v6981__03bx = v6981__03bx.reshape((70, 1))

# op _03cH_linear_combination_eval
# LANG: _03cC, _03cG --> _03cI
# SHAPES: (1,), (1,) --> (1,)
# full namespace: fish_model.ThrustDrag
v7020__03cI = v7017__03cC+-1*v7019__03cG

# op _03cX_linear_combination_eval
# LANG: _03cW --> _03cY
# SHAPES: (70, 1) --> (70, 1)
# full namespace: fish_model.ThrustDrag
v7029__03cY = v7028__03cW

# op _03cj_linear_combination_eval
# LANG: _03cb --> _03ck
# SHAPES: (70, 1) --> (70, 1)
# full namespace: fish_model.ThrustDrag
v7008__03ck = -1*v7003__03cb

# op _03d2_power_combination_eval
# LANG: _03d1 --> _03d3
# SHAPES: (70, 1) --> (70, 1)
# full namespace: fish_model.ThrustDrag
v7032__03d3 = (v7031__03d1)
v7032__03d3 = (v7032__03d3*_03d2_coeff).reshape((70, 1))

# op _03d5_linear_combination_eval
# LANG: _03d4 --> _03d6
# SHAPES: (70, 1) --> (70, 1)
# full namespace: fish_model.ThrustDrag
v7034__03d6 = v7033__03d4

# op _03dy_linear_combination_eval
# LANG: _03dx --> thrust_power
# SHAPES: (1,) --> (1,)
# full namespace: EfficiencyModel
v7051_thrust_power = -1*v7050__03dx

# op _03e6_linear_combination_eval
# LANG: _03dW, _03e5 --> panel_total_power
# SHAPES: (1,), (1,) --> (1,)
# full namespace: EfficiencyModel
v7071_panel_total_power = v7064__03dW+v7070__03e5

# op _03eL_power_combination_eval
# LANG: _03eK --> _03eM
# SHAPES: (1,) --> (1,)
# full namespace: EelViscousModel
v7093__03eM = (v7092__03eK)
v7093__03eM = (v7093__03eM*_03eL_coeff).reshape((1,))

# op _02BQ_power_combination_eval
# LANG: _02BP --> avg_C_T
# SHAPES: (1,) --> (1,)
# full namespace: 
v5704_avg_C_T = (v5703__02BP)
v5704_avg_C_T = (v5704_avg_C_T*_02BQ_coeff).reshape((1,))

# op _02Ua_power_combination_eval
# LANG: _02U9 --> eel_span_length
# SHAPES: (70, 50, 5) --> (70, 50, 5)
# full namespace: fish_model.MeshPreprocessing_comp
v6355_eel_span_length = (v6354__02U9)
v6355_eel_span_length = (v6355_eel_span_length*_02Ua_coeff).reshape((70, 50, 5))

# op _02Vj_power_combination_eval
# LANG: _02Vi --> eel_re_span
# SHAPES: (70, 5, 1) --> (70, 5, 1)
# full namespace: fish_model.MeshPreprocessing_comp
v6395_eel_re_span = (v6394__02Vi)
v6395_eel_re_span = (v6395_eel_re_span*_02Vj_coeff).reshape((70, 5, 1))

# op _02XW_indexed_passthrough_eval
# LANG: _02XT --> normal_concatenated_b
# SHAPES: (70, 250, 3) --> (70, 250, 3)
# full namespace: fish_model.solve_gamma_b_group.prepossing_before_Solve.RHS_group.Projection_k_vel
v6488_normal_concatenated_b__temp[i_v6491__02XT__02XW_indexed_passthrough_eval] = v6491__02XT.flatten()
v6488_normal_concatenated_b = v6488_normal_concatenated_b__temp.copy()

# op _039J reshape_eval
# LANG: _039I --> c_bar_exp
# SHAPES: (52500, 1) --> (70, 250, 3)
# full namespace: fish_model.ThrustDrag
v6919_c_bar_exp = v6918__039I.reshape((70, 250, 3))

# op _03b6_decompose_eval
# LANG: _03aX --> eel_traction_surfaces
# SHAPES: (70, 250, 3) --> (70, 250, 3)
# full namespace: fish_model.ThrustDrag
v6968_eel_traction_surfaces = ((v6962__03aX.flatten())[src_indices_eel_traction_surfaces__03b6]).reshape((70, 250, 3))

# op _03bE cross_product_eval
# LANG: eval_total_vel, bd_vec --> crosspd
# SHAPES: (70, 250, 3), (70, 250, 3) --> (70, 250, 3)
# full namespace: fish_model.ThrustDrag
v6985_crosspd = np.cross(v6889_eval_total_vel, v6886_bd_vec, axisa = 2, axisb = 2, axisc = 2)

# op _03bY_single_tensor_sum_with_axis_eval
# LANG: _03bX --> panel_power
# SHAPES: (70, 250) --> (70,)
# full namespace: fish_model.ThrustDrag
v6995_panel_power = np.sum(v6994__03bX, axis = (1,)).reshape((70,))

# op _03bc reshape_eval
# LANG: _03b9 --> eel_L
# SHAPES: (70, 1) --> (70, 1)
# full namespace: fish_model.ThrustDrag
v6971_eel_L = v6969__03b9.reshape((70, 1))

# op _03be reshape_eval
# LANG: _03bb --> eel_D
# SHAPES: (70, 1) --> (70, 1)
# full namespace: fish_model.ThrustDrag
v6972_eel_D = v6970__03bb.reshape((70, 1))

# op _03bo reshape_eval
# LANG: _03bn --> eel_C_L
# SHAPES: (70, 1) --> (70, 1)
# full namespace: fish_model.ThrustDrag
v6977_eel_C_L = v6976__03bn.reshape((70, 1))

# op _03by reshape_eval
# LANG: _03bx --> eel_C_D_i
# SHAPES: (70, 1) --> (70, 1)
# full namespace: fish_model.ThrustDrag
v6982_eel_C_D_i = v6981__03bx.reshape((70, 1))

# op _03cJ_power_combination_eval
# LANG: _03cI --> res
# SHAPES: (1,) --> (1,)
# full namespace: fish_model.ThrustDrag
v7021_res = (v7020__03cI**2)
v7021_res = v7021_res.reshape((1,))

# op _03cZ_indexed_passthrough_eval
# LANG: _03cY, _03d3, _03d6 --> M
# SHAPES: (70, 1), (70, 1), (70, 1) --> (70, 3)
# full namespace: fish_model.ThrustDrag
v7027_M__temp[i_v7029__03cY__03cZ_indexed_passthrough_eval] = v7029__03cY.flatten()
v7027_M = v7027_M__temp.copy()
v7027_M__temp[i_v7032__03d3__03cZ_indexed_passthrough_eval] = v7032__03d3.flatten()
v7027_M = v7027_M__temp.copy()
v7027_M__temp[i_v7034__03d6__03cZ_indexed_passthrough_eval] = v7034__03d6.flatten()
v7027_M = v7027_M__temp.copy()

# op _03ci_indexed_passthrough_eval
# LANG: _03c1, _03c7, _03ck --> F_s
# SHAPES: (70, 1), (70, 1), (70, 1) --> (70, 3)
# full namespace: fish_model.ThrustDrag
v7007_F_s__temp[i_v6997__03c1__03ci_indexed_passthrough_eval] = v6997__03c1.flatten()
v7007_F_s = v7007_F_s__temp.copy()
v7007_F_s__temp[i_v7000__03c7__03ci_indexed_passthrough_eval] = v7000__03c7.flatten()
v7007_F_s = v7007_F_s__temp.copy()
v7007_F_s__temp[i_v7008__03ck__03ci_indexed_passthrough_eval] = v7008__03ck.flatten()
v7007_F_s = v7007_F_s__temp.copy()

# op _03e8_power_combination_eval
# LANG: thrust_power, panel_total_power --> efficiency
# SHAPES: (1,), (1,) --> (1,)
# full namespace: EfficiencyModel
v7072_efficiency = (v7051_thrust_power)*(v7071_panel_total_power**-1)
v7072_efficiency = v7072_efficiency.reshape((1,))

# op _03eN_power_combination_eval
# LANG: _03eM --> C_F
# SHAPES: (1,) --> (1,)
# full namespace: EelViscousModel
v7094_C_F = (v7093__03eM)
v7094_C_F = (v7094_C_F*_03eN_coeff).reshape((1,))