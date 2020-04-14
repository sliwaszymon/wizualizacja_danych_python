class NaZakupy:
    nazwa_produktu=""
    ilosc=0
    jednostka_miary=""
    cena_jed=0

    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jedn):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jedn = cena_jedn
    
    def wyswietl_produkty(self):
        print("Nazwa: ", self.nazwa_produktu)
        print("Ilosc: ", self.ilosc)
        print("Jednostka: ", self.jednostka_miary)
        print("Cena: ", self.cena_jedn)

    def ile_produktu(self):
        print(self.ilosc, self.jednostka_miary, sep=" ")

    def ile_kosztuje(self):
        return self.ilosc*self.cena_jedn

produkt = NaZakupy("Mąka", 4, "kg", 3.99)
produkt.wyswietl_produkty()
produkt.ile_produktu()
print(produkt.ile_kosztuje())