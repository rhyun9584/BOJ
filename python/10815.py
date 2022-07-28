import sys

N = int(input())
have = set(map(int, sys.stdin.readline().rstrip().split()))

M = int(input())
check = list(map(int, sys.stdin.readline().rstrip().split()))

for x in check:
    if x in have:
        print(1, end=' ')
    else:
        print(0, end=' ')
