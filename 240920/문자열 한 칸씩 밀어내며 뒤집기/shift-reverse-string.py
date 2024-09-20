str1, n = input().split(" ")
n = int(n)

for i in range(n):
    cmd = int(input())
    if cmd == 1:
        str1 = str1[1:] + str1[:1]
    elif cmd == 2:
        str1 = str1[-1:] + str1[:-1]
    elif cmd == 3:
        str1 = str1[::-1]
    print(str1)