from collections import deque

M, N, H = map(int, input().split())

tomato = deque()
box = [[] for _ in range(H)]
for i in range(H):
    for j in range(N):
        arr = list(map(int, input().split()))
        box[i].append(arr)

        for k in range(M):
            if arr[k] == 1:
                tomato.append((i, j, k, 0))

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

result = 0
while tomato:
    z, x, y, cnt = tomato.popleft()

    result = cnt

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and box[nz][nx][ny] == 0:
            box[nz][nx][ny] = 1
            tomato.append((nz, nx, ny, cnt+1))

for i in range(H):
    for j in range(N):
        if 0 in box[i][j]:
            result = -1
            break

    if result == -1: break

print(result)