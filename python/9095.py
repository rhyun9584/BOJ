T = int(input())
number = []
for _ in range(T):
    number.append(int(input()))

N = max(number)
ways = [0] * (N+1)
for i in range(1, N+1):
    if i == 1: ways[i] = 1
    elif i == 2: ways[i] = 2
    elif i == 3: ways[i] = 4
    else:
        ways[i] = ways[i-1] + ways[i-2] + ways[i-3]

for i in range(T):
    print(ways[number[i]])