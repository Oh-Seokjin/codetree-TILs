min_len = 0
max_len = 0

str1 = input()
min_len, max_len = len(str1), len(str1)

for _ in range(2):
    str1 = input()
    if len(str1) > max_len:
        max_len = len(str1)
    if len(str1) < min_len:
        min_len = len(str1)

print(max_len-min_len)