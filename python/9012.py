import sys

N = int(sys.stdin.readline())
for _ in range(N):
    string = sys.stdin.readline()
    x = 0
    for ch in string:
        if ch == '(':
            x += 1
        elif ch == ')':
            x -= 1
            if x < 0:
                break

    if x == 0: print("YES")
    else: print("NO")