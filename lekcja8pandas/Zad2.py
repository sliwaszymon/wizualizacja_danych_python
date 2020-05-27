import pandas as pd
import numpy as np

def pktA(plik):
    print(plik[plik['Liczba']>1000])

def pktB(plik):
    print(plik[plik['Imie']=="SZYMON"])

def pktC(plik):
    print(plik.agg({"Liczba":['sum']}))

def pktD(plik):
    print("w latach 2000-2005:",plik[(plik['Rok']>=2000)&(plik['Rok']<=2005)].agg({"Liczba":['sum']}))

def pktE(plik):
    M, K = plik[plik["Plec"] == 'M'],  plik[plik["Plec"] == 'K']
    print("chłopcy:",M.agg({"Liczba":['sum']}),"\ndziewczynik:", K.agg({"Liczba":['sum']}), sep="")

def pktF(plik):
    temp = plik.sort_values("Liczba", ascending="False").groupby(['Rok',"Plec"])
    for x, y in enumerate(temp, start=1):
        print(f"{y[0]}")
        print(f"{y[1].iloc[[0],[1]].values[0][0]}", end=" ")
        print(f"{y[1].iloc[[0],[2]].values[0][0]}")

def pktG(plik):
    M, K = plik[plik["Plec"] == 'M'],  plik[plik["Plec"] == 'K']
    M_max, K_max = plik[plik["Plec"] == 'M'].max(), plik[plik["Plec"] == 'K'].max()
    print(M[(M['Liczba']==M_max['Liczba'])], K[(K['Liczba']==K_max['Liczba'])], sep="\n")

narodziny = pd.read_excel(pd.ExcelFile("D:\Szkola\WD\Lab8\imiona.xlsx"), "Arkusz1")

# pktA(narodziny)
# pktB(narodziny)
# pktC(narodziny)
# pktD(narodziny)
# pktE(narodziny)
# pktF(narodziny)
# PktG(narodziny)