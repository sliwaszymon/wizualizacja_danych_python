import numpy as np

def fun(n):
    return np.array([[x for x in range(y*n+1,y*n+n+1)] for y in range(0,n)] )

print(fun(6))