text1 = input()
text2 = input()

n = 0
leng = len(text1)
flag = -1

for i in range(leng):
    text1 = text1[-1] + text1[:-1]
    n += 1
    
    if text1 == text2:
        flag = 1
        break

if flag == 1:
    print(n)
else:
    print(-1)