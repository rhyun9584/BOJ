import sys

N, K = map(int, input().split())
coins = list(map(int, sys.stdin.readlines()))

dp = [10001] * (K+1)
dp[0] = 0
for i in range(1, K+1):
    for c in coins:
        if c <= i:
            dp[i] = min(dp[i], dp[i-c]+1)

print(dp[K] if dp[K] < 10001 else -1)
