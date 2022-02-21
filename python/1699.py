N = int(input())
minimum  = [x for x in range(N+1)]
for i in range(1, N+1):
    root = int(i**0.5)
    for j in range(1, root+1):
        if minimum[i] > minimum[i-(j*j)]+1:
            minimum[i] = minimum[i-(j*j)] + 1

print(minimum[N])