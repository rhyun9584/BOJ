import sys

N = int(input())
if N == 0:
    print(0)
    sys.exit()

result = ''
while N != 1:
    result = str(N%2) + result
    N = (N - N%2) // -2

result = str(N) + result
print(result)