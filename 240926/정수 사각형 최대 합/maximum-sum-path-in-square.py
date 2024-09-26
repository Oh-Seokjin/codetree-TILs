n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
max_sum = [[0]*n for _ in range(n)]
#####

# initial values
max_sum[0][0] = board[0][0]
for x in range(1, n):
    max_sum[0][x] = max_sum[0][x-1] + board[0][x]

for y in range(n):
    max_sum[y][0]  = max_sum[y-1][0] + board[y][0]
    
# fill
for row in range(1, n):
    for col in range(1, n):
        max_sum[row][col] = max(max_sum[row-1][col]+ board[row][col], max_sum[row][col-1]+ board[row][col]) 

max_sum[0][0] = board[0][0]
print(max(max_sum[n-1]))