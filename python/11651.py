import sys

point = sys.stdin.readlines()[1:]
point.sort(key=lambda x: (int(x.split()[1]), int(x.split()[0])))
print("".join(point))