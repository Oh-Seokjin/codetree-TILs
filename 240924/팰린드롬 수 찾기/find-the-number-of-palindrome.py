def is_palindrome(text):
    reversed_text = "".join(reversed(text))
    return text == reversed_text

x, y = map(int, input().split())

cnt = 0

for num in range(x, y+1):
    if is_palindrome(str(num)):
        cnt+=1

print(cnt)