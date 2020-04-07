def monotonicznosc(a, b):
    if (a > 0):
        return "Funkcja jest rosnaca"
    elif (a == 0):
        return "Funkcja jest stala"
    else:
        return "Funkcja jest malejaca"
        
print(monotonicznosc(-2, 4))