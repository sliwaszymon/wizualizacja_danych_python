import random
M = [[random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10)] for x in range(4)]
print(M)
L = [M[x][x] for x in range(4)]
print(L)