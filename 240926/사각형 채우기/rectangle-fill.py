n = int(input())
MOD = 10007
#####

dp = [-1] * (n+3)
dp[0], dp[1], dp[2] = 0, 1, 2

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n]%MOD)