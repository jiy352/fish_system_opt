import matplotlib.pyplot as plt
import numpy as np

# Updated Data
Vx = np.array([0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])  # Velocity in m/s
Tail_Frequency = np.array([0.32299, 0.48054, 0.64342, 0.80637, 0.96063, 1.11830, 1.28623, 1.45842, 1.60344])  # Tail Frequency in Hz
Amplitude_Max = np.array([0.03269, 0.02998, 0.02762, 0.02604, 0.02516, 0.02430, 0.02319, 0.02209, 0.02203])  # Amplitude Max in meters
CoT = np.array([0.01322, 0.02426, 0.03733, 0.05245, 0.06850, 0.08629, 0.10538, 0.12503, 0.14718])  # CoT × Mass in J/m

# Create a figure with subplots
fig, axes = plt.subplots(1, 3, figsize=(15/1.1, 5/1.1))  # 1 row, 3 columns

# Plot 1: Tail Frequency vs Velocity
axes[0].plot(Vx, Tail_Frequency, marker='o', linestyle='-', color='b')
axes[0].set_xlabel(r'$v_x$ ($\mathrm{m/s}$)', fontsize=12)
axes[0].set_ylabel(r'Tail Frequency [$\mathrm{Hz}$]', fontsize=12)

# Plot 2: Amplitude Max vs Velocity
axes[1].plot(Vx, Amplitude_Max, marker='s', linestyle='-', color='r')
axes[1].set_xlabel(r'$v_x$ ($\mathrm{m/s}$)', fontsize=12)
axes[1].set_ylabel(r'Amplitude [$\mathrm{m}$]', fontsize=12)

# Plot 3: Cost of Transport vs Velocity
axes[2].plot(Vx, CoT, marker='^', linestyle='-', color='g')
axes[2].set_xlabel(r'$v_x$ ($\mathrm{m/s}$)', fontsize=12)
axes[2].set_ylabel(r'Energy cost per unit distance $\mathrm{CoT} \times m$ ($\mathrm{J/m}$)', fontsize=12)

# Adjust layout
plt.tight_layout()

# Save the figure (optional)
plt.savefig('academic_plots_no_grid_with_units.pdf', dpi=400, bbox_inches='tight')

# Show the plot
plt.show()