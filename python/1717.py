import sys
sys.setrecursionlimit(10**7)
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

for _ in range(M):
    op, a, b = map(int, input().split())

    # 0이라면 union, 1이라면 같은 집합인지 판별
    if op == 0:
        union(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print("yes")
        else:
            print("no")
