n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
#####
# print(arr)

min_len = 103

for i in range(n):
    board = [0 for _ in range(103)]
    for j in range(n):
        if i == j:
            continue
        s, e = arr[j][0], arr[j][1]
        for k in range(s, e):
            board[k] += 1

    min_len = min(min_len, len("".join(list(map(str, board))).strip("0")))

print(min_len)