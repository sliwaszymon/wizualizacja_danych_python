import numpy as np

def fibonacci(x=0):
    if x==1 or x==0:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)

macierz = np.array([[fibonacci(x+(y*5)) for x in range(5)] for y in range(5)])
print(macierz)