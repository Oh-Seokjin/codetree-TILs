def palindrome(text):
    if len(text) == 2:
        return text[:len(text)//2] == text[len(text)//2:]
    else:
        return text[:len(text)//2] == text[len(text)//2+1:]
    # print(text[:len(text)//2], text[len(text)//2+1:])    
    # return text[:len(text)//2] == text[len(text)//2+1:]

x, y = map(int, input().split())

cnt = 0

for num in range(x, y+1):
    if palindrome(str(num)):
        cnt+=1

print(cnt)