from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start, visited):
    q = deque([start])
    visited[start] = 1
    
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1

count = 0
visited = [0] * (N+1)
for i in range(1, N+1):
    if visited[i] == 0:
        bfs(i, visited)
        count += 1

print(count)