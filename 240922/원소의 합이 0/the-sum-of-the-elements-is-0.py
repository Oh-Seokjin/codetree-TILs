n = int(input())

num = [list(map(int, input().split())) for _  in range(4)]
cnt = 0

dict_ab = {}
dict_cd = {}

for i in range(n):
    for j in range(n):
        if num[0][i] + num[1][j] not in dict_ab:
            dict_ab[num[0][i] + num[1][j]] = 1
        else:
            dict_ab[num[0][i] + num[1][j]] += 1

for i in range(n):
    for j in range(n):
        if num[2][i] + num[3][j] not in dict_cd:
            dict_cd[num[2][i] + num[3][j]] = 1
        else:
            dict_cd[num[2][i] + num[3][j]] += 1

for ab in dict_ab.keys():
    for cd in dict_cd.keys():
        if ab + cd == 0:
            cnt += dict_ab[ab] * dict_cd[cd]

print(cnt)