liczba = input("Podaj liczbę składającą się z wielu cyfr: ")
dlugosc = int(len(liczba))
i, wynik = (0, 0)
while i < dlugosc:
    wynik += int(liczba[i])
    i+=1
print(wynik)



#for cyfra in str(liczba):
#wynik += int(cyfra)

#sum([int(cyfra) for cyfra in str(liczba)])