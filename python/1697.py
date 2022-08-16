from collections import deque

N, K = map(int, input().split())

queue = deque([(N, 0)])
visited = [0] * 100001
visited[N] = 1
while queue:
    v, cnt = queue.popleft()

    if v == K:
        print(cnt)
        break

    if v-1 >= 0 and visited[v-1] == 0:
        visited[v-1] = 1
        queue.append((v-1, cnt+1))
    if v+1 <= 100000 and visited[v+1] == 0:
        visited[v+1] = 1
        queue.append((v+1, cnt+1))
    if v*2 <= 100000 and visited[v*2] == 0:
        visited[v*2] = 1
        queue.append((v*2, cnt+1))