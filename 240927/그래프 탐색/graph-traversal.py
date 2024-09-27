n, m = map(int, input().split())
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s-1][e-1], graph[e-1][s-1] = 1, 1

#####

cnt = 0
visited[1] = 1

def dfs(v):
    global cnt    
    for curr_v in range(n):
        if graph[v][curr_v] and not visited[curr_v]:
            visited[v] = 1
            cnt += 1
            dfs(curr_v)
            

dfs(1)

print(cnt)