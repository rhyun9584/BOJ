import sys

input = sys.stdin.readline

N, M = map(int, input().split())

count = dict()
for _ in range(N):
    word = input().rstrip()
    
    if len(word) < M:
        continue

    if word in count:
        count[word] += 1
    else:
        count[word] = 1

words = list(count.keys())
words.sort()
words.sort(key=len, reverse=True)
words.sort(key=count.get, reverse=True)

print("\n".join(words))