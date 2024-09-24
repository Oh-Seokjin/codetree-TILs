n = int(input())
arr = list(map(int, input().split()))
#####

max_mul = 0

arr.sort()

n2_p1 = 1
n2_p1 *= arr[0]*arr[1]*arr[-1]

p3 = 1
p3 *= arr[-1]*arr[-2]*arr[-3]

print(max([max_mul, n2_p1, p3]))