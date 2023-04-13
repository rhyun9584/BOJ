import sys
input = sys.stdin.readline

N, s, P = map(int, input().split())

score = [s]
if N > 0:
    score.extend(list(map(int, input().split())))

score.sort(reverse=True)

idx = score.index(s)
if idx < P and (N < P or score[P] < s):
    print(idx+1)
else:
    print(-1)