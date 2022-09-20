N = int(input())
M = int(input())

dist = [[int(1e9)] * i + [0] + [int(1e9)] * (N-i) for i in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    if c < dist[a][b]:
        dist[a][b] = c

for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            dist[j][k] = min(dist[j][k], dist[j][i]+dist[i][k])

for i in range(1, N+1):
    if int(1e9) in dist[i]:
        for j in range(1, N+1):
            if dist[i][j] == int(1e9): dist[i][j] = 0

for i in range(1, N+1):
    print(" ".join(map(str, dist[i][1:])))
