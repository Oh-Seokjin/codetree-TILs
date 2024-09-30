n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
###

def sum_33(x, y):
    temp_sum = 0
    for i in range(3):
        temp_sum += sum(board[x+i][y:y+3])
    return temp_sum

answer = 0

for i in range(n-2):
    for j in range(n-2):
        answer = max(answer, sum_33(i, j))

print(answer)