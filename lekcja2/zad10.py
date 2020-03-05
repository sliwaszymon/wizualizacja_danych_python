import sys
loops = input("Jak duża ma być wieża: ")
loops = int(loops)+1
i, j = (0, 0)
for i in range(loops):
    for j in range(i):
        sys.stdout.write("A")
    sys.stdout.write("\n")