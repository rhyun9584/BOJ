import sys
input = sys.stdin.readline

N = int(input())
d1, d2 = map(int, input().split())
M = int(input())

def dfs(i, arr, door1, door2, total):
    global answer
    if i == M:
        answer = min(answer, total)
        return
    
    dfs(i+1, arr, arr[i], door2, total+abs(arr[i]-door1))
    dfs(i+1, arr, door1, arr[i], total+abs(arr[i]-door2))

arr = []
for _ in range(M):
    arr.append(int(input()))

answer = int(1e9)
dfs(0, arr, d1, d2, 0)

print(answer)