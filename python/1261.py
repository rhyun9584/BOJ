import heapq

M, N = map(int, input().split())
maze = [input() for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

queue = []
heapq.heappush(queue, (0, 0, 0))
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1
while queue:
    cnt, x, y = heapq.heappop(queue)

    if x == N-1 and y == M-1:
        print(cnt)
        break

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            heapq.heappush(queue, (cnt+int(maze[nx][ny]), nx, ny))
