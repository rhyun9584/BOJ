import sys

n1, n2 = [int(x) for x in sys.stdin.readline().split()]

def GCD(A, B):
    if B == 0:
        return A
    return GCD(B, A%B)

gcd = GCD(n1, n2) if n1 > n2 else GCD(n2, n1)
lcm = n1 * n2 // gcd

print(gcd)
print(lcm)