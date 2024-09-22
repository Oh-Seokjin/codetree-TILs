m1, d1, m2, d2 = map(int, input().split())
day = input()
answer = 0

def cnt_days(m):
    days = 0
    if m in [1, 3, 5, 7, 8, 10, 12]:
        days += 31
    elif m == 2:
        days += 29
    else:
        days += 30
    return days

for m in range(m1, m2):
    answer += cnt_days(m)

answer = answer - d1 + d2
print(answer//7+1)