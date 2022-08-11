N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

def search(start):
    dp = [[0] * 3 for _ in range(N)]
    for i in range(3):
        dp[0][i] = cost[0][i] if start == i else int(1e9)
    for i in range(1, N):
        dp[i][0] = min(dp[i-1][1:]) + cost[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
        dp[i][2] = min(dp[i-1][:2]) + cost[i][2]

    dp[N-1][start] = int(1e9)

    return dp[N-1]

result = []
for i in range(3):
    result += search(i)
print(min(result))