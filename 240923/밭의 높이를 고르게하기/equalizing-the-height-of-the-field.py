n, h, t = map(int, input().split())

field = list(map(int, input().split()))

min_act = 9999999
min_idx = 0

answer = 0

for i in range(0, len(field)-t+1):
    cnt_flatten = sum([abs(h-elem) for elem in field[i:i+t]])
    if cnt_flatten < min_act:
        min_act = cnt_flatten
        min_idx = i

for elem in field[min_idx:min_idx+t]:
    answer += abs(elem-h)

print(answer)