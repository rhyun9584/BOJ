from itertools import permutations


N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

answer = int(1e9)
for arr in permutations(range(N), N):
    arr = list(arr)+[arr[0]]
    result = 0

    for i in range(N):
        if graph[arr[i]][arr[i+1]] == 0:
            result = 0
            break
        result += graph[arr[i]][arr[i+1]]

        if result >= answer:
            result = 0
            break

    if result > 0:
        answer = min(answer, result)

print(answer)