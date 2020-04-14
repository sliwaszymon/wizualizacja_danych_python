class Robaczek():
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def idz_w_gore(self, ile_krokow):
        self.y = self.y + ile_krokow
    
    def idz_w_dol(self, ile_krokow):
        self.y = self.y - ile_krokow
    def idz_w_lewo(self, ile_krokow):
        self.x = self.x - ile_krokow
    def idz_w_prawo(self, ile_krokow):
        self.x = self.x + ile_krokow
    def pokaz_gdzie_jestes(self):
        print("x:", self.x, "y:", self.y, sep=" ")
    

robaczek = Robaczek(7, 11)
robaczek.pokaz_gdzie_jestes()
robaczek.idz_w_prawo(4)
robaczek.pokaz_gdzie_jestes()
robaczek.idz_w_gore(5)
robaczek.idz_w_lewo(2)
robaczek.idz_w_gore(1)
robaczek.idz_w_dol(2)
robaczek.pokaz_gdzie_jestes()