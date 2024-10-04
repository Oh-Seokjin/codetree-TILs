n, m, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
balls = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    balls[x-1][y-1] = 1
###

def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<n

def move():
    global balls
    temp_board = [[0 for _ in range(n)] for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if balls[x][y]:
                temp = []
                for dx, dy in zip(dxs, dys):
                    nx, ny = x+dx, y+dy
                    if in_range(nx, ny):
                        temp.append(board[nx][ny])
                    
                max_val = max(temp)
                for dx, dy in zip(dxs, dys):
                    nx, ny = x+dx, y+dy
                    if in_range(nx, ny) and board[nx][ny] == max_val:
                        temp_board[nx][ny] += 1
                        break
    return temp_board

def remove_collision(temp_board):
    global balls

    for x in range(n):
        for y in range(n):
            if temp_board[x][y] >= 2 or temp_board[x][y] <= 0:
                temp_board[x][y] = 0
    balls = temp_board

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

for _ in range(t):
    temp_board = move()
    remove_collision(temp_board)

cnt = 0

for i in range(n):
    cnt += sum(balls[i])

print(cnt)