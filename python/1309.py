N = int(input())

# i번째 줄에 사자를 배치한 경우의 수 기록
lion = [[0, 0, 0] for _ in range(N+1)]
lion[1] = [1, 1, 1]
for i in range(2, N+1):
    # 수가 커져서 메모리 문제 발생 -> 그때그때 나눠주어서 기록
    lion[i][0] = sum(lion[i-1]) % 9901
    lion[i][1] = (lion[i-1][2] + lion[i-1][0]) % 9901
    lion[i][2] = (lion[i-1][1] + lion[i-1][0]) % 9901

print(sum(lion[N]) % 9901)