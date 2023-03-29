import sys
input = sys.stdin.readline

N = int(input())

bamboo = []
for i in range(N):
    bamboo.append(list(map(int, input().split())))

dp = [[0] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y):
    if dp[x][y] > 0:
        return dp[x][y]
    
    dp[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and bamboo[x][y] < bamboo[nx][ny]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny)+1)

    return dp[x][y]

result = 0
for i in range(N):
    for j in range(N):
        result = max(result, dfs(i, j))

print(result)