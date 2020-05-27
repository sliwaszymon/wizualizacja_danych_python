import numpy as np

def fun(tablica, kierunek):
    warunek = True
    if kierunek == "pion":
        if tablica.shape[1]%2 == 0:
            n = int(tablica.shape[1]/2)
            tab1 = tablica[:,:n]
            tab2 = tablica[:,n:]
        else:
            warunek=False
    elif kierunek == "poziom":
        if tablica.shape[0]%2 == 0:
            n = int(tablica.shape[0]/2)
            tab1 = tablica[:n,:]
            tab2 = tablica[n:,:]
        else:
            warunek=False
    else:
        print("Złe dane")
    if warunek==True:
        return tab1, tab2
    else:
        print("Tablica ma zle wymiary, nie mozna jej tak podzielic")
        return 0, 0

n = 7
tablica = np.array([[x for x in range(y*(n-1)+1, y*(n-1)+(n-1)+1)] for y in range(0, (n-1))])
print(tablica)
tab1, tab2 = fun(tablica, "pion")
print(tab1)
print(tab2)
tab1, tab2 = fun(tablica, "poziom")
print(tab1)
print(tab2)

tablica = np.array([[x for x in range(y*n+1, y*n+n+1)] for y in range(0, n)])
print(tablica)
tab1, tab2 = fun(tablica, "pion")
print(tab1)
print(tab2)
tab1, tab2 = fun(tablica, "poziom")
print(tab1)
print(tab2)