total = 0

for i in range(1, 5):
    num_list = list(map(int, input().split()))
    for j in range(i):
        total += num_list[j]

print(total)