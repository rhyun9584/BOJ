import sys
import heapq

N = int(input())

data = map(int, sys.stdin.readlines())
queue = []
for i in data:
    if i == 0:
        print(-heapq.heappop(queue) if len(queue) > 0 else 0)
    else:
        heapq.heappush(queue, -i)