N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

result = [1 for _ in range(N)]
for i in range(N):
    for j in range(i+1, N):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            result[i] += 1
        
        if arr[i][0] > arr[j][0] and arr[i][1] > arr[j][1]:
            result[j] += 1

print(" ".join(map(str, result)))