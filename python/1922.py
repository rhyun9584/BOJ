import sys
input = sys.stdin.readline

# union-find
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
M = int(input())

parent = [i for i in range(N+1)]

lines = []
for _ in range(M):
    a, b, c = map(int, input().split())
    lines.append((c, a, b))

lines.sort()

result = 0
count = 0
for i in range(M):
    c, a, b = lines[i]

    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        result += c
        count += 1

    # edge N-1개를 선택하면 tree가 완성되므로 종료 가능
    if count == N-1:
        break

print(result)