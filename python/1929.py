M, N = map(int, input().split())

is_prime = [1] * (N+1)
is_prime[1] = 0
for i in range(2, N+1):
    if is_prime[i] == 1:
        j = 2
        while i*j <= N:
            is_prime[i*j] = 0
            j += 1

for i in range(M, N+1):
    if is_prime[i] == 1: print(i)