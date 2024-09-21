n = int(input())
num = 0
for k in range(1, n+1):
    for _ in range(n):
        if k%2 == 0:
            num += 2
        else:
            num += 1
        print(num, end=" ")  
    print()