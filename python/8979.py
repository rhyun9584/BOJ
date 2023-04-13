import sys
input = sys.stdin.readline

N, K = map(int, input().split())

medal = [[0] * 3] * (N+1)
for _ in range(N):
    num, g, s, b = map(int, input().split())
    medal[num] = [g, s, b]

cnt = 1
for i in range(1, N+1):
    for j in range(3):
        if medal[K][j] > medal[i][j]:
            break
        if medal[K][j] < medal[i][j]:
            cnt += 1
            break

print(cnt)