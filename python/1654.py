import sys

K, N = map(int, input().split())
lines = list(map(int, sys.stdin.readlines()))
# lines = []
# for _ in range(K):
#     lines.append(int(input()))

start = 1
# end = max(lines)
end = sum(lines)//N

result = 0
while start <= end:
    mid = (start+end)//2
    count = sum([x//mid for x in lines])

    if count < N:
        end = mid-1
    else:
        result = mid
        start = mid+1

print(result)