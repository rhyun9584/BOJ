import sys
input = sys.stdin.readline

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

V, E = map(int, input().split())
edges = []
for _ in range(E):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()

n = V-1
total = 0
parent = [i for i in range(V+1)]
for e in edges:
    cost, a, b = e
    if find_parent(parent, a) != find_parent(parent, b):
        total += cost
        union_parent(parent, a, b)

        n -= 1
        if n == 0: break

print(total)