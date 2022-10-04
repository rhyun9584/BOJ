import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    S = [0] + list(map(int, input().split()))

    # 누적합
    for i in range(2, N+1):
        S[i] += S[i-1]

    # dp[i][j] -> i~j 합칠 때 최소비용
    dp = [[0] * (N+1) for _ in range(N+1)]
    for i in range(1, N):
        for j in range(1, N-i+1):
            dp[j][j+i] = min([dp[j][k]+dp[k+1][j+i] for k in range(j, j+i)]) + S[j+i] - S[j-1]

    print(dp[1][N])