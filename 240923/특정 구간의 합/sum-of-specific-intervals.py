n, m = map(int, input().split())

nums = list(map(int, input().split()))

for _ in range(m):
    s, e = map(int, input().split())
    print(sum(nums[s-1:e]))