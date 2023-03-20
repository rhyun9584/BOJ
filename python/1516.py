import sys
import copy
from collections import deque
input = sys.stdin.readline

N = int(input())

indgree = [0] * (N+1)
time = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for i in range(1, N+1):
    nums = list(map(int, input().split()))

    time[i] = nums[0]
    
    for n in nums[1:-1]:
        graph[n].append(i)
        indgree[i] += 1

queue = deque()
for i in range(1, N+1):
    if indgree[i] == 0:
        queue.append(i)

result = copy.deepcopy(time)
while queue:
    v = queue.popleft()

    for g in graph[v]:
        indgree[g] -= 1
        # "앞서 지어져야할 건물까지 걸리는 시간 + 해당 건물을 짓는 시간" 중
        # 가장 큰 값이 해당 건물을 짓는데 걸리는 시간 
        result[g] = max(result[g], result[v]+time[g])
        
        if indgree[g] == 0:
            queue.append(g)

for r in result[1:]:
    print(r)