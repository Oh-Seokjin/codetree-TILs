n = int(input())
i = 1
cnt = 0
while n >= 1:
    n = n//i
    cnt += 1
    i += 1
print(cnt)