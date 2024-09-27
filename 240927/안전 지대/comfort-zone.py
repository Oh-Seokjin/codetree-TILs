import sys
sys.setrecursionlimit(10 ** 30)

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
top_h = max(max(board))
#####


def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<m


def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y]:
        return False
    return True




def dfs(x, y):
    global num_safe_area
    global visited

    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]
    
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x+dx, y+dy
        if can_go(new_x, new_y):
            visited[new_x][new_y] = 1
            # for row in visited:
            #     print(row)
            # print()
            dfs(new_x, new_y)


max_k = 1
max_safe_area = 0

for k in range(1, top_h+1):
    num_safe_area = 0
    
    visited = [[0]*m for _  in range(n)]
    # if rain == k
    for i in range(n):
        for j in range(m):
            if board[i][j] <= k:
                visited[i][j] = 1
    
    # for row in visited:
    #     print(row)
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                dfs(i, j)
                num_safe_area += 1
    # print(num_safe_area)
    if max_safe_area < num_safe_area:
        max_safe_area = num_safe_area
        max_k = k
    # print()
print(max_k, max_safe_area)