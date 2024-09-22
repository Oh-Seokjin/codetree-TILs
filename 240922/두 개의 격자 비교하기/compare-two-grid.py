n, m = map(int, input().split())
matrix_a = []
matrix_b = []

for _ in range(n):
    row = list(map(int, input().split()))
    matrix_a.append(row)

for _ in range(n):
    row = list(map(int, input().split()))
    matrix_b.append(row)

for i in range(n):
    for j in range(m):
        if matrix_a[i][j] == matrix_b[i][j]:
            print("0 ", end="")
        else:
            print("1 ", end="")
    print()