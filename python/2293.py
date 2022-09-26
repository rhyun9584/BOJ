import sys

N, K = map(int, input().split())
coins = list(map(int, sys.stdin.readlines()))
coins.sort()

dp = [[1] + [0] * K for _ in range(2)]
for i in range(1, N+1):
    c = coins[i-1]
    now = i % 2
    before = abs(now-1)
    for j in range(1, K+1):
        dp[now][j] = dp[before][j]
        if c <= j:
            dp[now][j] += dp[now][j-c]

print(dp[N%2][K])
