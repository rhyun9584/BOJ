import sys

N = int(input())
child = [0] + list(map(int, sys.stdin.readlines()))

dp = [0] * (N+1)
for i in range(1, N+1):
    for j in range(i):
        if child[i] > child[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(N-max(dp))