A, B, C = map(int, input().split())

def pow(a, b, c):
    if b == 1:
        return a%C
    if b == 2:
        return (a**2)%C

    if b%2:
        return (a * (pow(a, (b-1)//2, c)**2)) % c
    else:
        return pow(a, b//2, c)**2 % c

print(pow(A, B, C))