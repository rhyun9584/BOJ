import sys
import copy
input = sys.stdin.readline

def check(start, end, N):
    cnt = 0
    for i in range(1, N):
        if start[i-1] != end[i-1]:
            cnt += 1
            for j in [i-1, i, i+1]:
                if j < N:
                    start[j] = 1 - start[j]
    
    if start[N-1] != end[N-1]:
        cnt = -1

    return cnt

N = int(input())
before = list(map(int, input().rstrip()))
after = list(map(int, input().rstrip()))

# 첫 버튼 누르지않고
answer = check(copy.deepcopy(before), after, N)

if answer == -1:
# 첫 버튼 누르고
    before[0] = 1 - before[0]
    before[1] = 1 - before[1]
    answer = check(before, after, N) + 1

    if answer == 0:
        answer = -1

print(answer)