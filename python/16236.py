import heapq

N = int(input()) 

sx, sy = 0, 0
board = []
for i in range(N):
    board.append(list(map(int, input().split())))
    if 9 in board[i]:
        sx = i
        sy = board[i].index(9)
board[sx][sy] = 0

size = 2
count = 0
time = 0

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs(i, j):
    global size, count
    queue = []
    heapq.heappush(queue, (0, i, j))

    visited = [[0] * N for _ in range(N)]
    visited[i][j] = 1

    while queue:
        t, x, y = heapq.heappop(queue)

        if 0 < board[x][y] < size:
            count += 1
            board[x][y] = 0
            if count == size:
                size += 1
                count = 0

            return x, y, t
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and (0 <= board[nx][ny] <= size) and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                heapq.heappush(queue, (t+1, nx, ny))

    return 0, 0, 0

nx, ny = sx, sy
while True:
    nx, ny, t = bfs(nx, ny)
    if t == 0:
        break
    
    time += t

print(time)