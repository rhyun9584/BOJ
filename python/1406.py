import sys

left = list(sys.stdin.readline().rstrip())
right = []
M = int(sys.stdin.readline())
for _ in range(M):
    op = sys.stdin.readline()
    if "L" in op and left:
        right.append(left.pop())
    elif "D" in op and right:
        left.append(right.pop())
    elif "B" in op and left:
        left.pop()
    elif "P" in op:
        left.append(op.split()[1])

right.reverse()
print("".join(left+right))