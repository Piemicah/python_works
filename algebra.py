import numpy as np
import matplotlib.pyplot as plt
a0,b0,c0,d0 = -2,-2,1,0
a,b,c,d=2,2,2,2
for i in range(200):
    a=8-b0-c0-d0
    b=(17-a*c0-a*d0-c0*d0)/(a+c0+d0)
    c=(-22-a*b*d0)/(a*b+b*d0+a*d0)
    d=-104/(a*b*c)
    #print('a = ',a,' : b = ',b,' : c = ',c,' : d = ',d)
    #a0 = a
    b0 = b
    c0 = c
    d0 = d

print('a = ',a,' : b = ',b,' : c = ',c,' : d = ',d)