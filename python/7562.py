from collections import deque

T = int(input())

direction = [(-1, -2), (-2, -1), (1, -2), (2, -1), (-1, 2), (-2, 1), (1, 2), (2, 1)]
for _ in range(T):
    I = int(input())

    x, y = map(int, input().split())
    gx, gy = map(int, input().split())

    queue = deque()
    queue.append((x, y, 0))
    
    visited = [[0] * I for _ in range(I)]
    visited[x][y] = 1
    while queue:
        nx, ny, cnt = queue.popleft()
        if nx == gx and ny == gy:
            print(cnt)
            break

        for dx, dy in direction:
            i = nx+dx
            j = ny+dy
            if 0 <= i < I and 0 <= j < I and visited[i][j] == 0:
                visited[i][j] = 1
                queue.append((i, j, cnt+1))