import sys
import heapq
input = sys.stdin.readline

N = int(input())

cup = []
for _ in range(N):
    cup.append(list(map(int, input().split())))
cup.sort()

cnt = 0
queue = []
for d, v in cup:
    if cnt < d:
        cnt += 1
        heapq.heappush(queue, v)
    else:
        if queue[0] < v:
            heapq.heappop(queue)
            heapq.heappush(queue, v)

answer = 0
while queue:
    answer += heapq.heappop(queue)

print(answer)