n = int(input())
result = []

for _ in range(n):
    result.append([])

num = n**2

for i in range(n):
    if i%2==0:
        for j in range(n):
            result[n-1-j].append(str(num))
            num -= 1
    if i%2==1:
        for j in range(n):
            result[j].append(str(num))
            num -= 1

for elem in result:
    print(" ".join(elem))