import sys

N = int(sys.stdin.readline())
d = []
for _ in range(N):
    operation = sys.stdin.readline()
    if "push_front" in operation:
        d = [operation.split()[1]] + d
    elif "push_back" in operation:
        d.append(operation.split()[1])
    elif "pop_front" in operation:
        if d:
            print(d[0])
            d = d[1:]
        else:
            print(-1)
    elif "pop_back" in operation:
        if d: print(d.pop())
        else: print(-1)
    elif "size" in operation:
        print(len(d))
    elif "empty" in operation:
        if d: print(0)
        else: print(1)
    elif "front" in operation:
        if d: print(d[0])
        else: print(-1)
    elif "back" in operation:
        if d: print(d[-1])
        else: print(-1)
