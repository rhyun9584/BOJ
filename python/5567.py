from collections import deque

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([(1, 0)])
count = 0

visited = [0] * (N+1)
visited[1] = 1
while queue:
    v, cnt = queue.popleft()

    for g in graph[v]:
        if visited[g] == 0:
            count += 1
            visited[g] = 1
            if cnt == 0: queue.append((g, cnt+1))

print(count)