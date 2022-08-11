import sys
MAX = 1000000009

T = int(input())
number = list(map(int, sys.stdin.readlines()))

maximum = max(number)
dp = [[0] * 3 for _ in range(max(maximum, 3)+1)]
dp[0] = [1, 1, 1]
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

for i in range(4, maximum+1):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % MAX
    dp[i][1] = (dp[i-2][0] + dp[i-2][2]) % MAX
    dp[i][2] = (dp[i-3][0] + dp[i-3][1]) % MAX

for n in number:
    print(sum(dp[n]) % MAX)