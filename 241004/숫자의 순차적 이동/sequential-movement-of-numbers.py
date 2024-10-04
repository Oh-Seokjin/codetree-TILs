n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
###

def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<n

def find_loc(num):
    for i in range(n):
        for j in range(n):
            if board[i][j] == num:
                return (i, j)

def find_max_loc(x, y):
    max_val, max_x, max_y = 0, -1, -1
    for nx in range(x-1, x+2):
        for ny in range(y-1, y+2):
            if (x, y) == (nx, ny):
                continue
            if in_range(nx, ny) and board[nx][ny] > max_val:
                max_val = board[nx][ny]
                max_x, max_y = nx, ny
    return (max_x, max_y)

def swap_cen_max(cen_x, cen_y, max_x, max_y):
    global board

    board[cen_x][cen_y], board[max_x][max_y] = board[max_x][max_y], board[cen_x][cen_y]

for _ in range(m):
    for num in range(1, n*n+1):
        cen_x, cen_y = find_loc(num)
        max_x, max_y = find_max_loc(cen_x, cen_y)
        swap_cen_max(cen_x, cen_y, max_x, max_y)

for i in range(n):
    for j in range(n):
        print(board[i][j], end=" ")
    print()