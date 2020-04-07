def ilejest(** rzeczy):
    suma = 0
    for x in rzeczy:
        suma += rzeczy[x]
    return suma

print(ilejest(cola=2, chleb=2, baton=4, piwo=10))