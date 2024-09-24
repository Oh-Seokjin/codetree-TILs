n, k = map(int, input().split())
nums = list(map(int, input().split()))
#####

cnt = 0

nums.sort()
while nums[-1] - nums[0] > k:
    min_cnt = nums.count(nums[0])
    max_cnt = nums.count(nums[-1])

    if min_cnt <= max_cnt:
        nums[0] += 1
        cnt += 1
    else:
        nums[-1] -= 1
        cnt += 1
    nums.sort()

print(cnt)