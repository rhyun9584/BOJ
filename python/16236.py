import heapq

N = int(input()) 

sx, sy = 0, 0
board = []
# 입력을 받으면서, 아기 상어의 위치 파악
for i in range(N):
    board.append(list(map(int, input().split())))
    if 9 in board[i]:
        sx = i
        sy = board[i].index(9)

# 아기 상어 위치의 값을 0으로 바꾸어 이동 가능하도록 변경
board[sx][sy] = 0

# 초기 사이즈, 먹은 횟수, 시간 초기화
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
        # heap queue를 사용하여
        # 이동하는데 걸리는 시간, 상하좌표, 좌우좌표 순서로 정렬하여 탐색 진행 
        t, x, y = heapq.heappop(queue)

        # 사이즈보다 작은, 먹을 수 있는 물고기를 발견
        if 0 < board[x][y] < size:
            count += 1
            board[x][y] = 0
            if count == size:
                # 지금 사이즈만큼 물고기를 먹었다면, 사이즈를 증가시키고 횟수 초기화
                size += 1
                count = 0

            # 물고기를 먹은 즉시 탐색 종료
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
    # 물고기를 먹은 시점에서 bfs를 종료하여,
    # 그 순간의 좌표와 시간을 기록하고 다시 bfs 반복
    nx, ny, t = bfs(nx, ny)

    # 만약 먹을 수 있는 물고기가 없다면 종료
    if t == 0:
        break
    
    time += t

print(time)