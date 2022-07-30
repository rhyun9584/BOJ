# 갈 수 없는 경로에 대해 체크할 수 있으면 시간이 더 줄어들것같은데... 
import sys
sys.setrecursionlimit(10**5)

N = int(input())

maps = [list(map(int, input().split())) for _ in range(N)]

dp_table = [[0]*N for _ in range(N)]
dp_table[N-1][N-1] = 1

road = []
def dfs(x, y):
    global count
    d = maps[x][y]

    if dp_table[x][y] > 0:
        # (x,y)에 도착했을때 이미 갈 수 있는 경로의 경우의 수가 기록된 위치인 경우
        # 그 경우의 수 만큼 더해주어 기록 
        for rx, ry in road:
            dp_table[rx][ry] += dp_table[x][y]
        return

    # 중간에 0을 만나면 더이상 갈 수 없음
    if d == 0:
        return 

    road.append((x,y))

    if x + d < N:
        dfs(x+d, y)
    if y + d < N:
        dfs(x, y+d)

    road.pop()

dfs(0, 0)
print(dp_table[0][0])