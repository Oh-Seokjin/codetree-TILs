n, m, r, c = map(int, input().split())
r, c = r-1, c-1
orders = input().split()
###
board = [[0 for _ in range(n)] for _ in range(n)]

def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<n

up, front, right = 1, 2, 3

board[r][c] = 7-up

for i in range(m):
    order = orders[i]

    if order == "D" and in_range(r+1, c):
        front, up = up, 7-front
        r, c = r+1, c
        board[r][c] = 7-up
    elif order == "U" and in_range(r-1, c):
        front, up = 7-up, front
        r, c = r-1, c
        board[r][c] = 7-up
    elif order == "R" and in_range(r, c+1):
        right, up = up, 7-right
        r, c = r, c+1
        board[r][c] = 7-up
    elif order == "L" and in_range(r, c-1):
        right, up = 7-up, right
        r, c = r, c-1
        board[r][c] = 7-up

answer = 0
for i in range(n):
    for j in range(n):
        answer += board[i][j]

print(answer)