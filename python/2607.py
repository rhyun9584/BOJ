import sys
import copy
input = sys.stdin.readline

N = int(input())
first = list(input().rstrip())
answer = 0
for _ in range(N-1):
    word = input().rstrip()

    target = copy.deepcopy(first)
    add = 0
    for w in word:
        if w in target:
            target.remove(w)
        else:
            add += 1

    if len(target) <= 1 and add <= 1:
        answer += 1

print(answer)