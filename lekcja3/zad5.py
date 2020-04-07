def rczp(a1, b1, a2, b2):
    if (a1==a2):
        return "Proste sa rownolegle"
    elif (a1*a2 == 1):
        return "Proste sa prostopadle"
    else:
        return "Proste nie sa rownolegle ani prostopadle"

print(rczp(2, 2, 1/2, 4))