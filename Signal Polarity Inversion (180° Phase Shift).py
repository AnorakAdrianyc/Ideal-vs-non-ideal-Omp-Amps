import numpy as np
import matplotlib.pyplot as plt

# Generate time data (representing one full cycle from 0 to 2*pi)
time = np.linspace(0, 2 * np.pi, 500)

# Calculate Input (sine wave) and Inverted Output (negative sine wave)
v_in = np.sin(time)
v_out = -np.sin(time)

# Set up the plot layout and style
plt.figure(figsize=(9, 5))
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.grid(True, linestyle='--', alpha=0.6)

# Plot the input and output signals
plt.plot(time, v_in, label='Input Signal V_in', color='#1f77b4', linewidth=2.5)
plt.plot(time, v_out, label='Inverted Output Signal V_out', color='#d62728', linewidth=2.5, linestyle='--')

# Highlight and label the critical points of inversion (Points of Interest)
# Label the peak of V_in
plt.scatter(np.pi/2, 1, color='#1f77b4', zorder=5)
plt.text(np.pi/2 + 0.1, 1.05, 'V_in Peak (π/2, 1)', fontsize=10, weight='bold', color='#1f77b4')

# Label the corresponding trough of V_out
plt.scatter(np.pi/2, -1, color='#d62728', zorder=5)
plt.text(np.pi/2 + 0.1, -1.15, 'V_out Trough (π/2, -1)', fontsize=10, weight='bold', color='#d62728')

# Format axes and labels
plt.title('Signal Polarity Inversion (180° Phase Shift)', fontsize=14, pad=15, weight='bold')
plt.xlabel('Time (Radians)', fontsize=12)
plt.ylabel('Voltage (V)', fontsize=12)

# Set custom X-axis ticks to display pi intervals nicely
plt.xticks(
    [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],
    ['0', 'π/2', 'π', '3π/2', '2π']
)
plt.xlim(0, 2 * np.pi)
plt.ylim(-1.4, 1.4)

# Add baseline axis references
plt.axhline(0, color='black', linewidth=0.8, alpha=0.5)

# Add legend
plt.legend(loc='upper right', frameon=True, facecolor='white', edgecolor='none', shadow=True)

# Display the final layout cleanly
plt.tight_layout()
plt.show()
