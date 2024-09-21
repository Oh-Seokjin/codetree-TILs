a, b = map(int, input().split())

for i in range(2, 9, 2):
    for n in range(b, a-1, -1):
        print(f"{n} * {i} = {n*i}", end="")
        if n != a:
            print(" / ", end="")
    
    print()