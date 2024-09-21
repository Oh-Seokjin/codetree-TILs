a, b = map(int, input().split())
c = 2*a+b
print(a, b, c, sep=" ", end=" ")
for _ in range(7):
    a, b = b, c
    c = 2*a+b
    print(2*a+b, end=" ")