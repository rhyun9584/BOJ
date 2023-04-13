board = []
for _ in range(5):
    board.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

result_set = set()

def dfs(x, y, cnt, number_str):
    if cnt == 6:
        result_set.add(number_str)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, cnt+1, number_str+str(board[nx][ny]))

for i in range(5):
    for j in range(5):
        dfs(i, j, 1, str(board[i][j]))

print(len(result_set))