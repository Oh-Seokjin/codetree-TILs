text = input()
cmd = input()

for elem in cmd:
    if elem == "L":
        text = text[1:] + text[0]
    else:
        text = text[-1] + text[:-1]

print(text)