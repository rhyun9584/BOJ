E, S, M = map(int, input().split())

y = S
while True:
    if (y-1)%15+1 == E and (y-1)%19+1 == M:
        break

    y += 28

print(y)