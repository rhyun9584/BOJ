import heapq


N, E = map(int, input().split())

def dijkstra(start, edges):
    distance = [int(1e9)] * (N+1)
    
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        dist, v = heapq.heappop(queue)
        
        if dist >= distance[v]:
            continue

        distance[v] = dist

        for n, c in edges[v]:
            if dist+c < distance[n]:
                heapq.heappush(queue, (dist+c, n))

    return distance

edges = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    edges[a].append((b,c))
    edges[b].append((a,c))

v1, v2 = map(int, input().split())

distance = dict()
distance[1] = dijkstra(1, edges)
distance[v1] = dijkstra(v1, edges)
distance[v2] = dijkstra(v2, edges)

result = int(1e9)

result = min(result, distance[1][v1]+distance[v1][v2]+distance[v2][N])
result = min(result, distance[1][v2]+distance[v2][v1]+distance[v1][N])

if result < int(1e9):
    print(result)
else:
    print(-1)