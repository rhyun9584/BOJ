import sys
import heapq
input = sys.stdin.readline

N = int(input())

left = []  # max heap
right = [] # min heap
for i in range(N):
    a = int(input())
    if len(left) == len(right):
        heapq.heappush(left, -a)
    else:
        heapq.heappush(right, a)
    
    # left의 가장 큰 수와 right의 가장 작은 수 비교
    if i > 0 and -(left[0]) > right[0]:
        r = -(heapq.heappop(left))
        l = heapq.heappop(right)

        heapq.heappush(left, -l)
        heapq.heappush(right, r)

    print(-left[0])