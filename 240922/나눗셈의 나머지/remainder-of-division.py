from collections import defaultdict
a, b = map(int, input().split())
cnt = defaultdict(int)
result = 0

while True:
    if a<=1:
        break
    cnt[a%b] += 1
    a = a//b

for elem in list(cnt.values()):
    result += elem**2
    
print(result)