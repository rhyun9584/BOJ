n = int(input())
box = [0] + list(map(int, input().split()))

count = [1] * (n+1)
for i in range(2, n+1):
    for j in range(i-1, 0, -1):
        if box[j] < box[i]:
            count[i] = max(count[i], count[j]+1)

print(max(count))
