full_text = input()
partial_text = input()

cnt = 0

for i in range(0, len(full_text)):
    if full_text[i:i+2] == partial_text:
        cnt +=1

print(cnt)