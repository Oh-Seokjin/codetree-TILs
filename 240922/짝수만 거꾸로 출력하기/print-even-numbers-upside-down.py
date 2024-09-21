n = int(input())

num_list = list(map(int, input().split()))
num_list.reverse()
for elem in num_list:
    if elem %2 == 0:
        print(elem, end=" ")