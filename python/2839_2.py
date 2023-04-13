N = int(input())

dp = [-1] * (N+1)
dp[0] = 0
dp[3] = 1
for i in range(5, N+1):
    result = []
    if dp[i-3] != -1:
        result.append(dp[i-3]+1)
    
    if dp[i-5] != -1:
        result.append(dp[i-5]+1)

    if result:
        dp[i] = min(result)

print(dp[N])