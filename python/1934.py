import sys

T = int(sys.stdin.readline())

def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a%b)

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(a * b // GCD(a, b))