n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
starting = [list(map(int, input().split())) for _ in range(k)]
for elem in starting:
    elem[0] -=1
    elem[1] -=1
visited = [[0]*n for _ in range(n)]
#####

def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y]:
        return False
    if board[x][y]:
        return False
    return True


def bfs(x, y):
    global q
    global cnt

    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

    while q:
        cur_node = q.pop(0)
        x = cur_node[0]
        y = cur_node[1]

        for dx, dy in zip(dxs, dys):
            new_x, new_y = x+dx, y+dy
            if can_go(new_x, new_y):
                q.append([new_x, new_y])
                visited[new_x][new_y] = 1
                cnt += 1
    
cnt = 0
q = []
for elem in starting:
    x, y = elem[0], elem[1]

    if not visited[x][y]:
        q.append(elem)
        cnt += 1
        visited[x][y] = 1
        bfs(x, y)
    
print(cnt)