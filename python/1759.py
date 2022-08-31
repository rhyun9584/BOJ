from itertools import combinations


L, C = map(int, input().split())
characters = input().split()

vowels = []
others = []
for c in characters:
    if c in ('a', 'e', 'i', 'o', 'u'):
        vowels.append(c)
    else:
        others.append(c)

result = set()
for i in range(max(1, L-len(others)), min(L-1, len(vowels)+1)):
    j = L - i

    for v in combinations(vowels, i):
        for o in combinations(others, j):
            using = sorted(v+o)
            for u in combinations(using, L):
                result.add(u)

result = sorted(list(result))
for r in result:
    print("".join(r))
