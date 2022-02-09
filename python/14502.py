import copy

N, M = [int(x) for x in input().split()]

map = []
for i in range(N):
    map.append([int(x) for x in input().split()])

max_safe = 0
def build_wall(idx):
    """
    idx: 몇번째로 세우는 벽인지 (1부터 시작)
    """
    global map, max_safe

    if idx == 4:
        # map 안에 2를 확산시킨다음에 0의 갯수 찾기
        spreaded_map = spread_virus()
        safe = get_safe(spreaded_map)
        max_safe = max(max_safe, safe)

        return

    for i in range(N):
        for j in range(M):
            if map[i][j] == 0:
                map[i][j] = 1
                build_wall(idx+1)
                map[i][j] = 0

def spread_virus():
    """
    `map`의 바이러스(2)를 확산시키기
    """
    new_map = copy.deepcopy(map)

    for i in range(N):
        for j in range(M):
            if new_map[i][j] == 2:
                spreading(new_map, i, j)
    
    return new_map

def spreading(new_map, i, j):
    if i > 0 and new_map[i-1][j] == 0:
        new_map[i-1][j] = 2
        spreading(new_map, i-1, j)
    if i < N-1 and new_map[i+1][j] == 0:
        new_map[i+1][j] = 2
        spreading(new_map, i+1, j)
    if j > 0 and new_map[i][j-1] == 0:
        new_map[i][j-1] = 2
        spreading(new_map, i, j-1)
    if j < M-1 and new_map[i][j+1] == 0:
        new_map[i][j+1] = 2
        spreading(new_map, i, j+1)

def get_safe(new_map):
    count = 0
    for i in range(N):
        for j in range(M):
            if new_map[i][j] == 0:
                count += 1

    return count

build_wall(1)
print(max_safe)