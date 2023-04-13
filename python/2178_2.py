from collections import deque


N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

queue = deque([(0, 0)])
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1

while queue:
    x, y = queue.popleft()
    
    if x == N-1 and y == M-1:
        print(visited[x][y])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 1 and visited[nx][ny] == 0:
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx, ny))
