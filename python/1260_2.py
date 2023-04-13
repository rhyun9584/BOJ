from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

def dfs(v, visited):
    print(v, end = ' ')
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i, visited)

def bfs(start, visited):
    queue = deque([start])
    visited[start] = 1

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)

visited = [0] * (N+1)
dfs(V, visited)
print()

visited = [0] * (N+1)
bfs(V, visited)