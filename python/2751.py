N = int(input())
number = []
for _ in range(N):
    number.append(int(input()))

list = sorted(number)
for i in range(N):
    print(list[i])