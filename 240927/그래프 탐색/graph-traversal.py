n, m = map(int, input().split())
graph = [[0 for _ in range(n)] for _ in range(n)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s-1][e-1], graph[e-1][s-1] = 1, 1

#####

def dfs(v):
    visited[v] = 1
    for curr_v in range(n):
        if graph[v][curr_v] and not visited[curr_v]:
            global cnt
            cnt += 1
            dfs(curr_v)
            
cnt = 0

dfs(1)

print(cnt)