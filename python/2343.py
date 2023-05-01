import sys
input = sys.stdin.readline

N, M = map(int, input().split())
minutes = list(map(int, input().split()))

start = max(minutes)
end = int(1e9)

answer = 0
while start <= end:
    # 강의의 최대 길이
    mid = (start+end)//2

    cnt = 1
    sum = 0
    for m in minutes:
        if sum + m <= mid:
            sum += m
        else:
            cnt += 1
            sum = m

    if cnt <= M:
        answer = mid
        end = mid-1
    else:
        start = mid+1
print(answer)