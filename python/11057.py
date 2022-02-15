N = int(input())
upper = [[0 for _ in range(10)] for _ in range(N+1)]
upper[1] = [1] * 10
for i in range(2, N+1):
    for j in range(10):
        for k in range(9, j-1, -1):
            upper[i][k] += upper[i-1][j]

print(sum(upper[N])%10007)