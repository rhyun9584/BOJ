from collections import deque


N, M = map(int, input().split())

known = deque(list(map(int, input().split()))[1:])
attendance = [[] for _ in range(N+1)]
party = [[] for _ in range(M+1)]
for i in range(1, M+1):
    arr = list(map(int, input().split()))[1:]
    for people in arr:
        attendance[people].append(i)
    party[i] = arr

if len(known) == 0:
    print(M)
else:
    checked = [0] * (N+1)
    checked[known[0]] = 1
    true_party = set()
    while known:
        n = known.popleft()
        true_party.update(attendance[n])
        for p in attendance[n]:
            for people in party[p]:
                if checked[people] == 0:
                    checked[people] = 1
                    known.append(people)

    print(M-len(true_party))
