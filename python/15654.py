import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())
number = list(map(int, input().split()))
number.sort()

for p in permutations(number, M):
    print(" ".join(map(str,p)))