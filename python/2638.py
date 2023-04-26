import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

board = []
cheese = 0
for _ in range(N):
    board.append(list(map(int, input().split())))
    cheese += board[-1].count(1)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def melt():
    global cheese

    queue = deque()
    queue.append((0, 0))

    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1

    melting = []
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                if board[nx][ny] == 1 and visited[nx][ny] < 2:
                    visited[nx][ny] += 1

                    if visited[nx][ny] == 2:
                        melting.append((nx, ny))

    for x, y in melting:
        cheese -= 1
        board[x][y] = 0

answer = 0
while cheese > 0:
    answer += 1    
    melt()

print(answer)