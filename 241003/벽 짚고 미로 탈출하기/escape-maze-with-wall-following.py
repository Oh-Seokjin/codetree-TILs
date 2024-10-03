n = int(input())
r, c = map(int, input().split())
r, c = r-1, c-1
board = [[x for x in input()] for _ in range(n)]
###

visited = [[[0, 0, 0, 0]]*n for _ in range(n)]

cnt = 0

def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<n

dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]

wall_x, wall_y = [1, 0, -1, 0], [0, 1, 0, -1]

d = 0

while True:
    nr, nc = r+dxs[d], c+dys[d]
    if nr == n or nc == n or nr == -1 or nc == -1:
        cnt += 1
        break
    if sum(visited[nr][nc]) == 4:
        cnt = -1
        break

    if board[nr][nc] == ".":
        if board[nr+wall_x[d]][nc+wall_y[d]] == "#":
            r, c = nr, nc
            cnt += 1
            visited[r][c][d] += 1
        elif board[nr+wall_x[d]][nc+wall_y[d]] == ".":
            r, c = nr, nc
            cnt += 1
            visited[r][c][d] += 1
            d += 1
            if d == 4:
                d = 0
            r, c = r+dxs[d], c+dys[d]
            cnt += 1
            visited[r][c][d] += 1
    elif board[nr][nc] == "#":
        visited[r][c][d] += 1
        d -= 1
        if d == -1:
            d = 3

print(cnt)
# for row in board:
#     print(row)