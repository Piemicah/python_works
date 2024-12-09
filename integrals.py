import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x*x+3


a = int(input('Enter Lower limit: '))
b = int(input('Enter Upper limit: '))
n = int(input('Enter number of divisions: '))
dx = (b-a)/n

sum1 = 0.5*dx*(f(a)+f(b))
sum2 = 0
for j in range(1,n):
    s = dx*f(a+j*dx)
    sum2+=s

ans = sum1+sum2
print(ans)

for i in range(n+1):
    d = a+i*dx
    x = [d,d]
    y = [f(d),0]
    plt.plot(x,y,'k')

x=np.linspace(0,5,200)
plt.plot(x,f(x))
plt.axhline(0)
plt.axvline(0)
plt.title('A=$\int_{a}^b (x^2-2) dx$')
plt.box(False)
plt.axis([0,5,0,30])
plt.show()