import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

start = 1
end = arr[K-1] - arr[0]

answer = ''

while start <= end:
    mid = (start+end) // 2
    
    tmp = [1] + [0] * (K-1)
    cnt = 1
    
    current = arr[0]
    for i in range(1, K):
        if arr[i] >= mid+current:
            tmp[i] = 1
            cnt += 1
            current = arr[i]

    if cnt < M:
        end = mid-1
    else:
        tmp_str = ''
        cnt = M
        for i in range(K):
            if tmp[i] == 1 and cnt > 0:
                tmp_str += '1'
                cnt -= 1
            else:
                tmp_str += '0'
        answer = tmp_str
            
        start = mid+1

print(answer)