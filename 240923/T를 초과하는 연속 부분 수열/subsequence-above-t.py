n, t = map(int, input().split())

nums = list(map(int, input().split()))

nums = [elem if elem>t else "x" for elem in nums]

x_split = [i for i, value in enumerate(nums) if value == "x"]

max_len = 0

if len(x_split) == 0:
    print(len(nums))
elif len(x_split) == 1:
    print(max(len(nums[:x_split[0]]), len(nums[x_split[0]+1:])))
else:
    for i in range(len(x_split)-1):
        cur_len = x_split[i+1]-1 - x_split[i]
        if cur_len > max_len:
            max_len = cur_len
    print(max_len)