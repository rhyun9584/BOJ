import sys
input = sys.stdin.readline

def chr_to_digit(ch):
    if ch == '0':
        return 0
    
    ord_ch = ord(ch)
    if ord_ch in range(ord('a'), ord('z')+1):
        return ord_ch - ord('a') + 1
    else:
        return ord_ch - ord('A') + 27

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

N = int(input())

edges = []
total = 0
for i in range(N):
    arr = list(map(chr_to_digit, input().rstrip()))
    
    for j in range(N):
        if arr[j] == 0:
            continue
        
        if i != j:
            edges.append((arr[j], i, j))

        total += arr[j]
        
edges.sort()

link = 0
parent = [i for i in range(N)]
for cost, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        link += 1
        total -= cost
        union(parent, a, b)

if link == N-1:
    print(total)
else:
    print(-1)