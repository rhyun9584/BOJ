import sys
input = sys.stdin.readline

R, C = map(int, input().split())

board = [input().rstrip() for _ in range(R)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

alpha = [0] * (ord('Z')-ord('A')+1)
alpha[(ord(board[0][0])-ord('A'))] = 1

def dfs(x, y, cnt):
    global result
    result = max(result, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < R and 0 <= ny < C and alpha[ord(board[nx][ny]) - ord('A')] == 0:
            alpha[ord(board[nx][ny]) - ord('A')] = 1
            dfs(nx, ny, cnt+1)
            alpha[ord(board[nx][ny]) - ord('A')] = 0

result = 0
dfs(0, 0, 1)

print(result)