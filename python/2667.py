from collections import deque

N = int(input())

map = [input() for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, visited):
    count = 0
    visited[x][y] = 1
    queue = deque([(x, y)])
    while queue:
        nx, ny = queue.popleft()
        count += 1

        for i in range(4):
            new_x = nx+dx[i]
            new_y = ny+dy[i]
            if 0 <= new_x < N and 0 <= new_y < N and map[new_x][new_y] == '1' and visited[new_x][new_y] == 0:
                visited[new_x][new_y] = 1
                queue.append((nx+dx[i], ny+dy[i]))

    return count
        
count = 0
home_count = []
visited = [[0] * (N) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if map[i][j] == '1' and visited[i][j] == 0:
            home_count.append(bfs(i, j, visited))
            count += 1

print(count)
home_count.sort()
for i in range(count):
    print(home_count[i])