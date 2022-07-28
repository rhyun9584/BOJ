import sys

N = int(input())
have = dict()
for x in list(map(int, sys.stdin.readline().rstrip().split())):
    if x in have:
        have[x] += 1
    else:
        have[x] = 1

input()
check = list(map(int, sys.stdin.readline().rstrip().split()))
print(' '.join(str(have[x]) if x in have else '0' for x in check))
