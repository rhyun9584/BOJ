import sys
import heapq

N = int(input())
data = map(int, sys.stdin.readlines())

queue = []
for i in data:
    if i == 0:
        a, b = heapq.heappop(queue) if len(queue) > 0 else (0, 0)
        print(a*b)
    elif i > 0:
        heapq.heappush(queue, (i, 1))
    else:
        heapq.heappush(queue, (-i, -1))