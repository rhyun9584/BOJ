N = int(input())
point = []
for _ in range(N):
    point.append([int(x) for x in input().split()])

point.sort(key=lambda point: (point[0], point[1]))
for i in range(N):
    print(point[i][0], point[i][1])