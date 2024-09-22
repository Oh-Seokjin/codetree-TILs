text1 = input()
text2 = input()

int1 = ""
int2 = ""

for tok in text1:
    try:
        int1 += str(int(tok))
    except:
        continue

for tok in text2:
    try:
        int2 += str(int(tok))
    except:
        continue

print(int(int1) + int(int2))