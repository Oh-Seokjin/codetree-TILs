n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
#####

# for row in board:
#     print(row)
# print()
# for row in visited:
#     print(row)

order = 1

board[0][0] = order
order += 1
visited[0][0] = 1



def in_range(x, y):
    return 0<=x and x<m and 0<=y and y<n


def can_go(x, y):
    if not in_range(x, y):
        return False
    
    if visited[x][y]:
        return False
    
    if board[x][y] == 0:
        return False

    return True


def dfs(x, y):
    global order
    dxs, dys = [1, 0], [0, 1]

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x+dx, y+dy

        if can_go(new_x, new_y):
            board[new_x][new_y] = order
            order += 1
            visited[new_x][new_y] = 1
            dfs(new_x, new_y)

dfs(0, 0)

# for row in visited:
#     print(row)

print(visited[n-1][m-1])