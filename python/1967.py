import sys, heapq
input = sys.stdin.readline


def dijkstra(start, edges):
    dist = [int(1e9)] * (N+1)
    
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        cost, v = heapq.heappop(queue)
        if cost >= dist[v]:
            continue

        dist[v] = cost

        for e, c in edges[v]:
            if cost + c < dist[e]:
                heapq.heappush(queue, (cost+c, e))

    return dist


if __name__ == "__main__":
    N = int(input())

    edges = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b, c = map(int, input().split())
        edges[a].append((b, c))
        edges[b].append((a, c))

    dist1 = dijkstra(1, edges)

    # n개의 노드, n-1개의 edge를 가진 tree -> 연결그래프
    new_start = dist1.index(max(dist1[1:]))
    dist2 = dijkstra(new_start, edges)

    print(max(dist2[1:]))
