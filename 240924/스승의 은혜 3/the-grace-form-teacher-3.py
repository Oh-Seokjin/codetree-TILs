n, b = map(int, input().split())

max_s = 0
wish_list = []

for _ in range(n):
    wish_list.append(list(map(int, input().split())))

for i in range(n):
    wish_list[i][0] /= 2
    sum_wish_list = sorted([sum(elem) for elem in wish_list])
    
    paid = 0
    temp_max_s = 0

    for wish in sum_wish_list:
        if paid+wish <= b:
            paid += wish
            temp_max_s += 1
    max_s = max(max_s, temp_max_s)

print(max_s)