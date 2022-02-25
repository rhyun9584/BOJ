import sys
from itertools import combinations

def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a%b)

T = int(sys.stdin.readline())
for _ in range(T):
    n, *arr = map(int, sys.stdin.readline().split())
    
    sum = 0
    for x, y in combinations(arr, 2):
        sum += GCD(x, y)

    print(sum)