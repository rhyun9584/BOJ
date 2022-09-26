import sys

N, K = map(int, input().split())
coins = list(map(int, sys.stdin.readlines()))

dp = [0] * (K+1)
dp[0] = 1
for c in coins:
    for i in range(c, K+1):
        dp[i] += dp[i-c]

print(dp[K])
