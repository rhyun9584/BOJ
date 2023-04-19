N, K = map(int, input().split())
number = input().rstrip()

answer = []
for i in range(N):
    num = number[i]
    while answer and K > 0:
        if answer[-1] >= num:
            break

        answer.pop()
        K -= 1

    answer.append(num)

for _ in range(K):
    answer.pop()

print("".join(answer))