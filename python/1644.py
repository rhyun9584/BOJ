N = int(input())

arr = [True] * (N+1)
primes = []
prime_cnt = 0
for i in range(2, N+1):
    if not arr[i]:
        continue

    primes.append(i)
    prime_cnt += 1

    j = i**2
    while j <= N:
        arr[j] = False
        j += i

S = [0]
for i in range(prime_cnt):
    S.append(S[i] + primes[i])

answer = 0
s, e = 0, 1
while e <= prime_cnt:
    total = S[e] - S[s]

    if total == N:
        answer += 1

    if total > N:
        s += 1
    else:
        e += 1

print(answer)