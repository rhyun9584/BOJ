import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

time = [0] * (N+1)
indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for i in range(1, N+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    indegree[i] = data[1]
    for d in data[2:]:
        graph[d].append(i)

queue = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i)

pre_time = [0] * (N+1)
while queue:
    n = queue.popleft()
    for g in graph[n]:
        indegree[g] -= 1
        pre_time[g] = max(pre_time[g], time[n])
        if indegree[g] == 0:
            time[g] += pre_time[g]
            queue.append(g)

print(max(time))