import sys
input = sys.stdin.readline

N = int(input())

queue = []
for _ in range(N):
    queue.append(int(input()))

queue.sort()
for i in range(N):
    print(queue[i])