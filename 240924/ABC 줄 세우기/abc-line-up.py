n = int(input())
arr = list(input().split())
#####

goal = [chr(ord("A") + i) for i in range(n)]

cnt = 0

for i in range(n):
    answer = chr(ord("A") + i)
    if arr[i] == answer:
        continue
    
    idx = arr.index(answer)
    arr.insert(i, arr.pop(idx))
    cnt += idx-i

print(cnt)