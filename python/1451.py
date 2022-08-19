N, M = map(int, input().split())

number = [list(map(int, input())) for _ in range(N)]
s = [[0] * M for _ in range(N)]
s[0][0] = number[0][0]

for i in range(1, N):
    s[i][0] = s[i-1][0] + number[i][0]

for i in range(1, M):
    s[0][i] = s[0][i-1] + number[0][i]

for i in range(1, N):
    for j in range(1, M):
        s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + number[i][j]

result = 0
if N >= 3:
    for i in range(N-2):
        for j in range(i+1, N-1):
            result = max(result, s[i][M-1]*(s[j][M-1]-s[i][M-1])*(s[N-1][M-1]-s[j][M-1]))

if M >= 3:
    for i in range(M-2):
        for j in range(i+1, M-1):
            result = max(result, s[N-1][i]*(s[N-1][j]-s[N-1][i])*(s[N-1][M-1]-s[N-1][j]))

if N >= 2:
    for i in range(N-1):
        for j in range(M-1):
            result = max(result, s[N-1][j]*(s[i][M-1]-s[i][j])*(s[N-1][M-1]-s[i][M-1]-s[N-1][j]+s[i][j]))
            result = max(result, s[i][j]*(s[N-1][j]-s[i][j])*(s[N-1][M-1]-s[N-1][j]))

if M >= 2:
    for i in range(N-1):
        for j in range(M-1):
            result = max(result, s[i][j]*(s[i][M-1]-s[i][j])*(s[N-1][M-1]-s[i][M-1]))
            result = max(result, s[i][M-1]*(s[N-1][j]-s[i][j])*(s[N-1][M-1]-s[i][M-1]-s[N-1][j]+s[i][j]))

print(result)