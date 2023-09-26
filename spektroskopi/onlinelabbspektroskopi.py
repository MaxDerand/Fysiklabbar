import os
import numpy as np
import matplotlib.pyplot as plt

# Initialize empty lists for each column
column1 = []
column2 = []
column3 = []
column4 = []
column5 = []
column6 = []

# List of file names
file_names = ['Kolmonoxiddata.txt', 'våglängdsdata.txt', 'vågtalsdata.txt']

# Get the script's directory
script_directory = os.path.dirname(os.path.abspath(__file__))

for file_name in file_names:
    # Construct the full file path
    file_path = os.path.join(script_directory, file_name)

    # Open the file for reading
    with open(file_path, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Split the line into six columns based on whitespace
            columns = line.split()
            
            # Convert the columns to floats and append to respective lists
            column1.append(float(columns[0]))
            column2.append(float(columns[1]))
            column3.append(float(columns[2]))
            column4.append(float(columns[3]))
            column5.append(float(columns[4]))
            column6.append(float(columns[5]))

# Convert the lists to numpy arrays
wave_number = np.array(column1)
number_intensity = np.array(column2)
# You can also convert column3 to column6 to numpy arrays if needed.

# Plot the data
plt.plot(wave_number, number_intensity)
plt.show()