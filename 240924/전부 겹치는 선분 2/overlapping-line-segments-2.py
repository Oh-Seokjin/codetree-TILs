n = int(input())

lines = [0 for _ in range(105)]
for _ in range(n):
    s, e = map(int, input().split())
    for i in range(s, e+1):
        lines[i] += 1

cnt = 0

for line in lines:
    if line == n-1:
        cnt += 1

if cnt:
    print("Yes")
else:
    print("No")