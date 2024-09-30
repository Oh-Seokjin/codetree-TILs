n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
###
reverse_grid = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        reverse_grid[i][j] = grid[j][i]

answer = 0

def happy_row(board, m):
    global answer
    for i in range(n):
        for j in range(n):
            check = board[i][j]
            if board[i][j:j+m] == [check]*m:
                answer += 1
                break

happy_row(grid, m)
happy_row(reverse_grid, m)

print(answer)