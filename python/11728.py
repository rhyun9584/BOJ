N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = []
i = j = 0
while True:
    if i == N and j == M:
        break
    if i == N:
        result.append(B[j])
        j += 1
    elif j == M:
        result.append(A[i])
        i += 1
    elif A[i] <= B[j]:
        result.append(A[i])
        i += 1
    else:
        result.append(B[j])
        j += 1

print(" ".join(map(str, result)))