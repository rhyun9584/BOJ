import sys
input = sys.stdin.readline

text = input().rstrip()
word = input().rstrip()
n = len(word)

i = 0
cnt = 0
while i < len(text):
    if text[i:i+n] == word:
        cnt += 1
        i += n

    else:
        i += 1

print(cnt)