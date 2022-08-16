from collections import deque

N = int(input())
g1, g2 = map(int, input().split())

M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([(g1, 0)])

visited = [0] * (N+1)
visited[g1] = 1
result = -1
while queue:
    v, cnt = queue.popleft()
    if v == g2:
        result = cnt
        break

    for g in graph[v]:
        if visited[g] == 0:
            visited[g] = 1
            queue.append((g, cnt+1))

print(result)