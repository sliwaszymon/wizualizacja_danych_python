import numpy as np

def wykresl():
    lista=['maj','ioa','śap']
    return np.array([[x for x in lista[i]] for i in range(3)])
    
print(wykresl())