from collections import deque

N = int(input())

tree = [[] for _ in range(N+1)]
parent = [0 for _ in range(N+1)]

# 트리 구조 생성
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

queue = deque([1])
while queue:
    v = queue.popleft()
    for i in tree[v]:
        if parent[i] == 0:
            parent[i] = v
            queue.append(i)

for i in range(2, N+1):
    print(parent[i])