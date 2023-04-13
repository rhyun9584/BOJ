import sys
input = sys.stdin.readline

S = [0] * 20
for _ in range(int(input())):
    op = input().split()
    x = 0
    if len(op) == 2:
        x = int(op[1]) - 1

    if op[0] == 'add':
        S[x] = 1
    elif op[0] == "remove":
        S[x] = 0
    elif op[0] == "check":
        print(S[x])
    elif op[0] == "toggle":
        S[x] = (S[x]+1) % 2
    elif op[0] == "all":
        S = [1] * 20
    else:
        S = [0] * 20