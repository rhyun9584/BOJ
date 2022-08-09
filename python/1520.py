import sys
sys.setrecursionlimit(500**2)

M, N = map(int, input().split())
height = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))

dp = [[0] * N for _ in range(M)]
dp[M-1][N-1] = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, dp):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and height[nx][ny] < height[x][y]:
            if dp[nx][ny] == 0:
                dp[x][y] += max(0, dfs(nx, ny, dp))
            elif dp[nx][ny] > 0:
                dp[x][y] += dp[nx][ny]

    if dp[x][y] == 0:
        dp[x][y] = -1
    return dp[x][y]

dfs(0, 0, dp)
print(max(dp[0][0], 0))