import numpy as np

a = np.array([2.9, 7.21, 3.14, 9.11])
print(a.dtype)
print(a)
b = a.astype('int64')
print(b.dtype)
print(b)
# konwertowanie float->int robi przybliżenie
# do największej liczby całkowitej mniejszej niż dana wartość