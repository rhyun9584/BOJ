import sys
input = sys.stdin.readline

N, C = map(int, input().split())
M = int(input())
box = []
for _ in range(M):
    a, b, c = map(int, input().split())
    box.append((a, b, c))

box.sort(key=lambda x:x[1])

remain = [C] * (N+1)
answer = 0
for s, e, c in box:
    minimum = min(c, min(remain[s:e]))

    for i in range(s, e):
        remain[i] -= minimum

    answer += minimum

print(answer)
