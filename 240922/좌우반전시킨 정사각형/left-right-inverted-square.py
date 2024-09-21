n = int(input())

for k in range(1, n+1):
    for i in range(n, 0, -1):
        print(f"{i*k }", end=" ")
    print()