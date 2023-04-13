import sys
input = sys.stdin.readline

N = int(input())

stack = []
answer = 0
for _ in range(N):
    x, y = map(int, input().split())

    while stack:
        if y < stack[-1]:
            stack.pop()
            answer += 1
        elif y == stack[-1]:
            stack.pop()
            break
        else:
            break
            
    if y > 0:
        stack.append(y)

while stack:
    stack.pop()
    answer += 1

print(answer)