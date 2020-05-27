import numpy as np

def fun(n):
    wynik = np.diag([2 for x in range(n)])
    for y in range(2,n+1):
        wynik += np.diag([2*y for x in range(n-y+1)],-(y-1))
        wynik += np.diag([2*y for x in range(n-y+1)],(y-1))
    return wynik

macierz = fun(5)
print(macierz)