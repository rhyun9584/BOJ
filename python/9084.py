for _ in range(int(input())):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    dp = [1] + [0] * M
    for c in coins:
        for i in range(c, M+1):
            dp[i] += dp[i-c]

    print(dp[M])