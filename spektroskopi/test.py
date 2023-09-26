import os
import numpy as np
import matplotlib.pyplot as plt

# Get the script's directory
script_directory = os.path.dirname(os.path.abspath(__file__))

# Define the data file path
file_path = os.path.join(script_directory, 'Kolmonoxiddata.txt')

# Shared graph settings
plt.rcParams['font.size'] = 13  # Set font size using the correct parameter name
plt.rcParams['lines.linewidth'] = 1
plt.rcParams['font.family'] = 'Arial'

label_settings = {
    'Interpreter': 'latex',
    'Fontsize': 19
}

# Read data from the data file
data = np.genfromtxt(file_path, delimiter=' ', names=['wave_number', 'intensity'])

# Set grid properties
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Create a figure and plot the data
plt.figure(1)
plt.plot(data['wave_number'], data['intensity'], 'k-')

plt.axis([4140, 4350, 0.075, 0.16])

# Set the x-axis label as plain text
plt.xlabel(r'$\lambda^{-1}$ / cm$^{-1}$', fontsize=19)

plt.ylabel('Relative intensity')
plt.xticks(np.arange(4000, 5050, 50))
plt.yticks(np.arange(0, 0.22, 0.02))
plt.savefig('CO_plot.png', format='png', dpi=300)

# Zoomed-in plot with peaks
plt.figure(2)

# Find peaks in the intensity data
from scipy.signal import find_peaks
peaks, _ = find_peaks(data['intensity'], distance=3, height=0.1)

# Plot the data with peaks
plt.plot(data['wave_number'], data['intensity'], 'k-')
plt.plot(data['wave_number'][peaks], data['intensity'][peaks], 'ro')

# Peak IDs
peak_labels = ['$P_3$', '$P_2$', '$P_1$', '$R_1$', '$R_2$', '$R_3$']
for i, (x, y) in enumerate(zip(data['wave_number'][peaks], data['intensity'][peaks])):
    plt.text(x - 0.5, y + 5e-3, peak_labels[i], **label_settings)

plt.axis([4230, 4290, 0.075, 0.16])
plt.xlabel(r'$\lambda^{-1}$ / cm$^{-1}$', fontsize=19)
plt.ylabel('Relative intensity', fontsize=19)
plt.yticks(np.arange(0, 0.22, 0.02))
plt.savefig('CO_peaks.png', format='png', dpi=300)

plt.show()