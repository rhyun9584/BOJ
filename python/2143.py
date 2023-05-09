import sys
input = sys.stdin.readline

def get_S(arr, N):
    S = [0]
    for i in range(N):
        S.append(S[i] + arr[i])

    return S

def get_dict(S, N):
    result = dict()
    for s in range(N+1):
        for e in range(s+1, N+1):
            sum = S[e] - S[s]
            if sum in result:
                result[sum] += 1
            else:
                result[sum] = 1
    
    return result

T = int(input())

N = int(input())
A = list(map(int, input().split()))
S_A = get_S(A, N)
dict_A = get_dict(S_A, N)

M = int(input())
B = list(map(int, input().split()))
S_B = get_S(B, M)
dict_B = get_dict(S_B, M)

answer = 0
for key, value in dict_A.items():
    if T-key in dict_B:
        answer += value * dict_B[T-key]

print(answer)
