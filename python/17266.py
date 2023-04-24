import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
light = list(map(int, input().split()))

max_distance = 0
for i in range(1, M):
    max_distance = max(max_distance, light[i]-light[i-1])

max_distance = max(max_distance, (light[0])*2, (N-light[M-1])*2)

print(max_distance//2 + max_distance%2)