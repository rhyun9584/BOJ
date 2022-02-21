import sys

N = int(sys.stdin.readline())
map = {}
for _ in range(N):
    number = int(sys.stdin.readline())
    map[number] = map.get(number, 0)+1

max_value = max(map.values())
max_key = [x for x, y in map.items() if y == max_value]
print(min(max_key))