from collections import deque

N, L, R = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(a, b, visited, p):
    queue = deque([(a, b)])
    visited[a][b] = 1

    sum = p[a][b]
    count = 1
    unite = [(a, b)]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and\
                L <= abs(p[nx][ny] - p[x][y]) <= R:
                visited[nx][ny] = 1
                sum += p[nx][ny]
                count += 1
                unite.append((nx, ny))

                queue.append((nx, ny))
    
    if count > 1:
        new_p = sum // count
        for ux, uy in unite:
            p[ux][uy] = new_p

        return True

    return False

c = 0
while True:
    result = False
    visited = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                # result가 False -> True로만 변경 가능
                result = (bfs(i, j, visited, p) | result)

    if result:
        c += 1
    else:
        print(c)
        break