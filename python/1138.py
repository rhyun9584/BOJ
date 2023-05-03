N = int(input())
taller = list(map(int, input().split()))

line = [0] * N
for i in range(N):
    cnt = taller[i]
    for j in range(N):
        if line[j] == 0:
            if cnt > 0:
                cnt -= 1
            else:
                line[j] = i+1
                break

print(" ".join(map(str, line)))
