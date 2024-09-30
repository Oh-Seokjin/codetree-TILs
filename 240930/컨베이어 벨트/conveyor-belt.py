n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))
###
t = t % (2*n)

for _ in range(t):
    temp = u[n-1]

    # 위 배열 뒤로 한칸씩 밀기
    for i in range(n-1, 0, -1):
        u[i] = u[i-1]
    u[0] = d[n-1]

    # 아래 배열 뒤로 한칸씩 밀기
    for i in range(n-1, 0, -1):
        d[i] = d[i-1]
    d[0] = temp

for elem in u:
    print(elem, end=" ")
print()

for elem in d:
    print(elem, end=" ")

# 아래처럼 풀거나, flatten해서 풀 수 있지만, 아무래도 2차원 행렬 조작 공부 목적에는 부합하지 않는 것 같아 해설 보고 다시 작성
# 위 방식이 시간도 더 빠름!

# n, t = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(2)]
# ###
# t = t % (2*n)

# for _ in range(t):
#     arr[0].insert(0, arr[1].pop())
#     arr[1].insert(0, arr[0].pop())

# for row in arr:
#     for elem in row:
#         print(elem, end=" ")
#     print()