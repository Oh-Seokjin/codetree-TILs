n = int(input())

nums = list(map(int, input().split()))

for i in range(len(nums)):
    if i%2==0:
        temp = sorted(nums[:i+1])
        print(temp[int(i//2)], end=" ")