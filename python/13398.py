n = int(input())
number = [0] + list(map(int, input().split()))

dp = [[0, 0] for _ in range(n+1)]
dp[1] = [number[1]] * 2
for i in range(2, n+1):
    dp[i][0] = max(dp[i-1][0]+number[i], number[i])
    dp[i][1] = max(dp[i-2][0], dp[i-1][1]) + number[i]

print(max(map(max, dp[1:])))