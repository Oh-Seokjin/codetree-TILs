n = int(input())
b = [list(map(int, input().split())) for _ in range(n)]
###

max_score = 0
tic = 1
while True:
    b = [elem for elem in b if elem[1] >= tic]
    b.sort(key=lambda x: x[1])
    # print(b)
    if not b:
        break
    now_time = b[0][1]
    now_max = 0
    max_idx = 0
    for i in range(len(b)):
        if b[i][1] != now_time:
            break
        else:
            if b[i][0] >= now_max:
                now_max = b[i][0]
                max_idx = i
    max_score += now_max
    b.pop(max_idx)
    tic += 1

print(max_score)