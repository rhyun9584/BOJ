import sys
import string

N, B = map(int, sys.stdin.readline().split())
arr = list(string.digits + string.ascii_uppercase)
change = []
while N > 0:
    mod = N % B
    change.append(arr[mod])
    N //= B

change.reverse()
print("".join(change))