N, M = map(int, input().split())
numbers = list(map(int, input().split()))

l, r = 0, 1
answer = 0
while r <= N and l <= r:
    result = sum(numbers[l:r])
    if result == M:
        answer += 1
        l += 1
    elif result > M:
        l += 1
    else:
        r += 1

print(answer)