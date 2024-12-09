import numpy as np
import matplotlib.pyplot as plt

g = 9.8

u = float(input("Enter initial Velocity: "))
theta = float(input("Enter angle: "))
d = theta * np.pi / 180
uy = u * np.sin(d)
ux = u * np.cos(d)
tf = 2 * uy / g
t = np.linspace(0, tf, 300)
height = (uy ** 2) / (2 * g)
max_range = (u ** 2) * np.sin(2 * d) / g
print("Maximum height = " + str(height))
print("Range  =  " + str(max_range))
print("Time of flight = " + str(tf))
fy = uy * t - (g * t ** 2) / 2
fx = ux * t

plt.plot(t, fy, label="vertical distance")
plt.plot(t, fx, label="Horizontal distance")
plt.xlabel(r"$time/s$")
plt.ylabel(r"$distance//m$")
plt.legend()
plt.show()
