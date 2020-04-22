class Material():
    rodzaj=""
    dlugosc=0
    szerokosc=0

    def __init__(self, rodzaj, dlugosc, szerokosc):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc
    def wyswietl_nazwe(self):
        print(self.__class__.__name__)


class Ubranie(Material):
    rozmiar = ""
    kolor = ""
    dla_kogo = ""

    def wyswietl_dane(self):
        print("{} {} {} {} {} {}".format(self.rodzaj, self.dlugosc, self.szerokosc, self.rozmiar, self.kolor, self.dla_kogo))


class Sweter(Ubranie):
    rodzaj_swetra = ""

    def wyswietl_dane(self):
        print("{} {} {} {} {} {} {}".format(self.rodzaj, self.dlugosc, self.szerokosc, self.rozmiar, self.kolor, self.dla_kogo, self.rodzaj_swetra))


od_babci_pod_choinke = Sweter("wloczka", 90, 210)
od_babci_pod_choinke.rozmiar = "trzy iks el"
od_babci_pod_choinke.dla_kogo = "dla starego"
od_babci_pod_choinke.rodzaj_swetra = "taki przez glowe zakladany no wiesz"
od_babci_pod_choinke.kolor = "taki jaka sie wloczka ostala ze skarpet dla dziadka"
od_babci_pod_choinke.wyswietl_nazwe()
od_babci_pod_choinke.wyswietl_dane()
Moher=Material("moherowy", 20, 10)
Moher.wyswietl_nazwe()
koszula=Ubranie("sztuczny fest", 20, 10)
koszula.rozmiar = "XD"
koszula.kolor = "rozowy"
koszula.dla_kogo="dla mnie"
koszula.wyswietl_dane()
koszula.wyswietl_nazwe()
