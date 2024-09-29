n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
###

arr.sort(key=lambda x: x[1])

cnt = 0
last_end = -1

for start, end in arr:
    if last_end <= start:
        last_end = end
        cnt += 1
print(cnt)