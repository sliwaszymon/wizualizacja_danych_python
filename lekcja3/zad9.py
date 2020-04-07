def iloczc(* liczby):
    if len(liczby) == 0:
        return 0
    else:
        iloczyn = 1
        for x in liczby:
            iloczyn *= x
        return iloczyn

print(iloczc(1,2,3,4,5))