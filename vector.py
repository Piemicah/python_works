import numpy as np 
import matplotlib.pyplot as plt

x,y = np.meshgrid(np.linspace(-5,5,10),np.linspace(-5,5,10))
u = 2*x
v= 2*y

plt.quiver(x,y,u,v,color='g')
plt.show()