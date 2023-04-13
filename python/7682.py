import sys
input = sys.stdin.readline

def check_win(board, mark):
    for i in range(3):
        # 가로 확인
        if board[i*3:(i+1)*3] == mark*3:
            return True
        
        # 세로 확인
        if board[i] + board[i+3] + board[i+6] == mark*3:
            return True
        
    # 대각선 \ 확인
    if board[0]+board[4]+board[8] == mark*3:
        return True
    
    # 대각선 / 확인
    if board[2]+board[4]+board[6] == mark*3:
        return True

    return False

while True:
    board = input().rstrip()
    
    if board == 'end':
        break

    cnt_X = board.count('X')
    cnt_O = board.count('O')

    if cnt_O <= cnt_X <= cnt_O+1:
        if '.' not in board:
            if not check_win(board, 'O'):
                print("valid")
                continue
        else:
            if cnt_O == cnt_X and check_win(board, 'O') and (not check_win(board, 'X')):
                print("valid")
                continue
            if cnt_O+1 == cnt_X and check_win(board, 'X') and (not check_win(board, 'O')):
                print("valid")
                continue

    print("invalid")