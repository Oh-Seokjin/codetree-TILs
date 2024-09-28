n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
#####

def in_range(x, y):
    return 0<=x and x<m and 0<=y and y<n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y]:
        return False
    if not board[x][y]:
        return False
    return True

def bfs():
    global q

    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

    while q:
        curr_node = q.pop(0)
        x = curr_node[0]
        y = curr_node[1]

        for dx, dy in zip(dxs, dys):
            new_x, new_y = x+dx, y+dy
            if can_go(new_x, new_y):
                q.append((new_x, new_y))
                visited[new_x][new_y] = 1
                # print(q)


q = []
q.append((0, 0))
visited[0][0] = 1
bfs()
print(visited[n-1][m-1])
# for row in visited:
    # print(row)