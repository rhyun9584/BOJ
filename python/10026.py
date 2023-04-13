from collections import deque

N = int(input())

board = []
for _ in range(N):
    board.append(list(input()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(sx, sy, point):
    queue = deque([(sx, sy)])
    visited[sx][sy] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] in point and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))

result = [0, 0]

visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            result[0] += 1
            bfs(i, j, board[i][j])

visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            result[1] += 1

            point = ""
            if board[i][j] in ("R", "G"): point = "RG"
            else: point = "B"
            bfs(i, j, point)

print(" ".join(map(str, result)))