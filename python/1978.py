N = int(input())
numbers = list(map(int, input().split()))

maximum = max(numbers)
is_prime = [1] * (maximum+1)
is_prime[1] = 0 # 1은 소수가 아님
for i in range(2, maximum+1):
    if is_prime[i] == 1:
        j = 2
        while i*j <= maximum:
            is_prime[i*j] = 0
            j += 1

count = 0
for n in numbers:
    if is_prime[n] == 1: count += 1
print(count)