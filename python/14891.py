gears = []

for i in range(4):
    gear = list(input())
    gears.append(gear)

K = int(input())

def turn_gear(idx, clockwise, left=True, right=True):
    """
    idx: 회전할 톱니바퀴
    clockwise: 회전 방향
    left, right: 각 방향의 옆 톱니바퀴 회전 유무 -> for 재귀
    """
    if idx > 0 and left and gears[idx][6] != gears[idx-1][2]:
        # 왼쪽 톱니바퀴 회전
        turn_gear(idx-1, clockwise*-1, right=False)
    if idx < 3 and right and gears[idx][2] != gears[idx+1][6]:
        # 오른쪽 톱니바퀴 회전
        turn_gear(idx+1, clockwise*-1, left=False)

    new_gear = []

    if clockwise == 1:
        new_gear.append(gears[idx][7])
        for i in range(7):
            new_gear.append(gears[idx][i])
    else:
        for i in range(7):
            new_gear.append(gears[idx][i+1])
        new_gear.append(gears[idx][0])
    
    gears[idx] = new_gear

for i in range(K):
    idx, dir = [int(x) for x in input().split(" ")]
    turn_gear(idx-1, dir)

result = 0
for i in range(4):
    if gears[i][0] == "1":
        result += 2 ** i

print(result)
