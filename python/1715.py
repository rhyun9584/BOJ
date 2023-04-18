import sys
import heapq
input = sys.stdin.readline

N = int(input())

cards = []
for _ in range(N):
    heapq.heappush(cards, int(input()))

total = 0
while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)

    total += a+b
    heapq.heappush(cards, a+b)

print(total)