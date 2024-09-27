n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if board[i][j] == 0:
            visited[i][j] = 1
#####
town_num = 2

def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if board[x][y] == 0:
        return False
    if visited[x][y] == 1:
        return False
    return True

def dfs(x, y):
    global town_num
    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x+dx, y+dy

        if can_go(new_x, new_y):
            board[new_x][new_y] = town_num
            visited[new_x][new_y] = 1
            dfs(new_x, new_y)

board[0][0] = town_num

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            board[i][j] = town_num
            dfs(i, j)
            town_num += 1

answer = []
for row in board:
    answer.extend(row)
print(max(answer)-1)

residents = []
for i in range(2, max(answer)+1):
    residents.append(answer.count(i))
residents.sort()
for elem in residents:
    print(elem)