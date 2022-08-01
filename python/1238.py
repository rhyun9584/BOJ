import sys
import heapq

input = sys.stdin.readline

N, M, X = map(int, input().split())

# 그래프 구축
graph = [[] for _ in range(N+1)]
graph_rev = [[] for _ in range(N+1)]
for _ in range(M):
    # s -> e 소요시간 t
    s, e, t = map(int, input().split())
    graph[s].append((e,t))
    # 그래프를 역방향으로!
    graph_rev[e].append((s,t))

def dijkstra(start, graph_):
    queue = []
    dists = [int(1e9)] * (N+1)
    dists[start] = 0
    heapq.heappush(queue, (0, start))
    while queue:
        dist, now = heapq.heappop(queue)

        if dist > dists[now]:
            continue

        dists[now] = dist
        
        for g, t in graph_[now]:
            if dist+t < dists[g]:
                heapq.heappush(queue, (dist+t, g))

    return dists[1:]

dist1 = dijkstra(X, graph)
dist2 = dijkstra(X, graph_rev)

print(max([a+b for a, b in zip(dist1, dist2)]))