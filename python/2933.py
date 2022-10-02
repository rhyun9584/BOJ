import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())

def bfs(i, j, visited, mine):
    cluster = []

    queue = deque()
    queue.append((i, j))
    visited[i][j] = 1
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while queue:
        x, y = queue.popleft()
        cluster.append((x,y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and mine[nx][ny] == 'x' and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))
    
    return cluster

def get_bottom(cluster):
    return max(map(lambda x: x[0], cluster))

def fall(mine, cluster):
    bottom_height = get_bottom(cluster)

    # 몇 칸을 내려야하는지 체크
    down = 0
    is_break = False
    while True:
        down += 1

        if bottom_height + down == R-1:
            break

        for cx, cy in cluster:
            if mine[cx+down+1][cy] == 'x' and (cx+down+1, cy) not in cluster:
                is_break = True
                break
        if is_break: break

    
    for cx, cy in cluster:
        mine[cx][cy] = '.'

    for cx, cy in cluster:
        mine[cx+down][cy] = 'x'
    

mine = [list(input().rstrip()) for _ in range(R)]

N = int(input())
heights = list(map(int, input().split()))

for i in range(N):
    # 맨 아래가 1(->R-1), 제일 위가 R(->0)
    h = R - heights[i]

    # 막대를 던진 높이에 미네랄이 없다면, 스킵
    if 'x' not in mine[h]:
        continue

    # i가 짝수면 왼쪽, i가 홀수면 오른쪽
    if i % 2 == 0:
        for j in range(C):
            if mine[h][j] == 'x':
                mine[h][j] = '.'
                break
    else:
        for j in range(C-1, -1, -1):
            if mine[h][j] == 'x':
                mine[h][j] = '.'
                break

    clusters = []
    visited = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if mine[i][j] == 'x' and visited[i][j] == 0:
                clusters.append(bfs(i, j, visited, mine))
    
    for c in clusters:
        if get_bottom(c) < R-1: 
            fall(mine, c)
            break

for i in range(R):
    print("".join(mine[i]))