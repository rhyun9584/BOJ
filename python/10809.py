import sys

S = sys.stdin.readline().rstrip()
atoz = list(range(ord('a'), ord('z')+1))
for x in atoz:
    print(S.find(chr(x)), end=' ')