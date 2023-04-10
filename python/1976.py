import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if x != parent[x]:
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

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# 여행 계획의 중복 제거 
road = list(set(map(int, input().split())))

parent = [i for i in range(N)]
for i in range(N):
    for j in range(i+1, N):
        if graph[i][j] == 1:
            union(parent, i, j)

result = "YES"
for i in range(len(road)-1):
    if find_parent(parent, road[i]-1) != find_parent(parent, road[i+1]-1):
        result = "NO"
        break

print(result)