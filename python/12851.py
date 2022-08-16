from collections import deque

N, K = map(int, input().split())

visited = [-1] * 100001
visited[N] = 0

queue = deque([(N, 0)])

count = 0
minimum = -1
while queue:
    v, s = queue.popleft()
    visited[v] = s
    
    if count > 0 and minimum < s:
        break

    if v == K:
        minimum = s
        count += 1
        continue

    for new_v in (v-1, v+1, v*2):
        if 0 <= new_v <= 100000 and visited[new_v] == -1:
            queue.append((new_v, s+1))

print(minimum)
print(count)