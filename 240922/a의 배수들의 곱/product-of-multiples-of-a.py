total_mul = 1
a, b = map(int, input().split())
for elem in range(a, b+1):
    if elem%a == 0 :
        total_mul *= elem

print(total_mul)