n = int(input())

for i in range(1, n+1):
    star = ("* "*i).rstrip()
    space = " "*(n-i)
    print(space+star)

for i in range(n-1, 0, -1):
    star = ("* "*i).rstrip()
    space = " "*(n-i)
    print(space+star)