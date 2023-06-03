import sys
input = sys.stdin.readline

N = int(input())

stack = []
result = []
last = 0
for _ in range(N):
    num = int(input())

    if not stack or stack[-1] < num:
        stack.extend([i for i in range(last+1, num+1)])
        result.extend(["+"] * (num-last))
        last = num
    elif stack[-1] > num:
        last = -1
        break

    stack.pop()
    result.append("-")

if last == -1:
    print("NO")
else:
    print("\n".join(result))