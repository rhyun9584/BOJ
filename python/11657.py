from collections import deque

N, M = map(int, input().split())

edges = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))

dist = [int(1e9)] * (N+1)
is_inQ = [0] * (N+1)
cnt = [0] * (N+1)

queue = deque()
queue.append(1)
dist[1] = 0
is_inQ[1] = 1

cycle = False
while queue:
    v = queue.popleft()
    is_inQ[v] = 0
    cnt[v] += 1

    if cnt[v] == N:
        cycle = True
        break

    for e, c in edges[v]:
        if dist[v] + c < dist[e]:
            dist[e] = dist[v] + c
            if is_inQ[e] == 0:
                queue.append(e)
                is_inQ[e] = 1
    
if cycle:
    print(-1)
else:
    for i in range(2, N+1):
        print(dist[i] if dist[i] < int(1e9) else -1)