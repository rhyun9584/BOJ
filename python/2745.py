import sys

N, B = sys.stdin.readline().split()
N = reversed(list(N))
B = int(B)
num = 0
b = 1
for n in N:
    if '0' <= n <= '9':
        num += int(n) * b
    else:
        num += int(ord(n)-ord('A')+10) * b
    b *= B

print(num)