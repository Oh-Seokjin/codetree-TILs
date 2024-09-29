n = int(input())
a = [i for i in range(1, 2*n+1)]
###
b = []
for _ in range(n):
    card = int(input())
    b.append(a.pop(a.index(card)))

a.sort()
b.sort()
a_win_cnt = 0

b_idx = 0
for a_idx in range(n):

    if b_idx < n and a[a_idx] > b[b_idx]:
        a_win_cnt += 1
        b_idx += 1

print(a_win_cnt)