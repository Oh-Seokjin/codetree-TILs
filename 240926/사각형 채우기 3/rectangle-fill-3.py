n = int(input())
MOD = 1000000007
#####
dp = [-1] * (n+3)

dp[0], dp[1], dp[2] = 1, 2, 7

for i in range(3, n+1):
    dp[i] = dp[i - 1] * 2 + dp[i - 2] * 3
    for j in range(i-3, -1, -1):
        dp[i] = dp[i] + dp[j]*2

print(dp[n]%MOD)