n = int(input())
MOD = 1000000007
#####
dp = [-1] * (n+3)

dp[0], dp[1], dp[2] = 0, 2, 7

for i in range(3, n+1):
    dp[i] = 3*dp[i-1] + dp[i-2] -1

print(dp[n]%MOD)