import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
X = int(input())

counter = Counter(numbers)
sorted_counter = sorted(counter.keys())

answer = 0
for key in sorted_counter:
    if key >= X/2:
        break

    if X-key in counter:
        answer += 1

print(answer)