N = int(input())

number = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N)]
dp[0] = number[0]

for i in range(1, N):
    dp[i][0] = max(dp[i-1][0], dp[i-1][1]) + number[i][0]
    dp[i][1] = max(dp[i-1]) + number[i][1]
    dp[i][2] = max(dp[i-1][1], dp[i-1][2]) + number[i][2]        
maximum = max(dp[N-1])

for i in range(1, N):
    dp[i][0] = min(dp[i-1][0], dp[i-1][1]) + number[i][0]
    dp[i][1] = min(dp[i-1]) + number[i][1]
    dp[i][2] = min(dp[i-1][1], dp[i-1][2]) + number[i][2]        
minimum = min(dp[N-1])    

print(maximum, minimum)