import sys

S = sys.stdin.readline().rstrip()
count = ['0'] * (ord('z')-ord('a')+1)
a = ord('a')
for ch in S:
    idx = ord(ch)-a
    count[idx] = str(1 + int(count[idx]))

print(" ".join(count))