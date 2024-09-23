n, t = map(int, input().split())

nums = list(map(int, input().split()))

nums = [elem if elem>t else 0 for elem in nums]

if sum(nums) == 0:
    print(0)
else:
    nums = "".join(map(str, nums))
    nums = nums.split("0")
    print(len(max(nums, key=lambda n: len(n))))