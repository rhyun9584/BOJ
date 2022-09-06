from collections import deque

R, C = map(int, input().split())

board = []
fire = []
init_x, init_y = 0, 0
for i in range(R):
    board.append(list(input()))

    for j in range(C):
        if board[i][j] == 'J':
            init_x, init_y = i, j
        
        if board[i][j] == "F":
            fire.append((i, j))

queue = deque()
queue.append((init_x, init_y, 1))
for f_x, f_y in fire:
    queue.append((f_x, f_y, 1))

result = -1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while queue:
    x, y, t = queue.popleft()
    
    if board[x][y] == 'J' and (x in (0, R-1) or y in (0, C-1)):
        result = t
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < R and 0 <= ny < C:
            if board[x][y] == 'J' and board[nx][ny] == '.':
                board[nx][ny] = 'J'
                queue.append((nx, ny, t+1))
            
            if board[x][y] == 'F' and board[nx][ny] not in ('#', 'F'):
                board[nx][ny] = 'F'
                queue.append((nx, ny, t+1))

if result > -1:
    print(result)
else:
    print('IMPOSSIBLE')