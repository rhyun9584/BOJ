import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy, visited):
    visited[sx][sy] = 1

    queue = deque([(sx, sy)])

    cnt = 0
    while queue:
        x, y = queue.popleft()
        cnt += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))

    return cnt

visited = [[0] * M for _ in range(N)]
cnt, result = 0, 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            result = max(result, bfs(i, j, visited))

print(cnt)
print(result)