n = int(input())

result = []
result.append([1 for _ in range(n)])
for _ in range(n-1):
    result.append([1])

for i in range(1, n):
    for j in range(1, n):
        temp = 0
        temp += result[i-1][j] + result[i][j-1] + result[i-1][j-1]
        result[i].append(temp)

for elem_list in result:
    for elem in elem_list:
        print(f"{elem }", end=" ")
    print()