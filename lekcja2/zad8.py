loops = input("Ile liczb chcesz dodać do listy: ")
loops = int(loops)
lista = []
for index in range(loops):
    a = input("Podaj liczbę: ")
    lista.insert(index, a)

print(lista)