import matplotlib.pyplot as plt

# Data
x = [
    0.0000, 0.0250, 0.0500, 0.0750, 0.1000, 0.1250, 0.1500, 0.1750, 0.2000,
    0.2250, 0.2500, 0.2750, 0.3000, 0.3250, 0.3500, 0.3750, 0.4000, 0.4250,
    0.4500, 0.4750, 0.5000, 0.5250, 0.5500, 0.5750, 0.6000, 0.6250, 0.6500,
    0.6750, 0.7000, 0.7250, 0.7500, 0.7750, 0.8000, 0.8250, 0.8500, 0.8750,
    0.9000, 0.9250, 0.9500, 0.9750, 1.0000
]

vx_0_3 = [
    0.0092, 0.0083, 0.0075, 0.0069, 0.0065, 0.0061, 0.0059, 0.0058, 0.0058,
    0.0059, 0.0060, 0.0062, 0.0065, 0.0068, 0.0071, 0.0075, 0.0079, 0.0084,
    0.0088, 0.0093, 0.0099, 0.0105, 0.0111, 0.0118, 0.0126, 0.0133, 0.0142,
    0.0151, 0.0160, 0.0170, 0.0180, 0.0190, 0.0200, 0.0211, 0.0221, 0.0230,
    0.0239, 0.0248, 0.0256, 0.0263, 0.0270
]

vx_0_6 = [
    0.0146, 0.0132, 0.0122, 0.0115, 0.0112, 0.0111, 0.0112, 0.0116, 0.0122,
    0.0130, 0.0139, 0.0150, 0.0161, 0.0173, 0.0186, 0.0198, 0.0211, 0.0224,
    0.0236, 0.0249, 0.0261, 0.0273, 0.0284, 0.0295, 0.0305, 0.0314, 0.0322,
    0.0330, 0.0336, 0.0341, 0.0346, 0.0350, 0.0353, 0.0356, 0.0358, 0.0360,
    0.0362, 0.0363, 0.0365, 0.0367, 0.0369
]

vx_0_9 = [
    0.0200, 0.0181, 0.0166, 0.0155, 0.0148, 0.0144, 0.0143, 0.0145, 0.0149,
    0.0156, 0.0164, 0.0174, 0.0184, 0.0196, 0.0208, 0.0220, 0.0233, 0.0246,
    0.0258, 0.0271, 0.0283, 0.0295, 0.0306, 0.0317, 0.0327, 0.0336, 0.0345,
    0.0352, 0.0358, 0.0364, 0.0368, 0.0372, 0.0376, 0.0379, 0.0381, 0.0384,
    0.0386, 0.0389, 0.0391, 0.0394, 0.0397
]

# Plot
plt.figure(figsize=(6, 3))
plt.plot(x, vx_0_3, label="$V_x=0.3$ m/s", linewidth=2, color="red")
plt.plot(x, vx_0_6, label="$V_x=0.6$ m/s", linewidth=2, color="green")
plt.plot(x, vx_0_9, label="$V_x=0.9$ m/s", linewidth=2, color="blue")

# Formatting
plt.xlabel("Longitudinal Coordinate ($x$) [m]", fontsize=12)
plt.ylabel("Undulation Amplitude ($y$) [m]", fontsize=12)
# plt.title("Variation of Undulation Amplitude Along Fish Body", fontsize=14)
# plt.grid(True, linestyle="--", alpha=0.7)
plt.legend(fontsize=12, loc="upper left")
plt.tight_layout()
# set figure size

plt.savefig("undulation_amplitude.pdf")
# Show plot
plt.show()