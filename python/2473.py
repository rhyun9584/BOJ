import sys
input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))
numbers.sort()

def search(target, l, r):
    global answer, answer_diff

    while l < r:
        diff = target + numbers[l] + numbers[r]

        if abs(diff) < answer_diff:
            answer_diff = abs(diff)
            answer = [target, numbers[l], numbers[r]]

        if diff == 0:
            return
        elif diff > 0:
            r -= 1
        else:
            l += 1

answer = []
answer_diff = int(1e9) * 3
for i in range(N):
    search(numbers[i], i+1, N-1)

    if answer_diff == 0:
        break

print(" ".join(map(str, sorted(answer))))