import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

_, K = map(int, input().split())
B = []
for _ in range(M):
    B.append(list(map(int, input().split())))

result = [[0] * K for _ in range(N)]
for i in range(N):
    for j in range(K):
        for k in range(M):
            result[i][j] += A[i][k] * B[k][j]

for i in range(N):
    print(" ".join(map(str, result[i])))