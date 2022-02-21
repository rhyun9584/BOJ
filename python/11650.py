import sys

point = sys.stdin.readlines()[1:]
point.sort(key=lambda point: (int(point.split()[0]), int(point.split()[1])))
print("".join(point))