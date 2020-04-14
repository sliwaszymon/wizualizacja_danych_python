with open("zad3.txt", "a") as plik:
    for x in range(5):
        plik.write("aksjdalskd\n")

with open("zad3.txt", "r") as plik:
    for linia in plik:
        print(linia, end="")