from collections import deque


N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

# 3차원 배열, 행/열/벽 부순 경로
dist = [[[0] * 2 for _ in range(M)] for _ in range(N)]
dist[0][0][0] = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

queue = deque()
queue.append((0, 0, 0))
while queue:
    x, y, is_break = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 1 and is_break == 0 and dist[nx][ny][1] == 0:
                dist[nx][ny][1] = dist[x][y][0] + 1
                queue.append((nx, ny, 1))
            elif graph[nx][ny] == 0 and dist[nx][ny][is_break] == 0:
                dist[nx][ny][is_break] = dist[x][y][is_break] + 1
                queue.append((nx, ny, is_break))

if dist[N-1][M-1] == [0,0]:
    print(-1)
else:
    if dist[N-1][M-1][0] == 0:
        print(dist[N-1][M-1][1])
    elif dist[N-1][M-1][1] == 0:
        print(dist[N-1][M-1][0])
    else:
        print(min(dist[N-1][M-1]))