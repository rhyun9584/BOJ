N = int(input())
candy = [list(input()) for _ in range(N)]

def get_cnt(i, j, dir, cnt):
    if dir == 'left':
        if j-1 < 0 or candy[i][j] != candy[i][j-1]: return cnt
        else: return get_cnt(i, j-1, dir, cnt+1)
    if dir == 'right':
        if j+1 >= N or candy[i][j] != candy[i][j+1]: return cnt
        else: return get_cnt(i, j+1, dir, cnt+1)
    if dir == 'up':
        if i-1 < 0 or candy[i][j] != candy[i-1][j]: return cnt
        else: return get_cnt(i-1, j, dir, cnt+1)
    if dir == 'down':
        if i+1 >= N or candy[i][j] != candy[i+1][j]: return cnt
        else: return get_cnt(i+1, j, dir, cnt+1)

result = 0
for i in range(N):
    for j in range(N):
        # 위-아래 교환
        if i+1 < N:
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
            result = max(result, get_cnt(i,j,'left',1)+get_cnt(i,j,'right',1)-1) # i
            result = max(result, get_cnt(i+1,j,'left',1)+get_cnt(i+1,j,'right',1)-1) # i+1
            result = max(result, get_cnt(i,j,'up',1)+get_cnt(i,j,'down',1)-1) # j
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
        # 왼-오 교환
        if j+1 < N:
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            result = max(result, get_cnt(i,j,'up',1)+get_cnt(i,j,'down',1)-1) # j
            result = max(result, get_cnt(i,j+1,'up',1)+get_cnt(i,j+1,'down',1)-1) # j+1
            result = max(result, get_cnt(i,j,'left',1)+get_cnt(i,j,'right',1)-1) # i
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
    if result == N:
        break

print(result)