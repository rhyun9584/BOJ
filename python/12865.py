N, K = map(int, input().split())

things = []
for _ in range(N):
    w, v = map(int, input().split())
    things.append((w, v))

dp = [[0] * (K+1) for _ in range(N+1)]
for i in range(1, N+1):
    w, v = things[i-1]
    for j in range(1, K+1):
        if w <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])