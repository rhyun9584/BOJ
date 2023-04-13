from collections import deque

N, K = map(int, input().split())

visited = [0] * 100001
visited[N] = 1

queue = deque([(N, 0)])
while queue:
    v, cnt = queue.popleft()

    if v == K:
        print(cnt)
        break

    for n in [v-1, v+1, v*2]:
        if 0 <= n <= 100000 and visited[n] == 0:
            visited[n] = 1
            queue.append((n, cnt+1))