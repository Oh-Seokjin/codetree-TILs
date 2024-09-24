n = int(input())

lines = [0 for _ in range(100)]
for _ in range(n):
    s, e = map(int, input().split())
    for i in range(s, e):
        lines[i] += 1
if "".join(map(str, lines)).strip("0").count("0") <= 1:
    print("Yes")
else:
    print("No")