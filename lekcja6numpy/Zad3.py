import numpy as np

def fun(n):
    tablica = np.array([[(x+1)+(y*n) for x in range(n)] for y in range(n)])
    return tablica

tablica = fun(3)
print(tablica)
tablica2 = fun(5)
print(tablica2)