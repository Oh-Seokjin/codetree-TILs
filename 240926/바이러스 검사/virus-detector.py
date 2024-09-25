n = int(input())
stores = [int(input()) for _ in range(n)]
leader_max, member_max = map(int, input().split())
#####

answer = n
for i in range(n):
    stores[i] -= leader_max

while True:
    if max(stores) <= 0:
        break
    for i in range(n):
        stores[i] -= member_max
        answer += 1
        if stores[i] <= 0:
            break

print(answer)