import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(pd.ExcelFile("D:\Szkola\WD\Lab8\imiona.xlsx"), "Arkusz1")
grupa = df.groupby(['Plec']).agg({"Liczba":['sum']})
wykres = grupa.plot.bar()
wykres.set_ylabel('Mln')
wykres.set_xlabel('Plec')
wykres.legend()
plt.title('Liczba urodzonych dzieci danej płci w latach 2000-2017')
plt.show()