import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())

jewels = []
for _ in range(N):
    m, v = map(int, input().split())
    jewels.append((m, v))
jewels.sort(reverse=True)

bags = []
for _ in range(K):
    bags.append(int(input()))
bags.sort()

total = 0
tmp_jewels = []
for bag in bags:
    # 가방에 넣을 수 있는 보석을 전부 꺼내서 최대 힙에 넣기
    while jewels and jewels[-1][0] <= bag:
        _, v = jewels.pop()
        heapq.heappush(tmp_jewels, -v)

    # 가방에 넣을 수 있는 보석이 있다면,
    # 제일 가치가 큰 보석을 넣기
    if tmp_jewels:
        total -= heapq.heappop(tmp_jewels)

print(total)