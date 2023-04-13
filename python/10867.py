N = int(input())

number = set(map(int, input().split()))

print(" ".join(map(str, sorted(number))))