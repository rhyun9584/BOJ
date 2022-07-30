N = int(input())
M = int(input())

seat = [int(input()) for _ in range(M)] + [0]
x = 0

count = [0] * (N+1)
count[0] = 1
count[1] = 1
for i in range(2, N+1):
    if i == seat[x]:
        count[i] = count[i-1]
    elif i == seat[x]+1:
        # VIP 다음 사람도 왼쪽과 자리를 바꿀 수 없음
        count[i] = count[i-1]
        x += 1
    else:
        count[i] = count[i-1] + count[i-2]

print(count[N])