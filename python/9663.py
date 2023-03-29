N = int(input())

# board[i] = j
# (j, i)의 위치에 queen 있음
board = [-1] * N

def check_row(row, column):
    for i in range(column):
        if board[i] == row: 
            return False
    
    return True

def check_diagonal(row, column):
    # 왼쪽 대각선 위와 아래 확인
    for i in range(0, column):
        idx = column - i
        if 0 <= row-idx and board[i] == row-idx:
            return False
        if row+idx < N and board[i] == row+idx:
            return False
        
    return True

result = 0
def dfs(num, rows):
    global result

    if num == N:
        result += 1
        return
    
    for i in range(N):
        if (i not in rows) and check_diagonal(i, num):
            board[num] = i
            rows.add(i)
            dfs(num+1, rows)
            rows.remove(i)
            board[num] = -1

dfs(0, set())
print(result)