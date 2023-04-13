from collections import deque

while True:
    W, H = map(int, input().split())
    # W와 H는 항상 1 이상이므로, 하나만 0이어도 바로 break
    if W == 0:
        break

    room = []
    dust = 0
    robot = (0, 0)
    for i in range(H):
        arr = list(input())

        # 로봇 청소기의 위치
        if 'o' in arr:
            robot =  (i, arr.index('o'))

        # 더러운 칸의 수
        dust += arr.count('*')

        room.append(arr)

    queue = deque()

    result = -1
    while queue:
        pass
    
    print(result)
