from collections import deque

F, S, G, U, D = map(int, input().split())

def bfs(S):
    queue = deque([(S, 0)])
    visited = [0] * (F+1)
    visited[S] = 1

    while queue:
        v, cnt = queue.popleft()

        if v == G:
            return cnt

        for n in (v+U, v-D):
            if 0 < n <= F and visited[n] == 0:
                visited[n] = 1
                queue.append((n, cnt+1))

    return -1

result = bfs(S)
if result > -1: print(result)
else: print("use the stairs")