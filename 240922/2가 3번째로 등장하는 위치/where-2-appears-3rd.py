n = int(input())

num_list = list(map(int, input().split()))
cnt = 0

for i in range(len(num_list)):
    if num_list[i] == 2:
        cnt +=1
    
    if cnt == 3:
        print(i+1)
        break