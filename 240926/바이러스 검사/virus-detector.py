n = int(input())
stores = list(map(int, input().split()))
leader_max, member_max = map(int, input().split())
#####

answer = n
for i in range(n):
    stores[i] -= leader_max

for i in range(n):
    if stores[i] <= 0:
        continue
    answer += stores[i] // member_max
    stores[i] = stores[i] % member_max
    if stores[i] <= member_max:
        answer += 1
        stores[i] -= member_max

print(answer)