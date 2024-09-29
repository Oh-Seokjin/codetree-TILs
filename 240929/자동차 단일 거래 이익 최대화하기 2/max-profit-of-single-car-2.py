n = int(input())
p = list(map(int, input().split()))
###
max_profit = 0
min_price = p[0]

for i in range(n):
    profit = p[i] - min_price

    if profit > max_profit:
        max_profit = profit
    if min_price > p[i]:
        min_price = p[i]

print(max_profit)