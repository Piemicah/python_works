import numpy as np 
import matplotlib.pyplot as plt

def f(k):
    return (np.cosh(80*k)-15*k-1)

def df(k):
    return (80*np.sinh(80*k)-15)

k0 = 0.1
for i in range(50):
    k = k0 - f(k0)/df(k0)
    k0=k

s = (2*np.sinh(80*k0))/k0

print('s = ',s)