import sys

S = list(sys.stdin.readline().rstrip())
length = len(S)
suffix = []
for i in range(length):
    suffix.append("".join(S[i:]))
    
suffix.sort()
for i in range(length):
    print(suffix[i])
