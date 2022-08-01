import sys
import heapq

i = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break

    maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    # (도둑루피 크기, x, y)
    queue = []
    heapq.heappush(queue, (maps[0][0], 0, 0))
    while queue:
        k, x, y = heapq.heappop(queue)

        if x == N-1 and y == N-1:
            print(f"Problem {i}: {k}")
            i += 1
            break

        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                heapq.heappush(queue, (k + maps[nx][ny], nx, ny))
                visited[nx][ny] = 1
