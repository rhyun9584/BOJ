import sys
input = sys.stdin.readline

N, K = map(int, input().split())

temp = list(map(int, input().split()))

S = [0]
for i in range(N):
    S.append(S[i] + temp[i])

result = -100*N
for i in range(K, N+1):
    result = max(result, S[i]-S[i-K])

print(result)