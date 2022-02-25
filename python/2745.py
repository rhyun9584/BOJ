import sys
import string

N, B = sys.stdin.readline().split()
N = reversed(list(N))
B = int(B)
arr = list(string.digits + string.ascii_uppercase)
num = 0
b = 1
for n in N:
    num += arr.index(n) * b
    b *= B

print(num)