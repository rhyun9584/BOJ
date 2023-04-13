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
heapq.heappush(queue, (0, start, str(start)))

while queue:
    cost, v, path = heapq.heappop(queue)

    if dist[v] <= cost:
        continue

    dist[v] = cost

    if v == end:
        print(dist[v])
        print(len(path.split()))
        print(path)
        break

    for g, c in bus[v]:
        if cost + c < dist[g]:
            heapq.heappush(queue, (cost+c, g, path+" "+str(g)))
