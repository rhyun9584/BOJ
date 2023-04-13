from collections import deque

# 입력값 처리
R, C = map(int, input().split())

board = []
sx, sy = 0, 0
ex, ey = 0, 0
water = []
for i in range(R):
    board.append(list(input()))
    
    if 'S' in board[i]:
        sx = i
        sy = board[i].index("S")

    if 'D' in board[i]:
        ex = i
        ey = board[i].index("D")

    if '*' in board[i]:
        for j in range(C):
            if board[i][j] == '*':
                water.append((i, j, 0, 0))


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

queue = deque(water)
queue.append((sx, sy, 0, 1))

visited = [[0] * C for _ in range(R)]
visited[sx][sy] = 1

result = -1
while queue:
    x, y, cnt, p = queue.popleft()

    if p == 1:
        if board[x][y] == 'D':
            result = cnt
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and board[nx][ny] in '.D' and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny, cnt+1, 1))

    elif p == 0:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and board[nx][ny] == '.':
                board[nx][ny] = '*'
                queue.append((nx, ny, cnt+1, 0))

if result > -1:
    print(result)
else:
    print("KAKTUS")