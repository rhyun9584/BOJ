from collections import deque

M, N, H = map(int, input().split())

start = []
board = []
for k in range(H):
    one_board = []
    for j in range(N):
        one_board.append(list(map(int, input().split())))
        for i in range(M):
            if one_board[j][i] == 1:
                start.append((k, j, i, 0))
    board.append(one_board)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

queue = deque(start)
result = 0
while queue:
    z, y, x, cnt = queue.popleft()

    result = cnt

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and board[nz][ny][nx] == 0:
            board[nz][ny][nx] = 1
            queue.append((nz, ny, nx, cnt+1))

for k in range(H):
    for j in range(N):
        if 0 in board[k][j]:
            result = -1
            break

    if result == -1:
        break

print(result)
