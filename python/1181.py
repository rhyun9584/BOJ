import sys
input = sys.stdin.readline

N = int(input())

words = [set() for _ in range(51)]
for _ in range(N):
    w = input().rstrip()
    words[len(w)].add(w)

for i in range(1, 51):
    for w in sorted(words[i]):
        print(w)
