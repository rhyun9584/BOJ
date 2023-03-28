import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

token = [[[] for _ in range(N)] for _ in range(N)]
direction = [0]
next_queue = []
for i in range(1, K+1):
    x, y, d = map(int, input().split())

    token[x-1][y-1].append(i)
    direction.append(d-1)
    if len(token[x-1][y-1]) == 1:
        heapq.heappush(next_queue, (i, x-1, y-1))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

turn = 0
is_end = False
while next_queue:
    queue = next_queue
    next_queue = []
    
    turn += 1
    while queue:
        number, x, y = heapq.heappop(queue)
        dir = direction[number]

        nx = x + dx[dir]
        ny = y + dy[dir]

        if (not (0 <= nx < N and 0 <= ny < N)) or board[nx][ny] == 2:
            # 이동하려는 칸이 파란색이거나 체스판 밖일 때 방향 뒤집기
            dir = dir+1 if dir%2 == 0 else dir-1
            direction[number] = dir

            nx = x + dx[dir]
            ny = y + dy[dir]

        if (not (0 <= nx < N and 0 <= ny < N)) or board[nx][ny] == 2:
            # 이동하려는 칸이 또 다시 파란색이거나 보드 밖이면 그대로 끝
            heapq.heappush(next_queue, (number, x, y))
            continue
        elif board[nx][ny] == 0:
            # 이동하려는 칸이 흰색
            token[nx][ny].extend(token[x][y])
            token[x][y] = []

            # 빈 칸으로 이동했다면, 다음에도 같은 번호를 기준으로 이동
            if token[nx][ny][0] == number:
                heapq.heappush(next_queue, (token[nx][ny][0], nx, ny))
        else:
            # 이동하려는 칸이 빨간색
            token[nx][ny].extend(reversed(token[x][y]))
            token[x][y] = []

            if token[nx][ny][0] <= number:
                heapq.heappush(next_queue, (token[nx][ny][0], nx, ny))
            else:
                heapq.heappush(queue, (token[nx][ny][0], nx, ny))

        # 칸에 쌓인 말이 4개 이상인 경우 종료
        if len(token[nx][ny]) >= 4:
            is_end = True
            break

    # 종료되는 턴이 1000보다 크다면 -1을 출력
    if turn == 1000:
        turn = -1

    if is_end or turn == -1:
        break

print(turn)