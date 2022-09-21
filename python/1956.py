V, E = map(int, input().split())

dist = [[int(1e9)]*i + [0] + [int(1e9)]*(V-i) for i in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    dist[a][b] = c

for i in range(1, V+1):
    for j in range(1, V+1):
        for k in range(1, V+1):
            dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])

result = int(1e9)
for i in range(1, V+1):
    for j in range(1, V+1):
        if i != j and dist[i][j] < int(1e9) and dist[j][i] < int(1e9):
            result = min(result, dist[i][j]+dist[j][i])

print(result if result < int(1e9) else -1)
