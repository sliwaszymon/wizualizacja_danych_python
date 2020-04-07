#cgeo.py

def suma(a=1, r=1, n=10):
    if n==1:
        return a
    return a+suma(a*r, r, n-1)

def iloczyn(a=1, r=1, n=10):
    if n==1:
        return a
    return a*iloczyn(a*r, r, n-1)

def wyraz(a=1, r=1, n=1):
    if n==1:
        return a
    return wyraz(a*r, r, n-1)