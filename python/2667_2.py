from collections import deque

N = int(input())

board = []
for _ in range(N):
    board.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(i, j, visited):
    queue = deque([(i, j)])
    visited[i][j] = 1

    count = 1
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 1 and visited[nx][ny] == 0:
                count += 1
                visited[nx][ny] = 1
                queue.append((nx, ny))

    return count

visited = [[0] * N for _ in range(N)]

count = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and visited[i][j] == 0:
            count.append(bfs(i, j, visited))

print(len(count))
count.sort()
for c in count:
    print(c)