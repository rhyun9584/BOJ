import sys
input = sys.stdin.readline

dp = [[[0] * 20 for _ in range(20)] for _ in range(20)]
flag = [[[0] * 20 for _ in range(20)] for _ in range(20)]

def w(a, b, c):
    # dp index를 위해서 숫자를 전부 -1 하여 접근
    if a < 0 or b < 0 or c < 0:
        return 1
    
    if a >= 20 or b >= 20 or c >= 20:
        return w(19, 19, 19)
    
    if flag[a][b][c] == 1:
        return dp[a][b][c]

    if a < b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

    flag[a][b][c] = 1
    return dp[a][b][c]

while True:
    a, b, c = map(int, input().split())

    if a == -1 and b == -1 and c == -1:
        break

    print(f"w({a}, {b}, {c}) = {w(a-1, b-1, c-1)}")