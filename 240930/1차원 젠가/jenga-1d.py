n = int(input())
arr = [int(input()) for _ in range(n)]
###

for _ in range(2):
    s, e = map(int, input().split())
    for i in range(s-1, e):
        arr[i] = -1
    temp = []
    for i in range(len(arr)):
        if arr[i] != -1:
            temp.append(arr[i])
    arr = temp

print(len(arr))
for elem in arr:
    print(elem)