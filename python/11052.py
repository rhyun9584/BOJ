import copy

N = int(input())
P = [int(x) for x in input().split()]
pay = [0] + copy.deepcopy(P)
for n in range(2, N+1):
    for j in range(1, n//2+1):
        pay[n] = max(pay[n], pay[n-j]+P[j-1])

print(pay[N])