import matplotlib.pyplot as plt
import numpy as np

# let's quickly plot that altitude vs temp stuff from the lab notes
# TODO: add more data points later if we get them from the weather station API? 
# for now just hardcoding what we measured yesterday

# X-axis: altitude in meters above see level (wait, typo in comment: sea level.. oh well, keeping it)
altitude = np.array([0, 1000, 2000, 3000, 4000])

# Y axis: Temperature in Degrees Celsius
# naming convention is a bit messy here with capital T, but it works
Temperature = np.array([25, 18.5, 12, 5.5, -1])

# init the plot 
fig, ax = plt.subplots()

# plotting with some basic styling... maybe change color later? blue is fine for cold temp tho
ax.plot(altitude, Temperature, marker='x', color='blue')

# adding labels manually because plt.title syntax sometimes slips my mind
ax.set_title("Atmospheric Temperature Lapse Rate")
ax.set_xlabel("Altitude (Meters)")
ax.set_ylabel("Temperature (°C)")

# let's throw in a grid so it's easier to read the values visually
ax.grid(True, linestyle='--', alpha=0.5)

# display the thing
plt.show()

# print out just to check values in terminal
# print(altitude, Temperature) # debug line, leaving it here commented out
