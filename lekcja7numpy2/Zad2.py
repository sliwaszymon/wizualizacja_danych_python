import numpy as np
import random as rand

a3x3 = np.array([[rand.randint(0,11) for x in range(3)] for y in range(3)])
b4x4 = np.array([[rand.randint(0,11) for x in range(4)] for y in range(4)])

print(a3x3)
print(b4x4)

print("Najniższa wartość każdej z kolumn macierzy 3x3:")
print(a3x3.min(axis=0))
print("Najniższa wartość każdgo z wierszy macierzy 3x3:")
print(a3x3.min(axis=1))

print("Najniższa wartość każdej z kolumn macierzy 4x4:")
print(b4x4.min(axis=0))
print("Najniższa wartość każdgo z wierszy macierzy 4x4:")
print(b4x4.min(axis=1))
