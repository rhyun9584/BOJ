import sys
input = sys.stdin.readline

N = int(input())

words = []
weights = dict()
for _ in range(N):
    word = input().rstrip()
    words.append(word)

    length = len(word)
    for i in range(length):
        ch = word[i]
        w = 10 ** (length-i-1)
        if ch not in weights:
            weights[ch] = w
        else:
            weights[ch] += w

answer = 0
i = 9
for weight in sorted(weights.values(), reverse=True):
    answer += weight * i
    i -= 1

print(answer)
