from collections import deque

N, K = map(int, input().split())

before = [-1] * 100001
before[N] = N

queue = deque([N])
while queue:
    v = queue.popleft()

    if v == K:
        break

    for new_v in (v*2, v-1, v+1):
        if 0 <= new_v <= 100000 and before[new_v] == -1:
            before[new_v] = v
            queue.append(new_v)

result = [K]
while result[-1] != N:
    result.append(before[result[-1]])

print(len(result)-1)
print(" ".join(map(str, reversed(result))))