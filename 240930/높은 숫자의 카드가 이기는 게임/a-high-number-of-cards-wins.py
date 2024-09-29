n = int(input())

###
b = [int(input()) for _ in range(n)]
a = [num for num in range(1, 2*n+1) if num not in b]

a.sort()
b.sort()
a_win_cnt = 0

b_idx = 0
for a_idx in range(n):

    if b_idx < n and a[a_idx] > b[b_idx]:
        a_win_cnt += 1
        b_idx += 1

print(a_win_cnt)