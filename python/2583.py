from collections import deque

M, N, K = map(int, input().split())

# 입력받은 직사각형 정보로 board 채우기
board = [[0] * N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            board[j][i] = 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(sx, sy, visited):
    queue = deque([(sx, sy)])
    visited[sy][sx] = 1

    count = 1
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and board[ny][nx] == 0 and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                count += 1
                queue.append((nx, ny))

    return count

# bfs 탐색으로 영역의 개수와 넓이 계산
count = 0
area = []
visited = [[0] * N for _ in range(M)]
for i in range(M):
    for j in range(N):
        if board[i][j] == 0 and visited[i][j] == 0:
            count += 1
            area.append(bfs(j, i, visited))

print(count)
area.sort()
print(" ".join(map(str, area)))