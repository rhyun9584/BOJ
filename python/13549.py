import heapq

N, K = map(int, input().split())

queue = []
heapq.heappush(queue, (0, N))

visited = [0] * 100001
visited[N] = 1

while queue:
    cnt, v = heapq.heappop(queue)

    if v == K:
        print(cnt)
        break

    if v*2 <= 100000 and visited[v*2] == 0:
        visited[v*2] = 1
        heapq.heappush(queue, (cnt, v*2))
    if v-1 >= 0 and visited[v-1] == 0:
        visited[v-1] = 1
        heapq.heappush(queue, (cnt+1, v-1))
    if v+1 <= 100000 and visited[v+1] == 0:
        visited[v+1] = 1
        heapq.heappush(queue, (cnt+1, v+1))