from collections import deque

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([1])
visited = [0] * (N+1)
visited[1] = 1

count = 0
while queue:
    n = queue.popleft()

    for g in graph[n]:
        if visited[g] == 0:
            count += 1
            visited[g] = 1
            queue.append(g)

print(count)