str1 = input()
str2 = input()

try:
    print(str1.index(str2))
except:
    print(-1)