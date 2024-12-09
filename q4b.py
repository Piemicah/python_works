import numpy as np 
import matplotlib.pyplot as plt
x = [0]
y = [2.5]

def f(x,y):
    return np.sin(x*y)

x0,y0 = 0,2.5
h=0.02

for i in range(int(10/h)):
    y1 = y0 + h*f(x0+i*h,y0)
    x.append(x0+i*h)
    y.append(y1)
    y0 = y1

plt.plot(x,y)
plt.show()
