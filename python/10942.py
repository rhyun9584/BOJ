import sys
input = sys.stdin.readline

N = int(input())
n = [0] + list(map(int, input().split()))

# dp[s][e] -> s번째에서 e번째까지 펠린드롬? yes:1, no:0
dp = [[1] * (N+1) for _ in range(N+1)]
for i in range(1, N):
    for j in range(1, N+1-i):
        if dp[j+1][j+i-1] == 0 or n[j] != n[j+i]:
            dp[j][j+i] = 0

for _ in range(int(input())):
    S, E = map(int, input().split())
    print(dp[S][E])
