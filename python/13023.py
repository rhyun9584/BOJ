import sys
input = sys.stdin.readline

def dfs(n, graph, friends):
    if len(friends) == 5:
        return True

    for g in graph[n]:
        if g not in friends:
            if dfs(g, graph, friends+[g]):
                return True

N, M = map(int, input().split())

graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = 0
for i in range(N):
    if dfs(i, graph, [i]):
        result = 1
        break

print(result)