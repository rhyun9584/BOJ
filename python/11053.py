N = int(input())
A = [int(x) for x in input().split()]

long = [1] * (N+1)
long[N-1] = 2 if A[N-2] < A[N-1] else 1

for i in range(N-1, 0, -1):
    for j in range(i+1, N+1):
        if A[i-1] < A[j-1]:
            long[i] = max(long[i], long[j]+1)
    
print(max(long))