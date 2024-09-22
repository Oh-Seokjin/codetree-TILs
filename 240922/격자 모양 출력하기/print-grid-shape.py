n, m = map(int, input().split())

result = []

for _ in range(n):
    result.append([0 for _ in range(n)])
    
for _ in range(m):
    row, col= map(int, input().split())
    result[row-1][col-1] = row*col

for elem_list in result:
    for elem in elem_list:
        print(f"{elem }", end=" ")
    print()