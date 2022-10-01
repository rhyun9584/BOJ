import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def bfs(i, j, board, visited):
    queue = deque([(i, j)])
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= 2000 and 0 <= ny <= 2000 and board[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))

N = int(input())
start = []
board = [[0] * 2001 for _ in range(2001)]
for _ in range(N):
    x1, y1, x2, y2 = map(lambda x: (int(x)+500)*2, input().split())
    start.append((x1, y1))
    for i in range(x1, x2+1):
        if i in (x1, x2):
            for j in range(y1, y2+1):
                board[i][j] = 1
        else:
            board[i][y1] = 1
            board[i][y2] = 1
    
answer = 0
visited = [[0] * 2001 for _ in range(2001)]
for sx, sy in start:
    if visited[sx][sy] == 0:
        bfs(sx, sy, board, visited)
        answer += 1

if board[1000][1000] == 1:
    answer -= 1

print(answer)
