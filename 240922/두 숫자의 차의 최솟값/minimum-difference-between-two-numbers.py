from itertools import combinations

n = int(input())
num_list = list(map(int, input().split()))
dif_list = []

for a, b in list(combinations(num_list, 2)):
    dif_list.append(abs(a-b))
print(min(dif_list))