import sys

N, M = map(int, input().split())
trees = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = max(trees)-1

result = 0
while start <= end:
    mid = (start+end)//2

    length = sum(list(map(lambda x: max(x-mid, 0), trees)))

    if length < M:
        end = mid-1
    else:
        start = mid+1
        result = mid

print(result)