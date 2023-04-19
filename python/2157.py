import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

edges = [[] for _ in range(N+1)]
for _ in range(K):
    a, b, c = map(int, input().split())
    
    # 동쪽에서 서쪽으로 이동하는 경우만 체크
    if a < b:
        # b로 이동할 수 있는 위치와 기내식 기록
        edges[b].append((a, c))

dp = [[-1] * M for _ in range(N+1)]
dp[1][0] = 0

for i in range(2, N+1):
    for a, c in edges[i]:
        for j in range(1, M):
            if dp[a][j-1] >= 0:
                dp[i][j] = max(dp[i][j], dp[a][j-1]+c)
    
print(max(dp[N]))