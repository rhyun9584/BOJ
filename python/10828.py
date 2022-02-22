import sys

N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    operation = sys.stdin.readline()
    if "push" in operation:
        stack.append(operation.split()[1])
    elif "pop" in operation:
        if stack: print(stack.pop())
        else: print(-1)
    elif "size" in operation:
        print(len(stack))
    elif "empty" in operation:
        if stack: print(0)
        else: print(1)
    elif "top" in operation:
        if stack: print(stack[-1])
        else: print(-1)