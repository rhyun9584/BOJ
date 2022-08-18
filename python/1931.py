N = int(input())

time = []
for _ in range(N):
    a, b = map(int, input().split())
    time.append((a, b))
time.sort(key=lambda x: (x[1], x[0]))

count = 0
last = 0
for t in time:
    if t[0] >= last:
        count += 1
        last = t[1]

print(count)