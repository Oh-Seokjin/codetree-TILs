n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
###


while True:
    bomb = []
    end_cnt = 0
    flag = 0
    for elem in set(arr):
        if arr.count(elem) >= m:
            flag = 1
    if flag == 0:
        break

    for i in range(len(arr)):
        cnt = 1
        tgt = arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] == tgt:
                cnt += 1
            else:
                break
        if cnt >= m:
            bomb.append([i, i+cnt])
        if cnt == 1:
            end_cnt += 1

    
    for s, e in bomb:
        for i in range(s, e):
            arr[i] = 0
    temp = []
    for elem in arr:
        if elem != 0:
            temp.append(elem)
    arr = temp
    if end_cnt == len(arr):
        break

if not arr:
    print(0)
else:
    print(len(arr))
    for elem in arr:
        print(elem)