N = int(input())

answer = 1
total = 1
while True:
    if N <= total:
        break
 
    total += 6 * answer
    answer += 1

print(answer)