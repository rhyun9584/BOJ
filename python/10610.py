import sys
from itertools import combinations

N = list(input())
N.sort(reverse=True)
for num in combinations(N, len(N)):
    num_str = "".join(num)
    if int(num_str) % 30 == 0:
        print(num_str)
        sys.exit()

print(-1)