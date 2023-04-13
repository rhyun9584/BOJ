import sys
input = sys.stdin.readline

N, M = map(int, input().split())

people = set()
for _ in range(N):
    p = input().rstrip()
    people.add(p)

answer = []
for _ in range(M):
    p = input().rstrip()
    if p in people:
        answer.append(p)

print(len(answer))
for p in sorted(answer):
    print(p)