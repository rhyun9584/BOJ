import sys
input = sys.stdin.readline

H, W = map(int, input().split())
height = list(map(int, input().split()))

result = 0
for i in range(1, W-1):
    left = max(height[:i])
    right = max(height[i+1:])

    h = height[i]
    if h < left and h < right:
        result += min(left-h, right-h)

print(result)