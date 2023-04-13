import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())

parent = [i for i in range(N+1)]

path = []
for _ in range(M):
    a, b, c = map(int, input().split())
    path.append((c, a, b))

path.sort()

result = 0
cnt = 0
for i in range(M):
    c, a, b = path[i]

    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        result += c
        cnt += 1

    if cnt == N-2:
        break

print(result)
