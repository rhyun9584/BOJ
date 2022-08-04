import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

result = []

queue = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i)
        result.append(i)

while queue:
    n = queue.popleft()
    for g in graph[n]:
        indegree[g] -= 1
        if indegree[g] == 0:
            queue.append(g)
            result.append(g)

print(' '.join(map(str, result)))