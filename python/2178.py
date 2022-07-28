from collections import deque

N, M = map(int, input().split())
maze = [input() for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, steps):
    steps[x][y] = 1
    queue = deque([(x,y)])

    while queue:
        nx, ny = queue.popleft()
        for i in range(4):
            next_x = nx+dx[i]
            next_y = ny+dy[i]
            if 0 <= next_x < N and 0 <= next_y < M and maze[next_x][next_y] == '1' and steps[next_x][next_y] == 0:
                steps[next_x][next_y] = steps[nx][ny] + 1
                queue.append((next_x, next_y))

steps = [[0] * M for _ in range(N)]
bfs(0, 0, steps)

print(steps[N-1][M-1])