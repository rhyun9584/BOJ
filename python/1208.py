import sys
import bisect
from itertools import combinations
input = sys.stdin.readline

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

left, right = numbers[:N//2], numbers[N//2:]

left_S, right_S = [0], [0]
for i in range(1, N//2+1):
    for arr in combinations(left, i):
        left_S.append(sum(arr))
left_S.sort()

for i in range(1, N-(N//2)+1):
    for arr in combinations(right, i):
        right_S.append(sum(arr))
right_S.sort()

answer = 0
for l in left_S:
    r = S - l
    answer += bisect.bisect_right(right_S, r) - bisect.bisect_left(right_S, r)

if S == 0: 
    answer -= 1
print(answer)
