import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

import os

# Determine the script's directory
script_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the file path to your file in the same directory
file_path = os.path.join(script_directory, 'Data_Heat_Pump_Del_2.txt')

# Initialize empty lists for each column
time_data = []
counts_data = []
tempH_data = []
tempC_data = []

# Open the file for reading
with open(file_path, 'r') as file:
    # Skip the first two lines
    next(file)
    next(file)

    # Iterate through the remaining lines
    for line in file:
        # Split the line into columns using tab as the delimiter
        columns = line.strip().split('\t')
        
        # Check if there are enough columns and if the second column has data
        if len(columns) >= 2 and columns[1]:
            # Extract and convert data from each column
            time_data.append(float(columns[0].replace(',', '.')))
            counts_data.append(int(columns[1]))
            tempH_data.append(float(columns[2].replace(',', '.')))
            tempC_data.append(float(columns[3].replace(',', '.')))

h_func = np.polyfit(time_data, tempH_data, 4)
c_func = np.polyfit(time_data, tempC_data, 4)

#Antar att effekten är jämn?
p_in = np.array(counts_data)
#W_graf1 = np.polyfit(time_data, p_in, 1)*4500
#W_graf2 = np.array([0.14208477508, 0])
W_graf3 = np.cumsum(p_in)*4500

#print(W_graf3)
#print(len(W_graf3))

W_t = np.polyfit(time_data, W_graf3, 1)
dWdt_func = np.polyder(W_t)
dWdt_val = np.polyval(dWdt_func, time_data)
#print(dWdt_func)

#Antar att m = 10 kg och c = 4180
dQdt_func = np.polyder(h_func)
dQdt_val = np.polyval(dQdt_func, time_data)*4810*10
#print(" ")
#print(h_func)
#print(" ")
#print(dQdt_func)

#Carnot 
Vftheory = (np.array(tempH_data)+273)/(np.array(tempH_data)-np.array(tempC_data))
Vfexperimental = dQdt_val/dWdt_val
Vfquota = Vfexperimental/Vftheory


print(Vftheory)

start_index = 0
end_index = 1360
#integral = np.t#rapz(W_graf1[start_index:end_index+1], x=time_data[start_index:end_index+1])
#print(W_graf3)
plt.plot(time_data, W_graf3)
#plt.plot(time_data, dQdt_val)
#plt.plot(time_data, dWdt_val)

#plt.plot(time_data, np.polyval(h_func, time_data), label="T$_H$(t)", color='red')
#plt.plot(time_data, np.polyval(c_func, time_data), label="T$_C$(t)", color = 'blue')

#plt.plot(time_data,tempH_data, "o", label = "verkliga värden Th", color = 'red')
#plt.plot(time_data,tempC_data, "o", label = "verkliga värden Tc", color = 'blue')

#plt.plot(time_data, Vftheory, label="Theoretical values", color = 'red')
#plt.plot(time_data, Vfexperimental, label="Experimental values", color = 'blue')
plt.plot(time_data, np.polyval(W_t, time_data)/1000, label="W$_{in}$(t)", color = 'red')

#plt.plot(time_data, Vfquota, label="V$_{f experimentell}$(t) / V$_{f teori}$(t)")
plt.xlabel('t / s')
plt.ylabel('W / kJ')
plt.legend()
plt.show()

#plt.plot(time_data, Vf, label="Vf(t)", color = 'green')
# Now you have the data in separate lists
#print("Time Data:", time_data)
#print("Counts Data:", counts_data)
#print("Temperature 1 Data:", temp1_data)
#print("Temperature 2 Data:", temp2_data)

#print(np.polyval(dQdt, time_data))
#print(np.polyval(dWdt, time_data))