number = input()

N = len(number)
ways = [0] * (N+1)
if int(number[0]) == 0:
    print(0)
else:
    ways[0:2] = [1, 1]
    for i in range(2, N+1):
        if int(number[i-1]) > 0:
            ways[i] += ways[i-1]
        if 10 <= int("".join(number[i-2:i])) <= 26:
            ways[i] += ways[i-2]

    print(ways[N]%1000000)