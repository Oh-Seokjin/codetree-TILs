num_list = list(map(int, input().split()))

for i in range(len(num_list)):
    if num_list[i] % 3 == 0:
        print(num_list[i-1])
        break