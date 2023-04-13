import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())

bus = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, c = map(int, input().split())
    bus[s].append((e, c))

start, end = map(int, input().split())

dist = [int(1e9)] * (N+1)

queue = []
heapq.heappush(queue, (0, start))
while queue:
    cost, d = heapq.heappop(queue)

    if dist[d] <= cost:
        continue

    dist[d] = cost

    for g, c in bus[d]:
        if cost + c < dist[g]:
            heapq.heappush(queue, (cost+c, g))

print(dist[end])
