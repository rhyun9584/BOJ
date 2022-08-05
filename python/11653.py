N = int(input())

m = 2
while N > 1:
    while N%m == 0:
        print(m)
        N //= m
    m += 1