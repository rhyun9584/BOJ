N, M, K = map(int, input().split())
board = [list(input()) for _ in range(N)]
word = input()
len_word = len(word)

dp = [[[0] * (len_word+1) for _ in range(M)] for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def dfs(x, y, cnt):
    if cnt == len_word and board[x][y] == word[-1]:
        dp[x][y][-1] = 1
        return 1
    if dp[x][y][cnt] > 0:
        return dp[x][y][cnt]

    for i in range(4):
        for j in range(1, K+1):
            nx = x + dx[i] * j
            ny = y + dy[i] * j
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == word[cnt]:
                if dp[nx][ny][cnt+1] > 0:
                    dp[x][y][cnt] += dp[nx][ny][cnt+1]
                    continue
                if dp[nx][ny][cnt+1] == -1:
                    continue

                dfs_result = dfs(nx, ny, cnt+1)
                if dfs_result > 0:
                    dp[x][y][cnt] += dfs_result

    if dp[x][y][cnt] == 0:
        dp[x][y][cnt] = -1
    return dp[x][y][cnt]

result = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == word[0]:
            dfs(i, j, 1)
            if dp[i][j][1] > 0:
                result += dp[i][j][1]

print(result)