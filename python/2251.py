from copy import deepcopy
from itertools import permutations
from collections import deque

volume = list(map(int, input().split()))

result = set()
queue = deque([[0, 0, volume[2]]])

visited = dict()
visited[".".join(map(str, [0, 0, volume[2]]))] = 1
while queue:
    arr = queue.popleft()
    if arr[0] == 0:
        result.add(arr[2])

    # m = (x, y) --> x -> y
    for move in permutations(range(3), 2):
        x, y = move
        # 옮길 물이 없거나, 옮겨 담을 빈 공간이 없으면 패스
        if arr[x] == 0 or arr[y] == volume[y]:
            continue
        move_water = min(arr[x], volume[y]-arr[y])
        
        new_arr = deepcopy(arr)
        new_arr[x] = arr[x] - move_water
        new_arr[y] = arr[y] + move_water

        key = ".".join(map(str, new_arr))
        if key not in visited:
            visited[key] = 1
            queue.append(new_arr)

result = sorted(list(result))
print(" ".join(map(str, result)))