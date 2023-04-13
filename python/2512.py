import sys
input = sys.stdin.readline

N = int(input())
offer = list(map(int, input().split()))
maximum = int(input())

start = maximum//N
end = max(offer)

result = 0
while start <= end:
    mid = (start+end)//2

    total = 0
    for o in offer:
        total += min(o, mid)
    
    if total > maximum:
        end = mid-1
    else:
        result = mid
        start = mid+1

print(result)