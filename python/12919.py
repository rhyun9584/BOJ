import sys

def dfs(s, t):
    if len(s) == len(t):
        if s == t:
            print(1)
            sys.exit(0)

        return
            
    if t[0] == 'B':
        dfs(s, "".join(reversed(list(t[1:]))))
    if t[-1] == 'A':
        dfs(s, t[:-1])

S = input()
T = input()

dfs(S, T)

print(0)