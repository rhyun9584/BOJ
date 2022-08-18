N = int(input())

result = int(1e9)
for i in range(0, (N//5)+1):
    m = N - 5*i
    if m%3 == 0:
        result = min(result, i+(m//3))

print(result if result < int(1e9) else -1)
