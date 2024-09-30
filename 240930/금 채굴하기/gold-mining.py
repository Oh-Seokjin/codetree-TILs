n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
###

max_gold = 0

def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<n

def calculate_cost(k):
    return k * k + (k + 1) * (k + 1)

def diamond(k):
    global max_gold
    cost = calculate_cost(k)
    for x in range(n):
        for y in range(n):
            temp_gold = 0
            for i in range(-k, k+1):
                for j in range(-k, k+1):
                    if abs(i)+abs(j) <=k:
                        nx, ny = x+i, y+j
                        if in_range(nx, ny) and board[nx][ny]:
                            temp_gold += m
            if cost <= temp_gold:
                max_gold = max(max_gold, temp_gold//m)

for k in range(n+1):
    diamond(k)

print(max_gold)