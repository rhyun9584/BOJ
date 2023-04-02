import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())

degree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1

queue = []
for i in range(1, N+1):
    if degree[i] == 0:
        heapq.heappush(queue, i)

answer = []
while queue:
    v = heapq.heappop(queue)

    answer.append(v)

    for g in graph[v]:
        degree[g] -= 1
        if degree[g] == 0:
            heapq.heappush(queue, g)

print(" ".join(map(str, answer)))