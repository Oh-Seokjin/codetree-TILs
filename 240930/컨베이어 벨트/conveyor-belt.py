n, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2)]
###
t = t % (2*n)

for _ in range(t):
    arr[0].insert(0, arr[1].pop())
    arr[1].insert(0, arr[0].pop())

for row in arr:
    for elem in row:
        print(elem, end=" ")
    print()