import sys
input = sys.stdin.readline

P = int(input())

result = []
for p in range(P):
    arr = list(map(int, input().split()))[1:]

    ordered = []
    cnt = 0
    for i in range(20):
        idx = i
        for j in range(i-1, -1, -1):
            if arr[i] > ordered[j]:
                break

            idx -= 1
            cnt += 1

        ordered.insert(idx, arr[i])

    print(p+1, cnt)