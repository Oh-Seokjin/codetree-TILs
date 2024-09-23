n, s = map(int, input().split())
nums = list(map(int, input().split()))
total = sum(nums)
min_diff = 999999

for i in range(n):
    for j in range(i+1, n):
        temp_total = total - nums[i] - nums[j]
        temp_diff = abs(temp_total-s)
        min_diff = min(min_diff, temp_diff)
        
print(min_diff)