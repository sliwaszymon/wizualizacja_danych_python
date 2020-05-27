import numpy as np
import random as rand

a = np.array([[rand.randint(1,10) for x in range(3)] for y in range(1)])
b = np.array([[rand.randint(1,10) for x in range(1)] for y in range(3)])
c = np.array([[rand.randint(1,10) for x in range(3)] for y in range(1)])
print(a)
print(b)
print(c)

# miloczyn macierzy
print(a.dot(b))
# mnożenie proste
print(a*c)