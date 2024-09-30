n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
###

def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<m

squares = []
for i in range(1, n+1):
    for j in range(1, m+1):
        squares.append((i, j))

answer = -1

for x in range(n):
    for y in range(m):
        for sq_x, sq_y in squares:
            temp_size = -1
            if in_range(x+sq_x, y+sq_y):
                temp_size = sq_x * sq_y
                for dx in range(sq_x):
                    for dy in range(sq_y):
                        nx, ny = x+dx, y+dy
                        if board[nx][ny] < 0:
                            temp_size = -1000000
            answer = max(answer, temp_size)

print(answer)