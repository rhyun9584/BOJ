import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

edges = [[] for _ in range(V+1)]
for _ in range(E):
    s, e, c = map(int, input().split())
    edges[s].append((e, c))

queue = []
heapq.heappush(queue, (0, K))

dist = [int(1e9)] * (V+1)
while queue:
    cost, n = heapq.heappop(queue)

    if cost >= dist[n]:
        continue

    dist[n] = cost
    for g, c in edges[n]:
        if cost+c < dist[g]:
            heapq.heappush(queue, (cost+c, g))

for i in range(1, V+1):
    print(dist[i] if dist[i] < int(1e9) else "INF")