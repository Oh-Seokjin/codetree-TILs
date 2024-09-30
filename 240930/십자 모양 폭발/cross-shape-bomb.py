n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r, c = r-1, c-1
###

def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<n

def bomb(r, c):
    global board
    
    size = board[r][c]
    
    for i in range(size):
        if in_range(r, c-i):
            board[r][c-i] = 0
        if in_range(r, c+i):
            board[r][c+i] = 0
        if in_range(r-i, c):
            board[r-i][c] = 0
        if in_range(r+i, c):
            board[r+i][c] = 0

def gravity():
    global board
    for col in range(n):
        temp = []
        for row in range(n):
            if board[row][col] != 0:
                temp.append(board[row][col])
        for _ in range(n-len(temp)):
            temp.insert(0, 0)
        for row in range(n):
            board[row][col] = temp[row]

    
bomb(r, c)
gravity()

for row in board:
    for elem in row:
        print(elem, end=" ")
    print()