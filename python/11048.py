N, M = map(int, input().split())

maze = [list(map(int, input().split())) for _ in range(N)]

d = [(-1, 0), (0, -1), (-1, -1)]

dp = [[0] * M for _ in range(N)]
dp[0][0] = maze[0][0]
for i in range(N):
    for j in range(M):
        for k in range(3):
            x = i + d[k][0]
            y = j + d[k][1]
            if 0 <= x < N and 0 <= y < M:
                dp[i][j] = max(dp[i][j], dp[x][y]+maze[i][j])

print(dp[N-1][M-1])