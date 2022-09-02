from itertools import combinations

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

result = 0
for i in range(1, N+1):
    for arr in combinations(numbers, i):
        if sum(arr) == S:
            result += 1

print(result)