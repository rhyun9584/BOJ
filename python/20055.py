import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
arr = deque(list(map(int, input().split())))

go = True
step = 1
zero_count = 0
robot = deque([0] * (N))

while go:
    # 1. 벨트 회전
    arr.appendleft(arr.pop())
    robot.pop()
    robot.appendleft(0)

    # 2. 로봇 이동
    if robot[N-1] == 1:
        robot[N-1] = 0
    for i in range(N-2, -1, -1):
        if robot[i] == 1 and robot[i+1] == 0 and arr[i+1] > 0:
            robot[i] = 0
            robot[i+1] = 1
            arr[i+1] -= 1

            if arr[i+1] == 0:
                zero_count += 1

    # 3. 로봇 올리기
    if arr[0] > 0:
        robot[0] = 1
        arr[0] -= 1

        if arr[0] == 0:
            zero_count += 1

    # 4. 내구도가 0인 칸의 개수 K와 비교
    if zero_count < K:
        step += 1
    else:
        go = False

print(step)