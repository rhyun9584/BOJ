import sys
input = sys.stdin.readline

N, T = map(int, input().split())

list = []
for _ in range(N):
    K, S = map(int, input().split())
    list.append((K, S))

dp = [[0]*(T+1) for _ in range(N+1)]

for i in range(1, N+1):
    k, s = list[i-1]

    for j in range(1, T+1):
        if j < k:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-k] + s)

print(dp[N][T])