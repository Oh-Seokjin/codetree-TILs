n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
###

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
one = {0:3, 3:0, 1:2, 2:1}
two = {0:2, 2:0, 1:3, 3:1}
answer = 0

def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<n

def move(x, y, d):
    global answer
    cnt = 0

    while True:
        cnt += 1
        nx, ny = x+dxs[d], y+dys[d]
        if not in_range(nx, ny):
            break
        if board[nx][ny] == 1:
            d = one[d]
        elif board[nx][ny] == 2:
            d = two[d]
        x, y = nx, ny
    answer = max(answer, cnt)

for i in range(n):
    move(n, i, 0)
    move(-1, i, 1)
    move(i, n, 2)
    move(i, -1, 3)

print(answer)