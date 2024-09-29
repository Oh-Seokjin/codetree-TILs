n = int(input())
a = [i for i in range(1, 2*n+1)]
###
b = []
for _ in range(n):
    card = int(input())
    b.append(a.pop(a.index(card)))

a.sort()
a_win_cnt = 0

for i in range(n):
    cur_b = b.pop(0)
    for j in range(len(a)):
        cur_a = a[j]
        if cur_b < cur_a:
            a.pop(j)
            a_win_cnt += 1
            break

print(a_win_cnt)