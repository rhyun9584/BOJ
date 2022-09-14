from collections import deque

def get_distance(f, t):
    return abs(f[0]-t[0]) + abs(f[1]-t[1])

T = int(input())
for _ in range(T):
    N = int(input())
    
    home = tuple(map(int, input().split()))
    store = [tuple(map(int, input().split())) for _ in range(N)]
    festival = tuple(map(int, input().split()))

    is_reach = False
    visited = [0] * (N)
    queue = deque([home])
    while queue:
        x, y = queue.popleft()

        if get_distance((x, y), festival) <= 1000:
            is_reach = True
            break

        for i in range(N):
            if visited[i] == 0 and 0 < get_distance((x, y), store[i]) <= 1000:
                visited[i] = 1
                queue.append(store[i])

    if is_reach:
        print("happy")
    else:
        print("sad")