import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    result = input().rstrip()
    
    answer = 0
    cnt = 0
    for ch in result:
        if ch == 'X':
            cnt = 0
        if ch == 'O':
            cnt += 1
            answer += cnt

    print(answer)