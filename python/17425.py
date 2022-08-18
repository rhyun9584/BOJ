import sys

_ = input()
number = list(map(int, sys.stdin.readlines()))

n = max(number)

dp = [0] * (n+1)
for i in range(1, n+1):
    j = 1
    while i*j <= n:
        dp[i*j] += i
        j += 1
        
result = [0] * (n+1)
for i in range(1, n+1):
    result[i] = result[i-1] + dp[i]

for i in number:
    print(result[i])