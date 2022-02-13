N = int(input())
min_op = [0] * (N+1)
min_op[1] = 0

for i in range(2, N+1):
    min_op[i] = min_op[i-1] + 1
    if i % 3 == 0:
        min_op[i] = min(min_op[i], min_op[i//3]+1)
    if i % 2 == 0:
        min_op[i] = min(min_op[i], min_op[i//2]+1)

print(min_op[N])