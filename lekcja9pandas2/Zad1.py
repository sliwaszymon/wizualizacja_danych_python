import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel(pd.ExcelFile("D:\Szkola\WD\Lab8\imiona.xlsx"), "Arkusz1")
wykres = df.groupby(['Rok']).agg({'Liczba':['sum']})
wykres.plot()
plt.legend()
plt.show()
