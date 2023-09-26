import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Initialize empty lists for each column
wavelengthfotot = []
intensityfotot = []

# Specify the CSV file path
csv_file_path = 'C:\\Users\\masma\\OneDrive\\Skrivbord\\spektroskopi\\balmer.csv'

# Open the CSV file and read its contents using pandas
df = pd.read_csv(csv_file_path, sep=';')  # Assuming ';' is the delimiter

# Extract the data from the DataFrame
wavelengthfotot = df['Våglängd (nm)'].astype(float)
intensityfotot = df['Intensitet Källa #3'].astype(float)

# Now, wavelengthfotot and intensityfotot contain the numerical data from the CSV file

# Create a figure and axis for the plot
fig, ax = plt.subplots()

# Plot the data
ax.plot(wavelengthfotot, intensityfotot)

# Label the axes
ax.set_xlabel('Våglängd (nm)')
ax.set_ylabel('Intensity')

# Show the plot
plt.show()