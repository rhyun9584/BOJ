N = int(input())
A = [int(x) for x in input().split()]
long = [1] * N
for i in range(1, N):
    for j in range(i):
        if A[i] < A[j]:
            long[i] = max(long[i], long[j]+1)
        
print(max(long))