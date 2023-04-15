import sys
input = sys.stdin.readline

N, L = map(int, input().split())

pool = []
for _ in range(N):
    s, e = map(int, input().split())
    pool.append((s, e))
pool.sort()

answer = 0
last = 0
for s, e in pool:
    if s < last:
        s = last

    cnt  = (e-s-1) // L + 1
    
    answer += cnt
    last = s + L*cnt

print(answer)