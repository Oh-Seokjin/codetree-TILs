n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
max_sum = [[0]*n for _ in range(n)]
#####

# initial values
max_sum[0][0] = board[0][0]
for x in range(n):
    temp_sum = 0
    for i in range(x+1):
        temp_sum += board[0][i]
    max_sum[0][x] = temp_sum

for y in range(n):
    temp_sum = 0
    for i in range(y):
        temp_sum += board[y][0]
    max_sum[y][0] = temp_sum

# fill
for row in range(1, n):
    for col in range(1, n):
        max_sum[row][col] = max(max_sum[row-1][col], max_sum[row][col-1]) + board[row][col]

max_sum[0][0] = board[0][0]

print(max(max_sum[n-1]))