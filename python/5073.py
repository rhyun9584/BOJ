import sys
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())

    if a == 0:
        break

    if a + b + c - max(a, b, c) <= max(a, b, c):
        print("Invalid")
        continue

    tri = set([a, b, c])
    if len(tri) == 1:
        print("Equilateral")
    elif len(tri) == 2:
        print("Isosceles")
    else:
        print("Scalene")