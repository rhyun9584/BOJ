N = int(input())
S = []
for i in range(N):
    temp = [int(x) for x in list(input().split())]
    S.append(temp)

def getStat(member):
    result = 0
    for i in member:
        for j in member:
            result += S[i][j] + S[j][i]

    return int(result/2)

min_val = N * (N-1) * 100
def divideTeam(team1, team2, idx):
    global min_val
    if idx == N:
        stat1 = getStat(team1)
        stat2 = getStat(team2)

        min_val = min(abs(stat1 - stat2), min_val)
        return

    if len(team1) < N/2:
        new_team = team1 + [idx]
        divideTeam(new_team, team2, idx+1)
    if len(team2) < N/2:
        new_team = team2 + [idx]
        divideTeam(team1, new_team, idx+1)

divideTeam([0], [], 1)
print(min_val)