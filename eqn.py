y0=0
z0=0
x,y,z=1,1,1
for i in range(50):
    x=7-2*y0-3*z0
    y=2*x+2*z0-5
    z=3*y-3*x+4
    print('x = ',x,' : y = ',y,' : z = ',z)
    #x0=x
    y0=y
    z0=z
    
print(x)
print(y)
print(z)
