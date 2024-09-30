n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
###

def max_22(n, m):
    global answer
    for i in range(n-1):
        for j in range(m-1):
            ul = board[i][j+1] + board[i+1][j] + board[i+1][j+1]
            ur = board[i][j] + board[i+1][j] + board[i+1][j+1]
            ll = board[i][j] + board[i][j+1] + board[i+1][j+1]
            lr = board[i][j] + board[i][j+1] + board[i+1][j]
            answer = max(answer, ul, ur, ll, lr)

def max_13(n, m):
    global answer
    for i in range(n):
        for j in range(m-2):
            answer = max(answer, sum(board[i][j:j+3]))

def max_31(n, m):
    global answer
    for i in range(n-2):
        for j in range(m):
            temp = 0
            for k in range(3):
                temp += board[i+k][j]
            answer = max(answer, temp)

answer = 0
max_22(n, m)
max_13(n, m)
max_31(n, m)

print(answer)