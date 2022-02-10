import copy

N, M = [int(x) for x in input().split()]
office = [[int(x) for x in input().split()] for _ in range(N)]
cctv_list = []
empty = []
for x in range(N):
    for y in range(M):
        if office[x][y] == 0:
            empty.append((x, y))
        elif 0 < office[x][y] < 6:
            # (a, b, n) a, b 위치의 n번 cctv
            cctv_list.append((x, y, office[x][y]))

# (right, left, down, up)
observe_area = [
    [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)],
    [(1, 1, 0, 0), (0, 0, 1, 1)],
    [(1, 0, 0, 1), (0, 1, 0, 1), (0, 1, 1, 0), (1, 0, 1, 0)],
    [(1, 1, 0, 1), (0, 1, 1, 1), (1, 1, 1, 0), (1, 0, 1, 1)],
    [(1, 1, 1, 1)],
]

min_area = len(empty)
def observe(idx, empty_list):
    global min_area, cctv_list

    if idx == len(cctv_list):
        # 사각지대 계산
        min_area = min(min_area, len(empty_list))
        return

    # 1번 cctv라면 observe_area[0] 참조
    for direction in observe_area[cctv_list[idx][2]-1]:
        remove = []
        area = cctv_list[idx][:2]
        if direction[0]:
            # 오른쪽 방향으로 한칸씩 
            for time in range(1, M-area[1]):
                check = (area[0], area[1]+time)
                # 벽
                if office[check[0]][check[1]] == 6:
                    break

                if check in empty_list:
                    empty_list.remove(check)
                    remove.append(check)
        if direction[1]:
            for time in range(1, area[1]+1):
                check = (area[0], area[1]-time)
                if office[check[0]][check[1]] == 6:
                    break

                if check in empty_list:
                    empty_list.remove(check)
                    remove.append(check)
        if direction[2]:
            for time in range(1, N-area[0]):
                check = (area[0]+time, area[1])
                if office[check[0]][check[1]] == 6:
                    break

                if check in empty_list:
                    empty_list.remove(check)
                    remove.append(check)
        if direction[3]:
            for time in range(1, area[0]+1):
                check = (area[0]-time, area[1])
                if office[check[0]][check[1]] == 6:
                    break

                if check in empty_list:
                    empty_list.remove(check)
                    remove.append(check)

        observe(idx+1, empty_list)
        empty_list += remove

observe(0, copy.deepcopy(empty))
print(min_area)