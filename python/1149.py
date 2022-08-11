N = int(input())

cost = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(2)]
dp[0] = cost[0]
for i in range(1, N):
    b_idx = (i-1)%2
    n_idx = i%2
    dp[n_idx][0] = min(dp[b_idx][1:3]) + cost[i][0]
    dp[n_idx][1] = min(dp[b_idx][0], dp[b_idx][2]) + cost[i][1]
    dp[n_idx][2] = min(dp[b_idx][:2]) + cost[i][2]

print(min(dp[(N-1)%2]))