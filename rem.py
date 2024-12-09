import numpy as np
import math
def f(x):
    s=0
    for i in range(1,x):
        s=s+math.factorial(i)
    return s

r=f(15)%30
print(r)