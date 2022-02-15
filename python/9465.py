T = int(input())
for _ in range(T):
    n = int(input())
    score = [[int(x) for x in input().split()] for _ in range(2)]
    max_score = [[0, 0] for _ in range(n+1)]

    max_score[1] = [score[0][0], score[1][0]]

    for i in range(2, n+1):
        before_score = [
            max(max_score[i-1][1], max(max_score[i-2])), # 윗 줄을 선택할 때 더할 값
            max(max_score[i-1][0], max(max_score[i-2])), # 아랫 줄을 선택할 때 더할 값
        ]

        max_score[i][0] = before_score[0] + score[0][i-1]
        max_score[i][1] = before_score[1] + score[1][i-1]

    print(max(max_score[n]))
