import heapq

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dist = [int(1e9)] * (V+1)

queue = []
heapq.heappush(queue, (0, K))

while queue:
    cost, v = heapq.heappop(queue)

    if dist[v] <= cost:
        continue

    dist[v] = cost
    
    for g, c in graph[v]:
        if cost + c < dist[g]:
            heapq.heappush(queue, (cost+c, g))

for i in range(1, V+1):
    if dist[i] < int(1e9):
        print(dist[i])
    else:
        print("INF")