import os
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

# Initialize empty lists for each column
column1 = []
column2 = []
column3 = []
column4 = []
column5 = []
column6 = []

# Open the file for reading

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, 'vågtalsdata.txt')

with open(file_path, 'r') as file:
    # Iterate through each line in the file
    for line in file:
        # Split the line into two columns based on whitespace
        columns = line.split()
        
        # Convert the columns to floats and append to respective lists
        column1.append(float(columns[0]))
        column2.append(float(columns[1]))

file_path1 = os.path.join(script_directory, 'Kolmonoxiddata.txt')

with open(file_path1, 'r') as file:
    # Iterate through each line in the file
    for line in file:
        # Split the line into two columns based on whitespace
        columns = line.split()
        
        # Convert the columns to floats and append to respective lists
        column3.append(float(columns[0]))
        column4.append(float(columns[1]))

file_path2 = os.path.join(script_directory, 'våglängdsdata.txt')

with open(file_path2, 'r') as file:
    # Iterate through each line in the file
    for line in file:
        # Split the line into two columns based on whitespace
        columns = line.split()
        
        # Convert the columns to floats and append to respective lists
        column5.append(float(columns[0]))
        column6.append(float(columns[1]))


# Convert the lists to numpy arrays
# Wavenumumber for the CO spectrum
wave_number = np.array(column1)
number_intensity = np.array(column2)

# Carbon monoxide spectrum
wave_number1 = np.array(column3)
number_intensity1 = np.array(column4)

# Wavenumumber for the background data
wave_number2 = np.array(column5)*10**9
number_intensity2 = np.array(column6)

# Interpolate the background data
background_interp = interp1d(wave_number2, number_intensity2, kind='linear', fill_value="extrapolate")

# Create a common wavelength grid based on your CO spectrum
common_wavelength_grid = wave_number1

# Calculate the background values at the common wavelengths
background_at_common_wavelengths = background_interp(common_wavelength_grid)

# Subtract the background at common wavelengths from your CO spectrum
corrected_spectrum = number_intensity1 - background_at_common_wavelengths

# Plot the corrected spectrum
plt.figure(figsize=(10, 6))
plt.plot(wave_number1, corrected_spectrum, label='Corrected Spectrum', color='blue')
plt.xlabel('Wavenumber')
plt.ylabel('Intensity')
plt.legend()
plt.title('CO Absorption Spectrum with Background Subtracted')
plt.grid(True)
plt.show()