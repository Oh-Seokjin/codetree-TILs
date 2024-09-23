n, s = map(int, input().split())
nums = list(map(int, input().split()))
total = sum(nums)
min_diff = 999999

for i in range(n):
    for j in range(i+1, n):
        temp_total = total - nums[i] - nums[j]
        # print(temp_total)
        temp_diff = abs(temp_total-s)
        # print(temp_diff)
        # print()
        if temp_diff < min_diff:
            min_diff = temp_diff

print(min_diff)

















# def combination(arr, n):
#     result = []
#     if n == 0:
#         return [[]]
    
#     for i in range(len(arr)):
#         elem = arr[i]
#         for rest in combination(arr[i+1:], n-1):
#             result.append([elem] + rest)
#     return result
        

# n, s = map(int, input().split())
# nums = list(map(int, input().split()))

# min_diff = 0

# comb_nums = combination(nums, n-2)
# comb_nums = sorted([sum(elem) for elem in comb_nums])

# for i in range(len(comb_nums)):
#     if i == 0:
#         min_diff = abs(comb_nums[i]-s)
#     else:
#         if min_diff > abs(comb_nums[i]-s):
#             min_diff = abs(comb_nums[i]-s)
# print(min_diff)