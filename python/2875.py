N, M, K = map(int, input().split())

i = (N+M-K) // 3
while i > 0:
    if 2*i <= N and i <= M:
        break

    i -= 1

print(i)