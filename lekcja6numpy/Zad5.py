import numpy as np

def fun(n):
    return np.diag([n-x for x in range(n)])

wektor = fun(3)
print(wektor)