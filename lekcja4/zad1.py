plik = open("zad1.txt","w")
dane = []
for x in range(4,101,4):
    dane += [x]
plik.writelines(str(dane))
plik.close()