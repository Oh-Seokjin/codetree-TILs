n = int(input())
arr = list(map(int, input().split()))
#####

answer = -1001
temp_sum = 0

for i in range(n):
    if temp_sum < 0:
        temp_sum = arr[i]
    else:
        temp_sum += arr[i]
    # print("Temp:", temp_sum, end=" ")
    # print("answer: ", answer)
    answer = max(answer, temp_sum)

print(answer)