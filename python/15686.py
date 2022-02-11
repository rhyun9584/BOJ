from itertools import combinations

N, M = [int(x) for x in input().split()]
city = [[int(x) for x in input().split()] for _ in range(N)]
store = []
home = []
for x in range(N):
    for y in range(N):
        if city[x][y] == 1:
            home.append((x, y))
        elif city[x][y] == 2:
            store.append((x, y))

def get_distance(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

min_distance = 2 * N * len(home)
for select in combinations(store, M):
    sum_distacne = 0
    for h in home:
        min_home = 2 * N
        for s in select:
            min_home = min(min_home, get_distance(s, h))

        sum_distacne += min_home

    min_distance = min(min_distance, sum_distacne)

print(min_distance)