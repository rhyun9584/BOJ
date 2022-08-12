N = int(input())
jump = list(map(int, input().split()))

dp = [int(1e9)] * N
dp[0] = 0
for i in range(N):
    for j in range(1, jump[i]+1):
        if i+j < N:
            dp[i+j] = min(dp[i+j], dp[i]+1)

print(dp[N-1] if dp[N-1] < int(1e9) else -1)