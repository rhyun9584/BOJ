from collections import deque

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
max_height = max(map(max, board))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def bfs(i, j, visited):
    queue = deque([(i, j)])
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] > 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))

part = 1
for h in range(1, max_height):
    for i in range(N):
        for j in range(N):
            if 0 < board[i][j] <= h:
                board[i][j] = -1

    cnt = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0 and visited[i][j] == 0:
                cnt += 1
                bfs(i, j, visited)

    part = max(part, cnt)

print(part)
