N = int(input())
count = [[0, 0] for _ in range(N+1)]
count[1] = [0, 1]
for i in range(2, N+1):
    count[i][0] = count[i-1][0] + count[i-1][1]
    count[i][1] = count[i-1][0]

print(sum(count[N]))