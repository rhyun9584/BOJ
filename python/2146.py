from collections import deque

N = int(input())

maps = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(i, j, visited, num):
    queue = deque([(i,j)])
    visited[i][j] = num

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and maps[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = num
                queue.append((nx, ny))

def bridge_bfs(i, j, island):
    queue = deque([(i,j, 0)])

    visited = [[0] * N for _ in range(N)]
    visited[i][j] = 1

    while queue:
        x, y, cnt = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N:
                if island[nx][ny] == 0:
                    if visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        queue.append((nx, ny, cnt+1))
                elif island[nx][ny] != island[i][j]:
                    return cnt

    return int(1e9)

# 섬 구분 구성
island = [[0] * N for _ in range(N)]
count = 1
for i in range(N):
    for j in range(N):
        if maps[i][j] == 1 and island[i][j] == 0:
            bfs(i, j, island, count)
            count += 1

# 다리 구축 탐색
visited = [[0] * N for _ in range(N)]
min_dist = int(1e9)
for i in range(N):
    for j in range(N):
        if island[i][j] > 0:
            min_dist = min(min_dist, bridge_bfs(i, j, island))

print(min_dist)