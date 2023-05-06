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

G = int(input())
P = int(input())
gates = list(map(int, sys.stdin.readlines()))

answer = 0
parent = [i for i in range(G+1)]
for g_i in gates:
    gate_idx = find_parent(parent, g_i)
    
    if gate_idx > 0:
        answer += 1
        union(parent, gate_idx, gate_idx-1)
    else:
        break

print(answer)