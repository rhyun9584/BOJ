import sys

N, C = map(int, input().split())
home = list(map(int, sys.stdin.readlines()))
home.sort()

start = 1
end = home[-1] - home[0]

result = 0
while start <= end:
    # 최소거리
    mid = (start+end)//2
    current = home[0]
    count = 1

    for i in range(1, N):
        if home[i] >= current+mid:
            count += 1
            current = home[i]
        
    # 목표 갯수 이상으로 설치됨 -> 최소거리를 늘려봄
    if count >= C:
        result = mid
        start = mid+1
    # 목표 갯수보다 적게 설치됨 -> 최소거리를 줄여봄
    else:
        end = mid-1

print(result)