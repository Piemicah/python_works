import numpy as np
def square(n):
    x=np.arange(1,n**2+1)
    np.random.shuffle(x)
    return x.reshape(n,n)


def isMagic(m):
    n=m.shape[0]
    total=n*(n**2+1)/2
    for i in range(n):
        if m[i,:].sum()!=total:
            return False
    for j in range(n):
        if m[:,j].sum()!=total:
            return False

    s3=0	
    for k in range(n):
        s3+=m[k,k]
    if s3!=total:
        return False

    s4=0
    for l in range(n):
        s4+=m[l,(n-1)-l]

    if s4!=total:
        return False
    
    return True

def main():
    n=int(input("Enter magic size: "))
    b=square(n)
    while not isMagic(b):
        b=square(n)

    print(b)

main()
