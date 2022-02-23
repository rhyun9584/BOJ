import sys

N = int(sys.stdin.readline())
q = []
for _ in range(N):
    operation = sys.stdin.readline()
    if "push" in operation:
        q.append(operation.split()[1])
    elif "pop" in operation:
        if q:
            front = q[0]
            q = q[1:]
            print(front)
        else:
            print(-1)
    elif "size" in operation:
        print(len(q))
    elif "empty" in operation:
        if q: print(0)
        else: print(1)
    elif "front" in operation:
        if q: print(q[0])
        else: print(-1)
    elif "back" in operation:
        if q: print(q[-1])
        else: print(-1)
