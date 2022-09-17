import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()

cnt = 0
for i in range(N):
    num = A[i]
    s, e = 0, N-1
    while s < e:
        result = A[s]+A[e]
        if i not in (s, e) and result == num:
            cnt += 1
            break
        
        if i == s or result < num:
            s += 1
        elif i == e or result > num:
            e -= 1
        
print(cnt)