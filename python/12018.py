import sys
input = sys.stdin.readline

N, M = map(int, input().split())

subject = []
for _ in range(N):
    P, L = map(int, input().split())
    mile = list(map(int, input().split()))

    if P < L:
        subject.append(1)
    else:
        mile.sort(reverse=True)
        subject.append(mile[L-1])

subject.sort()

answer = 0
total = 0
while answer < N and total < M:
    if total + subject[answer] > M:
        break

    total += subject[answer]
    answer += 1

print(answer)