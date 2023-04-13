import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    W, H = map(int, input().split())

    start = (0, 0)
    fire = []
    board = []
    for i in range(H):
        arr = list(input().rstrip())

        if '@' in arr:
            start = (i, arr.index('@'))

        for j in range(W):
            if arr[j] == '*':
                fire.append((i, j))

        board.append(arr)

    queue = deque()
    for fx, fy in fire:
        queue.append((fx, fy, '*', 0))
    queue.append((start[0], start[1], '@', 0))

    result = -1

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while queue:
        x, y, ch, cnt = queue.popleft()

        if (x in (0, H-1) or y in (0, W-1)) and ch == '@':
            result = cnt+1
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < H and 0 <= ny < W and board[nx][ny] in ('.', '@'):
                board[nx][ny] = ch
                queue.append((nx, ny, ch, cnt+1))

    print(result if result != -1 else 'IMPOSSIBLE')