# code by "mraz3068"

import sys

si = sys.stdin.readline

n = int(si())

arr = [0] + list(map(int, si().split()))


arr.sort()

min_diff = sys.maxsize 
for i in range(1, n + 1):
    min_diff = min(min_diff, arr[n + i] - arr[i])

print(min_diff)