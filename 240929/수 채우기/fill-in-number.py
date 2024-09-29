n = int(input())
INF = 1e11
###

ans = MAX_NUM

for i in range(0, INF + 1):
    remainder = n - 5 * i
    if remainder >= 0 and remainder % 2 == 0:
        ans = min(ans, i + (remainder // 2))
    
if ans == MAX_NUM:
    ans = -1

print(ans)