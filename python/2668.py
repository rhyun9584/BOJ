import sys

def dfs(i, graph, visited, cycle):
    visited[i] = 1

    if i in cycle:
        return cycle[cycle.index(i):]

    return dfs(graph[i], graph, visited, cycle+[i])

N = int(input())
number = [0] + list(map(int, sys.stdin.readlines()))

cycle = set()
visited = [0] * (N+1)
for i in range(1, N+1):
    if visited[i] == 0:
        cycle.update(dfs(i, number, visited, []))
        
print(len(cycle))
print("\n".join(map(str, sorted(cycle))))