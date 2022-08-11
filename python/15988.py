import sys

_ = input()
number = list(map(int, sys.stdin.readlines()))

n = max(number)
dp = [0] * max(3, n+1)
dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3, n+1):
    dp[i] = sum(dp[i-3:i]) % 1000000009

for n in number:
    print(dp[n])