import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    nums = list(map(int, input().split()))

    for i in range(2, len(nums)):
        v = nums[i]
        indegree[v] += i-1

        for n in nums[1:i]:
            graph[n].append(v)

queue = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i)

result = []
while queue:
    v = queue.popleft()

    result.append(v)

    for g in graph[v]:
        indegree[g] -= 1
        if indegree[g] == 0:
            queue.append(g)

# 모든 가수의 순서를 정하지 못한 경우 0 출력
if len(result) == N:
    for r in result:
        print(r)
else:
    print(0)