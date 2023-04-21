N = int(input())
P = list(map(int, input().split()))
M = int(input())

def dfs(num, total):
    global answer
    answer = max(answer, num)

    for i in range(N):
        if total + P[i] <= M:
            dfs(num*10+i, total+P[i])

answer = 0
for i in range(N):
    if P[i] <= M:
        dfs(i, P[i])

print(answer)