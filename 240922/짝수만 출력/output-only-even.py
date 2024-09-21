a, b = map(int, input().split())
odd_list = []
for i in range(a, b+1):
    if i%2 == 0:
        print(i, end=" ")