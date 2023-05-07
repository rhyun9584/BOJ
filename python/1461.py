import sys
input = sys.stdin.readline

N, M = map(int, input().split())
books = list(map(int, input().split()))

plus, minus = [], []
for book in books:
    if book > 0:
        plus.append(book)
    else:
        minus.append(book)
plus.sort(reverse=True)
minus.sort()

answer = 0

i = 0
while i < len(plus):
    answer += plus[i]*2
    i += M

i = 0
while i < len(minus):
    answer -= minus[i]*2
    i += M

if not plus:
    answer += min(minus)
elif not minus:
    answer -= max(plus)
else:
    answer -= max(-min(minus), max(plus))

print(answer)