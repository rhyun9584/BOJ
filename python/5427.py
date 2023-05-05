import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(int(input())):
    W, H = map(int, input().split())

    board = []
    fire = []
    sx, sy = 0, 0
    for i in range(H):
        board.append(list(input().rstrip()))

        # 시작 위치 확인
        if '@' in board[-1]:
            sx = i
            sy = board[-1].index('@')
            board[sx][sy] = '.'
        
        # 불 위치 확인
        for j in range(W):
            if board[i][j] == '*':
                fire.append((i, j))

    queue = deque()
    for fx, fy in fire:
        queue.append((fx, fy, True, 0))
    queue.append((sx, sy, False, 0))

    visited = [[0] * W for _ in range(H)]
    visited[sx][sy] = 1

    answer = -1
    while queue:
        x, y, is_fire, cnt = queue.popleft()

        # 탈출 성공
        if not is_fire and (x in (0, H-1) or y in (0, W-1)):
            answer = cnt+1
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < H and 0 <= ny < W and board[nx][ny] == '.':
                if is_fire:
                    board[nx][ny] = '*'
                    queue.append((nx, ny, True, cnt+1))
                elif visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny, False, cnt+1))

    if answer == -1:
        print("IMPOSSIBLE")
    else:
        print(answer)