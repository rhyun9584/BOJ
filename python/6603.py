from itertools import combinations

while True:
    S = list(map(int, input().split()))
    if S[0] == 0:
        break

    for arr in combinations(S[1:], 6):
        print(" ".join(map(str, arr)))

    print()
