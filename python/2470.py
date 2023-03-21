import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
arr.sort()

start = 0
end = N-1

value = 2000000001
result = []
while start < end:
    v = arr[end] + arr[start]
    abs_v = abs(v)

    if abs_v < value:
        value = abs_v
        result = (arr[start], arr[end])

    if v == 0:
        break
    
    if v < 0:
        start += 1
    else:
        end -= 1

print(" ".join(map(str, result)))