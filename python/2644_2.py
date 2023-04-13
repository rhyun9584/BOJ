from collections import deque

N = int(input())
A, B = map(int, input().split())

M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

queue = deque([A])
visited = [-1] * (N+1)
visited[A] = 0

while queue:
    n = queue.popleft()

    if n == B:
        break

    for g in graph[n]:
        if visited[g] == -1:
            visited[g] = visited[n] + 1
            queue.append(g)

print(visited[B])