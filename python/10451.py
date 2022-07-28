T = int(input())

def bfs(start, visited, arr):
    visited[start] = 1
    
    next = start
    while True:
        next = arr[next]
        if visited[next] == 1:
            break
        else:
            visited[next] = 1


for _ in range(T):
    N = int(input())
    arr = [0] + list(map(int, input().split()))

    count = 0
    visited = [0] * (N+1)
    for i in range(1, N+1):
        if visited[i] == 0:
            bfs(i, visited, arr)
            count += 1

    print(count)