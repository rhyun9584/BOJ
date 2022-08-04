import sys
input = sys.stdin.readline

def dfs(n, graph, visited, ans):
    if ans == 5:
        print(1)
        sys.exit()

    for g in graph[n]:
        if visited[g] == 0:
            visited[g] = 1
            dfs(g, graph, visited, ans+1)
            visited[g] = 0

N, M = map(int, input().split())

graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = 0
visited = [0] * (N)
for i in range(N):
    visited[i] = 1
    dfs(i, graph, visited, 1)
    visited[i] = 0

print(0)