listazakupow = {
    "Mleko" : "litry",
    "Baton" : "sztuki",
    "Woda" : "litry",
    "Jogurt" : "sztuki",
    "Szynka" : "kilogramy",
    "Chleb" : "sztuki",
}

szt = [x for x in listazakupow.keys() if listazakupow[x] == "sztuki"]
print(szt)