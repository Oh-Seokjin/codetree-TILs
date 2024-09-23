n, h, t = map(int, input().split())

field = list(map(int, input().split()))

min_act = 9999999
for i in range(0, len(field)-t):
    cnt_flatten = abs(h*t - sum(field[i:i+t]))
    print(i, cnt_flatten)
    if cnt_flatten < min_act:
        min_act = cnt_flatten
print(min_act)