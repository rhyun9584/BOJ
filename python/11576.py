A, B = map(int, input().split())
m = int(input())

numbers = list(map(int, input().split()))
numbers.reverse()

num = 0
for i in range(m):
    num += numbers[i] * (A ** i)

numbers_B = []
while num > 0:
    numbers_B.append(str(num%B))
    num //= B

numbers_B.reverse()
print(' '.join(numbers_B))