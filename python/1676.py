N = int(input())

n = 1
for i in range(2, N+1):
    # 2와 5를 곱할 때만 끝 자리를 0으로 바꿀 수 있음
    if i%2 == 0 or i%5 == 0:
        n *= i

number = list(str(n))
number.reverse()

count = 0
for n in number:
    if n != '0':
        break
    count += 1

print(count)