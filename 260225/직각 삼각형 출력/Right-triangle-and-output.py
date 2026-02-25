n = int(input())
for i in range(0, (2*n) - 1, 2):
    print("*", end="")
    for j in range(i):
        print("*", end="")
    print()