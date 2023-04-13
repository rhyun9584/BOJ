import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

indgree = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    indgree[b] += 1
    graph[a].append(b)

queue = deque()
for i in range(1, N+1):
    if indgree[i] == 0:
        queue.append(i)

result = []
while queue:
    v = queue.popleft()

    result.append(v)

    for g in graph[v]:
        indgree[g] -= 1
        if indgree[g] == 0:
            queue.append(g)

print(" ".join(map(str, result)))