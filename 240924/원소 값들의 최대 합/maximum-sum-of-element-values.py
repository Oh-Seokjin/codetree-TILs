n, m = map(int, input().split())
elements = list(map(int, input().split()))
# print(elements)
max_sum = 0

for i in range(n):
    curr_idx = i
    temp_sum = 0
    for _ in range(m):
        # print(curr_idx)
        temp_sum += elements[curr_idx]
        curr_idx = elements[curr_idx]-1
    max_sum = max(max_sum, temp_sum)

print(max_sum)