def coloring(color, x1, y1, x2, y2):
    for x in range(x1, x2):
        for y in range(y1, y2):
            board[x][y] = color

n = int(input())

board = [[0 for _ in range(201)] for _ in range(201)]

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())

    if i%2==0:
        coloring(0, x1, y1, x2, y2)
    else:
        coloring(1, x1, y1, x2, y2)

print(sum(sum(row) for row in board))