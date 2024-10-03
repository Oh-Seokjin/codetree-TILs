n = int(input())
original_board = [list(map(int, input().split())) for _ in range(n)]
###

def in_range(x, y):
    return 0<=x and x<n-1 and 0<=y and y<n-1

def bomb(board, x, y, size):
    #가로
    for ny in range(y-size, y+size+1):
        if in_range(x, ny):
            board[x][ny] = 0

    #세로
    for nx in range(x-size, x+size+1):
        if in_range(nx, y):
            board[nx][y] = 0
    return board

def gravity(board):

    temp = [[]*n for _ in range(n)]
    trans = list(map(list, zip(*board)))


    for i in range(n):
        for elem in trans[i]:
            if elem != 0:
                temp[i].append(elem)
        for _ in range(n-len(temp[i])):
            temp[i].insert(0, 0)
    
    trans = list(map(list, zip(*temp)))
    return trans

def count_pair(board):
    cnt = 0
    for x in range(n):
        for y in range(n):
            for dx, dy in zip([1, 0], [0, 1]):
                nx, ny = x+dx, y+dy
                if in_range(nx, ny) and board[x][y] and board[x][y] == board[nx][ny]:
                    cnt += 1
    return cnt

max_cnt = 0

for bomb_size in range(n):
    for i in range(n):
        for j in range(n):
            temp = [[original_board[x][y] for y in range(n)] for x in range(n)]
            temp = bomb(temp, i, j, bomb_size)
            temp = gravity(temp)
            if count_pair(temp) == 6:
                for row in temp:
                    print(row)
            max_cnt = max(max_cnt, count_pair(temp))

print(max_cnt)