a = input("Podaj pierwszą liczbę: ")
b = input("Podaj drugą liczbę: ")
c = input("Podaj trzecią liczbę: ")
a = int(a)
b = int(b)
c = int(c)

if (0 < a <= 10):
    if a>c or b>c:
        print("a lub b jest większe od c")
    else:
        print("c jest największą wartością")

else:
    print("a nie mieści sie w przedziale (0,10>")