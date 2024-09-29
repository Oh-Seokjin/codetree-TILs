n = int(input())
arr = list(map(int, input().split()))
###

cost = 0

while True:
    if len(arr) == 1:
        break
    arr.sort(reverse=True)
    min1 = arr.pop()
    min2 = arr.pop()
    cost += min1+min2
    arr.append(min1+min2)

    # min1 = arr.pop(arr.index(min(arr)))
    # min2 = arr.pop(arr.index(min(arr)))
    # temp_cost = min1+min2
    # cost += temp_cost
    # arr.append(temp_cost)

print(cost)