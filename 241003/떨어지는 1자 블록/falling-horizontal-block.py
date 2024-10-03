n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
k = k-1
###

for i in range(n):
    if i == n-1:
        for j in range(m):
            board[i][k+j] = 1
        break
    
    if 1 in board[i+1][k:k+m]:
        for j in range(m):
            board[i][k+j] = 1
        break

for row in board:
    for elem in row:
        print(elem, end=" ")
    print()