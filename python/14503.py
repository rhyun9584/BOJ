N, M = [int(x) for x in input().split()]
cleaner = [0, 0]
cleaner[0], cleaner[1], direction = [int(x) for x in input().split()]
map = []
for i in range(N):
    map.append([int(x) for x in input().split()])

clean_count = 0
while True:
    if map[cleaner[0]][cleaner[1]] == 0:
        clean_count += 1
        map[cleaner[0]][cleaner[1]] = 2 # 청소완료
    
    is_moved = False
    for i in range(4):
        # 북쪽을 바라봄, 서쪽이 아직 청소되지 않았다면 이동
        if direction == 0 and map[cleaner[0]][cleaner[1]-1] == 0:
            cleaner[1] -= 1
            is_moved = True
            break
        # 동쪽을 바라봄, 북쪽이 아직 청소되지 않았다면 이동
        elif direction == 1 and map[cleaner[0]-1][cleaner[1]] == 0:
            cleaner[0] -= 1
            is_moved = True
            break
        # 남쪽을 바라봄, 동쪽이 아직 청소되지 않았다면 이동
        elif direction == 2 and map[cleaner[0]][cleaner[1]+1] == 0:
            cleaner[1] += 1
            is_moved = True
            break
        # 동쪽을 바라봄, 북쪽이 아직 청소되지 않았다면 이동
        elif direction == 3 and map[cleaner[0]+1][cleaner[1]] == 0:
            cleaner[0] += 1
            is_moved = True
            break

        if direction == 0: direction = 3
        else: direction -= 1

    if is_moved:
        if direction == 0: direction = 3
        else: direction -= 1
    else:
        if direction == 0 and map[cleaner[0]+1][cleaner[1]] != 1:
            cleaner[0] += 1
        elif direction == 1 and map[cleaner[0]][cleaner[1]-1] != 1:
            cleaner[1] -= 1
        elif direction == 2 and map[cleaner[0]-1][cleaner[1]] != 1:
            cleaner[0] -= 1
        elif direction == 3 and map[cleaner[0]][cleaner[1]+1] != 1:
            cleaner[1] += 1
        else:
            break

print(clean_count)
