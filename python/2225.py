N, K = [int(x) for x in input().split()]
ways = [[1 for _ in range(K+1)] for _ in range(N+1)]

for n in range(1, N+1):
    for k in range(2, K+1):
        if n == 1: ways[n][k] = k
        elif k == 2: ways[n][k] = n+1
        else:
            for m in range(1, n+1):
                ways[n][k] += ways[m][k-1]

print(ways[N][K]%1000000000)