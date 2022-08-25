from itertools import combinations


N, M = map(int, input().split())

for arr in combinations(range(1, N+1), M):
    print(" ".join(map(str, arr)))