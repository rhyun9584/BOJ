import sys

lines = sys.stdin.readlines()
for line in lines:
    A, B = [int(x) for x in line.split()]
    print(A+B)