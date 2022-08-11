N = int(input())
arr = list(map(int, input().split()))

dp = [[arr[i]] for i in range(N)]

idx = 0
length = 1
for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i] and len(dp[j])+1 > len(dp[i]):
            dp[i] = dp[j] + [arr[i]]
            if len(dp[i]) > length:
                length = len(dp[i])
                idx = i

print(length)
print(" ".join(map(str, dp[idx])))
