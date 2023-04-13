import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    W = input().rstrip()
    K = int(input())

    idx = [[] for _ in range(ord('z')-ord('a')+1)]
    for i in range(len(W)):
        w = W[i]
        idx[ord(w)-ord('a')].append(i)

    result = []
    for i in idx:
        if len(i) < K:
            continue

        for j in range(len(i)-K+1):
            result.append(i[j+K-1] - i[j] + 1)

    if result:
        print(min(result), max(result))
    else:
        print(-1)