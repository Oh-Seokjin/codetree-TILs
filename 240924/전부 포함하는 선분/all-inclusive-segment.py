n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
#####

min_len = float('inf')

for i in range(n):
    board = [0 for _ in range(100)]
    for j in range(n):
        if i == j:
            continue
        s, e = arr[j][0], arr[j][1]
        for k in range(s, e):
            board[k] += 1

    min_len = min(min_len, len("".join(list(map(str, board))).strip("0")))
print(min_len)

# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]

# min_len = float('inf')

# for i in range(n):
#     # i번째 선분을 제외한 나머지 선분들의 최소 시작점과 최대 끝점 찾기
#     min_start = float('inf')
#     max_end = float('-inf')
    
#     for j in range(n):
#         if i == j:
#             continue
#         min_start = min(min_start, arr[j][0])
#         max_end = max(max_end, arr[j][1])
    
#     # 나머지 선분들을 모두 포함하는 선분의 길이
#     min_len = min(min_len, max_end - min_start)

# print(min_len)