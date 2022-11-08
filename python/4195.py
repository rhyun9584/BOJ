import sys

def find_parent(x, parent):
    if x != parent[x]:
        parent[x] = find_parent(parent[x], parent)

    return parent[x]

def union(a, b, parent, cnt):
    pa = find_parent(a, parent)
    pb = find_parent(b, parent)

    if pa != pb:
        parent[pa] = pb
        cnt[pb] += cnt[pa]


for _ in range(int(input())):
    parent = dict()
    cnt = dict()
    for _ in range(int(input())):
        a, b = sys.stdin.readline().rstrip().split()

        # 처음 등장한 친구 init
        if a not in parent:
            parent[a] = a
            cnt[a] = 1
        if b not in parent:
            parent[b] = b
            cnt[b] = 1

        # union
        union(a, b, parent, cnt)

        print(cnt[find_parent(a, parent)])