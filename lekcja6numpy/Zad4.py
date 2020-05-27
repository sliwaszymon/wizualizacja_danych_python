import numpy as np

def generuj(i, n):
    tablica = np.logspace(1, n, n, base=i, dtype="int64")
    return tablica

tablica = generuj(2, 10)
print(tablica)