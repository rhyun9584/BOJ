N = int(input())

if N % 2 == 1:
    print(0)
else:
    ways = [0] * (N//2+1)
    ways[0] = 1
    for i in range(1, N//2+1):
        ways[i] = ways[i-1] * 3
        for j in range(i-1):
            ways[i] += (ways[j] * 2)
    
    print(ways[N//2])