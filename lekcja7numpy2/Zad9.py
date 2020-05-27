import numpy as np
import random as rand

macierz = np.array([[rand.randint(0, 11) for x in range(3)] for y in range(3)])
print(macierz)

for x in macierz.flat:
    print(x)