import sys
import heapq

input = sys.stdin.readline

N = int(input())

queue = []
for _ in range(N):
    num = int(input())
    
    if num == 0:
        if queue:
            print(heapq.heappop(queue))
        else:
            print(0)
    else:
        heapq.heappush(queue, num)
