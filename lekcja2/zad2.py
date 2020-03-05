import sys

sys.stdout.write("Podaj pierwsza liczbe: ")
a = sys.stdin.readline()
sys.stdout.write("Podaj druga liczbe: ")
b = sys.stdin.readline()
wynik = int(a)*int(b)
sys.stdout.write(str(wynik))