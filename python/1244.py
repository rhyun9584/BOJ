import sys
input = sys.stdin.readline

N = int(input())

switch = list(map(int, input().split()))

T = int(input())
for _ in range(T):
    g, n = map(int, input().split())

    num = n-1
    if g == 1:
        while num < N:
            switch[num] = 1 - switch[num]
            num += n

    if g == 2:
        i = 0
        while 0 <= num - (i+1) and num + (i+1) < N and switch[num-(i+1)] == switch[num+(i+1)]:
            i += 1

        for j in range(num-i, num+i + 1):
            switch[j] = 1 - switch[j]

for i in range(0, N, 20):
    print(" ".join(map(str, switch[i: i+20])))