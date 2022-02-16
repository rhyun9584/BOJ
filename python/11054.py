N = int(input())
A = [int(x) for x in input().split()]
left = [1] * N
right = [1] * N
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            left[i] = max(left[i], left[j]+1)
for i in range(N-2, -1, -1):
    for j in range(i+1, N):
        if A[i] > A[j]:
            right[i] = max(right[i], right[j]+1)

sum = [x+y for (x,y) in zip(left,right)]
print(max(sum)-1)