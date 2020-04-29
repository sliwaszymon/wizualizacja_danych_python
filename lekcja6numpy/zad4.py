import numpy as np

def generuj(m,n):
    return np.logspace(1, n, num=n, base=m, dtype='int64')

print(generuj(2,4))