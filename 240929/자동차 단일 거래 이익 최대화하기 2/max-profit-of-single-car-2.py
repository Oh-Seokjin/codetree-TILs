n = int(input())
p = list(map(int, input().split()))
###

max_profit = 0

for i in range(n):
    for j in range(i+1, n):
        temp_profit = p[j] - p[i]
        max_profit = max(max_profit, temp_profit)

print(max_profit)


# n = int(input())
# arr = list(map(int, input().split()))
# #####

# answer = -1001
# temp_sum = 0

# for i in range(n):
#     if temp_sum < 0:
#         temp_sum = arr[i]
#     else:
#         temp_sum += arr[i]
#     # print("Temp:", temp_sum, end=" ")
#     # print("answer: ", answer)
#     answer = max(answer, temp_sum)

# print(answer)