import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    stock = list(map(int, input().split()))

    sell = stock[-1]
    answer = 0
    for s in reversed(stock[:-1]):
        if s < sell:
            answer += sell-s
        else:
            sell = s

    print(answer)