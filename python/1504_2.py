import sys
import heapq

input = sys.stdin.readline

N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

start = [1, v1, v2]
dist = [[int(1e9)] * (N+1) for _ in range(3)]
for i in range(3):
    queue = []
    heapq.heappush(queue, (0, start[i]))

    while queue:
        cost, v = heapq.heappop(queue)

        if dist[i][v] <= cost:
            continue

        dist[i][v] = cost

        for g, c in graph[v]:
            if cost + c < dist[i][g]:
                heapq.heappush(queue, (cost+c, g))

result = min(dist[0][v1] + dist[1][v2] + dist[2][N], dist[0][v2] + dist[2][v1] + dist[1][N])

if result < int(1e9):
    print(result)
else:
    print(-1)
    