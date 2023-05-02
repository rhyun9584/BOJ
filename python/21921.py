import sys
input = sys.stdin.readline

N, X = map(int, input().split())
views = list(map(int, input().split()))

cnt, now = 1, sum(views[:X])
_max = now
for i in range(N-X):
    now -= views[i]
    now += views[i+X]

    if now == _max:
        cnt += 1
    elif now > _max:
        _max = now
        cnt = 1

if _max == 0:
    print("SAD")
else:
    print(_max)
    print(cnt)