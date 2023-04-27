import sys
input = sys.stdin.readline

N = int(input())

road = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = int(1e9)
answer = 0
for i in range(N-1):
    min_price = min(min_price, price[i])

    answer += min_price * road[i]

print(answer)