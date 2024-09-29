n, m = map(int, input().split())
graph = [[0]*n for _ in range(n)]
visited = [0]*n
INF = 1e11
dist = [INF] * n
edges = [tuple(map(int, input().split())) for _ in range(m)]
for edge in edges:
    x, y, z = edge[0]-1, edge[1]-1, edge[2]
    graph[x][y] = z
#####

def dijkstra(s):
    global visited
    global dist

    dist[s] = 0
    for i in range(n):
        min_index = -1
        for j in range(n):
            if visited[j]:
                continue
            if min_index == -1 or dist[min_index] > dist[j]: # 처음 or 작은것 탐색
                min_index = j
        visited[min_index] = 1
    
        for j in range(n):
            if graph[min_index][j] == 0:
                continue
            dist[j] = min(dist[j], dist[min_index] + graph[min_index][j]) # 현재 저장된 최단 거리 vs 해당 노드를 거친 후의 거리 비교 후 최소값 찾기

dijkstra(0)

for i in range(len(dist)):
    if dist[i] == 1e11:
        dist[i] = -1
for i in range(1, n):
    print(dist[i])