import numpy as np
import random as rand

a = np.array([[rand.randint(1,10) for x in range(3)] for y in range(1)])
b = np.array([[rand.randint(1,10) for x in range(3)] for y in range(1)])
print(a)
print(b)

#nie da się wykonać iloczynu macierzy 1x3 przez macierz 1x3
#print(a.dot(b))