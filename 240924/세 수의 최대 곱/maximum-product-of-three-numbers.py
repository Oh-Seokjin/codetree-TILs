n = int(input())
arr = list(map(int, input().split()))
#####

arr.sort()

n2_p1 = arr[0]*arr[1]*arr[-1]
p3 = arr[-1]*arr[-2]*arr[-3]

print(max(n2_p1, p3))