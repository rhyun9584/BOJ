from collections import deque

A, B = map(int, input().split())

queue = deque([(A, 1)])

result = -1
while queue:
    v, cnt = queue.popleft()

    if v == B:
        result = cnt
        break

    for n in [v*2, v*10+1]:
        if n <= B:
            queue.append((n, cnt+1))

print(result)