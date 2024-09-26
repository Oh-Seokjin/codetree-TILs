n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
#####

dp[0][n-1] = board[0][n-1]

# initial values
for x in range(-1, -1*n-1, -1):
    dp[0][x] = dp[0][x+1] + board[0][x]

for y in range(0, n):
    dp[y][n-1]  = dp[y-1][n-1] + board[y][n-1]
    
# fill
for y in range(1, n):
    for x in range(-2, -1*n-1, -1):
        dp[y][x] = min(dp[y-1][x], dp[y][x+1]) + board[y][x]
    
print(dp[n-1][0])