n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    total_sum = 0
    for elem in range(a, b+1):
        if elem%2==0:
            total_sum += elem
    print(total_sum)