from collections import deque

F, S, G, U, D = map(int, input().split())

def bfs(start, visited):
    queue = deque([(start, 0)])
    visited[start] = 1

    while queue:
        v, cnt = queue.popleft()

        if v == G:
            return cnt

        if v + U <= F and visited[v+U] == 0:
            visited[v+U] = 1
            queue.append((v+U, cnt+1))
        if v - D > 0 and visited[v-D] == 0:
            visited[v-D] = 1
            queue.append((v-D, cnt+1))

    return -1
    
visited = [0] * (F+1)
result = bfs(S, visited)

print(result if result > -1 else "use the stairs")