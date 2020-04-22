class Ksztalty:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x=x 
        self.y=y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik


class Kwadrat(Ksztalty):

    def __init__(self, x):
        self.x = x
        self.y = x

    def __str__(self):
            return 'Kwadrat o boku {}'.format(self.x)

    def __add__(self, other):
        newx = self.x + other.x
        return Kwadrat(newx)


kwadratpier=Kwadrat(3)
kwadratdru=Kwadrat(5)
kwadrattrz=Kwadrat(7)
kwadratczw=kwadratpier + kwadrattrz
print(kwadratczw)