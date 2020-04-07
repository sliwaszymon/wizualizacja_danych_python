A = [1/x for x in range(11) if x>0]
B = [pow(2,x) for x in range(11)]
C = [x for x in B if x%4==0]
print(C)