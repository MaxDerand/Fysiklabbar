import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Specify the first CSV file path
csv_file_path = 'C:\\Users\\masma\\fysik\\Fysiklabbar-1\\spektroskopi\\balmer.csv'

# Open the first CSV file and read its contents using pandas
df = pd.read_csv(csv_file_path, sep=';')  # Assuming ';' is the delimiter

# Replace commas with periods and convert to float for the first CSV data
df['Våglängd (nm)'] = df['Våglängd (nm)'].str.replace(',', '.').astype(float)
df['Intensitet Källa #3'] = df['Intensitet Källa #3'].str.replace(',', '.').astype(float)

# Specify the second CSV file path
csv_file_path2 = 'C:\\Users\\masma\\fysik\\Fysiklabbar-1\\spektroskopi\\balmerdarkcount.csv'

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

wavevalue1 = []

for i in range(len(result_intensity)):
    if result_intensity[i] > 5:
        if df['Våglängd (nm)'][i] > 605 or df['Våglängd (nm)'][i] < 560:
            wavevalue1.append(df['Våglängd (nm)'][i])

wavevalue = np.array(wavevalue1)
print(wavevalue)

valuelist = []
i = 21
while i < len(wavevalue)-1:
    valuelist.append(1 / (wavevalue[i] * (5 / 36)))
    i+=1

val = sum(valuelist) / len(valuelist)
#val = 1
index = None
for i in range(len(wavevalue)):
    if wavevalue[i] == 487.39:
        index = i
        break

print("Index of 487.39 in wavevalue:", index)

print(" ")
print(val)
# Show the plot
#plt.show()


#n = 6 -> Rh = 1.1002146236405856*10^7 m^-1
#n = 5 -> Rh = 1.1001180926909836*10^7 m^-1
#n = 4 -> Rh = 1.0992221082430004*10^7 m^-1
#n = 3 -> Rh = 1.099040697439882*10^7 m^-1


#Ger uppmätt <Rh> = 1.0996488805*10^7 m^-1
#Riktig uppmätt Rh = 1.09677576 x 10^-7 m1