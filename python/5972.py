import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dist = [int(1e9)] * (N+1)

queue = []
heapq.heappush(queue, (0, 1))

while queue:
    cost, v = heapq.heappop(queue)

    if dist[v] <= cost:
        continue

    dist[v] = cost

    for g, c in graph[v]:
        if cost + c < dist[g]:
            heapq.heappush(queue, (cost+c, g))

print(dist[N])