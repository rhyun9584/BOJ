N = int(input())
stair = [int(input()) for _ in range(N)]
sum_stair = [0] * (N+1)
sum_stair[1] = stair[0]
for i in range(2, N+1):
    if i == 2: sum_stair[i] = sum_stair[i-1] + stair[i-1]
    else:
        sum_stair[i] = max(sum_stair[i-2]+stair[i-1], sum_stair[i-3]+stair[i-2]+stair[i-1])

print(sum_stair[N])