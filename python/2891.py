N, S, R = map(int, input().split())
broken = list(map(int, input().split()))
more = list(map(int, input().split()))

kayak = [1 for _ in range(N+1)]
for b in broken:
    kayak[b] -= 1
for m in more:
    kayak[m] += 1

answer = 0
for i in range(1, N+1):
    if kayak[i] == 0:
        for j in [i-1, i+1]:
            if 1 <= j <= N and kayak[j] > 1:
                kayak[j] -= 1
                kayak[i] += 1
                break

        if kayak[i] == 0:
            answer += 1

print(answer)