import sys
import heapq
input = sys.stdin.readline

N = int(input())

def dijkstra(start, graph):
    distance = [int(1e9)] * (N+1)
    distance[start] = 0

    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        nd, v = heapq.heappop(queue)

        for g, d in graph[v]:
            dist = nd + d
            if dist < distance[g]:
                distance[g] = dist
                heapq.heappush(queue, (dist, g))

    return distance[1:]

graph = [[] for _ in range(N+1)]
for _ in range(N):
    data = list(map(int, input().split()))
    n = data[0]
    for i in range(1, len(data)-1, 2):
        graph[n].append((data[i], data[i+1]))

distance = dijkstra(1, graph)
result = max(dijkstra(distance.index(max(distance))+1, graph))
print(result)