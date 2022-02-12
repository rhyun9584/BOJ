import sys
sys.setrecursionlimit(10**5)

N, L, R = [int(x) for x in input().split()]
population = [[int(x) for x in input().split()] for _ in range(N)]
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def build_unite(start, check, unite):
    unite.append(start)
    check.remove(start)
    for (x, y) in direction:
        move = (start[0]+x, start[1]+y)
        if move in check and 0 <= move[0] < N and 0 <= move[1] < N:
            sub = abs(population[start[0]][start[1]] - population[move[0]][move[1]])
            if L <= sub <= R:
                build_unite(move, check, unite)

    return unite

time = 0
while True:
    check = [(x, y) for x in range(N) for y in range(N)]
    unite_list = []
    while len(check) > 0:
        seed = check[0]
        unite = build_unite(seed, check, [])
        if len(unite) > 1:
            unite_list.append(unite)

    if len(unite_list) == 0:
        break
    else:
        for unite in unite_list:
            sum = 0
            for unit in unite:
                sum += population[unit[0]][unit[1]]
            popluar = int(sum/len(unite))
            for unit in unite:
                population[unit[0]][unit[1]] = popluar

    time += 1

print(time)