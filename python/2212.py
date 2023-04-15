import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

sensor = list(map(int, input().split()))
sensor.sort()

diff = []
for i in range(1, N):
    diff.append(sensor[i]-sensor[i-1])

diff.sort(reverse=True)
print(sum(diff[K-1:]))
