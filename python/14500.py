N, M = [int(x) for x in input().split()]

map = []
for i in range(N):
    map.append([int(x) for x in input().split()])

max_sum = 0
for i in range(N):
    for j in range(M):
        # ㅁ
        if i < N-1 and j < M-1:
            sum = map[i][j] + map[i][j+1] + map[i+1][j] + map[i+1][j+1]
            max_sum = max(max_sum, sum)

        # ㅣ
        if i < N-3:
            sum = map[i][j] + map[i+1][j] + map[i+2][j] + map[i+3][j]
            max_sum = max(max_sum, sum)
        # ㅡ
        if j < M-3:
            sum = map[i][j] + map[i][j+1] + map[i][j+2] + map[i][j+3]
            max_sum = max(max_sum, sum)

        if i < N-1 and j < M-2:
            # ㄴ
            sum1 = map[i][j+2] + map[i+1][j] + map[i+1][j+1] + map[i+1][j+2]
            sum2 = map[i][j] + map[i+1][j] + map[i+1][j+1] + map[i+1][j+2]
            sum3 = map[i][j] + map[i][j+1] + map[i][j+2] + map[i+1][j+2]
            sum4 = map[i][j] + map[i][j+1] + map[i][j+2] + map[i+1][j]

            # 가로 S
            sum5 = map[i][j] + map[i][j+1] + map[i+1][j+1] + map[i+1][j+2]
            sum6 = map[i+1][j] + map[i+1][j+1] + map[i][j+1] + map[i][j+2]

            # T and ㅗ
            sum7 = map[i][j] + map[i][j+1] + map[i][j+2] + map[i+1][j+1]
            sum8 = map[i][j+1] + map[i+1][j] + map[i+1][j+1] + map[i+1][j+2]

            max_sum = max(max_sum, sum1, sum2, sum3, sum4, sum5, sum6, sum7, sum8)

        if i < N-2 and j < M-1:
            # L 
            sum1 = map[i][j] + map[i][j+1] + map[i+1][j] + map[i+2][j]
            sum2 = map[i][j] + map[i+1][j] + map[i+2][j] + map[i+2][j+1]
            sum3 = map[i][j+1] + map[i+1][j+1] + map[i+2][j] + map[i+2][j+1]
            sum4 = map[i][j] + map[i][j+1] + map[i+1][j+1] + map[i+2][j+1]

            # 세로 S
            sum5 = map[i][j] + map[i+1][j] + map[i+1][j+1] + map[i+2][j+1]
            sum6 = map[i][j+1] + map[i+1][j+1] + map[i+1][j] + map[i+2][j]

            # ㅓ and ㅏ
            sum7 = map[i][j+1] + map[i+1][j] + map[i+2][j+1] + map[i+1][j+1]
            sum8 = map[i][j] + map[i+1][j] + map[i+2][j] + map[i+1][j+1]
            max_sum = max(max_sum, sum1, sum2, sum3, sum4, sum5, sum6, sum7, sum8)

print(max_sum)