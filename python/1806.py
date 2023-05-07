import sys
input = sys.stdin.readline

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

arr = [0]
for i in range(N):
    arr.append(arr[i] + numbers[i])

if arr[N] < S:
    print(0)
elif arr[N] == S:
    print(N)
else:
    answer = int(1e9)
    s, e = 0, 1
    while e <= N:
        if S <= arr[e]-arr[s]:
            answer = min(answer, (e-s))
            s += 1
        else:
            e += 1

    print(answer)
