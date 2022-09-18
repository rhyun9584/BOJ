import sys
input = sys.stdin.readline

N = int(input())
tops = list(map(int, input().split()))

stack = []
result = []
for i in range(N):
    while stack and stack[-1][0] < tops[i]:
        stack.pop()

    if stack == []:
        result.append(0)
    else:
        result.append(stack[-1][1])

    stack.append((tops[i], i+1))

print(" ".join(map(str, result)))