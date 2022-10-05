import sys
input = sys.stdin.readline

N = int(input())
matrix = [(0,0)] + [tuple(map(int, input().split())) for _ in range(N)]

dp = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N):
    for j in range(1, N-i+1):
        dp[j][j+i] = min([dp[j][k] + dp[k+1][j+i] + (matrix[j][0]*matrix[k][1]*matrix[j+i][1]) for k in range(j, j+i)])

print(dp[1][N])