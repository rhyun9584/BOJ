N = int(input())
arr = list(map(int, input().split()))

close = 2000000001
pair = [0, 0]
i = 0
j = N-1
while i != j:
    result = arr[i] + arr[j]
    if abs(result) < close:
        close = abs(result)
        pair = [arr[i], arr[j]]

    if result == 0:
        break

    if result > 0:
        j -= 1
    else:
        i += 1

print(" ".join(map(str, pair)))