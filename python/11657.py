from collections import deque

N, M = map(int, input().split())

edges = []
for _ in range(M):
    edges.append(tuple(map(int, input().split())))

dist = [int(1e9)] * (N+1)
dist[1] = 0

cycle = False
for i in range(N):
    for s, e, c in edges:
        if dist[s] != int(1e9) and dist[s] + c < dist[e]:
            if i == N-1:
                cycle = True
                break
            dist[e] = dist[s] + c
    
    if cycle: break

if cycle:
    print(-1)
else:
    for i in range(2, N+1):
        print(dist[i] if dist[i] < int(1e9) else -1)