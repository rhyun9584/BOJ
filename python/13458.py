N = int(input())
candidate = list(map(int, input().split()))
B, C = map(int, input().split())

answer = 0
for c in candidate:
    answer += 1
    other = c - B
    if other > 0:
        answer += (other-1)//C + 1

print(answer)