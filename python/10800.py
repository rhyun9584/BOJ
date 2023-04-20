import sys
input = sys.stdin.readline

N = int(input())

ball = []
color = dict()
for i in range(N):
    c, s = map(int, input().split())

    if c not in color:
        color[c] = 0

    ball.append((s, c, i))
ball.sort()

total = 0
answer = [0] * N
now_size = 0
now_cnt = dict()
for s, c, idx in ball:
    if s > now_size:
        now_size = s
        for k, v in now_cnt.items():
            total += v
            color[k] += v
            
        now_cnt = dict()

    answer[idx] = total - color[c]

    if c in now_cnt:
        now_cnt[c] += s
    else:
        now_cnt[c] = s

for i in range(N):
    print(answer[i])