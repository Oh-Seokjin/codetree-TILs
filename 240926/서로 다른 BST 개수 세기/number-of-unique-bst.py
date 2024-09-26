n = int(input())
#####

dp = [0] * (n+2)
dp[0], dp[1], dp[2] = 1, 1, 2

for i in range(3, n+1):
    for j in range(n):
        dp[i] += dp[j] * dp[i-j-1]

print(dp[n])