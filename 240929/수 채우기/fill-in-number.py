n = int(input())
coins = [5, 2]
###

cnt = 0

for coin in coins:
    if coin <= n:
        cnt += n // coin
        n = n % coin
    
if n != 0:
    print(-1)
else:
    print(cnt)