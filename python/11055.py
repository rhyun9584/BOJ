import copy

N = int(input())
A = [int(x) for x in input().split()]
sum = copy.deepcopy(A)
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            sum[i] = max(sum[i], sum[j]+A[i])

print(max(sum))