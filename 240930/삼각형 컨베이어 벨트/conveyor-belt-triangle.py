n, t = map(int, input().split())
first = list(map(int, input().split()))
second = list(map(int, input().split()))
third = list(map(int, input().split()))
###

t = t % (3*n)

for _ in range(t):
    # 뒤에서부터 당겨야지 제대로 당겨짐 index 잘 확인하기 
    # 첫번째 줄 당기기
    first_temp = first[n-1]
    for i in range(n-1, 0, -1):
        first[i] = first[i-1]
    first[0] = third[n-1]

    # 두번째 줄 당기기
    second_temp = second[n-1]
    for i in range(n-1, 0, -1):
        second[i] = second[i-1]
    second[0] = first_temp

    # 세번째 줄 당기기
    for i in range(n-1, 0, -1):
        third[i] = third[i-1]
    third[0] = second_temp

for elem in first:
    print(elem, end = " ")
print()

for elem in second:
    print(elem, end = " ")
print()

for elem in third:
    print(elem, end = " ")