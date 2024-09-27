n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
#####

def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<n


def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] == 1:
        return False
    return True


def dfs(x, y):
    global curr_block_size
    puyo_num = board[x][y]
    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
    
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x+dx, y+dy
    
        if can_go(new_x, new_y) and not visited[new_x][new_y] and board[new_x][new_y] == puyo_num:
            visited[new_x][new_y] = 1
            curr_block_size += 1
            dfs(new_x, new_y)
            
max_block_size = 1
num_blocks = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            curr_block_size = 0
            dfs(i, j)
            if 4 <= curr_block_size :
                num_blocks += 1
            max_block_size = max(max_block_size, curr_block_size)
            
# print(visited)
print(num_blocks, max_block_size)