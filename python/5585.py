N = int(input())

charge = 1000-N

answer = 0
for c in [500, 100, 50, 10, 5, 1]:
    answer += charge // c
    charge %= c

print(answer)