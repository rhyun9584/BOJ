N = int(input())

plus, minus = [], []
zero = False
for _ in range(N):
    a = int(input())
    if a > 0:
        plus.append(a)
    elif a < 0:
        minus.append(a)
    else:
        zero = True
plus.sort(reverse=True)
minus.sort()

result = 0
# 양수는 큰 순서대로 묶어서 더하기
# 만약 묶는 수에 1이 있다면 묶지말고 더하는 것이 이득
for i in range(0, len(plus)-1, 2):
    if plus[i] != 1 and plus[i+1] != 1:
        result += plus[i]*plus[i+1]
    else:
        result += plus[i]+plus[i+1]

# 양수가 홀수인 경우 마지막 수도 빼놓지 말고 더해준다
if len(plus)%2 == 1:
    result += plus[-1]

# 음수는 큰 순서대로 묶어서 더한다
for i in range(0, len(minus)-1, 2):
    result += minus[i]*minus[i+1]

# 음수가 홀수이면서 0이 있는 경우, 0과 묶어 0으로 만든다.
if len(minus)%2 == 1:
    if zero: pass
    else:
        result += minus[-1]

print(result)