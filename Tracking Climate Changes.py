import matplotlib.pyplot as plt
import numpy as np


#X-axis: altitude in meters above see level
altitude = np.array([0, 1000, 2000, 3000, 4000])
#Y axis: Temperature in Degrees Celsius
Temperature = np.array([25, 18.5, 12, 5.5, -1])


plt.plot(altitude, Temperature, marker='x', color ='blue')
plt.title("Atmospheric Temperature Lapse Rate")
plt.xlabel("Altitude (Meters)")
plt.ylabel("Temperature (°C)")

plt.show()