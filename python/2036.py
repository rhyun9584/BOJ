import sys
input = sys.stdin.readline

N = int(input())

plus, minus = [], []
plus_cnt, minus_cnt, one_cnt = 0, 0, 0
zero = False
for _ in range(N):
    num = int(input())
    if num == 0:
        zero = True
    elif num == 1:
        one_cnt += 1
    elif num > 0:
        plus.append(num)
        plus_cnt += 1
    else: 
        minus.append(num)
        minus_cnt += 1

answer = one_cnt

plus.sort()
if plus_cnt % 2 == 1:
    answer += plus[0]
for i in range(plus_cnt%2, plus_cnt, 2):
    answer += plus[i] * plus[i+1]

minus.sort(reverse=True)
if minus_cnt % 2 == 1 and not zero:
    answer += minus[0]
for i in range(minus_cnt%2, minus_cnt, 2):
    answer += minus[i] * minus[i+1]

print(answer)