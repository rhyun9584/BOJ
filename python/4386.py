import math

def get_dist(s1, s2):
    x1, y1 = s1
    x2, y2 = s2

    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

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

parent = [i for i in range(N)]

# 별 좌표
star = []
for _ in range(N):
    x, y = map(float, input().split())
    star.append((x, y))

# 각 별 간의 거리 계산
dist = []
for i in range(N):
    for j in range(i+1, N):
        d = get_dist(star[i], star[j])
        dist.append((d, i, j))
dist.sort()

count = 0
result = 0
for d, a, b in dist:
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        result += d
        count += 1

    if count == N-1:
        break

print(result)