import heapq

W, H = map(int, input().split())

start = (0, 0)
board = []
for i in range(H):
    arr = list(input())
    if 'C' in arr:
        start = (i, arr.index('C'))
    board.append(arr)

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

# 방문 배열은 사용한 거울의 수로 기록
visited = [[int(1e9)] * W for _ in range(H)]
visited[start[0]][start[1]] = 0

# 시작점에서 모든 점을 거울 이용 없이 갈 수 있으므로, queue에 바로 넣어줌
queue = []
for i in range(4):
    x = start[0] + dx[i]
    y = start[1] + dy[i]
    if 0 <= x < H and 0 <= y < W and board[x][y] != '*':
        heapq.heappush(queue, (0, i, x, y))
    
while queue:
    cnt, dir, x, y = heapq.heappop(queue)

    # 'C'에 도착했고, 시작점이 아니라면? 도착점!
    if board[x][y] == 'C' and (x, y) != start:
        print(cnt)
        break

    # 이전에 더 적은 거울 수로 방문했다면, 다시 방문하여도 최적 값을 찾을 수 없음.
    # 같은 수로 방문해서 다시 확인하는 건, 다른 방향으로 진행할 수 있기 때문
    if visited[x][y] < cnt:
        continue

    visited[x][y] = cnt

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 왔던 방향에서 다시 돌아가지 않기 위해 dir != (i+2)%4 조건 추가 
        if 0 <= nx < H and 0 <= ny < W and board[nx][ny] != '*' and dir != (i+2)%4:
            if dir != i:
                heapq.heappush(queue, (cnt+1, i, nx, ny))
            else:
                heapq.heappush(queue, (cnt, i, nx, ny))
