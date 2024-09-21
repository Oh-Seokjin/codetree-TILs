total_sum = 0
a, b = map(int, input().split())
for elem in range(a, b+1):
    if elem%6 == 0 and elem%8 != 0:
        total_sum += elem

print(total_sum)