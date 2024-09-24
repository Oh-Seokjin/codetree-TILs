n, b = map(int, input().split())

max_s = 0
wish_list = []

for _ in range(n):
    wish_list.append(tuple(map(int, input().split())))
wish_list.sort(key=lambda x: x[0])
# print(wish_list)
# print()
for i in range(n):
    temp_wish_list = [list(wish) for wish in wish_list]
    temp_wish_list[i][0] /= 2
    sum_wish_list = sorted([sum(elem) for elem in temp_wish_list])
    # print(sum_wish_list)    
    paid = 0
    temp_max_s = 0

    for wish in sum_wish_list:
        if paid+wish <= b:
            paid += wish
            temp_max_s += 1
    # print(max_s, temp_max_s, paid)
    max_s = max(max_s, temp_max_s)

print(max_s)