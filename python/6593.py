import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

while True:
    L, R, C = map(int, input().split())

    if L == R == C == 0:
        break

    board = [[] for _ in range(L)]
    Sx, Sy, Sz = 0, 0, 0
    for i in range(L):
        for j in range(R):
            board[i].append(list(input().rstrip()))
            
            if 'S' in board[i][-1]:
                Sx = j
                Sy = board[i][-1].index('S')
                Sz = i

        input()

    queue = deque()
    queue.append((Sz, Sx, Sy, 0))

    visited = [[[0] * C for _ in range(R)] for _ in range(L)]
    visited[Sz][Sx][Sy] = 1

    result = 0
    while queue:
        z, x, y, cnt = queue.popleft()

        if board[z][x][y] == 'E':
            result = cnt
            break

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < R and 0 <= ny < C and 0 <= nz < L and board[nz][nx][ny] != '#' and visited[nz][nx][ny] == 0:
                visited[nz][nx][ny] = 1
                queue.append((nz, nx, ny, cnt+1))

    if result > 0:
        print(f"Escaped in {result} minute(s).")
    else:
        print("Trapped!")