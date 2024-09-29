import heapq

n = int(input())
arr = list(map(int, input().split()))
###
pq = []
cost = 0

for elem in arr:
    heapq.heappush(pq, elem)

while len(pq) > 1:
    x1 = heapq.heappop(pq)
    x2 = heapq.heappop(pq)
    cost += (x1 + x2)
    heapq.heappush(pq, x1 + x2)
    # min1 = arr.pop(arr.index(min(arr)))
    # min2 = arr.pop(arr.index(min(arr)))
    # temp_cost = min1+min2
    # cost += temp_cost
    # arr.append(temp_cost)

print(cost)