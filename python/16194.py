N = int(input())
P = [0] + list(map(int, input().split()))

price = [0] * (N+1)
price[1] = P[1]
for i in range(1, N+1):
    price[i] = P[i]
    for j in range(i-1, i//2-1, -1):
        price[i] = min(price[i], price[j]+price[i-j])

print(price[N])