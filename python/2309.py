import sys
from itertools import combinations

seven = list(map(int, sys.stdin.readlines()))

for arr in combinations(seven, 7):
    if sum(arr) == 100:
        print("\n".join(map(str, sorted(arr))))
        break
