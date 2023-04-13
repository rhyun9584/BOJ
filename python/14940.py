import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

sx, sy = 0, 0
board = []
for i in range(N):
    board.append(list(map(int, input().split())))

    if 2 in board[-1]:
        sx = i
        sy = board[-1].index(2)

queue = deque()
queue.append((sx, sy, 0))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[-1] * M for _ in range(N)]
visited[sx][sy] = 0
while queue:
    x, y, cnt = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 1 and visited[nx][ny] == -1:
            visited[nx][ny] = cnt+1
            queue.append((nx, ny, cnt+1))

for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            visited[i][j] = 0

for i in range(N):
    print(" ".join(map(str, visited[i])))