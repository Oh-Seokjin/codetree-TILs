n = int(input())

nums = list(map(int, input().split()))

for i in range(len(nums)):
    if i==0:
        print(nums[0], end=" ")
        break

    if i%2==0:
        print(nums[int(i//2)], end=" ")