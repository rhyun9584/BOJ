from collections import deque

M, N = map(int, input().split())

tomato = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start, days):
    queue = deque(start)

    while queue:
        nx, ny = queue.popleft()
        for i in range(4):
            now_x = nx+dx[i]
            now_y = ny+dy[i]

            if 0 <= now_x < N and 0 <= now_y < M and tomato[now_x][now_y] == 0:
                day = days[nx][ny] + 1
                if days[now_x][now_y] == 0 or day < days[now_x][now_y]:
                    queue.append((now_x, now_y))
                    days[now_x][now_y] = days[nx][ny] + 1

start = []
days = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            start.append((i, j))    

bfs(start, days)

# -1과 1 자리에만 0일이 들어간 경우 -> 전부 익음
tomato_count = sum([row.count(1) for row in tomato]) + sum([row.count(-1) for row in tomato])
days_count = sum([row.count(0) for row in days])
if tomato_count != days_count:
    print(-1)
else:
    print(max(map(max, days)))