from itertools import permutations

N = int(input())
number = list(map(int, input().split()))

def summation(arr, N):
    result = 0
    for i in range(N-1):
        result += abs(arr[i]-arr[i+1])
    return result

result = 0
for arr in permutations(number, N):
    result = max(result, summation(arr, N))

print(result)