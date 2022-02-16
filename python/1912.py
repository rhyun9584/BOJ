import copy

n = int(input())
A = [int(x) for x in input().split()]
sum = copy.deepcopy(A)

for i in range(1, n):
    sum[i] = max(sum[i], sum[i]+sum[i-1])

print(max(sum))