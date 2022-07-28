import sys

sys.setrecursionlimit(10 ** 6)

def dfs(idx, visited):
    global result
    visited[idx] = 1
    cycle.append(idx)

    next = select[idx]
    if visited[next] != 0:
        if next in cycle:
            result += cycle[cycle.index(next):]
        return
    else:
        dfs(next, visited)


T = int(input())
for _ in range(T):
    n = int(input())
    select = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
    visited = [0] * (n+1)
    result = []

    for i in range(1, n+1):
        if visited[i] == 0:
            cycle = []
            dfs(i, visited)

    print(n - len(result))