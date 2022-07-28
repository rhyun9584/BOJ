from collections import deque

dx = [-1, -1, -1, 1, 1, 1, 0, 0]
dy = [-1, 0, 1, -1, 0, 1, -1, 1]

def bfs(x, y, visited):
    global h, w, land
    visited[x][y] = 1
    queue = deque([(x,y)])
    while queue:
        nx, ny = queue.popleft()

        for i in range(8):
            now_x = nx+dx[i]
            now_y = ny+dy[i]
            if 0 <= now_x < h and 0 <= now_y < w and land[now_x][now_y] == 1 and visited[now_x][now_y] == 0:
                visited[now_x][now_y] = 1
                queue.append((now_x, now_y))


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    land = [list(map(int, input().split())) for _ in range(h)]

    count = 0
    visited = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if land[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j, visited)
                count += 1
    
    print(count)
