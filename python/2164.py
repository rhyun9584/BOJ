from collections import deque

N = int(input())
queue = deque([i for i in range(1, N+1)])

i = 0
length = len(queue)
while length > 1:
    if i % 2 == 0:
        queue.popleft()
        length -= 1
    else:
        queue.append(queue.popleft())

    i += 1

print(queue.pop())
