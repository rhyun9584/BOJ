import sys
import heapq
input = sys.stdin.readline

N = int(input())

station = []
for _ in range(N):
    a, b = map(int, input().split())

    station.append((a, b))
station.sort(reverse=True)

L, P = map(int, input().split())

queue = []
answer = 0
while P < L:
    while station and station[-1][0] <= P:
        _, b = station.pop()
        heapq.heappush(queue, -b)

    if queue:
        P -= heapq.heappop(queue)
        answer += 1
    else:
        answer = -1
        break

print(answer)