import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    number = list(map(int, input().split()))
    last_team = max(number)

    # 각 팀 참가자 수 세기 및 다섯번 째 선수 등수 기록
    count = [0] * (last_team+1)
    five = [0] * (last_team+1)
    for i in range(N):
        count[number[i]] += 1

        if count[number[i]] == 5:
            five[number[i]] = i

    # 참가 선수가 6명 이상인 팀 번호 확인 
    score_team = []
    for t in range(1, last_team+1):
        if count[t] >= 6:
            score_team.append(t)

    # 점수 계산 - 상위 4명 점수 합산
    score = [0] * (last_team+1)
    count = [0] * (last_team+1)
    s = 1
    for i in range(N):
        if number[i] in score_team:
            s += 1
            if count[number[i]] < 4:
                score[number[i]] += s
                count[number[i]] += 1

    # 승리 팀 찾기
    answer = 0
    min_score = int(1e9)
    min_five = N
    for t in score_team:
        if 0 < score[t] < min_score:
            min_score = score[t]
            min_five = five[t]
            answer = t
        elif score[t] == min_score and five[t] < min_five:
            min_five = five[t]
            answer = t
            
    print(answer)