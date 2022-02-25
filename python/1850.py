import sys

A, B = map(int, sys.stdin.readline().split())

def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a%b)

print('1'*GCD(A,B))