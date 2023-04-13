import sys
input = sys.stdin.readline

N = int(input())

heart_x, heart_y = 0, 0

board = []
for _ in range(N):
    board.append(list(input().rstrip()))

# 심장 위치 찾기
for i in range(N):
    if '*' in board[i]:
        heart_x = i+1
        heart_y = board[i].index('*')
        break

answer = [0, 0, 0, 0, 0]

# 왼쪽 팔
for i in range(heart_y-1 , -1, -1):
    if board[heart_x][i] != '*':
        break

    answer[0] += 1

# 오른쪽 팔
for i in range(heart_y+1, N):
    if board[heart_x][i] != '*':
        break

    answer[1] += 1

# 허리
leg_start = 0
for i in range(heart_x+1, N):
    if board[i][heart_y] != '*':
        leg_start = i
        break
        
    answer[2] += 1

# 왼쪽 다리
for i in range(leg_start, N):
    if board[i][heart_y-1] != '*':
        break

    answer[3] += 1

# 오른쪽 다리
for i in range(leg_start, N):
    if board[i][heart_y+1] != '*':
        break

    answer[4] += 1

print(heart_x+1, heart_y+1)
print(" ".join(map(str, answer)))