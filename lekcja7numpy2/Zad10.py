import numpy as np

macierz = np.arange(81).reshape(9,9)
print(macierz)
print(macierz.reshape(3,27))
print(macierz.reshape(27,3))
print(macierz.reshape(81, 1))

# macierz musi zawierać 81 elementow wiec mamy mozliwosc macierz.reshape(x, y) gdzie x*y=81 i x,y naleza do N