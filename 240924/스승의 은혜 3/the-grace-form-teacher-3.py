n, b = map(int, input().split())

max_s = 0
wish_list = []

for _ in range(n):
    wish_list.append(list(map(int, input().split())))
wish_list.sort(key=lambda x: x[0], reverse=True)
# print(wish_list)
for i in range(n):
    paid = 0
    temp_max_s = 0

    wish_list[i][0] /= 2
    for wish in wish_list:
        if paid <= b:
            paid += sum(wish)
            temp_max_s += 1
    # print(max_s, temp_max_s)
    if max_s <= temp_max_s:
        max_s = temp_max_s
    else:
        break        

print(max_s)