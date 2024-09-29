n = int(input())
arr = list(map(int, input().split()))
###

cost = 0

while True:
    if len(arr) == 1:
        break
    min1 = arr.pop(arr.index(min(arr)))
    min2 = arr.pop(arr.index(min(arr)))
    temp_cost = min1+min2
    cost += temp_cost
    arr.append(temp_cost)

print(cost)