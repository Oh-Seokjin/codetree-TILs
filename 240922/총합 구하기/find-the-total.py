total_sum = 0
a, b = map(int, input().split())
for i in range(a, b+1):
    if a%6 == 0 and a%8 != 0:
        total_sum += a

print(total_sum)