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
    temp = [[0 for _ in range(n)] for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if balls[x][y]:
                for dx, dy in zip(dxs, dys):
                    nx, ny = x+dx, y+dy
                    if in_range(nx, ny) and board[x][y] < board[nx][ny] and balls[x][y]:
                        # print(nx, ny)
                        temp[nx][ny] += 1
                        break
                    else:
                        temp[x][y] += 1
    return temp

def remove_collision(temp):
    global balls
    for x in range(n):
        for y in range(n):
            if temp[x][y] >= 2:
                temp[x][y] = 0
    balls = temp
    

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

for _ in range(t):
    temp = move()
    remove_collision(temp)
    # print(balls)

cnt = 0

for i in range(n):
    cnt += sum(balls[i])

print(cnt)