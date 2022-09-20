T = int(input())

for _ in range(T):
    N, M, W = map(int, input().split())

    edges = []
    for _ in range(M):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
        edges.append((b, a, c))
    for _ in range(W):
        a, b, c = map(int, input().split())
        edges.append((a, b, -c))

    dist = [0] * (N+1)

    cycle = False
    for i in range(N):
        for s, e, c in edges:
            if dist[s] + c < dist[e]:
                if i == N-1:
                    cycle = True
                    break
                dist[e] = dist[s] + c

        if cycle: break

    print("YES" if cycle else "NO")