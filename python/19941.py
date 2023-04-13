import sys
input = sys.stdin.readline

N, K = map(int, input().split())
table = input().rstrip()

cnt = 0
take = [0] * (N)
for i in range(N):
    if table[i] == 'H':
        continue

    for j in range(-K, K+1):
        if 0 <= i+j < N and table[i+j] == 'H' and take[i+j] == 0:
            take[i+j] = 1
            cnt += 1
            break

print(cnt)
