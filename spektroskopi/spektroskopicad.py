import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Specify the first CSV file path
csv_file_path = 'C:\\Users\\masma\\OneDrive\\Skrivbord\\spektroskopi\\balmer.csv'

# Open the first CSV file and read its contents using pandas
df = pd.read_csv(csv_file_path, sep=';')  # Assuming ';' is the delimiter

# Replace commas with periods and convert to float for the first CSV data
df['Våglängd (nm)'] = df['Våglängd (nm)'].str.replace(',', '.').astype(float)
df['Intensitet Källa #3'] = df['Intensitet Källa #3'].str.replace(',', '.').astype(float)

# Specify the second CSV file path
csv_file_path2 = 'C:\\Users\\masma\\OneDrive\\Skrivbord\\spektroskopi\\balmerdarkcount.csv'

# Open the second CSV file and read its contents using pandas
df2 = pd.read_csv(csv_file_path2, sep=';')  # Assuming ';' is the delimiter

# Replace commas with periods and convert to float for the second CSV data
df2['Våglängd (nm)'] = df2['Våglängd (nm)'].str.replace(',', '.').astype(float)
df2['Intensitet Källa #4'] = df2['Intensitet Källa #4'].str.replace(',', '.').astype(float)

# Subtract "Intensitet Källa #4" from "Intensitet Källa #3" using NumPy arrays
result_intensity = df['Intensitet Källa #3'] - df2['Intensitet Källa #4']

# Create a figure and axis for the plot
fig, ax = plt.subplots()

# Plot the result
ax.plot(df['Våglängd (nm)'], result_intensity, label='Subtracted Intensity')

# Label the axes
ax.set_xlabel('Våglängd (nm)')
ax.set_ylabel('Subtracted Intensity')

# Show the plot
plt.show()