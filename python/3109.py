import sys
input = sys.stdin.readline

R, C = map(int, input().split())

board = []
for _ in range(R):
    board.append(list(input().rstrip()))

def dfs(x, y):
    board[x][y] = 'o'

    if y == C-1:
        return True
    
    for dx in [-1, 0, 1]:
        nx = x + dx
        ny = y + 1
        if 0 <= nx < R and board[nx][ny] == '.':
            if dfs(nx, ny):
                return True
            
    return False

answer = 0
for i in range(R):
    if dfs(i, 0):
        answer += 1

print(answer)