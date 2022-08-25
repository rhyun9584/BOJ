from collections import deque

S = int(input())

queue = deque()
queue.append((1, 0))

dp = [[-1]*(S+1) for _ in range(S+1)]
dp[1][0] = 0
while queue:
    cnt, clip = queue.popleft()
    s = dp[cnt][clip]

    if cnt != clip and dp[cnt][cnt] == -1:
        dp[cnt][cnt] = s+1
        queue.append((cnt, cnt))
    if cnt+clip <= S and dp[cnt+clip][clip] == -1:
        dp[cnt+clip][clip] = s+1
        queue.append((cnt+clip, clip))
    if cnt-1 >= 0 and dp[cnt-1][clip] == -1:
        dp[cnt-1][clip] = s+1
        queue.append((cnt-1, clip))

minimum = int(1e9)
for i in range(S+1):
    if dp[S][i] != -1:
        minimum = min(minimum, dp[S][i])

print(minimum)