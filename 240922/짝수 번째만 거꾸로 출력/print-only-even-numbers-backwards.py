text = input()
for i in range(len(text), 0, -1):
    if i%2 == 0:
        print(text[i-1], end="")