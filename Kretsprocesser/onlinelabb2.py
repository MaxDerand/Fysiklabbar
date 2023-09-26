import numpy as np
import matplotlib.pyplot as plt

T1 = np.array([49.2, 42.2, 24.8, 21, -2.6,-1.3, 17, 17.9])
T2 = np.array([64.8, 55.7, 37.2, 29.8, -2, -1, 8, 13.6])

p1 = np.array([8.2,  8.2,  8.2,  8.2, 1.8, 1.8, 1.8, 1.8])
p2 = np.array([11.8, 11.8, 11.8, 11.8, 1.8, 1.8, 1.8, 1.8])

#for i in range(7):
 #   print(T1[i])

plt.scatter(T1, p1, label= "Efter 5 minuter")
plt.scatter(T2, p2, label= "Efter 15 minuter")
plt.xlabel('T / °C')
plt.ylabel('P / bar')
plt.legend()
plt.show()


