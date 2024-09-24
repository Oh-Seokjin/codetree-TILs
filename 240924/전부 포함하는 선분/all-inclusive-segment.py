n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
#####

min_len = float('inf')

for i in range(n):
    min_start = float('inf')
    max_end = float('-inf')
    
    for j in range(n):
        if i == j:
            continue
        min_start = min(min_start, arr[j][0])
        max_end = max(max_end, arr[j][1])
    
    min_len = min(min_len, max_end - min_start)

print(min_len)