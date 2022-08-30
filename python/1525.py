from copy import deepcopy
from collections import deque

init_board = ""
for _ in range(3):
    init_board += "".join(input().split())
zero = init_board.index('0')

visited = dict()
visited[init_board] = 0

result = -1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

queue = deque([(zero, init_board)])
while queue:
    z, board = queue.popleft()

    if board == '123456780':
        result = visited['123456780']
        break

    x, y = z//3, z%3
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_z = nx*3 + ny

            new_board = list(board)
            new_board[new_z], new_board[z] = new_board[z], new_board[new_z]
            new_board = "".join(new_board)

            if new_board not in visited:
                visited[new_board] = visited[board]+1
                queue.append((new_z, new_board))
            
print(result)