# this code compute the length of the battery given its volumatric energy density and the energy required

enery_required = 0.01 # in wh
volumatric_energy_density = 250 # in wh/L

width = 5e-3 # in m
height = 0.05 # in m

width_dm = width*10 # in dm
height_dm = height*10 # in dm

battery_length_dm = enery_required/volumatric_energy_density/(width_dm*height_dm)
battery_length = battery_length_dm*10