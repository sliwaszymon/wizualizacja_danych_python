def sumc(a=1, r=1, n=10):
    if n == 1:
        return a
    return a+sumc(a+r, r, n-1)
print(sumc())