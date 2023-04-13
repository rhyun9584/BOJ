import sys
input = sys.stdin.readline

dp = [[0, 0] for _ in range(41)]
dp[0] = [1, 0]
dp[1] = [0, 1]

def count_fibo(n):
    if dp[n] != [0, 0]:
        return dp[n]

    zero1, one1 = count_fibo(n-1)
    zero2, one2 = count_fibo(n-2)

    dp[n][0] = zero1 + zero2
    dp[n][1] = one1 + one2

    return dp[n]

T = int(input())
for _ in range(T):
    n = int(input())

    zero, one = count_fibo(n)
    print(zero, one)
