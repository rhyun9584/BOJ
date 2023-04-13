import sys
input = sys.stdin.readline

N, M = map(int, input().split())
heights = list(map(int, input().split()))

start = 0
end = max(heights)-1

result = 0
while start <= end:
    mid = (start+end) // 2

    total = 0
    for h in heights:
        total += max(0, h-mid)
    
    if total < M:
        end = mid - 1
    else:
        start = mid + 1
        result = mid

print(result)