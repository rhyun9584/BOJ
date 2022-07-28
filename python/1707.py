from collections import deque

K = int(input())

def bfs(start, checked, graph):
    q = deque([start])
    checked[start] = 1

    while q:
        v = q.popleft()
        for i in graph[v]:
            # 인접한 노드가 같은 형태로 체크되면 NO
            if checked[i] == checked[v]:
                return False

            if checked[i] == 0:
                q.append(i)
                checked[i] = checked[v] * (-1)

    return True

for _ in range(K):
    V, E = map(int, input().split())
    
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    checked = [0] * (V+1)

    result = True
    for i in range(1, V+1):
        if checked[i] == 0:
            if bfs(i, checked, graph) == False:
                result = False
                break 
    
    if result: print('YES')
    else: print('NO')