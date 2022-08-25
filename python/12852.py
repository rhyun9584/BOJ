from collections import deque

N = int(input())
queue = deque([N])
before = [-1] * (N+1)
while queue:
    v = queue.popleft()

    if v == 1:
        break

    if v%3 == 0 and before[v//3] == -1:
        before[v//3] = v
        queue.append(v//3)
    if v%2 == 0 and before[v//2] == -1:
        before[v//2] = v
        queue.append(v//2)
    if v-1 > 0 and before[v-1] == -1:
        before[v-1] = v
        queue.append(v-1)

cnt = 0
result = []
next = 1
while next != N:
    cnt += 1
    result.append(next)
    next = before[next]

result += [N]
result.reverse()

print(cnt)
print(" ".join(map(str, result)))
