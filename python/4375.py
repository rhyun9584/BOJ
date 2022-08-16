import sys

number = list(map(int, sys.stdin.readlines()))

for n in number:
    s = 1
    i = 1
    while s % n != 0:
        s = (s*10+1) % n
        i += 1

    print(i)