import sys

N, K = map(int, input().split())
coin = list(map(int, sys.stdin.readlines()))

count = 0
for i in range(N-1, -1, -1):
    count += K//coin[i]
    K -= coin[i] * (K//coin[i])
    if K == 0:
        break

print(count)
