def lcm(a, b):
    for i in range(max(a, b), a*b+1):
        if i%a==0 and i%b==0:
            return i

def rec_lcm(arr):
    if len(arr) == 1:
        return arr[0]

    temp_lcm = lcm(arr[0], arr[1])

    for i in range(2, len(arr)):
        temp_lcm = lcm(temp_lcm, arr[i])

    return temp_lcm


n = int(input())

nums = list(map(int, input().split()))

print(rec_lcm(nums))