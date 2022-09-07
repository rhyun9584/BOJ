import sys
from collections import deque

N, M = map(int, input().split())

ocean = []
iceberg = []
for i in range(N):
    arr = list(map(int, input().split()))
    ocean.append(arr)

    for j in range(M):
        if arr[j] > 0:
            iceberg.append((i,j))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(init_x, init_y, arr, visited):
    queue = deque([(init_x, init_y)])
    visited[init_x][init_y] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] > 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))

def is_divide(arr):
    cnt = 0
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0 and visited[i][j] == 0:
                if cnt > 0:
                    return True

                bfs(i, j, arr, visited)
                cnt += 1

    if cnt == 0: return True
    return False

result = 0
while is_divide(ocean) == False:
    result += 1

    queue = deque(iceberg)
    iceberg = []

    decrease = [[0] * M for _ in range(N)]
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and ocean[nx][ny] == 0:
                decrease[x][y] += 1

    for i in range(N):
        for j in range(M):
            ocean[i][j] = max(0, ocean[i][j] - decrease[i][j])
            if ocean[i][j] > 0: 
                iceberg.append((i, j))

for i in range(N):
    for j in range(M):
        if ocean[i][j] > 0:
            print(result)
            sys.exit()

print(0)