import numpy as np
def f2(r,u,w):
    return (-w/r +u/(r**2))


def f(m):
    w0=m
    r0,u0 = 5,0.0038371
    for i in np.arange(5,8.75,.75):
        h = .75
        u = u0 + w0*h
        w = w0 + f2(r0,u0,w0)*h
        
        u0 = u
        w0 = w
        r0 = i
        print('r = ',r0,' ; u = ',u,' ; w = ',w)
    return u


f(-0.00053076)
p0,p1 = -0.00026538,-0.00053076
q0 =f(p0)
q1 =f(p1)
q=0.0030770

p = p0 + (p1-p0)*(q-q0)/(q1-q0)

f(p)
