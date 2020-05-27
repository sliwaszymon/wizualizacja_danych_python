import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(pd.ExcelFile("D:\Szkola\WD\Lab8\imiona.xlsx"), "Arkusz1")
a = df.agg({"Rok":['max']})
b = df[(df["Rok"]<=a.values[0][0])&(df["Rok"]>a.values[0][0]-5)]
grupa = b.groupby(["Plec"]).agg({"Liczba":["sum"]})
wykres = grupa.plot.pie(subplots=True, autopct='%.2f%%', fontsize=10, figsize=(6,6))
plt.show()