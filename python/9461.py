T = int(input())
N = [int(input()) for _ in range(T)]

P = [0] * (max(N + [4])+1)
P[1:5] = [1, 1, 1, 2]
for i in range(5, max(N)+1):
    P[i] = P[i-1] + P[i-5]

for n in N:
    print(P[n])