import numpy as np
import random as rand

a = np.array([[rand.randint(1,10) for x in range(3)] for y in range(1)])
b = np.array([[1/rand.randint(2,10) for x in range(3)] for y in range(1)])
print(a)
print(b)
print(a*b)