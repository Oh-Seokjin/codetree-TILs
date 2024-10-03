n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
k = k-1
###

for i in range(n-1, -1, -1):
    if board[i][k:k+m] == [0]*m:
        for j in range(m):
            board[i][k+j] = 1
        break

for row in board:
    for elem in row:
        print(elem, end=" ")
    print()