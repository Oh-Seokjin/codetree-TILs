n, r, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
r, c = r-1, c-1
###

def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<n

def search(x, y):
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if in_range(nx, ny) and (board[x][y] < board[nx][ny]):
            return (nx, ny)
    
    return -1

answer = []
answer.append(board[r][c])

while True:
    next_loc = search(r, c)
    if next_loc == -1:
        break
    else:
        r, c = next_loc
        answer.append(board[r][c])

for elem in answer:
    print(elem, end=" ")