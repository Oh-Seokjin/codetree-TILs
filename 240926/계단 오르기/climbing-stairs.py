n = int(input())
MOD = 10007
#####

dp = [0] * (n+3)
dp[2], dp[3] = 1, 1

for i in range(4, n+1):
    dp[i] = dp[i-2] + dp[i-3]

print(dp[n]%MOD)