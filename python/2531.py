import sys

N, d, k, c = map(int, input().split())
sushi = list(map(int, sys.stdin.readlines()))
sushi += sushi[:k]

answer = 0
for left in range(N):
    right = left + k
    check = set(sushi[left:right])

    result = len(check)
    if c not in check:
        result += 1
    
    answer = max(answer, result)
    if answer == k+1:
        break

print(answer)