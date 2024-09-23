n, t = map(int, input().split())
orders = input()
board = [list(map(int, input().split())) for _ in range(n)]
pos_x, pos_y = n//2, n//2
score = board[pos_x][pos_y]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
d_idx = 0

for i in range(len(orders)):
    if orders[i] == "R":
        d_idx += 1
        d_idx %= 4
    elif orders[i] == "L":
        d_idx -= 1
        if d_idx == -1:
            d_idx = 3
    elif orders[i] == "F":
        next_x = pos_x + dx[d_idx]
        next_y = pos_y + dy[d_idx]
        if (0 <= next_x <= n-1) and (0 <= next_y <= n-1):
            pos_x += dx[d_idx]
            pos_y += dy[d_idx]
            score += board[pos_x][pos_y]

print(score)