import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    paper = input().rstrip()
    N = len(paper)

    result = True
    mid = N//2
    while mid > 0:
        for i in range(1, mid+1):
            if paper[mid+i] == paper[mid-i]:
                result = False
                break

        if not result:
            break

        mid //= 2

    if result: print("YES")
    else: print("NO")
