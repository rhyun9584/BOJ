import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())

edges = []
for _ in range(M):
    a, b, cost = map(int, sys.stdin.readline().split())
    edges.append((cost, a, b))
edges.sort()

total_cost = 0
last_cost = 0
parent = [i for i in range(N+1)]
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total_cost += cost
        last_cost = cost

print(total_cost - last_cost)