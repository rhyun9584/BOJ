import sys

inputs = sys.stdin.readlines()
N, M = map(int, inputs[0].split())

memo = dict()
for x in inputs[1:N+1]:
    memo[x.rstrip()] = 1

memo_len = len(memo)
for x in inputs[N+1:]:
    keywords = x.rstrip().split(',')

    for k in keywords:
        if k in memo and memo[k] == 1:
            memo[k] = 0
            memo_len -= 1

    print(memo_len)