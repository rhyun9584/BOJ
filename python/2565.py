N = int(input())

lines = []
for _ in range(N):
    a, b = map(int, input().split())
    lines.append((a, b))
lines.sort()

dp = [1] * (N+1)
for i in range(2, N+1):
    for j in range(1, i):
        if lines[j-1][1] < lines[i-1][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(N-max(dp))