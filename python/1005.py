import heapq

for _ in range(int(input())):
    N, K = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    
    degree = [0] * (N+1)
    graph = [[] for _ in range(N+1)]
    for _ in range(K):
        a, b = map(int, input().split())
        graph[a].append(b)
        degree[b] += 1

    goal = int(input())

    queue = []
    for i in range(1, N+1):
        if degree[i] == 0:
            heapq.heappush(queue, (time[i], i))

    result = 0
    complete = [0] * (N+1)
    while queue:
        cost, i = heapq.heappop(queue)

        if i == goal:
            result = cost
            break

        if complete[i] == 1:
            continue

        complete[i] = 1

        for g in graph[i]:
            degree[g] -= 1
            if degree[g] == 0:
                heapq.heappush(queue, (cost+time[g], g))

    print(result)