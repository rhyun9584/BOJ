import sys

board = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))

zeros = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            zeros.append((i, j))
cnt_zero = len(zeros)

def dfs(zero_idx):
    if zero_idx == cnt_zero:
        return True

    x, y = zeros[zero_idx]
    numbers = set(range(1, 10))
    numbers -= set(board[x])
    numbers -= set([board[i][y] for i in range(9)])

    rect_x = x//3 * 3
    rect_y = y//3 * 3
    for i in range(rect_x, rect_x+3):
        for j in range(rect_y, rect_y+3):
            if board[i][j] in numbers:
                numbers.remove(board[i][j])

    for n in numbers:
        board[x][y] = n
        if dfs(zero_idx+1):
            return True
        board[x][y] = 0
    
    return False

dfs(0)

for i in range(9):
    print(" ".join(map(str, board[i])))
    