N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]

dp = [[0] * (M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        if board[i-1][j-1] == 1:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1


print(max(map(max, dp))**2)