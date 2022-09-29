N, M = map(int, input().split())
mem = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))

total_cost = sum(cost)

result = total_cost
dp = [[0] * (total_cost+1) for _ in range(N+1)]
for i in range(1, N+1):
    m = mem[i]
    c = cost[i]
    for j in range(total_cost+1):
        dp[i][j] = dp[i-1][j]

        if c <= j:
            dp[i][j] = max(dp[i][j], dp[i-1][j-c] + m)

        if dp[i][j] >= M:
            result = min(result, j)

print(result)