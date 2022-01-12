n = int(input())

a = [int(x) for x in input().split(" ")]
b = [int(x) for x in input().split(" ")]

a.sort()
b.sort(reverse=True)

result = 0
for i in range(n):
    result += a[i] * b[i]

print(result)