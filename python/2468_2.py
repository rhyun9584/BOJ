from collections import deque

N = int(input())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(sx, sy, visited, h):
    visited[sx][sy] = 1
    
    queue = deque([(sx, sy)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] >= h and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))

max_height = max(map(max, board))
min_height = min(map(min, board))

result = 1
for h in range(min_height+1, max_height+1):
    count = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] >= h and visited[i][j] == 0:
                count += 1
                bfs(i, j, visited, h)

    result = max(result, count)

print(result)