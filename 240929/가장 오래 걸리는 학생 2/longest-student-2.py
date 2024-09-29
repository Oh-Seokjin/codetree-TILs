n, m = map(int, input().split())
graph = [[0]*n for _ in range(n)]
visited = [0]*n
edges = [tuple(map(int, input().split())) for _ in range(m)]
for edge in edges:
    x, y, z = edge[1], edge[0], edge[2]
    graph[x-1][y-1] = z
INF = 1e11
dist = [INF]*n
#####

def dijkstra(s):
    global visited
    global dist

    dist[s] = 0

    # 모든 노드를 탐색하는데,
    for i in range(n):
        # 주변 노드 중 가장 가까운 노드부터 탐색 
        min_index = -1
        for j in range(n):
            if visited[j]:
                continue
            if min_index == -1 or dist[min_index] > dist[j]:
                min_index = j
        visited[min_index] = 1

        for j in range(n):
            # 연결되어 있지 않으면 continue
            if not graph[min_index][j]:
                continue
            # 연결되어있다면, 현재 거리 vs. 해당 노드 거친 후의 거리 중 작은 값을 최소 거리로 업데이트
            dist[j] = min(dist[j], dist[min_index]+graph[min_index][j])
            

dijkstra(n-1)

print(max(dist))