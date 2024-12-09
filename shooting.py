import numpy as np

def f2(x,y):
    return (2*y+8*x*(9-x))


def f(m):
    z0=m
    x0,y0 = 0,0
    for i in np.linspace(3,9,3):
        h = 3
        y = y0 + z0*h
        z = z0 + f2(x0,y0)*h
        
        y0 = y
        z0 = z
        x0 = i
        print('x = ',x0,' ; y = ',y,' ; z = ',z)
    return y


p0,p1 = 1,-25
q0 =f(p0)
q1 =f(p1)
q=0

p = p0 + (p1-p0)*(q-q0)/(q1-q0)

f(p)

